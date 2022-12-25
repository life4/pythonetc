---
published: 2018-04-26
id: 70
author: pushtaev
---

# Unicode vs utf-8

To store any information in memory or on a storage device, you should represent it in bytes.
Python usually provides the level of abstraction where you can think about data itself, not its byte form.

Still, when you write, say, a string to a file, you deal with a physical structure of data.
To put characters into a file you should transform them into bytes; that is called *encoding*.
When you get bytes from a file, you probably want to convert them into meaningful characters; that is call *decoding*.

There are hundreds of encoding methods out there.
The most popular one is probably Unicode, but you can't transform anything to bytes with it.
In the sense of byte representation, Unicode *is not even an encoding*.
Unicode defines a mapping between characters and their *integer* codes.
🐍 is 128 013, for example.

But to put integers into a file, you need a real encoding.
Unicode is usually used with `utf-8`, which is (usually) a default in Python.
When you read form a file, Python automatically decodes `utf-8`.
You can choose any other encoding with `encoding=` parameter of the `open` function, or you can read plane bytes by appending `b` to its mode.
