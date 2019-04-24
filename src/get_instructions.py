import dis
import sys
from io import StringIO
import yatzy

out = StringIO()
stdout = sys.stdout
sys.stdout = out
try:
    dis.dis(yatzy)
finally:
    sys.stdout = stdout
out = out.getvalue()


out_file = open("./yatzy_disassembly.py", "w") # open for [w]riting as [b]inary
out_file.write(out)
out_file.close()

# no good, just getting None
