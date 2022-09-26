from textwrap import dedent

import pytest

from sdk.post_markdown import PostMarkdown


MD = dedent("""
    # HEADER

    SOME TEXT 1

    ```python {skip}
    a = 1
    ```

    ```python {continue}
    a += 1
    ```

    ```python {skip} {continue}
    assert a == 2
    ```

    SOME TEXT 2
""")


def test_post_markdown_has_header():
    p = PostMarkdown(MD)
    assert p.has_header()


def test_post_markdown_has_header__no_header():
    p = PostMarkdown('SOME TEXT')
    assert not p.has_header()


def test_post_markdown_has_empty_line_eof():
    p = PostMarkdown(MD)
    assert p.has_empty_line_eof()


def test_post_markdown_has_empty_line_eof__no_empty_line():
    p = PostMarkdown('SOME TEXT')
    assert not p.has_empty_line_eof()


def test_post_markdown_title():
    p = PostMarkdown(MD)
    assert p.title() == 'HEADER'


MD_CONTENT = dedent("""
    # HEADER

    SOME TEXT 1
""")


def test_post_markdown_content():
    p = PostMarkdown(MD_CONTENT)
    assert p.content() == '\nSOME TEXT 1\n'


def test_post_markdown_html_content():
    p = PostMarkdown('# HEADER')
    assert p.html_content() == '<h1>HEADER</h1>\n'


def test_post_markdown__paragraphs():
    p = PostMarkdown(MD)
    paragraphs = list(p._paragraphs())
    assert len(paragraphs) == 6
    assert [len(p.tokens) for p in paragraphs] == [
        3,  # header: open, inline, close
        3,  # text: open, inline, close
        1,  # fence
        1,  # fence
        1,  # fence
        3,  # text: open, inline, close
    ]

    assert paragraphs[2].code is not None
    assert paragraphs[2].code.body == 'a = 1\n'
    assert paragraphs[2].code.info == ['python', '{skip}']
    assert paragraphs[2].code.skip is True
    assert paragraphs[2].code.continue_code is False

    assert paragraphs[3].code is not None
    assert paragraphs[3].code.body == 'a += 1\n'
    assert paragraphs[3].code.info == ['python', '{continue}']
    assert paragraphs[3].code.skip is False
    assert paragraphs[3].code.continue_code is True

    assert paragraphs[4].code is not None
    assert paragraphs[4].code.body == 'assert a == 2\n'
    assert paragraphs[4].code.info == ['python', '{skip}', '{continue}']
    assert paragraphs[4].code.skip is True
    assert paragraphs[4].code.continue_code is True


MD_CODE_INFO = dedent("""
    ```python
    a = 2
    ```
""")


def test_post_markdown__remove_code_info():
    p = PostMarkdown(MD_CODE_INFO)
    p._remove_code_info()
    assert p.text == '\n```\na = 2\n```\n'


SKIPS_MD = dedent("""
    ```{skip}
    a
    ```

    ```
    b
    ```
""")


def test_post_markdown__skipped_removed():
    p = PostMarkdown(SKIPS_MD)
    p._skipped_removed()
    assert p.text == '\n```\nb\n```\n'


def test_post_markdown__skipped_removed__no_skips():
    p = PostMarkdown('SOME TEXT')
    p._skipped_removed()
    assert p.text == 'SOME TEXT'


def test_post_markdown__skipped_removed__no_new_line_after():
    p = PostMarkdown('```{skip}\na\n```')
    p._skipped_removed()
    assert p.text == ''


MD_TELEGRAM = dedent("""
    # HEADER

    SOME TEXT 1

    ```
    a += 1
    ```

    SOME TEXT 2
""")


def test_post_markdown_to_telegram():
    p = PostMarkdown(MD)
    p.to_telegram()
    assert p.text == MD_TELEGRAM


MD_CODE = dedent("""
    ```
    a = 1
    ```
""")


MD_CODE_ERROR = dedent("""
    ```
    assert False
    ```
""")


def test_post_markdown_run_code():
    PostMarkdown(MD_CODE).run_code()

    with pytest.raises(AssertionError):
        PostMarkdown(MD_CODE_ERROR).run_code()
