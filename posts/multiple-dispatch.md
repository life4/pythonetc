---
published: 2018-04-23
id: 66
author: pushtaev
buttons:
- title: Python double dispatch emulation
  url: "https://replit.com/@VadimPushtaev/visitor"
- title: Java overloading doesn't work as multiple dispatch
  url: "https://replit.com/@VadimPushtaev/singledispatch"
- title: C# multiple dispatch
  url: "https://replit.com/@VadimPushtaev/multipledispatch"
---

# Multiple dispatch

When Python executes a method call, say `a.f(b, c, d)`, it should first select the right `f` function. Due to polymorphism, it depends on the type of `a`. The process of choosing the method is usually called *dynamic dispatch*.

Python supports only single-dispatch polymorphism because a single object alone (`a` in the example) affects the method selection. Some other languages, however, may also consider a type of `b`, `c` and `d`. This mechanism is called *multiple disaptch*. C# is a notable example of languages that support that technique.

However, multiple dispatch can be emulated via single-dispatch. The *visitor* design pattern is created exactly for this. What *visitor* do is essentially calling single-dispatch twice to imitate double-dispatch.

Mind, that the ability to overload methods (like in Java and C++) is not the same as multiple dispatch. Dynamic dispatch works in runtime while overloading solely affects compile time.
