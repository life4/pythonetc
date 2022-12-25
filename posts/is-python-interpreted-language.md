---
published: 2018-04-27
id: 71
author: pushtaev
---

# Is Python interpreted language?

Is Python interpreted or compiled? The simple answer here is *interpreted*; the right one is — *it's both*.

Python compiles your source code to bytecode (`.pyc` files).
It does that implicitly, but it's still an essential phase of Python code execution.
Java, for example, does the same but explicitly: you compile with `javac` and run with `java`.

Despite that, Python is usually called interpreted language while Java is called compiled language, which is, strictly speaking, not entirely correct.

Here is an [article on the subject](https://nedbatchelder.com//blog/201803/is_python_interpreted_or_compiled_yes.html) with more details and explanations.
