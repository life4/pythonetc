from __future__ import annotations

from textwrap import dedent

from sdk.ipython_executor import IPythonCommand, IPythonExecutor


def test__lines_of_code() -> None:
    code = dedent("""
        In [1]: a = 2

        In [2]: a + a
        Out[2]: 4

        In [3]: print("
           ...: n")
          Cell In [3], line 1
            print("
                  ^
        SyntaxError: unterminated string literal (detected at line 1)

        In [5]: print("n\\
           ...: ")
        n
    """)

    assert list(IPythonExecutor(code)._commands) == [
        IPythonCommand('a = 2', ''),
        IPythonCommand('a + a', '4'),
        IPythonCommand('print("\nn")', ''),
        IPythonCommand('print("n")', ''),
    ]


def test_run():
    shared_globals: dict = {}
    exec('a = 4', shared_globals)
    code = dedent("""
        In [0]: a *= 2
        In [1]: a
        Out[1]: 7
    """)

    executor = IPythonExecutor(code)
    run_result = list(executor.run(shared_globals))

    assert [
        IPythonCommand('a *= 2', '', ''),
        IPythonCommand('a', '7', '8'),  # 7 is just for test, should not happen
    ] == run_result
    assert shared_globals['a'] == 8
