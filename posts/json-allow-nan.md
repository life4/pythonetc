---
published: 2021-08-31
id: 677
author: orsinium
topic:
  - stdlib
  - arg
qname: json.dumps
---

# allow_nan

JSON states for "JavaScript Object Notation". It's a subset of JavaScript and representation of values is based on how they are represented in JavaScript:

```python
import json
json.dumps(1)     # '1'
json.dumps(1.2)   # '1.2'
json.dumps('hi')  # '"hi"'
json.dumps({})    # '{}'
json.dumps([])    # '[]'
json.dumps(None)  # 'null'
json.dumps(float('inf'))  # 'Infinity'
json.dumps(float('nan'))  # 'NaN'
```

The last two examples are valid JavaScript but explicitly forbidden by [RFC 4627](https://tools.ietf.org/html/rfc4627) "The application/json Media Type for JSON":

> Numeric values that cannot be represented as sequences of digits (such as Infinity and NaN) are not permitted.

And so, the `inf` / `nan` values, successfully serialized in Python, can fail deserialization in another language. For example, in Go:

```go
import "encoding/json"

func main() {
    var v float64
    err := json.Unmarshal(`Infinity`, &v)
    println(err)
    // Output: invalid character 'I' looking for beginning of value
}
```

To prevent producing invalid JSON, pass `allow_nan=False` argument:

```python
json.dumps(float('nan'), allow_nan=False)
# ValueError: Out of range float values are not JSON compliant
```
