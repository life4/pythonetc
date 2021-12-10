# faulthandler part 2

Now, let's see how to dump stack trace when a specific signal received. We will use [SIGUSR1](https://www.gnu.org/software/libc/manual/html_node/Miscellaneous-Signals.html) but you can do the same for any signal.

```python
import faulthandler
from signal import SIGUSR1
from time import sleep

faulthandler.register(SIGUSR1)
sleep(60)
```

Now, in a new terminal, find out the [PID](https://en.wikipedia.org/wiki/Process_identifier) of the interpreter. If the file is named `tmp.py`, this is how you can do it (we add `[]` in grep to exclude the grep itself from the output):

```bash
ps -ax | grep '[t]mp.py'
```

The first number in the output is the PID. Now, use it to send the signal for PID 12345:

```bash
kill -SIGUSR1 12345
```

And back in the terminal with the running script. You will see the stack trace:

```python
Current thread 0x00007f22edb29740 (most recent call first):
  File "tmp.py", line 6 in <module>
```
