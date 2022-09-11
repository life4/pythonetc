---
published: 2021-04-01
id: 658
author: orsinium
---

# eval strategy

In most of the programming languages (like C, PHP, Go, Rust) values can be passed into a function either as value or as reference (pointer):

+ [Call by value](https://en.wikipedia.org/wiki/Evaluation_strategy#Call_by_value) means that the value of the variable is copied, so all modification with the argument value inside the function won't affect the original value. This is an example of how it works in [Go](https://golang.org/):

```go
package main

func f(v2 int) {
  v2 = 2
  println("f v2:", v2)
  // Output: f v2: 2
}

func main() {
  v1 := 1
  f(v1)
  println("main v1:", v1)
  // Output: main v1: 1
}
```

+ [Call by reference](https://en.wikipedia.org/wiki/Evaluation_strategy#Call_by_reference) means that all modifications that are done by the function, including reassignment, will modify the original value:

```go
package main

func f(v2 *int) {
  *v2 = 2
  println("f v2:", *v2)
  // Output: f v2: 2
}

func main() {
  v1 := 1
  f(&v1)
  println("main v1:", v1)
  // Output: main v1: 2
}
```

So, which one is used in Python? Well, neither.

In Python, the caller and the function share the same value:

```python
def f(v2: list):
  v2.append(2)
  print('f v2:', v2)
  # f v2: [1, 2]

v1 = [1]
f(v1)
print('v1:', v1)
# v1: [1, 2]
```

However, the function can't replace the value (reassign the variable):

```python
def f(v2: int):
  v2 = 2
  print('f v2:', v2)
  # f v2: 2

v1 = 1
f(v1)
print('v1:', v1)
# v1: 1
```

This approach is called [Call by sharing](https://en.wikipedia.org/wiki/Evaluation_strategy#Call_by_sharing). That means the argument is always passed into a function as a copy of the pointer. So, both variables point to the same boxed object in memory but if the pointer itself is modified inside the function, it doesn't affect the caller code.
