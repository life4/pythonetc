---
published: 2018-04-08
id: 46
author: pushtaev
sequence: fsm
---

# Chomsky

Apart from regular languages, [Chomsky](https://en.wikipedia.org/wiki/Chomsky_hierarchy) distinguishes three more types (ordered by descending strictness):
context-free, context-sensitive, and unrestricted.

Context-free languages are more powerful than regular ones but still can be efficiently parsed by a program.
`XML`, `JSON` and `SQL` are context-free for example.

Many tools allow you to parse such languages easily.
Usually, they require you to define some *grammar*, the rules on how to parse and create a parser automatically.
The most popular way to define such grammar is the [BNF](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form) language.
Here is the grammar to parse simple arithmetical expressions (only `+` supported) defined in BNF:

```txt
 <expr> ::= <operand> "+" <expr>  |  <operand>
 <operand> ::= "(" <expr> ")"  |  <const>
 <const> ::= integer
```

This is the set of rules.
An expression is an operand plus another expression or just operand.
An operand is either a constant or an expression enclosed in brackets.
This way we can see the recursive nature of this language, which makes it non-regular.

The example of a context-free grammar parser for Python is [lark](https://github.com/erezsh/lark).
It is what you want if regexes are not enough or code that does the parsing gets messy.
