class Winnie(str):

    def __init__(self, str_value):
        self.value = str_value;
        super();

    def your_mom(self):
        thing = input('give me an activity')
        return print('YOUR MOM does {}!!!'.format(thing));

# Disassembly of __init__:
#   4           0 LOAD_FAST                1 (str_value)
#               2 LOAD_FAST                0 (self)
#               4 STORE_ATTR               0 (value)
#
#   5           6 LOAD_GLOBAL              1 (super)
#               8 CALL_FUNCTION            0
#              10 POP_TOP
#              12 LOAD_CONST               0 (None)
#              14 RETURN_VALUE
#
# Disassembly of your_mom:
#   8           0 LOAD_CONST               1 ('YOUR MOM!!!')
#               2 RETURN_VALUE
