from textwrap import dedent

import pytest

from sdk.post_markdown import Language, PostMarkdown


MD = dedent("""
    # HEADER

    SOME TEXT 1

    ```python {hide}
    a = 1
    ```

    ```python {continue}
    a += 1
    ```

    ```python {hide} {continue}
    assert a == 2
    ```

    ```python {no-run} {hide}
    assert False
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
    assert len(paragraphs) == 7
    assert [len(p.tokens) for p in paragraphs] == [
        3,  # header: open, inline, close
        3,  # text: open, inline, close
        1,  # fence
        1,  # fence
        1,  # fence
        1,  # fence
        3,  # text: open, inline, close
    ]

    assert paragraphs[2].code is not None
    assert paragraphs[2].code.body == 'a = 1\n'
    assert paragraphs[2].code.language == Language.PYTHON
    assert paragraphs[2].code.hide is True
    assert paragraphs[2].code.continue_code is False

    assert paragraphs[3].code is not None
    assert paragraphs[3].code.body == 'a += 1\n'
    assert paragraphs[3].code.language == Language.PYTHON
    assert paragraphs[3].code.hide is False
    assert paragraphs[3].code.continue_code is True

    assert paragraphs[4].code is not None
    assert paragraphs[4].code.body == 'assert a == 2\n'
    assert paragraphs[4].code.language == Language.PYTHON
    assert paragraphs[4].code.hide is True
    assert paragraphs[4].code.continue_code is True

    assert paragraphs[5].code is not None
    assert paragraphs[5].code.body == 'assert False\n'
    assert paragraphs[5].code.language == Language.PYTHON
    assert paragraphs[5].code.hide is True
    assert paragraphs[5].code.continue_code is False
    assert paragraphs[5].code.no_run is True


MD_CODE_INFO = dedent("""
    ```python
    a = 2
    ```
""")


def test_post_markdown__remove_code_info():
    p = PostMarkdown(MD_CODE_INFO)
    p._remove_code_info()
    assert p.text == '\n```\na = 2\n```\n'


HIDDEN_MD = dedent("""
    ```{hide}
    a
    ```

    ```
    b
    ```
""")


def test_post_markdown__remove_hidden_code_blocks():
    p = PostMarkdown(HIDDEN_MD)
    p._remove_hidden_code_blocks()
    assert p.text == '\n```\nb\n```\n'


def test_post_markdown__remove_hidden_code_blocks__no_hidden():
    p = PostMarkdown('SOME TEXT')
    p._remove_hidden_code_blocks()
    assert p.text == 'SOME TEXT'


def test_post_markdown__remove_hidden_code_blocks__no_new_line_after():
    p = PostMarkdown('```{hide}\na\n```')
    p._remove_hidden_code_blocks()
    assert p.text == ''


MERGE_MD = dedent("""
    ```
    a
    ```



    ```{merge} {continue}
    b
    ```
""")


def test_post_markdown__merge_code_blocks():
    p = PostMarkdown(MERGE_MD)
    p._merge_code_blocks()
    assert p.text == '\n```\na\nb\n```\n'


MD_TELEGRAM = dedent("""
    SOME TEXT 1

    ```
    a += 1
    ```

    SOME TEXT 2
""").lstrip()


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
    ```python
    assert False
    ```
""")


def test_post_markdown_run_code():
    PostMarkdown(MD_CODE).run_code()

    with pytest.raises(AssertionError):
        PostMarkdown(MD_CODE_ERROR).run_code()
