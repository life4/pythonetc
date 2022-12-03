---
published: 2018-04-01
id: 34
author: pushtaev
---

# Python + Perl + Ruby = <3

I bet you often ask yourself:
“How do I make a script that can be run not only by Python interpreter
but by Perl and Ruby as well?”

Calm yourself down; I've got a solution for you:

```python {no-print}
"@{[sub {while (<DATA>) {last if /^\"\"\"__PERL__/}; eval join '', <DATA>}->()]}"
__DATA__ = 0
"""#{

    # Place Ruby code here
    if (2 > 1)
        puts "Hi, I'm Ruby!"
    end

}""";
__END__ = 0
__END__

# Place Python code here
if 2 > 1:
   print("Hi, I'm Python!")

"""__PERL__

    # Place perl code here
    use feature 'say';
    if (2 > 1) {
        say "Hi, I'm Perl!";
    }

__END__
"""
```


Here is how it works:

```bash
$ ruby script && python script && perl script
Hi, I'm Ruby!
Hi, I'm Python!
Hi, I'm Perl!
```
