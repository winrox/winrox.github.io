Disassembly of D6:
Disassembly of __init__:
 52           0 LOAD_GLOBAL              0 (super)
              2 CALL_FUNCTION            0
              4 LOAD_ATTR                1 (__init__)
              6 LOAD_CONST               1 (6)
              8 LOAD_FAST                1 (value)
             10 LOAD_CONST               2 (('sides', 'value'))
             12 CALL_FUNCTION_KW         2
             14 POP_TOP
             16 LOAD_CONST               0 (None)
             18 RETURN_VALUE


Disassembly of Dice:
Disassembly of __add__:
 41           0 LOAD_GLOBAL              0 (int)
              2 LOAD_FAST                0 (self)
              4 CALL_FUNCTION            1
              6 LOAD_FAST                1 (other)
              8 BINARY_ADD
             10 RETURN_VALUE

Disassembly of __eq__:
 21           0 LOAD_GLOBAL              0 (int)
              2 LOAD_FAST                0 (self)
              4 CALL_FUNCTION            1
              6 LOAD_FAST                1 (other)
              8 COMPARE_OP               2 (==)
             10 RETURN_VALUE

Disassembly of __ge__:
 33           0 LOAD_GLOBAL              0 (int)
              2 LOAD_FAST                0 (self)
              4 CALL_FUNCTION            1
              6 STORE_FAST               2 (this)

 34           8 LOAD_FAST                2 (this)
             10 LOAD_FAST                1 (other)
             12 COMPARE_OP               4 (>)
             14 JUMP_IF_TRUE_OR_POP     22
             16 LOAD_FAST                2 (this)
             18 LOAD_FAST                1 (other)
             20 COMPARE_OP               2 (==)
        >>   22 RETURN_VALUE

Disassembly of __gt__:
 27           0 LOAD_GLOBAL              0 (int)
              2 LOAD_FAST                0 (self)
              4 CALL_FUNCTION            1
              6 LOAD_FAST                1 (other)
              8 COMPARE_OP               4 (>)
             10 RETURN_VALUE

Disassembly of __init__:
  8           0 LOAD_FAST                1 (sides)
              2 LOAD_CONST               1 (2)
              4 COMPARE_OP               5 (>=)
              6 POP_JUMP_IF_TRUE        16

  9           8 LOAD_GLOBAL              0 (ValueError)
             10 LOAD_CONST               2 ('Must have at least 2 sides')
             12 CALL_FUNCTION            1
             14 RAISE_VARARGS            1

 10     >>   16 LOAD_GLOBAL              1 (isinstance)
             18 LOAD_FAST                1 (sides)
             20 LOAD_GLOBAL              2 (int)
             22 CALL_FUNCTION            2
             24 POP_JUMP_IF_TRUE        34

 11          26 LOAD_GLOBAL              0 (ValueError)
             28 LOAD_CONST               3 ('Sides must be a whole number')
             30 CALL_FUNCTION            1
             32 RAISE_VARARGS            1

 12     >>   34 LOAD_GLOBAL              1 (isinstance)
             36 LOAD_FAST                2 (value)
             38 LOAD_GLOBAL              2 (int)
             40 CALL_FUNCTION            2
             42 POP_JUMP_IF_TRUE        52

 13          44 LOAD_GLOBAL              0 (ValueError)
             46 LOAD_CONST               4 ('Value must be a whole number')
             48 CALL_FUNCTION            1
             50 RAISE_VARARGS            1

 15     >>   52 LOAD_FAST                2 (value)
             54 JUMP_IF_TRUE_OR_POP     64
             56 LOAD_GLOBAL              3 (randint)
             58 LOAD_CONST               5 (1)
             60 LOAD_FAST                1 (sides)
             62 CALL_FUNCTION            2
        >>   64 LOAD_FAST                0 (self)
             66 STORE_ATTR               4 (value)
             68 LOAD_CONST               0 (None)
             70 RETURN_VALUE

Disassembly of __int__:
 18           0 LOAD_FAST                0 (self)
              2 LOAD_ATTR                0 (value)
              4 RETURN_VALUE

Disassembly of __le__:
 37           0 LOAD_GLOBAL              0 (int)
              2 LOAD_FAST                0 (self)
              4 CALL_FUNCTION            1
              6 STORE_FAST               2 (this)

 38           8 LOAD_FAST                2 (this)
             10 LOAD_FAST                1 (other)
             12 COMPARE_OP               0 (<)
             14 JUMP_IF_TRUE_OR_POP     22
             16 LOAD_FAST                2 (this)
             18 LOAD_FAST                1 (other)
             20 COMPARE_OP               2 (==)
        >>   22 RETURN_VALUE

Disassembly of __lt__:
 30           0 LOAD_GLOBAL              0 (int)
              2 LOAD_FAST                0 (self)
              4 CALL_FUNCTION            1
              6 LOAD_FAST                1 (other)
              8 COMPARE_OP               0 (<)
             10 RETURN_VALUE

Disassembly of __ne__:
 24           0 LOAD_GLOBAL              0 (int)
              2 LOAD_FAST                0 (self)
              4 CALL_FUNCTION            1
              6 LOAD_FAST                1 (other)
              8 COMPARE_OP               3 (!=)
             10 RETURN_VALUE

Disassembly of __radd__:
 44           0 LOAD_GLOBAL              0 (int)
              2 LOAD_FAST                0 (self)
              4 CALL_FUNCTION            1
              6 LOAD_FAST                1 (other)
              8 BINARY_ADD
             10 RETURN_VALUE

Disassembly of __repr__:
 47           0 LOAD_GLOBAL              0 (str)
              2 LOAD_FAST                0 (self)
              4 LOAD_ATTR                1 (value)
              6 CALL_FUNCTION            1
              8 RETURN_VALUE


Disassembly of Hand:
Disassembly of __init__:
 57           0 LOAD_FAST                2 (die_class)
              2 POP_JUMP_IF_TRUE        12

 58           4 LOAD_GLOBAL              0 (ValueError)
              6 LOAD_CONST               1 ('You must provide a die class!')
              8 CALL_FUNCTION            1
             10 RAISE_VARARGS            1

 59     >>   12 LOAD_GLOBAL              1 (super)
             14 CALL_FUNCTION            0
             16 LOAD_ATTR                2 (__init__)
             18 CALL_FUNCTION            0
             20 POP_TOP

 61          22 SETUP_LOOP              28 (to 52)
             24 LOAD_GLOBAL              3 (range)
             26 LOAD_FAST                1 (size)
             28 CALL_FUNCTION            1
             30 GET_ITER
        >>   32 FOR_ITER                16 (to 50)
             34 STORE_FAST               5 (_)

 62          36 LOAD_FAST                0 (self)
             38 LOAD_ATTR                4 (append)
             40 LOAD_FAST                2 (die_class)
             42 CALL_FUNCTION            0
             44 CALL_FUNCTION            1
             46 POP_TOP
             48 JUMP_ABSOLUTE           32
        >>   50 POP_BLOCK

 63     >>   52 LOAD_FAST                0 (self)
             54 LOAD_ATTR                5 (sort)
             56 CALL_FUNCTION            0
             58 POP_TOP
             60 LOAD_CONST               0 (None)
             62 RETURN_VALUE

Disassembly of _by_value:
 66           0 BUILD_LIST               0
              2 STORE_FAST               2 (dice)

 67           4 SETUP_LOOP              30 (to 36)
              6 LOAD_FAST                0 (self)
              8 GET_ITER
        >>   10 FOR_ITER                22 (to 34)
             12 STORE_FAST               3 (die)

 68          14 LOAD_FAST                3 (die)
             16 LOAD_FAST                1 (value)
             18 COMPARE_OP               2 (==)
             20 POP_JUMP_IF_FALSE       10

 69          22 LOAD_FAST                2 (dice)
             24 LOAD_ATTR                0 (append)
             26 LOAD_FAST                3 (die)
             28 CALL_FUNCTION            1
             30 POP_TOP
             32 JUMP_ABSOLUTE           10
        >>   34 POP_BLOCK

 70     >>   36 LOAD_FAST                2 (dice)
             38 RETURN_VALUE

Disassembly of roll:
 74           0 LOAD_FAST                0 (Hand)
              2 LOAD_FAST                2 (size)
              4 LOAD_FAST                1 (die_type)
              6 LOAD_CONST               1 (('die_class',))
              8 CALL_FUNCTION_KW         2
             10 RETURN_VALUE


Disassembly of PlayYatzy:
Disassembly of choose_score:
794           0 LOAD_FAST                0 (self)
              2 LOAD_ATTR                0 (score)
              4 STORE_FAST               2 (score)

795           6 LOAD_FAST                2 (score)
              8 LOAD_ATTR                1 (get_state)
             10 CALL_FUNCTION            0
             12 STORE_FAST               3 (old_score)

796          14 LOAD_FAST                0 (self)
             16 LOAD_ATTR                2 (help_shown_last)
             18 POP_JUMP_IF_FALSE       46

797          20 LOAD_FAST                2 (score)
             22 LOAD_ATTR                3 (print_score)
             24 CALL_FUNCTION            0
             26 POP_TOP

798          28 LOAD_FAST                0 (self)
             30 LOAD_ATTR                4 (print_hand)
             32 LOAD_FAST                1 (hand)
             34 LOAD_CONST               1 (False)
             36 CALL_FUNCTION            2
             38 POP_TOP

799          40 LOAD_CONST               1 (False)
             42 LOAD_FAST                0 (self)
             44 STORE_ATTR               2 (help_shown_last)

801     >>   46 LOAD_GLOBAL              5 (input)
             48 LOAD_CONST               2 ("Please indicate which part of your scorecard you'd like to fill in by typing a matching category.\n(example: three of a kind OR twos)\n>>  ")
             50 CALL_FUNCTION            1
             52 LOAD_ATTR                6 (lower)
             54 CALL_FUNCTION            0
             56 LOAD_ATTR                7 (strip)
             58 CALL_FUNCTION            0
             60 STORE_FAST               4 (category)

803          62 LOAD_FAST                4 (category)
             64 LOAD_CONST               3 ('help')
             66 COMPARE_OP               2 (==)
             68 POP_JUMP_IF_TRUE        78
             70 LOAD_FAST                4 (category)
             72 LOAD_CONST               4 ('h')
             74 COMPARE_OP               2 (==)
             76 POP_JUMP_IF_FALSE       96

804     >>   78 LOAD_FAST                0 (self)
             80 LOAD_ATTR                8 (show_help)
             82 CALL_FUNCTION            0
             84 POP_TOP

805          86 LOAD_FAST                0 (self)
             88 LOAD_ATTR                9 (choose_score)
             90 LOAD_FAST                1 (hand)
             92 CALL_FUNCTION            1
             94 RETURN_VALUE

807     >>   96 LOAD_FAST                0 (self)
             98 LOAD_ATTR                0 (score)
            100 LOAD_ATTR               10 (set_score)
            102 LOAD_FAST                1 (hand)
            104 LOAD_FAST                4 (category)
            106 LOAD_FAST                0 (self)
            108 LOAD_ATTR               11 (invalid_choice)
            110 CALL_FUNCTION            3
            112 POP_TOP

810         114 LOAD_FAST                2 (score)
            116 LOAD_ATTR                1 (get_state)
            118 CALL_FUNCTION            0
            120 STORE_FAST               5 (new_score)

811         122 LOAD_FAST                5 (new_score)
            124 LOAD_ATTR               12 (items)
            126 CALL_FUNCTION            0
            128 LOAD_FAST                3 (old_score)
            130 LOAD_ATTR               12 (items)
            132 CALL_FUNCTION            0
            134 BINARY_SUBTRACT
            136 POP_JUMP_IF_TRUE       170

812         138 LOAD_GLOBAL             13 (print)
            140 LOAD_CONST               5 ("Error encountered.\nSorry, but I'll have to ask again.")
            142 CALL_FUNCTION            1
            144 POP_TOP

813         146 LOAD_FAST                0 (self)
            148 LOAD_ATTR                4 (print_hand)
            150 LOAD_FAST                1 (hand)
            152 LOAD_CONST               1 (False)
            154 CALL_FUNCTION            2
            156 POP_TOP

814         158 LOAD_FAST                0 (self)
            160 LOAD_ATTR                9 (choose_score)
            162 LOAD_FAST                1 (hand)
            164 CALL_FUNCTION            1
            166 POP_TOP
            168 JUMP_FORWARD            60 (to 230)

816     >>  170 LOAD_FAST                2 (score)
            172 LOAD_ATTR               14 (lower_total)
            174 LOAD_CONST               0 (None)
            176 COMPARE_OP               3 (!=)
            178 POP_JUMP_IF_FALSE      212
            180 LOAD_FAST                2 (score)
            182 LOAD_ATTR               15 (upper_total)
            184 LOAD_CONST               0 (None)
            186 COMPARE_OP               3 (!=)
            188 POP_JUMP_IF_FALSE      212
            190 LOAD_FAST                0 (self)
            192 LOAD_ATTR               16 (turn)
            194 LOAD_CONST               6 (2)
            196 BINARY_MODULO
            198 LOAD_CONST               7 (0)
            200 COMPARE_OP               2 (==)
            202 POP_JUMP_IF_FALSE      212

817         204 LOAD_FAST                0 (self)
            206 LOAD_ATTR               17 (end_game)
            208 CALL_FUNCTION            0
            210 RETURN_VALUE

819     >>  212 LOAD_FAST                0 (self)
            214 DUP_TOP
            216 LOAD_ATTR               16 (turn)
            218 LOAD_CONST               8 (1)
            220 INPLACE_ADD
            222 ROT_TWO
            224 STORE_ATTR              16 (turn)

820         226 LOAD_FAST                5 (new_score)
            228 RETURN_VALUE
        >>  230 LOAD_CONST               0 (None)
            232 RETURN_VALUE

Disassembly of clear_screen:
630           0 LOAD_GLOBAL              0 (os_system)
              2 LOAD_GLOBAL              1 (os_name)
              4 LOAD_CONST               1 ('nt')
              6 COMPARE_OP               2 (==)
              8 POP_JUMP_IF_FALSE       14
             10 LOAD_CONST               2 ('cls')
             12 JUMP_FORWARD             2 (to 16)
        >>   14 LOAD_CONST               3 ('clear')
        >>   16 CALL_FUNCTION            1
             18 POP_TOP
             20 LOAD_CONST               0 (None)
             22 RETURN_VALUE

Disassembly of comp_choose_score:
896           0 LOAD_FAST                0 (self)
              2 LOAD_ATTR                0 (comp_score)
              4 STORE_FAST               3 (comp_score)

897           6 LOAD_CONST               0 (None)
              8 STORE_FAST               4 (chosen_score)

899          10 LOAD_CONST              35 ((False, ''))

900          12 LOAD_FAST                3 (comp_score)
             14 LOAD_ATTR                1 (ones)
             16 LOAD_CONST               0 (None)
             18 COMPARE_OP               2 (==)
             20 LOAD_CONST               3 ('ones')
             22 BUILD_TUPLE              2

901          24 LOAD_FAST                3 (comp_score)
             26 LOAD_ATTR                2 (twos)
             28 LOAD_CONST               0 (None)
             30 COMPARE_OP               2 (==)
             32 LOAD_CONST               4 ('twos')
             34 BUILD_TUPLE              2

902          36 LOAD_FAST                3 (comp_score)
             38 LOAD_ATTR                3 (threes)
             40 LOAD_CONST               0 (None)
             42 COMPARE_OP               2 (==)
             44 LOAD_CONST               5 ('threes')
             46 BUILD_TUPLE              2

903          48 LOAD_FAST                3 (comp_score)
             50 LOAD_ATTR                4 (fours)
             52 LOAD_CONST               0 (None)
             54 COMPARE_OP               2 (==)
             56 LOAD_CONST               6 ('fours')
             58 BUILD_TUPLE              2

904          60 LOAD_FAST                3 (comp_score)
             62 LOAD_ATTR                5 (fives)
             64 LOAD_CONST               0 (None)
             66 COMPARE_OP               2 (==)
             68 LOAD_CONST               7 ('fives')
             70 BUILD_TUPLE              2

905          72 LOAD_FAST                3 (comp_score)
             74 LOAD_ATTR                6 (sixes)
             76 LOAD_CONST               0 (None)
             78 COMPARE_OP               2 (==)
             80 LOAD_CONST               8 ('sixes')
             82 BUILD_TUPLE              2
             84 BUILD_LIST               7
             86 STORE_FAST               5 (current_upper_scores)

907          88 LOAD_GLOBAL              7 (len)
             90 LOAD_GLOBAL              8 (list)
             92 LOAD_GLOBAL              9 (filter)
             94 LOAD_CONST               9 (<code object <lambda> at 0x10a310810, file "/Users/winniepalangpour/git/winrox.github.io/src/yatzy.py", line 907>)
             96 LOAD_CONST              10 ('PlayYatzy.comp_choose_score.<locals>.<lambda>')
             98 MAKE_FUNCTION            0
            100 LOAD_FAST                2 (new_hand)
            102 CALL_FUNCTION            2
            104 CALL_FUNCTION            1
            106 CALL_FUNCTION            1
            108 STORE_FAST               6 (ones)

908         110 LOAD_GLOBAL              7 (len)
            112 LOAD_GLOBAL              8 (list)
            114 LOAD_GLOBAL              9 (filter)
            116 LOAD_CONST              11 (<code object <lambda> at 0x10a3108a0, file "/Users/winniepalangpour/git/winrox.github.io/src/yatzy.py", line 908>)
            118 LOAD_CONST              10 ('PlayYatzy.comp_choose_score.<locals>.<lambda>')
            120 MAKE_FUNCTION            0
            122 LOAD_FAST                2 (new_hand)
            124 CALL_FUNCTION            2
            126 CALL_FUNCTION            1
            128 CALL_FUNCTION            1
            130 STORE_FAST               7 (twos)

909         132 LOAD_GLOBAL              7 (len)
            134 LOAD_GLOBAL              8 (list)
            136 LOAD_GLOBAL              9 (filter)
            138 LOAD_CONST              12 (<code object <lambda> at 0x10a310930, file "/Users/winniepalangpour/git/winrox.github.io/src/yatzy.py", line 909>)
            140 LOAD_CONST              10 ('PlayYatzy.comp_choose_score.<locals>.<lambda>')
            142 MAKE_FUNCTION            0
            144 LOAD_FAST                2 (new_hand)
            146 CALL_FUNCTION            2
            148 CALL_FUNCTION            1
            150 CALL_FUNCTION            1
            152 STORE_FAST               8 (threes)

910         154 LOAD_GLOBAL              7 (len)
            156 LOAD_GLOBAL              8 (list)
            158 LOAD_GLOBAL              9 (filter)
            160 LOAD_CONST              13 (<code object <lambda> at 0x10a3109c0, file "/Users/winniepalangpour/git/winrox.github.io/src/yatzy.py", line 910>)
            162 LOAD_CONST              10 ('PlayYatzy.comp_choose_score.<locals>.<lambda>')
            164 MAKE_FUNCTION            0
            166 LOAD_FAST                2 (new_hand)
            168 CALL_FUNCTION            2
            170 CALL_FUNCTION            1
            172 CALL_FUNCTION            1
            174 STORE_FAST               9 (fours)

911         176 LOAD_GLOBAL              7 (len)
            178 LOAD_GLOBAL              8 (list)
            180 LOAD_GLOBAL              9 (filter)
            182 LOAD_CONST              14 (<code object <lambda> at 0x10a310a50, file "/Users/winniepalangpour/git/winrox.github.io/src/yatzy.py", line 911>)
            184 LOAD_CONST              10 ('PlayYatzy.comp_choose_score.<locals>.<lambda>')
            186 MAKE_FUNCTION            0
            188 LOAD_FAST                2 (new_hand)
            190 CALL_FUNCTION            2
            192 CALL_FUNCTION            1
            194 CALL_FUNCTION            1
            196 STORE_FAST              10 (fives)

912         198 LOAD_GLOBAL              7 (len)
            200 LOAD_GLOBAL              8 (list)
            202 LOAD_GLOBAL              9 (filter)
            204 LOAD_CONST              15 (<code object <lambda> at 0x10a310ae0, file "/Users/winniepalangpour/git/winrox.github.io/src/yatzy.py", line 912>)
            206 LOAD_CONST              10 ('PlayYatzy.comp_choose_score.<locals>.<lambda>')
            208 MAKE_FUNCTION            0
            210 LOAD_FAST                2 (new_hand)
            212 CALL_FUNCTION            2
            214 CALL_FUNCTION            1
            216 CALL_FUNCTION            1
            218 STORE_FAST              11 (sixes)

917         220 LOAD_FAST                1 (possibilities)
            222 LOAD_CONST              16 ('yat')
            224 BINARY_SUBSCR
            226 POP_JUMP_IF_FALSE      246
            228 LOAD_FAST                3 (comp_score)
            230 LOAD_ATTR               10 (yatzy)
            232 LOAD_CONST               0 (None)
            234 COMPARE_OP               2 (==)
            236 POP_JUMP_IF_FALSE      246

918         238 LOAD_CONST              17 ('yatzy')
            240 STORE_FAST               4 (chosen_score)
            242 EXTENDED_ARG             4
            244 JUMP_FORWARD          1050 (to 1296)

919     >>  246 LOAD_FAST                1 (possibilities)
            248 LOAD_CONST              18 ('large_str')
            250 BINARY_SUBSCR
            252 EXTENDED_ARG             1
            254 POP_JUMP_IF_FALSE      276
            256 LOAD_FAST                3 (comp_score)
            258 LOAD_ATTR               11 (large_straight)
            260 LOAD_CONST               0 (None)
            262 COMPARE_OP               2 (==)
            264 EXTENDED_ARG             1
            266 POP_JUMP_IF_FALSE      276

920         268 LOAD_CONST              19 ('large straight')
            270 STORE_FAST               4 (chosen_score)
            272 EXTENDED_ARG             3
            274 JUMP_FORWARD          1020 (to 1296)

921     >>  276 LOAD_FAST                1 (possibilities)
            278 LOAD_CONST              20 ('small_str')
            280 BINARY_SUBSCR
            282 EXTENDED_ARG             1
            284 POP_JUMP_IF_FALSE      306
            286 LOAD_FAST                3 (comp_score)
            288 LOAD_ATTR               12 (small_straight)
            290 LOAD_CONST               0 (None)
            292 COMPARE_OP               2 (==)
            294 EXTENDED_ARG             1
            296 POP_JUMP_IF_FALSE      306

922         298 LOAD_CONST              21 ('small straight')
            300 STORE_FAST               4 (chosen_score)
            302 EXTENDED_ARG             3
            304 JUMP_FORWARD           990 (to 1296)

923     >>  306 LOAD_FAST                3 (comp_score)
            308 LOAD_ATTR                6 (sixes)
            310 LOAD_CONST               0 (None)
            312 COMPARE_OP               2 (==)
            314 EXTENDED_ARG             1
            316 POP_JUMP_IF_FALSE      354
            318 LOAD_GLOBAL              7 (len)
            320 LOAD_GLOBAL              8 (list)
            322 LOAD_GLOBAL              9 (filter)
            324 LOAD_CONST              22 (<code object <lambda> at 0x10a310b70, file "/Users/winniepalangpour/git/winrox.github.io/src/yatzy.py", line 923>)
            326 LOAD_CONST              10 ('PlayYatzy.comp_choose_score.<locals>.<lambda>')
            328 MAKE_FUNCTION            0
            330 LOAD_FAST                2 (new_hand)
            332 CALL_FUNCTION            2
            334 CALL_FUNCTION            1
            336 CALL_FUNCTION            1
            338 LOAD_CONST              23 (3)
            340 COMPARE_OP               5 (>=)
            342 EXTENDED_ARG             1
            344 POP_JUMP_IF_FALSE      354

924         346 LOAD_CONST               8 ('sixes')
            348 STORE_FAST               4 (chosen_score)
            350 EXTENDED_ARG             3
            352 JUMP_FORWARD           942 (to 1296)

925     >>  354 LOAD_FAST                1 (possibilities)
            356 LOAD_CONST              24 ('four_of_a')
            358 BINARY_SUBSCR
            360 LOAD_CONST              25 (0)
            362 BINARY_SUBSCR
            364 EXTENDED_ARG             1
            366 POP_JUMP_IF_FALSE      438
            368 LOAD_FAST                3 (comp_score)
            370 LOAD_ATTR               13 (four_of_a_kind)
            372 LOAD_CONST               0 (None)
            374 COMPARE_OP               2 (==)
            376 EXTENDED_ARG             1
            378 POP_JUMP_IF_FALSE      438

926         380 LOAD_FAST                1 (possibilities)
            382 LOAD_CONST              24 ('four_of_a')
            384 BINARY_SUBSCR
            386 LOAD_CONST              26 (1)
            388 BINARY_SUBSCR
            390 STORE_FAST              12 (num)

927         392 LOAD_FAST                5 (current_upper_scores)
            394 LOAD_FAST               12 (num)
            396 BINARY_SUBSCR
            398 LOAD_CONST              25 (0)
            400 BINARY_SUBSCR
            402 EXTENDED_ARG             1
            404 POP_JUMP_IF_FALSE      430
            406 LOAD_FAST               12 (num)
            408 LOAD_CONST              25 (0)
            410 COMPARE_OP               3 (!=)
            412 EXTENDED_ARG             1
            414 POP_JUMP_IF_FALSE      430

928         416 LOAD_FAST                5 (current_upper_scores)
            418 LOAD_FAST               12 (num)
            420 BINARY_SUBSCR
            422 LOAD_CONST              26 (1)
            424 BINARY_SUBSCR
            426 STORE_FAST               4 (chosen_score)
            428 JUMP_FORWARD             4 (to 434)

930     >>  430 LOAD_CONST              27 ('four of a kind')
            432 STORE_FAST               4 (chosen_score)
        >>  434 EXTENDED_ARG             3
            436 JUMP_FORWARD           858 (to 1296)

931     >>  438 LOAD_FAST                1 (possibilities)
            440 LOAD_CONST              28 ('full_ho')
            442 BINARY_SUBSCR
            444 EXTENDED_ARG             1
            446 POP_JUMP_IF_FALSE      468
            448 LOAD_FAST                3 (comp_score)
            450 LOAD_ATTR               14 (full_house)
            452 LOAD_CONST               0 (None)
            454 COMPARE_OP               2 (==)
            456 EXTENDED_ARG             1
            458 POP_JUMP_IF_FALSE      468

932         460 LOAD_CONST              29 ('full house')
            462 STORE_FAST               4 (chosen_score)
            464 EXTENDED_ARG             3
            466 JUMP_FORWARD           828 (to 1296)

933     >>  468 LOAD_FAST                1 (possibilities)
            470 LOAD_CONST              30 ('three_of_a')
            472 BINARY_SUBSCR
            474 LOAD_CONST              25 (0)
            476 BINARY_SUBSCR
            478 EXTENDED_ARG             2
            480 POP_JUMP_IF_FALSE      556
            482 LOAD_FAST                3 (comp_score)
            484 LOAD_ATTR               15 (three_of_a_kind)
            486 LOAD_CONST               0 (None)
            488 COMPARE_OP               2 (==)
            490 EXTENDED_ARG             2
            492 POP_JUMP_IF_FALSE      556

934         494 LOAD_FAST                1 (possibilities)
            496 LOAD_CONST              30 ('three_of_a')
            498 BINARY_SUBSCR
            500 LOAD_CONST              26 (1)
            502 BINARY_SUBSCR
            504 LOAD_CONST              26 (1)
            506 BINARY_SUBSCR
            508 STORE_FAST              12 (num)

935         510 LOAD_FAST                5 (current_upper_scores)
            512 LOAD_FAST               12 (num)
            514 BINARY_SUBSCR
            516 LOAD_CONST              25 (0)
            518 BINARY_SUBSCR
            520 EXTENDED_ARG             2
            522 POP_JUMP_IF_FALSE      548
            524 LOAD_FAST               12 (num)
            526 LOAD_CONST              25 (0)
            528 COMPARE_OP               3 (!=)
            530 EXTENDED_ARG             2
            532 POP_JUMP_IF_FALSE      548

936         534 LOAD_FAST                5 (current_upper_scores)
            536 LOAD_FAST               12 (num)
            538 BINARY_SUBSCR
            540 LOAD_CONST              26 (1)
            542 BINARY_SUBSCR
            544 STORE_FAST               4 (chosen_score)
            546 JUMP_FORWARD             4 (to 552)

938     >>  548 LOAD_CONST              31 ('three of a kind')
            550 STORE_FAST               4 (chosen_score)
        >>  552 EXTENDED_ARG             2
            554 JUMP_FORWARD           740 (to 1296)

939     >>  556 LOAD_FAST                3 (comp_score)
            558 LOAD_ATTR                5 (fives)
            560 LOAD_CONST               0 (None)
            562 COMPARE_OP               2 (==)
            564 EXTENDED_ARG             2
            566 POP_JUMP_IF_FALSE      586
            568 LOAD_FAST               10 (fives)
            570 LOAD_CONST              23 (3)
            572 COMPARE_OP               5 (>=)
            574 EXTENDED_ARG             2
            576 POP_JUMP_IF_FALSE      586

940         578 LOAD_CONST               7 ('fives')
            580 STORE_FAST               4 (chosen_score)
            582 EXTENDED_ARG             2
            584 JUMP_FORWARD           710 (to 1296)

941     >>  586 LOAD_FAST                3 (comp_score)
            588 LOAD_ATTR                4 (fours)
            590 LOAD_CONST               0 (None)
            592 COMPARE_OP               2 (==)
            594 EXTENDED_ARG             2
            596 POP_JUMP_IF_FALSE      616
            598 LOAD_FAST                9 (fours)
            600 LOAD_CONST              23 (3)
            602 COMPARE_OP               5 (>=)
            604 EXTENDED_ARG             2
            606 POP_JUMP_IF_FALSE      616

942         608 LOAD_CONST               6 ('fours')
            610 STORE_FAST               4 (chosen_score)
            612 EXTENDED_ARG             2
            614 JUMP_FORWARD           680 (to 1296)

943     >>  616 LOAD_FAST                3 (comp_score)
            618 LOAD_ATTR                3 (threes)
            620 LOAD_CONST               0 (None)
            622 COMPARE_OP               2 (==)
            624 EXTENDED_ARG             2
            626 POP_JUMP_IF_FALSE      646
            628 LOAD_FAST                8 (threes)
            630 LOAD_CONST              23 (3)
            632 COMPARE_OP               5 (>=)
            634 EXTENDED_ARG             2
            636 POP_JUMP_IF_FALSE      646

944         638 LOAD_CONST               5 ('threes')
            640 STORE_FAST               4 (chosen_score)
            642 EXTENDED_ARG             2
            644 JUMP_FORWARD           650 (to 1296)

945     >>  646 LOAD_FAST                3 (comp_score)
            648 LOAD_ATTR                2 (twos)
            650 LOAD_CONST               0 (None)
            652 COMPARE_OP               2 (==)
            654 EXTENDED_ARG             2
            656 POP_JUMP_IF_FALSE      676
            658 LOAD_FAST                7 (twos)
            660 LOAD_CONST              23 (3)
            662 COMPARE_OP               5 (>=)
            664 EXTENDED_ARG             2
            666 POP_JUMP_IF_FALSE      676

946         668 LOAD_CONST               4 ('twos')
            670 STORE_FAST               4 (chosen_score)
            672 EXTENDED_ARG             2
            674 JUMP_FORWARD           620 (to 1296)

947     >>  676 LOAD_FAST                3 (comp_score)
            678 LOAD_ATTR                1 (ones)
            680 LOAD_CONST               0 (None)
            682 COMPARE_OP               2 (==)
            684 EXTENDED_ARG             2
            686 POP_JUMP_IF_FALSE      706
            688 LOAD_FAST                6 (ones)
            690 LOAD_CONST              23 (3)
            692 COMPARE_OP               5 (>=)
            694 EXTENDED_ARG             2
            696 POP_JUMP_IF_FALSE      706

948         698 LOAD_CONST               3 ('ones')
            700 STORE_FAST               4 (chosen_score)
            702 EXTENDED_ARG             2
            704 JUMP_FORWARD           590 (to 1296)

949     >>  706 LOAD_FAST                3 (comp_score)
            708 LOAD_ATTR                6 (sixes)
            710 LOAD_CONST               0 (None)
            712 COMPARE_OP               2 (==)
            714 EXTENDED_ARG             2
            716 POP_JUMP_IF_FALSE      736
            718 LOAD_FAST               11 (sixes)
            720 LOAD_CONST              32 (2)
            722 COMPARE_OP               2 (==)
            724 EXTENDED_ARG             2
            726 POP_JUMP_IF_FALSE      736

950         728 LOAD_CONST               8 ('sixes')
            730 STORE_FAST               4 (chosen_score)
            732 EXTENDED_ARG             2
            734 JUMP_FORWARD           560 (to 1296)

951     >>  736 LOAD_FAST                3 (comp_score)
            738 LOAD_ATTR                5 (fives)
            740 LOAD_CONST               0 (None)
            742 COMPARE_OP               2 (==)
            744 EXTENDED_ARG             2
            746 POP_JUMP_IF_FALSE      766
            748 LOAD_FAST               10 (fives)
            750 LOAD_CONST              32 (2)
            752 COMPARE_OP               2 (==)
            754 EXTENDED_ARG             2
            756 POP_JUMP_IF_FALSE      766

952         758 LOAD_CONST               7 ('fives')
            760 STORE_FAST               4 (chosen_score)
            762 EXTENDED_ARG             2
            764 JUMP_FORWARD           530 (to 1296)

953     >>  766 LOAD_FAST                3 (comp_score)
            768 LOAD_ATTR                4 (fours)
            770 LOAD_CONST               0 (None)
            772 COMPARE_OP               2 (==)
            774 EXTENDED_ARG             3
            776 POP_JUMP_IF_FALSE      796
            778 LOAD_FAST                9 (fours)
            780 LOAD_CONST              32 (2)
            782 COMPARE_OP               2 (==)
            784 EXTENDED_ARG             3
            786 POP_JUMP_IF_FALSE      796

954         788 LOAD_CONST               6 ('fours')
            790 STORE_FAST               4 (chosen_score)
            792 EXTENDED_ARG             1
            794 JUMP_FORWARD           500 (to 1296)

955     >>  796 LOAD_FAST                3 (comp_score)
            798 LOAD_ATTR                3 (threes)
            800 LOAD_CONST               0 (None)
            802 COMPARE_OP               2 (==)
            804 EXTENDED_ARG             3
            806 POP_JUMP_IF_FALSE      826
            808 LOAD_FAST                8 (threes)
            810 LOAD_CONST              32 (2)
            812 COMPARE_OP               2 (==)
            814 EXTENDED_ARG             3
            816 POP_JUMP_IF_FALSE      826

956         818 LOAD_CONST               5 ('threes')
            820 STORE_FAST               4 (chosen_score)
            822 EXTENDED_ARG             1
            824 JUMP_FORWARD           470 (to 1296)

957     >>  826 LOAD_FAST                3 (comp_score)
            828 LOAD_ATTR                2 (twos)
            830 LOAD_CONST               0 (None)
            832 COMPARE_OP               2 (==)
            834 EXTENDED_ARG             3
            836 POP_JUMP_IF_FALSE      856
            838 LOAD_FAST                7 (twos)
            840 LOAD_CONST              32 (2)
            842 COMPARE_OP               2 (==)
            844 EXTENDED_ARG             3
            846 POP_JUMP_IF_FALSE      856

958         848 LOAD_CONST               4 ('twos')
            850 STORE_FAST               4 (chosen_score)
            852 EXTENDED_ARG             1
            854 JUMP_FORWARD           440 (to 1296)

959     >>  856 LOAD_FAST                3 (comp_score)
            858 LOAD_ATTR                1 (ones)
            860 LOAD_CONST               0 (None)
            862 COMPARE_OP               2 (==)
            864 EXTENDED_ARG             3
            866 POP_JUMP_IF_FALSE      886
            868 LOAD_FAST                6 (ones)
            870 LOAD_CONST              32 (2)
            872 COMPARE_OP               2 (==)
            874 EXTENDED_ARG             3
            876 POP_JUMP_IF_FALSE      886

960         878 LOAD_CONST               3 ('ones')
            880 STORE_FAST               4 (chosen_score)
            882 EXTENDED_ARG             1
            884 JUMP_FORWARD           410 (to 1296)

961     >>  886 LOAD_FAST                3 (comp_score)
            888 LOAD_ATTR                1 (ones)
            890 LOAD_CONST               0 (None)
            892 COMPARE_OP               2 (==)
            894 EXTENDED_ARG             3
            896 POP_JUMP_IF_FALSE      916
            898 LOAD_FAST                6 (ones)
            900 LOAD_CONST              26 (1)
            902 COMPARE_OP               2 (==)
            904 EXTENDED_ARG             3
            906 POP_JUMP_IF_FALSE      916

962         908 LOAD_CONST               3 ('ones')
            910 STORE_FAST               4 (chosen_score)
            912 EXTENDED_ARG             1
            914 JUMP_FORWARD           380 (to 1296)

963     >>  916 LOAD_FAST                3 (comp_score)
            918 LOAD_ATTR                2 (twos)
            920 LOAD_CONST               0 (None)
            922 COMPARE_OP               2 (==)
            924 EXTENDED_ARG             3
            926 POP_JUMP_IF_FALSE      946
            928 LOAD_FAST                7 (twos)
            930 LOAD_CONST              26 (1)
            932 COMPARE_OP               2 (==)
            934 EXTENDED_ARG             3
            936 POP_JUMP_IF_FALSE      946

964         938 LOAD_CONST               4 ('twos')
            940 STORE_FAST               4 (chosen_score)
            942 EXTENDED_ARG             1
            944 JUMP_FORWARD           350 (to 1296)

965     >>  946 LOAD_FAST                3 (comp_score)
            948 LOAD_ATTR                3 (threes)
            950 LOAD_CONST               0 (None)
            952 COMPARE_OP               2 (==)
            954 EXTENDED_ARG             3
            956 POP_JUMP_IF_FALSE      976
            958 LOAD_FAST                8 (threes)
            960 LOAD_CONST              26 (1)
            962 COMPARE_OP               2 (==)
            964 EXTENDED_ARG             3
            966 POP_JUMP_IF_FALSE      976

966         968 LOAD_CONST               5 ('threes')
            970 STORE_FAST               4 (chosen_score)
            972 EXTENDED_ARG             1
            974 JUMP_FORWARD           320 (to 1296)

967     >>  976 LOAD_FAST                3 (comp_score)
            978 LOAD_ATTR                4 (fours)
            980 LOAD_CONST               0 (None)
            982 COMPARE_OP               2 (==)
            984 EXTENDED_ARG             3
            986 POP_JUMP_IF_FALSE     1006
            988 LOAD_FAST                9 (fours)
            990 LOAD_CONST              26 (1)
            992 COMPARE_OP               2 (==)
            994 EXTENDED_ARG             3
            996 POP_JUMP_IF_FALSE     1006

968         998 LOAD_CONST               6 ('fours')
           1000 STORE_FAST               4 (chosen_score)
           1002 EXTENDED_ARG             1
           1004 JUMP_FORWARD           290 (to 1296)

969     >> 1006 LOAD_FAST                3 (comp_score)
           1008 LOAD_ATTR                5 (fives)
           1010 LOAD_CONST               0 (None)
           1012 COMPARE_OP               2 (==)
           1014 EXTENDED_ARG             4
           1016 POP_JUMP_IF_FALSE     1036
           1018 LOAD_FAST               10 (fives)
           1020 LOAD_CONST              26 (1)
           1022 COMPARE_OP               2 (==)
           1024 EXTENDED_ARG             4
           1026 POP_JUMP_IF_FALSE     1036

970        1028 LOAD_CONST               7 ('fives')
           1030 STORE_FAST               4 (chosen_score)
           1032 EXTENDED_ARG             1
           1034 JUMP_FORWARD           260 (to 1296)

971     >> 1036 LOAD_FAST                3 (comp_score)
           1038 LOAD_ATTR                6 (sixes)
           1040 LOAD_CONST               0 (None)
           1042 COMPARE_OP               2 (==)
           1044 EXTENDED_ARG             4
           1046 POP_JUMP_IF_FALSE     1064
           1048 LOAD_FAST               11 (sixes)
           1050 LOAD_CONST              26 (1)
           1052 COMPARE_OP               2 (==)
           1054 EXTENDED_ARG             4
           1056 POP_JUMP_IF_FALSE     1064

972        1058 LOAD_CONST               8 ('sixes')
           1060 STORE_FAST               4 (chosen_score)
           1062 JUMP_FORWARD           232 (to 1296)

973     >> 1064 LOAD_FAST                3 (comp_score)
           1066 LOAD_ATTR               16 (chance)
           1068 LOAD_CONST               0 (None)
           1070 COMPARE_OP               2 (==)
           1072 EXTENDED_ARG             4
           1074 POP_JUMP_IF_FALSE     1082

974        1076 LOAD_CONST              33 ('chance')
           1078 STORE_FAST               4 (chosen_score)
           1080 JUMP_FORWARD           214 (to 1296)

975     >> 1082 LOAD_FAST                3 (comp_score)
           1084 LOAD_ATTR                1 (ones)
           1086 LOAD_CONST               0 (None)
           1088 COMPARE_OP               2 (==)
           1090 EXTENDED_ARG             4
           1092 POP_JUMP_IF_FALSE     1100

976        1094 LOAD_CONST               3 ('ones')
           1096 STORE_FAST               4 (chosen_score)
           1098 JUMP_FORWARD           196 (to 1296)

977     >> 1100 LOAD_FAST                3 (comp_score)
           1102 LOAD_ATTR                2 (twos)
           1104 LOAD_CONST               0 (None)
           1106 COMPARE_OP               2 (==)
           1108 EXTENDED_ARG             4
           1110 POP_JUMP_IF_FALSE     1118

978        1112 LOAD_CONST               4 ('twos')
           1114 STORE_FAST               4 (chosen_score)
           1116 JUMP_FORWARD           178 (to 1296)

979     >> 1118 LOAD_FAST                3 (comp_score)
           1120 LOAD_ATTR                3 (threes)
           1122 LOAD_CONST               0 (None)
           1124 COMPARE_OP               2 (==)
           1126 EXTENDED_ARG             4
           1128 POP_JUMP_IF_FALSE     1136

980        1130 LOAD_CONST               5 ('threes')
           1132 STORE_FAST               4 (chosen_score)
           1134 JUMP_FORWARD           160 (to 1296)

981     >> 1136 LOAD_FAST                3 (comp_score)
           1138 LOAD_ATTR                4 (fours)
           1140 LOAD_CONST               0 (None)
           1142 COMPARE_OP               2 (==)
           1144 EXTENDED_ARG             4
           1146 POP_JUMP_IF_FALSE     1154

982        1148 LOAD_CONST               6 ('fours')
           1150 STORE_FAST               4 (chosen_score)
           1152 JUMP_FORWARD           142 (to 1296)

983     >> 1154 LOAD_FAST                3 (comp_score)
           1156 LOAD_ATTR                5 (fives)
           1158 LOAD_CONST               0 (None)
           1160 COMPARE_OP               2 (==)
           1162 EXTENDED_ARG             4
           1164 POP_JUMP_IF_FALSE     1172

984        1166 LOAD_CONST               7 ('fives')
           1168 STORE_FAST               4 (chosen_score)
           1170 JUMP_FORWARD           124 (to 1296)

985     >> 1172 LOAD_FAST                3 (comp_score)
           1174 LOAD_ATTR               15 (three_of_a_kind)
           1176 LOAD_CONST               0 (None)
           1178 COMPARE_OP               2 (==)
           1180 EXTENDED_ARG             4
           1182 POP_JUMP_IF_FALSE     1190

986        1184 LOAD_CONST              34 ('three_of_a_kind')
           1186 STORE_FAST               4 (chosen_score)
           1188 JUMP_FORWARD           106 (to 1296)

987     >> 1190 LOAD_FAST                3 (comp_score)
           1192 LOAD_ATTR               13 (four_of_a_kind)
           1194 LOAD_CONST               0 (None)
           1196 COMPARE_OP               2 (==)
           1198 EXTENDED_ARG             4
           1200 POP_JUMP_IF_FALSE     1208

988        1202 LOAD_CONST              27 ('four of a kind')
           1204 STORE_FAST               4 (chosen_score)
           1206 JUMP_FORWARD            88 (to 1296)

989     >> 1208 LOAD_FAST                3 (comp_score)
           1210 LOAD_ATTR                6 (sixes)
           1212 LOAD_CONST               0 (None)
           1214 COMPARE_OP               2 (==)
           1216 EXTENDED_ARG             4
           1218 POP_JUMP_IF_FALSE     1226

990        1220 LOAD_CONST               8 ('sixes')
           1222 STORE_FAST               4 (chosen_score)
           1224 JUMP_FORWARD            70 (to 1296)

991     >> 1226 LOAD_FAST                3 (comp_score)
           1228 LOAD_ATTR               14 (full_house)
           1230 LOAD_CONST               0 (None)
           1232 COMPARE_OP               2 (==)
           1234 EXTENDED_ARG             4
           1236 POP_JUMP_IF_FALSE     1244

992        1238 LOAD_CONST              29 ('full house')
           1240 STORE_FAST               4 (chosen_score)
           1242 JUMP_FORWARD            52 (to 1296)

993     >> 1244 LOAD_FAST                3 (comp_score)
           1246 LOAD_ATTR               12 (small_straight)
           1248 LOAD_CONST               0 (None)
           1250 COMPARE_OP               2 (==)
           1252 EXTENDED_ARG             4
           1254 POP_JUMP_IF_FALSE     1262

994        1256 LOAD_CONST              21 ('small straight')
           1258 STORE_FAST               4 (chosen_score)
           1260 JUMP_FORWARD            34 (to 1296)

995     >> 1262 LOAD_FAST                3 (comp_score)
           1264 LOAD_ATTR               11 (large_straight)
           1266 LOAD_CONST               0 (None)
           1268 COMPARE_OP               2 (==)
           1270 EXTENDED_ARG             5
           1272 POP_JUMP_IF_FALSE     1280

996        1274 LOAD_CONST              19 ('large straight')
           1276 STORE_FAST               4 (chosen_score)
           1278 JUMP_FORWARD            16 (to 1296)

997     >> 1280 LOAD_FAST                3 (comp_score)
           1282 LOAD_ATTR               10 (yatzy)
           1284 LOAD_CONST               0 (None)
           1286 COMPARE_OP               2 (==)
           1288 EXTENDED_ARG             5
           1290 POP_JUMP_IF_FALSE     1296

998        1292 LOAD_CONST              17 ('yatzy')
           1294 STORE_FAST               4 (chosen_score)

1000     >> 1296 LOAD_FAST                4 (chosen_score)
           1298 RETURN_VALUE

Disassembly of comp_determine_reroll:
823           0 LOAD_GLOBAL              0 (list)
              2 CALL_FUNCTION            0
              4 STORE_FAST               3 (nums_to_reroll)

824           6 LOAD_FAST                0 (self)
              8 LOAD_ATTR                1 (comp_score)
             10 STORE_FAST               4 (comp_score)

826          12 LOAD_FAST                1 (possibilities)
             14 LOAD_CONST               1 ('small_str')
             16 BINARY_SUBSCR
             18 POP_JUMP_IF_FALSE      220

828          20 LOAD_GLOBAL              2 (set)
             22 LOAD_CONST               2 (<code object <listcomp> at 0x10a3106f0, file "/Users/winniepalangpour/git/winrox.github.io/src/yatzy.py", line 828>)
             24 LOAD_CONST               3 ('PlayYatzy.comp_determine_reroll.<locals>.<listcomp>')
             26 MAKE_FUNCTION            0
             28 LOAD_FAST                2 (hand)
             30 GET_ITER
             32 CALL_FUNCTION            1
             34 CALL_FUNCTION            1
             36 STORE_FAST               5 (set_hand)

829          38 LOAD_GLOBAL              2 (set)
             40 CALL_FUNCTION            0
             42 STORE_FAST               6 (sym_diff)

831          44 LOAD_GLOBAL              3 (len)
             46 LOAD_FAST                5 (set_hand)
             48 LOAD_CONST               4 (1)
             50 LOAD_CONST               5 (2)
             52 LOAD_CONST               6 (3)
             54 LOAD_CONST               7 (4)
             56 BUILD_SET                4
             58 BINARY_SUBTRACT
             60 CALL_FUNCTION            1
             62 LOAD_CONST               8 (0)
             64 COMPARE_OP               2 (==)
             66 POP_JUMP_IF_FALSE       86

832          68 LOAD_FAST                5 (set_hand)
             70 LOAD_CONST               4 (1)
             72 LOAD_CONST               5 (2)
             74 LOAD_CONST               6 (3)
             76 LOAD_CONST               7 (4)
             78 BUILD_SET                4
             80 BINARY_XOR
             82 STORE_FAST               6 (sym_diff)
             84 JUMP_FORWARD            82 (to 168)

833     >>   86 LOAD_GLOBAL              3 (len)
             88 LOAD_FAST                5 (set_hand)
             90 LOAD_CONST               5 (2)
             92 LOAD_CONST               6 (3)
             94 LOAD_CONST               7 (4)
             96 LOAD_CONST               9 (5)
             98 BUILD_SET                4
            100 BINARY_SUBTRACT
            102 CALL_FUNCTION            1
            104 LOAD_CONST               8 (0)
            106 COMPARE_OP               2 (==)
            108 POP_JUMP_IF_FALSE      128

834         110 LOAD_FAST                5 (set_hand)
            112 LOAD_CONST               5 (2)
            114 LOAD_CONST               6 (3)
            116 LOAD_CONST               7 (4)
            118 LOAD_CONST               9 (5)
            120 BUILD_SET                4
            122 BINARY_XOR
            124 STORE_FAST               6 (sym_diff)
            126 JUMP_FORWARD            40 (to 168)

835     >>  128 LOAD_GLOBAL              3 (len)
            130 LOAD_FAST                5 (set_hand)
            132 LOAD_CONST               6 (3)
            134 LOAD_CONST               7 (4)
            136 LOAD_CONST               9 (5)
            138 LOAD_CONST              10 (6)
            140 BUILD_SET                4
            142 BINARY_SUBTRACT
            144 CALL_FUNCTION            1
            146 LOAD_CONST               8 (0)
            148 COMPARE_OP               2 (==)
            150 POP_JUMP_IF_FALSE      168

836         152 LOAD_FAST                5 (set_hand)
            154 LOAD_CONST               6 (3)
            156 LOAD_CONST               7 (4)
            158 LOAD_CONST               9 (5)
            160 LOAD_CONST              10 (6)
            162 BUILD_SET                4
            164 BINARY_XOR
            166 STORE_FAST               6 (sym_diff)

838     >>  168 LOAD_GLOBAL              3 (len)
            170 LOAD_FAST                6 (sym_diff)
            172 CALL_FUNCTION            1
            174 LOAD_CONST               8 (0)
            176 COMPARE_OP               4 (>)
            178 POP_JUMP_IF_FALSE      196

839         180 LOAD_FAST                3 (nums_to_reroll)
            182 LOAD_ATTR                4 (append)
            184 LOAD_FAST                6 (sym_diff)
            186 LOAD_ATTR                5 (pop)
            188 CALL_FUNCTION            0
            190 CALL_FUNCTION            1
            192 POP_TOP
            194 JUMP_FORWARD            20 (to 216)

841     >>  196 LOAD_FAST                4 (comp_score)
            198 LOAD_ATTR                6 (find_duplicates)
            200 LOAD_FAST                2 (hand)
            202 CALL_FUNCTION            1
            204 STORE_FAST               7 (reroll)

842         206 LOAD_FAST                3 (nums_to_reroll)
            208 LOAD_ATTR                4 (append)
            210 LOAD_FAST                7 (reroll)
            212 CALL_FUNCTION            1
            214 POP_TOP
        >>  216 EXTENDED_ARG             3
            218 JUMP_FORWARD           804 (to 1024)

843     >>  220 LOAD_FAST                1 (possibilities)
            222 LOAD_CONST              11 ('four_of_a')
            224 BINARY_SUBSCR
            226 LOAD_CONST               8 (0)
            228 BINARY_SUBSCR
            230 EXTENDED_ARG             1
            232 POP_JUMP_IF_FALSE      282

844         234 SETUP_LOOP              42 (to 278)
            236 LOAD_FAST                2 (hand)
            238 GET_ITER
        >>  240 FOR_ITER                34 (to 276)
            242 STORE_FAST               8 (num)

845         244 LOAD_FAST                8 (num)
            246 LOAD_ATTR                7 (value)
            248 LOAD_FAST                1 (possibilities)
            250 LOAD_CONST              11 ('four_of_a')
            252 BINARY_SUBSCR
            254 LOAD_CONST               4 (1)
            256 BINARY_SUBSCR
            258 COMPARE_OP               3 (!=)
            260 POP_JUMP_IF_FALSE      240

846         262 LOAD_FAST                3 (nums_to_reroll)
            264 LOAD_ATTR                4 (append)
            266 LOAD_FAST                8 (num)
            268 LOAD_ATTR                7 (value)
            270 CALL_FUNCTION            1
            272 POP_TOP
            274 JUMP_ABSOLUTE          240
        >>  276 POP_BLOCK
        >>  278 EXTENDED_ARG             2
            280 JUMP_FORWARD           742 (to 1024)

847     >>  282 LOAD_FAST                1 (possibilities)
            284 LOAD_CONST              12 ('three_of_a')
            286 BINARY_SUBSCR
            288 LOAD_CONST               8 (0)
            290 BINARY_SUBSCR
            292 EXTENDED_ARG             1
            294 POP_JUMP_IF_FALSE      352

848         296 SETUP_LOOP              50 (to 348)
            298 LOAD_FAST                2 (hand)
            300 GET_ITER
        >>  302 FOR_ITER                42 (to 346)
            304 STORE_FAST               8 (num)

849         306 LOAD_FAST                8 (num)
            308 LOAD_ATTR                7 (value)
            310 LOAD_FAST                1 (possibilities)
            312 LOAD_CONST              12 ('three_of_a')
            314 BINARY_SUBSCR
            316 LOAD_CONST               4 (1)
            318 BINARY_SUBSCR
            320 LOAD_CONST               4 (1)
            322 BINARY_SUBSCR
            324 COMPARE_OP               3 (!=)
            326 EXTENDED_ARG             1
            328 POP_JUMP_IF_FALSE      302

850         330 LOAD_FAST                3 (nums_to_reroll)
            332 LOAD_ATTR                4 (append)
            334 LOAD_FAST                8 (num)
            336 LOAD_ATTR                7 (value)
            338 CALL_FUNCTION            1
            340 POP_TOP
            342 EXTENDED_ARG             1
            344 JUMP_ABSOLUTE          302
        >>  346 POP_BLOCK
        >>  348 EXTENDED_ARG             2
            350 JUMP_FORWARD           672 (to 1024)

851     >>  352 LOAD_FAST                1 (possibilities)
            354 LOAD_CONST              13 ('two_pair')
            356 BINARY_SUBSCR
            358 LOAD_CONST               8 (0)
            360 BINARY_SUBSCR
            362 EXTENDED_ARG             1
            364 POP_JUMP_IF_FALSE      456
            366 LOAD_FAST                4 (comp_score)
            368 LOAD_ATTR                8 (full_house)
            370 LOAD_CONST               0 (None)
            372 COMPARE_OP               2 (==)
            374 EXTENDED_ARG             1
            376 POP_JUMP_IF_FALSE      456

852         378 SETUP_LOOP              72 (to 452)
            380 LOAD_FAST                2 (hand)
            382 GET_ITER
        >>  384 FOR_ITER                64 (to 450)
            386 STORE_FAST               8 (num)

853         388 LOAD_FAST                8 (num)
            390 LOAD_ATTR                7 (value)
            392 LOAD_FAST                1 (possibilities)
            394 LOAD_CONST              13 ('two_pair')
            396 BINARY_SUBSCR
            398 LOAD_CONST               4 (1)
            400 BINARY_SUBSCR
            402 LOAD_CONST               8 (0)
            404 BINARY_SUBSCR
            406 COMPARE_OP               3 (!=)
            408 EXTENDED_ARG             1
            410 POP_JUMP_IF_FALSE      384
            412 LOAD_FAST                8 (num)
            414 LOAD_FAST                1 (possibilities)
            416 LOAD_CONST              13 ('two_pair')
            418 BINARY_SUBSCR
            420 LOAD_CONST               4 (1)
            422 BINARY_SUBSCR
            424 LOAD_CONST               4 (1)
            426 BINARY_SUBSCR
            428 COMPARE_OP               3 (!=)
            430 EXTENDED_ARG             1
            432 POP_JUMP_IF_FALSE      384

854         434 LOAD_FAST                3 (nums_to_reroll)
            436 LOAD_ATTR                4 (append)
            438 LOAD_FAST                8 (num)
            440 LOAD_ATTR                7 (value)
            442 CALL_FUNCTION            1
            444 POP_TOP
            446 EXTENDED_ARG             1
            448 JUMP_ABSOLUTE          384
        >>  450 POP_BLOCK
        >>  452 EXTENDED_ARG             2
            454 JUMP_FORWARD           568 (to 1024)

855     >>  456 LOAD_FAST                1 (possibilities)
            458 LOAD_CONST              14 ('three_seq')
            460 BINARY_SUBSCR
            462 LOAD_CONST               8 (0)
            464 BINARY_SUBSCR
            466 EXTENDED_ARG             2
            468 POP_JUMP_IF_FALSE      562
            470 LOAD_FAST                4 (comp_score)
            472 LOAD_ATTR                9 (small_straight)
            474 LOAD_CONST               0 (None)
            476 COMPARE_OP               2 (==)
            478 EXTENDED_ARG             1
            480 POP_JUMP_IF_TRUE       494
            482 LOAD_FAST                4 (comp_score)
            484 LOAD_ATTR               10 (large_straight)
            486 LOAD_CONST               0 (None)
            488 COMPARE_OP               2 (==)
            490 EXTENDED_ARG             2
            492 POP_JUMP_IF_FALSE      562

856     >>  494 LOAD_FAST                1 (possibilities)
            496 LOAD_CONST              14 ('three_seq')
            498 BINARY_SUBSCR
            500 LOAD_CONST               4 (1)
            502 BINARY_SUBSCR
            504 STORE_FAST               9 (nums_not_to_roll)

857         506 SETUP_LOOP              50 (to 558)
            508 LOAD_FAST                2 (hand)
            510 GET_ITER
        >>  512 FOR_ITER                42 (to 556)
            514 STORE_FAST               8 (num)

858         516 LOAD_FAST                8 (num)
            518 LOAD_ATTR                7 (value)
            520 LOAD_FAST                9 (nums_not_to_roll)
            522 COMPARE_OP               7 (not in)
            524 EXTENDED_ARG             2
            526 POP_JUMP_IF_FALSE      542

859         528 LOAD_FAST                3 (nums_to_reroll)
            530 LOAD_ATTR                4 (append)
            532 LOAD_FAST                8 (num)
            534 LOAD_ATTR                7 (value)
            536 CALL_FUNCTION            1
            538 POP_TOP
            540 JUMP_FORWARD            10 (to 552)

861     >>  542 LOAD_FAST                9 (nums_not_to_roll)
            544 LOAD_ATTR               11 (remove)
            546 LOAD_FAST                8 (num)
            548 CALL_FUNCTION            1
            550 POP_TOP
        >>  552 EXTENDED_ARG             2
            554 JUMP_ABSOLUTE          512
        >>  556 POP_BLOCK
        >>  558 EXTENDED_ARG             1
            560 JUMP_FORWARD           462 (to 1024)

862     >>  562 LOAD_FAST                1 (possibilities)
            564 LOAD_CONST              15 ('two_of_a')
            566 BINARY_SUBSCR
            568 LOAD_CONST               8 (0)
            570 BINARY_SUBSCR
            572 EXTENDED_ARG             2
            574 POP_JUMP_IF_FALSE      628

863         576 SETUP_LOOP              46 (to 624)
            578 LOAD_FAST                2 (hand)
            580 GET_ITER
        >>  582 FOR_ITER                38 (to 622)
            584 STORE_FAST               8 (num)

864         586 LOAD_FAST                8 (num)
            588 LOAD_ATTR                7 (value)
            590 LOAD_FAST                1 (possibilities)
            592 LOAD_CONST              15 ('two_of_a')
            594 BINARY_SUBSCR
            596 LOAD_CONST               4 (1)
            598 BINARY_SUBSCR
            600 COMPARE_OP               3 (!=)
            602 EXTENDED_ARG             2
            604 POP_JUMP_IF_FALSE      582

865         606 LOAD_FAST                3 (nums_to_reroll)
            608 LOAD_ATTR                4 (append)
            610 LOAD_FAST                8 (num)
            612 LOAD_ATTR                7 (value)
            614 CALL_FUNCTION            1
            616 POP_TOP
            618 EXTENDED_ARG             2
            620 JUMP_ABSOLUTE          582
        >>  622 POP_BLOCK
        >>  624 EXTENDED_ARG             1
            626 JUMP_FORWARD           396 (to 1024)

866     >>  628 LOAD_CONST               4 (1)
            630 LOAD_FAST                2 (hand)
            632 COMPARE_OP               6 (in)
            634 EXTENDED_ARG             2
            636 POP_JUMP_IF_FALSE      694
            638 LOAD_FAST                4 (comp_score)
            640 LOAD_ATTR               12 (ones)
            642 LOAD_CONST               0 (None)
            644 COMPARE_OP               2 (==)
            646 EXTENDED_ARG             2
            648 POP_JUMP_IF_FALSE      694

867         650 SETUP_LOOP              38 (to 690)
            652 LOAD_FAST                2 (hand)
            654 GET_ITER
        >>  656 FOR_ITER                30 (to 688)
            658 STORE_FAST               8 (num)

868         660 LOAD_FAST                8 (num)
            662 LOAD_ATTR                7 (value)
            664 LOAD_CONST               4 (1)
            666 COMPARE_OP               3 (!=)
            668 EXTENDED_ARG             2
            670 POP_JUMP_IF_FALSE      656

869         672 LOAD_FAST                3 (nums_to_reroll)
            674 LOAD_ATTR                4 (append)
            676 LOAD_FAST                8 (num)
            678 LOAD_ATTR                7 (value)
            680 CALL_FUNCTION            1
            682 POP_TOP
            684 EXTENDED_ARG             2
            686 JUMP_ABSOLUTE          656
        >>  688 POP_BLOCK
        >>  690 EXTENDED_ARG             1
            692 JUMP_FORWARD           330 (to 1024)

870     >>  694 LOAD_CONST               5 (2)
            696 LOAD_FAST                2 (hand)
            698 COMPARE_OP               6 (in)
            700 EXTENDED_ARG             2
            702 POP_JUMP_IF_FALSE      760
            704 LOAD_FAST                4 (comp_score)
            706 LOAD_ATTR               13 (twos)
            708 LOAD_CONST               0 (None)
            710 COMPARE_OP               2 (==)
            712 EXTENDED_ARG             2
            714 POP_JUMP_IF_FALSE      760

871         716 SETUP_LOOP              38 (to 756)
            718 LOAD_FAST                2 (hand)
            720 GET_ITER
        >>  722 FOR_ITER                30 (to 754)
            724 STORE_FAST               8 (num)

872         726 LOAD_FAST                8 (num)
            728 LOAD_ATTR                7 (value)
            730 LOAD_CONST               5 (2)
            732 COMPARE_OP               3 (!=)
            734 EXTENDED_ARG             2
            736 POP_JUMP_IF_FALSE      722

873         738 LOAD_FAST                3 (nums_to_reroll)
            740 LOAD_ATTR                4 (append)
            742 LOAD_FAST                8 (num)
            744 LOAD_ATTR                7 (value)
            746 CALL_FUNCTION            1
            748 POP_TOP
            750 EXTENDED_ARG             2
            752 JUMP_ABSOLUTE          722
        >>  754 POP_BLOCK
        >>  756 EXTENDED_ARG             1
            758 JUMP_FORWARD           264 (to 1024)

874     >>  760 LOAD_CONST               6 (3)
            762 LOAD_FAST                2 (hand)
            764 COMPARE_OP               6 (in)
            766 EXTENDED_ARG             3
            768 POP_JUMP_IF_FALSE      824
            770 LOAD_FAST                4 (comp_score)
            772 LOAD_ATTR               14 (threes)
            774 LOAD_CONST               0 (None)
            776 COMPARE_OP               2 (==)
            778 EXTENDED_ARG             3
            780 POP_JUMP_IF_FALSE      824

875         782 SETUP_LOOP             240 (to 1024)
            784 LOAD_FAST                2 (hand)
            786 GET_ITER
        >>  788 FOR_ITER                30 (to 820)
            790 STORE_FAST               8 (num)

876         792 LOAD_FAST                8 (num)
            794 LOAD_ATTR                7 (value)
            796 LOAD_CONST               6 (3)
            798 COMPARE_OP               3 (!=)
            800 EXTENDED_ARG             3
            802 POP_JUMP_IF_FALSE      788

877         804 LOAD_FAST                3 (nums_to_reroll)
            806 LOAD_ATTR                4 (append)
            808 LOAD_FAST                8 (num)
            810 LOAD_ATTR                7 (value)
            812 CALL_FUNCTION            1
            814 POP_TOP
            816 EXTENDED_ARG             3
            818 JUMP_ABSOLUTE          788
        >>  820 POP_BLOCK
            822 JUMP_FORWARD           200 (to 1024)

878     >>  824 LOAD_CONST               7 (4)
            826 LOAD_FAST                2 (hand)
            828 COMPARE_OP               6 (in)
            830 EXTENDED_ARG             3
            832 POP_JUMP_IF_FALSE      888
            834 LOAD_FAST                4 (comp_score)
            836 LOAD_ATTR               15 (fours)
            838 LOAD_CONST               0 (None)
            840 COMPARE_OP               2 (==)
            842 EXTENDED_ARG             3
            844 POP_JUMP_IF_FALSE      888

879         846 SETUP_LOOP             176 (to 1024)
            848 LOAD_FAST                2 (hand)
            850 GET_ITER
        >>  852 FOR_ITER                30 (to 884)
            854 STORE_FAST               8 (num)

880         856 LOAD_FAST                8 (num)
            858 LOAD_ATTR                7 (value)
            860 LOAD_CONST               7 (4)
            862 COMPARE_OP               3 (!=)
            864 EXTENDED_ARG             3
            866 POP_JUMP_IF_FALSE      852

881         868 LOAD_FAST                3 (nums_to_reroll)
            870 LOAD_ATTR                4 (append)
            872 LOAD_FAST                8 (num)
            874 LOAD_ATTR                7 (value)
            876 CALL_FUNCTION            1
            878 POP_TOP
            880 EXTENDED_ARG             3
            882 JUMP_ABSOLUTE          852
        >>  884 POP_BLOCK
            886 JUMP_FORWARD           136 (to 1024)

882     >>  888 LOAD_CONST               9 (5)
            890 LOAD_FAST                2 (hand)
            892 COMPARE_OP               6 (in)
            894 EXTENDED_ARG             3
            896 POP_JUMP_IF_FALSE      952
            898 LOAD_FAST                4 (comp_score)
            900 LOAD_ATTR               16 (fives)
            902 LOAD_CONST               0 (None)
            904 COMPARE_OP               2 (==)
            906 EXTENDED_ARG             3
            908 POP_JUMP_IF_FALSE      952

883         910 SETUP_LOOP             112 (to 1024)
            912 LOAD_FAST                2 (hand)
            914 GET_ITER
        >>  916 FOR_ITER                30 (to 948)
            918 STORE_FAST               8 (num)

884         920 LOAD_FAST                8 (num)
            922 LOAD_ATTR                7 (value)
            924 LOAD_CONST               9 (5)
            926 COMPARE_OP               3 (!=)
            928 EXTENDED_ARG             3
            930 POP_JUMP_IF_FALSE      916

885         932 LOAD_FAST                3 (nums_to_reroll)
            934 LOAD_ATTR                4 (append)
            936 LOAD_FAST                8 (num)
            938 LOAD_ATTR                7 (value)
            940 CALL_FUNCTION            1
            942 POP_TOP
            944 EXTENDED_ARG             3
            946 JUMP_ABSOLUTE          916
        >>  948 POP_BLOCK
            950 JUMP_FORWARD            72 (to 1024)

886     >>  952 LOAD_CONST              10 (6)
            954 LOAD_FAST                2 (hand)
            956 COMPARE_OP               6 (in)
            958 EXTENDED_ARG             3
            960 POP_JUMP_IF_FALSE     1016
            962 LOAD_FAST                4 (comp_score)
            964 LOAD_ATTR               17 (sixes)
            966 LOAD_CONST               0 (None)
            968 COMPARE_OP               2 (==)
            970 EXTENDED_ARG             3
            972 POP_JUMP_IF_FALSE     1016

887         974 SETUP_LOOP              48 (to 1024)
            976 LOAD_FAST                2 (hand)
            978 GET_ITER
        >>  980 FOR_ITER                30 (to 1012)
            982 STORE_FAST               8 (num)

888         984 LOAD_FAST                8 (num)
            986 LOAD_ATTR                7 (value)
            988 LOAD_CONST              10 (6)
            990 COMPARE_OP               3 (!=)
            992 EXTENDED_ARG             3
            994 POP_JUMP_IF_FALSE      980

889         996 LOAD_FAST                3 (nums_to_reroll)
            998 LOAD_ATTR                4 (append)
           1000 LOAD_FAST                8 (num)
           1002 LOAD_ATTR                7 (value)
           1004 CALL_FUNCTION            1
           1006 POP_TOP
           1008 EXTENDED_ARG             3
           1010 JUMP_ABSOLUTE          980
        >> 1012 POP_BLOCK
           1014 JUMP_FORWARD             8 (to 1024)

891     >> 1016 LOAD_FAST                2 (hand)
           1018 LOAD_ATTR               18 (copy)
           1020 CALL_FUNCTION            0
           1022 STORE_FAST               3 (nums_to_reroll)

893     >> 1024 LOAD_FAST                3 (nums_to_reroll)
           1026 RETURN_VALUE

Disassembly of computer_turn:
1003           0 LOAD_FAST                0 (self)
              2 LOAD_ATTR                0 (comp_score)
              4 STORE_DEREF              0 (comp_score)

1004           6 LOAD_DEREF               0 (comp_score)
              8 STORE_FAST               1 (old_comp_score)

1005          10 LOAD_GLOBAL              1 (YatzyHand)
             12 CALL_FUNCTION            0
             14 STORE_FAST               2 (hand)

1006          16 LOAD_GLOBAL              2 (print)
             18 LOAD_CONST               1 ("\n* Computer's score is {}")
             20 LOAD_ATTR                3 (format)
             22 LOAD_FAST                0 (self)
             24 LOAD_ATTR                0 (comp_score)
             26 LOAD_ATTR                4 (grand_total)
             28 CALL_FUNCTION            1
             30 CALL_FUNCTION            1
             32 POP_TOP

1007          34 LOAD_GLOBAL              2 (print)
             36 LOAD_CONST               2 ('* Computer rolls {} {} {} {} {}')
             38 LOAD_ATTR                3 (format)
             40 LOAD_FAST                2 (hand)
             42 LOAD_CONST               3 (0)
             44 BINARY_SUBSCR
             46 LOAD_FAST                2 (hand)
             48 LOAD_CONST               4 (1)
             50 BINARY_SUBSCR
             52 LOAD_FAST                2 (hand)
             54 LOAD_CONST               5 (2)
             56 BINARY_SUBSCR
             58 LOAD_FAST                2 (hand)
             60 LOAD_CONST               6 (3)
             62 BINARY_SUBSCR
             64 LOAD_FAST                2 (hand)
             66 LOAD_CONST               7 (4)
             68 BINARY_SUBSCR
             70 CALL_FUNCTION            5
             72 CALL_FUNCTION            1
             74 POP_TOP

1009          76 LOAD_CLOSURE             0 (comp_score)
             78 BUILD_TUPLE              1
             80 LOAD_CONST               8 (<code object set_possibilities at 0x10a310c90, file "/Users/winniepalangpour/git/winrox.github.io/src/yatzy.py", line 1009>)
             82 LOAD_CONST               9 ('PlayYatzy.computer_turn.<locals>.set_possibilities')
             84 MAKE_FUNCTION            8
             86 STORE_FAST               3 (set_possibilities)

1022          88 LOAD_FAST                3 (set_possibilities)
             90 LOAD_FAST                2 (hand)
             92 CALL_FUNCTION            1
             94 STORE_FAST               4 (possibilities)

1024          96 LOAD_CONST              10 (<code object comp_invalid_choice at 0x10a310d20, file "/Users/winniepalangpour/git/winrox.github.io/src/yatzy.py", line 1024>)
             98 LOAD_CONST              11 ('PlayYatzy.computer_turn.<locals>.comp_invalid_choice')
            100 MAKE_FUNCTION            0
            102 STORE_FAST               5 (comp_invalid_choice)

1029         104 LOAD_FAST                4 (possibilities)
            106 LOAD_CONST              12 ('yat')
            108 BINARY_SUBSCR
            110 POP_JUMP_IF_FALSE      148
            112 LOAD_DEREF               0 (comp_score)
            114 LOAD_ATTR                5 (yatzy)
            116 LOAD_CONST               0 (None)
            118 COMPARE_OP               2 (==)
            120 POP_JUMP_IF_FALSE      148

1030         122 LOAD_DEREF               0 (comp_score)
            124 LOAD_ATTR                6 (set_score)
            126 LOAD_FAST                2 (hand)
            128 LOAD_CONST              13 ('yatzy')
            130 LOAD_FAST                5 (comp_invalid_choice)
            132 CALL_FUNCTION            3
            134 POP_TOP

1031         136 LOAD_GLOBAL              2 (print)
            138 LOAD_CONST              14 ('* YATZY!\n')
            140 CALL_FUNCTION            1
            142 POP_TOP
            144 EXTENDED_ARG             1
            146 JUMP_FORWARD           414 (to 562)

1032     >>  148 LOAD_FAST                4 (possibilities)
            150 LOAD_CONST              15 ('large_str')
            152 BINARY_SUBSCR
            154 POP_JUMP_IF_FALSE      192
            156 LOAD_DEREF               0 (comp_score)
            158 LOAD_ATTR                7 (large_straight)
            160 LOAD_CONST               0 (None)
            162 COMPARE_OP               2 (==)
            164 POP_JUMP_IF_FALSE      192

1033         166 LOAD_DEREF               0 (comp_score)
            168 LOAD_ATTR                6 (set_score)
            170 LOAD_FAST                2 (hand)
            172 LOAD_CONST              16 ('large straight')
            174 LOAD_FAST                5 (comp_invalid_choice)
            176 CALL_FUNCTION            3
            178 POP_TOP

1034         180 LOAD_GLOBAL              2 (print)
            182 LOAD_CONST              17 ('* Computer chooses large straight')
            184 CALL_FUNCTION            1
            186 POP_TOP
            188 EXTENDED_ARG             1
            190 JUMP_FORWARD           370 (to 562)

1035     >>  192 LOAD_FAST                4 (possibilities)
            194 LOAD_CONST              18 ('full_ho')
            196 BINARY_SUBSCR
            198 POP_JUMP_IF_FALSE      236
            200 LOAD_DEREF               0 (comp_score)
            202 LOAD_ATTR                8 (full_house)
            204 LOAD_CONST               0 (None)
            206 COMPARE_OP               2 (==)
            208 POP_JUMP_IF_FALSE      236

1036         210 LOAD_DEREF               0 (comp_score)
            212 LOAD_ATTR                6 (set_score)
            214 LOAD_FAST                2 (hand)
            216 LOAD_CONST              19 ('full house')
            218 LOAD_FAST                5 (comp_invalid_choice)
            220 CALL_FUNCTION            3
            222 POP_TOP

1037         224 LOAD_GLOBAL              2 (print)
            226 LOAD_CONST              20 ('* Computer chooses full house')
            228 CALL_FUNCTION            1
            230 POP_TOP
            232 EXTENDED_ARG             1
            234 JUMP_FORWARD           326 (to 562)

1038     >>  236 LOAD_FAST                4 (possibilities)
            238 LOAD_CONST              21 ('small_str')
            240 BINARY_SUBSCR
            242 EXTENDED_ARG             1
            244 POP_JUMP_IF_FALSE      296
            246 LOAD_DEREF               0 (comp_score)
            248 LOAD_ATTR                9 (small_straight)
            250 LOAD_CONST               0 (None)
            252 COMPARE_OP               2 (==)
            254 EXTENDED_ARG             1
            256 POP_JUMP_IF_FALSE      296
            258 LOAD_DEREF               0 (comp_score)
            260 LOAD_ATTR                7 (large_straight)
            262 LOAD_CONST               0 (None)
            264 COMPARE_OP               3 (!=)
            266 EXTENDED_ARG             1
            268 POP_JUMP_IF_FALSE      296

1039         270 LOAD_DEREF               0 (comp_score)
            272 LOAD_ATTR                6 (set_score)
            274 LOAD_FAST                2 (hand)
            276 LOAD_CONST              22 ('small straight')
            278 LOAD_FAST                5 (comp_invalid_choice)
            280 CALL_FUNCTION            3
            282 POP_TOP

1040         284 LOAD_GLOBAL              2 (print)
            286 LOAD_CONST              23 ('* Computer chooses small straight')
            288 CALL_FUNCTION            1
            290 POP_TOP
            292 EXTENDED_ARG             1
            294 JUMP_FORWARD           266 (to 562)

1042     >>  296 LOAD_FAST                2 (hand)
            298 STORE_FAST               6 (old_hand)

1043         300 LOAD_FAST                0 (self)
            302 LOAD_ATTR               10 (comp_determine_reroll)
            304 LOAD_FAST                4 (possibilities)
            306 LOAD_FAST                2 (hand)
            308 CALL_FUNCTION            2
            310 STORE_FAST               7 (nums_to_reroll)

1044         312 LOAD_CONST              24 (', ')
            314 LOAD_ATTR               11 (join)
            316 LOAD_CONST              25 (<code object <listcomp> at 0x10a310db0, file "/Users/winniepalangpour/git/winrox.github.io/src/yatzy.py", line 1044>)
            318 LOAD_CONST              26 ('PlayYatzy.computer_turn.<locals>.<listcomp>')
            320 MAKE_FUNCTION            0
            322 LOAD_FAST                7 (nums_to_reroll)
            324 GET_ITER
            326 CALL_FUNCTION            1
            328 CALL_FUNCTION            1
            330 STORE_FAST               8 (nums)

1045         332 LOAD_GLOBAL              2 (print)
            334 LOAD_CONST              27 ('* Computer re-rolls ')
            336 LOAD_FAST                8 (nums)
            338 FORMAT_VALUE             0
            340 LOAD_CONST              28 ('.')
            342 BUILD_STRING             3
            344 CALL_FUNCTION            1
            346 POP_TOP

1047         348 SETUP_LOOP              34 (to 384)
            350 LOAD_FAST                7 (nums_to_reroll)
            352 GET_ITER
        >>  354 FOR_ITER                26 (to 382)
            356 STORE_FAST               9 (num)

1048         358 LOAD_FAST                9 (num)
            360 LOAD_FAST                6 (old_hand)
            362 COMPARE_OP               6 (in)
            364 EXTENDED_ARG             1
            366 POP_JUMP_IF_FALSE      354

1049         368 LOAD_FAST                6 (old_hand)
            370 LOAD_ATTR               12 (remove)
            372 LOAD_FAST                9 (num)
            374 CALL_FUNCTION            1
            376 POP_TOP
            378 EXTENDED_ARG             1
            380 JUMP_ABSOLUTE          354
        >>  382 POP_BLOCK

1050     >>  384 LOAD_CONST              29 (5)
            386 LOAD_GLOBAL             13 (len)
            388 LOAD_FAST                6 (old_hand)
            390 CALL_FUNCTION            1
            392 BINARY_SUBTRACT
            394 STORE_FAST              10 (new_dice_needed)

1051         396 LOAD_FAST                6 (old_hand)
            398 STORE_FAST              11 (new_hand)

1053         400 SETUP_LOOP              30 (to 432)
            402 LOAD_GLOBAL             14 (range)
            404 LOAD_FAST               10 (new_dice_needed)
            406 CALL_FUNCTION            1
            408 GET_ITER
        >>  410 FOR_ITER                18 (to 430)
            412 STORE_FAST              12 (_)

1054         414 LOAD_FAST               11 (new_hand)
            416 LOAD_ATTR               15 (append)
            418 LOAD_GLOBAL             16 (D6)
            420 CALL_FUNCTION            0
            422 CALL_FUNCTION            1
            424 POP_TOP
            426 EXTENDED_ARG             1
            428 JUMP_ABSOLUTE          410
        >>  430 POP_BLOCK

1056     >>  432 LOAD_FAST               11 (new_hand)
            434 LOAD_ATTR               17 (sort)
            436 CALL_FUNCTION            0
            438 POP_TOP

1057         440 LOAD_GLOBAL              2 (print)
            442 LOAD_CONST              30 ("* Computer's new hand is ")
            444 LOAD_FAST               11 (new_hand)
            446 LOAD_CONST               3 (0)
            448 BINARY_SUBSCR
            450 FORMAT_VALUE             0
            452 LOAD_CONST              31 (' ')
            454 LOAD_FAST               11 (new_hand)
            456 LOAD_CONST               4 (1)
            458 BINARY_SUBSCR
            460 FORMAT_VALUE             0
            462 LOAD_CONST              31 (' ')
            464 LOAD_FAST               11 (new_hand)
            466 LOAD_CONST               5 (2)
            468 BINARY_SUBSCR
            470 FORMAT_VALUE             0
            472 LOAD_CONST              31 (' ')
            474 LOAD_FAST               11 (new_hand)
            476 LOAD_CONST               6 (3)
            478 BINARY_SUBSCR
            480 FORMAT_VALUE             0
            482 LOAD_CONST              31 (' ')
            484 LOAD_FAST               11 (new_hand)
            486 LOAD_CONST               7 (4)
            488 BINARY_SUBSCR
            490 FORMAT_VALUE             0
            492 BUILD_STRING            10
            494 CALL_FUNCTION            1
            496 POP_TOP

1058         498 LOAD_FAST                0 (self)
            500 LOAD_ATTR               18 (comp_choose_score)
            502 LOAD_FAST                3 (set_possibilities)
            504 LOAD_FAST               11 (new_hand)
            506 CALL_FUNCTION            1
            508 LOAD_FAST               11 (new_hand)
            510 CALL_FUNCTION            2
            512 STORE_FAST              13 (chosen_score)

1060         514 LOAD_FAST               13 (chosen_score)
            516 LOAD_CONST               0 (None)
            518 COMPARE_OP               3 (!=)
            520 EXTENDED_ARG             2
            522 POP_JUMP_IF_FALSE      554

1061         524 LOAD_DEREF               0 (comp_score)
            526 LOAD_ATTR                6 (set_score)
            528 LOAD_FAST               11 (new_hand)
            530 LOAD_FAST               13 (chosen_score)
            532 LOAD_FAST                5 (comp_invalid_choice)
            534 CALL_FUNCTION            3
            536 POP_TOP

1062         538 LOAD_GLOBAL              2 (print)
            540 LOAD_CONST              32 ('* Computer chooses ')
            542 LOAD_FAST               13 (chosen_score)
            544 FORMAT_VALUE             0
            546 BUILD_STRING             2
            548 CALL_FUNCTION            1
            550 POP_TOP
            552 JUMP_FORWARD             8 (to 562)

1064     >>  554 LOAD_GLOBAL             19 (throw)
            556 LOAD_CONST              33 ('ERROR chosen_score is unset!!!')
            558 CALL_FUNCTION            1
            560 POP_TOP

1067     >>  562 LOAD_FAST                1 (old_comp_score)
            564 LOAD_ATTR               20 (yatzy_bonus)
            566 LOAD_DEREF               0 (comp_score)
            568 LOAD_ATTR               20 (yatzy_bonus)
            570 COMPARE_OP               3 (!=)
            572 EXTENDED_ARG             2
            574 POP_JUMP_IF_FALSE      586

1068         576 LOAD_GLOBAL              2 (print)
            578 LOAD_CONST              34 ('* Computer scores yatzy bonus +100')
            580 CALL_FUNCTION            1
            582 POP_TOP
            584 JUMP_FORWARD            22 (to 608)

1069     >>  586 LOAD_FAST                1 (old_comp_score)
            588 LOAD_ATTR               21 (bonus)
            590 LOAD_DEREF               0 (comp_score)
            592 LOAD_ATTR               21 (bonus)
            594 COMPARE_OP               3 (!=)
            596 EXTENDED_ARG             2
            598 POP_JUMP_IF_FALSE      608

1070         600 LOAD_GLOBAL              2 (print)
            602 LOAD_CONST              35 ('* Computer scores upper section bonus +35')
            604 CALL_FUNCTION            1
            606 POP_TOP

1071     >>  608 LOAD_GLOBAL              2 (print)
            610 LOAD_CONST              36 ("* Computer's new score is ")
            612 LOAD_FAST                0 (self)
            614 LOAD_ATTR                0 (comp_score)
            616 LOAD_ATTR                4 (grand_total)
            618 FORMAT_VALUE             0
            620 BUILD_STRING             2
            622 CALL_FUNCTION            1
            624 POP_TOP

1072         626 LOAD_FAST                0 (self)
            628 DUP_TOP
            630 LOAD_ATTR               22 (turn)
            632 LOAD_CONST               4 (1)
            634 INPLACE_ADD
            636 ROT_TWO
            638 STORE_ATTR              22 (turn)
            640 LOAD_CONST               0 (None)
            642 RETURN_VALUE

Disassembly of end_game:
774           0 LOAD_FAST                0 (self)
              2 LOAD_ATTR                0 (clear_screen)
              4 CALL_FUNCTION            0
              6 POP_TOP

775           8 LOAD_GLOBAL              1 (print)
             10 LOAD_CONST               1 ('\nGAME OVER\nHere are the final scorecards:\n')
             12 CALL_FUNCTION            1
             14 POP_TOP

776          16 LOAD_FAST                0 (self)
             18 LOAD_ATTR                2 (comp_score)
             20 LOAD_ATTR                3 (print_score)
             22 CALL_FUNCTION            0
             24 POP_TOP

777          26 LOAD_GLOBAL              4 (sleep)
             28 LOAD_CONST               2 (1)
             30 CALL_FUNCTION            1
             32 POP_TOP

778          34 LOAD_FAST                0 (self)
             36 LOAD_ATTR                5 (score)
             38 LOAD_ATTR                3 (print_score)
             40 CALL_FUNCTION            0
             42 POP_TOP

779          44 LOAD_GLOBAL              1 (print)
             46 LOAD_CONST               3 ('\n\nYou scored ')
             48 LOAD_FAST                0 (self)
             50 LOAD_ATTR                5 (score)
             52 LOAD_ATTR                6 (grand_total)
             54 FORMAT_VALUE             0
             56 LOAD_CONST               4 (' points')
             58 BUILD_STRING             3
             60 CALL_FUNCTION            1
             62 POP_TOP

780          64 LOAD_GLOBAL              4 (sleep)
             66 LOAD_CONST               2 (1)
             68 CALL_FUNCTION            1
             70 POP_TOP

781          72 LOAD_GLOBAL              1 (print)
             74 LOAD_CONST               5 ('The computer scored ')
             76 LOAD_FAST                0 (self)
             78 LOAD_ATTR                2 (comp_score)
             80 LOAD_ATTR                6 (grand_total)
             82 FORMAT_VALUE             0
             84 LOAD_CONST               4 (' points')
             86 BUILD_STRING             3
             88 CALL_FUNCTION            1
             90 POP_TOP

782          92 LOAD_FAST                0 (self)
             94 LOAD_ATTR                5 (score)
             96 LOAD_ATTR                6 (grand_total)
             98 LOAD_FAST                0 (self)
            100 LOAD_ATTR                2 (comp_score)
            102 LOAD_ATTR                6 (grand_total)
            104 COMPARE_OP               4 (>)
            106 POP_JUMP_IF_FALSE      118

783         108 LOAD_GLOBAL              1 (print)
            110 LOAD_CONST               6 ('Congratulations, you won!!! 🎉 ')
            112 CALL_FUNCTION            1
            114 POP_TOP
            116 JUMP_FORWARD            34 (to 152)

784     >>  118 LOAD_FAST                0 (self)
            120 LOAD_ATTR                5 (score)
            122 LOAD_ATTR                6 (grand_total)
            124 LOAD_FAST                0 (self)
            126 LOAD_ATTR                2 (comp_score)
            128 LOAD_ATTR                6 (grand_total)
            130 COMPARE_OP               2 (==)
            132 POP_JUMP_IF_FALSE      144

785         134 LOAD_GLOBAL              1 (print)
            136 LOAD_CONST               7 ('Yuck, looks like you and the computer tie.')
            138 CALL_FUNCTION            1
            140 POP_TOP
            142 JUMP_FORWARD             8 (to 152)

787     >>  144 LOAD_GLOBAL              1 (print)
            146 LOAD_CONST               8 ('Darn! The computer beat you this time.')
            148 CALL_FUNCTION            1
            150 POP_TOP

788     >>  152 LOAD_GLOBAL              4 (sleep)
            154 LOAD_CONST               2 (1)
            156 CALL_FUNCTION            1
            158 POP_TOP

789         160 LOAD_GLOBAL              1 (print)
            162 LOAD_CONST               9 ('See you next time 👋 ')
            164 CALL_FUNCTION            1
            166 POP_TOP

790         168 LOAD_GLOBAL              4 (sleep)
            170 LOAD_CONST              10 (2)
            172 CALL_FUNCTION            1
            174 POP_TOP

791         176 LOAD_CONST              11 (False)
            178 LOAD_FAST                0 (self)
            180 STORE_ATTR               7 (playing)
            182 LOAD_CONST               0 (None)
            184 RETURN_VALUE

Disassembly of invalid_choice:
769           0 LOAD_GLOBAL              0 (print)
              2 LOAD_CONST               1 ("Sorry you've already used this portion of your scorecard\nOR your choice didn't match an item on the scorecard.\nPlease try again.\n")
              4 CALL_FUNCTION            1
              6 POP_TOP

770           8 LOAD_FAST                0 (self)
             10 LOAD_ATTR                1 (choose_score)
             12 LOAD_FAST                1 (hand)
             14 CALL_FUNCTION            1
             16 POP_TOP

771          18 LOAD_FAST                0 (self)
             20 DUP_TOP
             22 LOAD_ATTR                2 (turn)
             24 LOAD_CONST               2 (1)
             26 INPLACE_SUBTRACT
             28 ROT_TWO
             30 STORE_ATTR               2 (turn)
             32 LOAD_CONST               0 (None)
             34 RETURN_VALUE

Disassembly of play:
1075           0 LOAD_FAST                0 (self)
              2 LOAD_ATTR                0 (turn)
              4 LOAD_CONST               1 (2)
              6 BINARY_MODULO
              8 LOAD_CONST               2 (0)
             10 COMPARE_OP               2 (==)
             12 STORE_FAST               1 (comp_turn)

1076          14 LOAD_FAST                0 (self)
             16 LOAD_ATTR                1 (score)
             18 LOAD_ATTR                2 (lower_total)
             20 LOAD_CONST               0 (None)
             22 COMPARE_OP               3 (!=)
             24 POP_JUMP_IF_FALSE       70
             26 LOAD_FAST                0 (self)
             28 LOAD_ATTR                1 (score)
             30 LOAD_ATTR                3 (upper_total)
             32 LOAD_CONST               0 (None)
             34 COMPARE_OP               3 (!=)
             36 POP_JUMP_IF_FALSE       70
             38 LOAD_FAST                0 (self)
             40 LOAD_ATTR                4 (comp_score)
             42 LOAD_ATTR                2 (lower_total)
             44 LOAD_CONST               0 (None)
             46 COMPARE_OP               3 (!=)
             48 POP_JUMP_IF_FALSE       70
             50 LOAD_FAST                0 (self)
             52 LOAD_ATTR                4 (comp_score)
             54 LOAD_ATTR                3 (upper_total)
             56 LOAD_CONST               0 (None)
             58 COMPARE_OP               3 (!=)
             60 POP_JUMP_IF_FALSE       70

1077          62 LOAD_FAST                0 (self)
             64 LOAD_ATTR                5 (end_game)
             66 CALL_FUNCTION            0
             68 RETURN_VALUE

1078     >>   70 LOAD_FAST                1 (comp_turn)
             72 UNARY_NOT
             74 POP_JUMP_IF_FALSE      114
             76 LOAD_FAST                0 (self)
             78 LOAD_ATTR                6 (help_shown_last)
             80 UNARY_NOT
             82 POP_JUMP_IF_FALSE      114
             84 LOAD_FAST                0 (self)
             86 LOAD_ATTR                0 (turn)
             88 LOAD_CONST               3 (1)
             90 COMPARE_OP               3 (!=)
             92 POP_JUMP_IF_FALSE      114

1079          94 LOAD_GLOBAL              7 (print)
             96 LOAD_CONST               4 ("\nIt's your turn now {}. Type 'roll' to continue.")
             98 LOAD_ATTR                8 (format)
            100 LOAD_FAST                0 (self)
            102 LOAD_ATTR                1 (score)
            104 LOAD_ATTR                9 (player_name)
            106 CALL_FUNCTION            1
            108 CALL_FUNCTION            1
            110 POP_TOP
            112 JUMP_FORWARD            58 (to 172)

1080     >>  114 LOAD_FAST                0 (self)
            116 LOAD_ATTR                6 (help_shown_last)
            118 POP_JUMP_IF_FALSE      148
            120 LOAD_FAST                0 (self)
            122 LOAD_ATTR                1 (score)
            124 LOAD_ATTR                9 (player_name)
            126 LOAD_CONST               0 (None)
            128 COMPARE_OP               3 (!=)
            130 POP_JUMP_IF_FALSE      148

1081         132 LOAD_GLOBAL              7 (print)
            134 LOAD_CONST               5 ("Please type 'roll' to continue.")
            136 CALL_FUNCTION            1
            138 POP_TOP

1082         140 LOAD_CONST               6 (False)
            142 LOAD_FAST                0 (self)
            144 STORE_ATTR               6 (help_shown_last)
            146 JUMP_FORWARD            24 (to 172)

1083     >>  148 LOAD_FAST                0 (self)
            150 LOAD_ATTR                6 (help_shown_last)
            152 POP_JUMP_IF_FALSE      172
            154 LOAD_FAST                0 (self)
            156 LOAD_ATTR                1 (score)
            158 LOAD_ATTR                9 (player_name)
            160 LOAD_CONST               0 (None)
            162 COMPARE_OP               2 (==)
            164 POP_JUMP_IF_FALSE      172

1084         166 LOAD_CONST               6 (False)
            168 LOAD_FAST                0 (self)
            170 STORE_ATTR               6 (help_shown_last)

1086     >>  172 LOAD_FAST                0 (self)
            174 LOAD_ATTR                0 (turn)
            176 LOAD_CONST               3 (1)
            178 COMPARE_OP               2 (==)
            180 JUMP_IF_FALSE_OR_POP   192
            182 LOAD_FAST                0 (self)
            184 LOAD_ATTR                1 (score)
            186 LOAD_ATTR                9 (player_name)
            188 LOAD_CONST               0 (None)
            190 COMPARE_OP               2 (==)
        >>  192 EXTENDED_ARG             1
            194 POP_JUMP_IF_FALSE      288

1087         196 LOAD_GLOBAL              7 (print)
            198 LOAD_CONST               7 ('Welcome to script yatzy!')
            200 CALL_FUNCTION            1
            202 POP_TOP

1088         204 LOAD_GLOBAL             10 (input)
            206 LOAD_CONST               8 ('What is your name?\n>>  ')
            208 CALL_FUNCTION            1
            210 STORE_FAST               2 (name)

1089         212 LOAD_FAST                2 (name)
            214 LOAD_CONST               9 ('h')
            216 COMPARE_OP               2 (==)
            218 POP_JUMP_IF_TRUE       228
            220 LOAD_FAST                2 (name)
            222 LOAD_CONST              10 ('help')
            224 COMPARE_OP               2 (==)
            226 POP_JUMP_IF_FALSE      244

1090     >>  228 LOAD_FAST                0 (self)
            230 LOAD_ATTR               11 (show_help)
            232 CALL_FUNCTION            0
            234 POP_TOP

1091         236 LOAD_FAST                0 (self)
            238 LOAD_ATTR               12 (play)
            240 CALL_FUNCTION            0
            242 RETURN_VALUE

1093     >>  244 LOAD_FAST                0 (self)
            246 LOAD_ATTR                1 (score)
            248 LOAD_ATTR               13 (set_name)
            250 LOAD_FAST                2 (name)
            252 CALL_FUNCTION            1
            254 POP_TOP

1095         256 LOAD_GLOBAL              7 (print)

1102         258 LOAD_CONST              11 ("\n    Hi {}.\n\n    You'll be playing against one other computer player.\n    When you are done rolling fill in your scorecard by\n    typing a matching category from the scorecard below.\n\n    Type 'help' if you get lost.")
            260 LOAD_ATTR                8 (format)
            262 LOAD_FAST                2 (name)
            264 CALL_FUNCTION            1
            266 CALL_FUNCTION            1
            268 POP_TOP

1103         270 LOAD_FAST                0 (self)
            272 LOAD_ATTR                1 (score)
            274 LOAD_ATTR               14 (print_score)
            276 CALL_FUNCTION            0
            278 POP_TOP

1104         280 LOAD_GLOBAL              7 (print)
            282 LOAD_CONST              12 ("\nType 'roll' or 'r' to begin playing 😀")
            284 CALL_FUNCTION            1
            286 POP_TOP

1106     >>  288 LOAD_FAST                1 (comp_turn)
            290 EXTENDED_ARG             1
            292 POP_JUMP_IF_FALSE      304

1107         294 LOAD_FAST                0 (self)
            296 LOAD_ATTR               15 (computer_turn)
            298 CALL_FUNCTION            0
            300 POP_TOP
            302 JUMP_FORWARD           142 (to 446)

1109     >>  304 LOAD_FAST                0 (self)
            306 LOAD_ATTR                0 (turn)
            308 LOAD_CONST               3 (1)
            310 COMPARE_OP               3 (!=)
            312 EXTENDED_ARG             1
            314 POP_JUMP_IF_FALSE      326

1110         316 LOAD_FAST                0 (self)
            318 LOAD_ATTR                1 (score)
            320 LOAD_ATTR               14 (print_score)
            322 CALL_FUNCTION            0
            324 POP_TOP

1112     >>  326 LOAD_GLOBAL             10 (input)
            328 LOAD_CONST              13 ('>>  ')
            330 CALL_FUNCTION            1
            332 LOAD_ATTR               16 (lower)
            334 CALL_FUNCTION            0
            336 LOAD_ATTR               17 (strip)
            338 CALL_FUNCTION            0
            340 STORE_FAST               3 (action)

1114         342 LOAD_FAST                3 (action)
            344 LOAD_CONST              14 ('roll')
            346 COMPARE_OP               2 (==)
            348 EXTENDED_ARG             1
            350 POP_JUMP_IF_TRUE       362
            352 LOAD_FAST                3 (action)
            354 LOAD_CONST              15 ('r')
            356 COMPARE_OP               2 (==)
            358 EXTENDED_ARG             1
            360 POP_JUMP_IF_FALSE      372

1115     >>  362 LOAD_FAST                0 (self)
            364 LOAD_ATTR               18 (roll_action)
            366 CALL_FUNCTION            0
            368 POP_TOP
            370 JUMP_FORWARD            74 (to 446)

1116     >>  372 LOAD_FAST                3 (action)
            374 LOAD_CONST              16 ('quit')
            376 COMPARE_OP               2 (==)
            378 EXTENDED_ARG             1
            380 POP_JUMP_IF_TRUE       392
            382 LOAD_FAST                3 (action)
            384 LOAD_CONST              17 ('q')
            386 COMPARE_OP               2 (==)
            388 EXTENDED_ARG             1
            390 POP_JUMP_IF_FALSE      408

1117     >>  392 LOAD_FAST                0 (self)
            394 LOAD_ATTR               19 (clear_screen)
            396 CALL_FUNCTION            0
            398 POP_TOP

1118         400 LOAD_CONST               6 (False)
            402 LOAD_FAST                0 (self)
            404 STORE_ATTR              20 (playing)
            406 JUMP_FORWARD            38 (to 446)

1119     >>  408 LOAD_FAST                3 (action)
            410 LOAD_CONST              10 ('help')
            412 COMPARE_OP               2 (==)
            414 EXTENDED_ARG             1
            416 POP_JUMP_IF_TRUE       428
            418 LOAD_FAST                3 (action)
            420 LOAD_CONST               9 ('h')
            422 COMPARE_OP               2 (==)
            424 EXTENDED_ARG             1
            426 POP_JUMP_IF_FALSE      438

1120     >>  428 LOAD_FAST                0 (self)
            430 LOAD_ATTR               11 (show_help)
            432 CALL_FUNCTION            0
            434 POP_TOP
            436 JUMP_FORWARD             8 (to 446)

1122     >>  438 LOAD_GLOBAL              7 (print)
            440 LOAD_CONST              18 ("I'm sorry your choice wasn't recognized.\nPlease type one of the following next time: 'roll', 'help', or 'quit'\nYour turn will now restart.")
            442 CALL_FUNCTION            1
            444 POP_TOP
        >>  446 LOAD_CONST               0 (None)
            448 RETURN_VALUE

Disassembly of print_hand:
707           0 LOAD_FAST                2 (new)
              2 POP_JUMP_IF_FALSE        8
              4 LOAD_CONST               1 ('new ')
              6 JUMP_FORWARD             2 (to 10)
        >>    8 LOAD_CONST               2 ('')
        >>   10 STORE_FAST               3 (re_rolled)

708          12 LOAD_GLOBAL              0 (print)
             14 LOAD_CONST               3 ('Your {}hand is {} {} {} {} {}')
             16 LOAD_ATTR                1 (format)
             18 LOAD_FAST                3 (re_rolled)
             20 LOAD_FAST                1 (hand)
             22 LOAD_CONST               4 (0)
             24 BINARY_SUBSCR
             26 LOAD_FAST                1 (hand)
             28 LOAD_CONST               5 (1)
             30 BINARY_SUBSCR
             32 LOAD_FAST                1 (hand)
             34 LOAD_CONST               6 (2)
             36 BINARY_SUBSCR
             38 LOAD_FAST                1 (hand)
             40 LOAD_CONST               7 (3)
             42 BINARY_SUBSCR
             44 LOAD_FAST                1 (hand)
             46 LOAD_CONST               8 (4)
             48 BINARY_SUBSCR
             50 CALL_FUNCTION            6
             52 CALL_FUNCTION            1
             54 POP_TOP
             56 LOAD_CONST               0 (None)
             58 RETURN_VALUE

Disassembly of prompt_to_roll_again_and_score:
689           0 LOAD_FAST                0 (self)
              2 LOAD_ATTR                0 (help_shown_last)
              4 POP_JUMP_IF_FALSE       24

690           6 LOAD_FAST                0 (self)
              8 LOAD_ATTR                1 (print_hand)
             10 LOAD_FAST                1 (hand)
             12 LOAD_CONST               1 (False)
             14 CALL_FUNCTION            2
             16 POP_TOP

691          18 LOAD_CONST               1 (False)
             20 LOAD_FAST                0 (self)
             22 STORE_ATTR               0 (help_shown_last)

692     >>   24 LOAD_GLOBAL              2 (input)
             26 LOAD_CONST               2 ('Would you like to roll again? Y/N\n>>  ')
             28 CALL_FUNCTION            1
             30 LOAD_ATTR                3 (lower)
             32 CALL_FUNCTION            0
             34 LOAD_ATTR                4 (strip)
             36 CALL_FUNCTION            0
             38 STORE_FAST               2 (roll_again)

693          40 LOAD_FAST                2 (roll_again)
             42 LOAD_CONST               3 ('help')
             44 COMPARE_OP               2 (==)
             46 POP_JUMP_IF_TRUE        56
             48 LOAD_FAST                2 (roll_again)
             50 LOAD_CONST               4 ('h')
             52 COMPARE_OP               2 (==)
             54 POP_JUMP_IF_FALSE       74

694     >>   56 LOAD_FAST                0 (self)
             58 LOAD_ATTR                5 (show_help)
             60 CALL_FUNCTION            0
             62 POP_TOP

695          64 LOAD_FAST                0 (self)
             66 LOAD_ATTR                6 (prompt_to_roll_again_and_score)
             68 LOAD_FAST                1 (hand)
             70 CALL_FUNCTION            1
             72 RETURN_VALUE

696     >>   74 LOAD_FAST                2 (roll_again)
             76 LOAD_CONST               5 ('y')
             78 COMPARE_OP               2 (==)
             80 POP_JUMP_IF_TRUE        90
             82 LOAD_FAST                2 (roll_again)
             84 LOAD_CONST               6 ('yes')
             86 COMPARE_OP               2 (==)
             88 POP_JUMP_IF_FALSE      102

697     >>   90 LOAD_FAST                0 (self)
             92 LOAD_ATTR                7 (re_roll)
             94 LOAD_FAST                1 (hand)
             96 CALL_FUNCTION            1
             98 POP_TOP
            100 JUMP_FORWARD            10 (to 112)

699     >>  102 LOAD_FAST                0 (self)
            104 LOAD_ATTR                8 (choose_score)
            106 LOAD_FAST                1 (hand)
            108 CALL_FUNCTION            1
            110 POP_TOP
        >>  112 LOAD_CONST               0 (None)
            114 RETURN_VALUE

Disassembly of re_roll:
711           0 LOAD_FAST                0 (self)
              2 LOAD_ATTR                0 (help_shown_last)
              4 POP_JUMP_IF_FALSE       32

712           6 LOAD_FAST                0 (self)
              8 LOAD_ATTR                1 (clear_screen)
             10 CALL_FUNCTION            0
             12 POP_TOP

713          14 LOAD_FAST                0 (self)
             16 LOAD_ATTR                2 (print_hand)
             18 LOAD_FAST                1 (hand)
             20 LOAD_CONST               1 (True)
             22 CALL_FUNCTION            2
             24 POP_TOP

714          26 LOAD_CONST               2 (False)
             28 LOAD_FAST                0 (self)
             30 STORE_ATTR               0 (help_shown_last)

716     >>   32 LOAD_GLOBAL              3 (input)

720          34 LOAD_CONST               3 ("Please indicate which numbers you'd like to roll again\nby separating them with commas (example: 1,2,3)\nOR type 'all', 'cancel' or 'help'\n>>  ")
             36 CALL_FUNCTION            1
             38 LOAD_ATTR                4 (lower)
             40 CALL_FUNCTION            0
             42 STORE_FAST               2 (nums_to_reroll)

722          44 LOAD_CONST               2 (False)
             46 STORE_FAST               3 (cancelled)

723          48 LOAD_CONST               2 (False)
             50 STORE_FAST               4 (error)

724          52 LOAD_FAST                1 (hand)
             54 STORE_FAST               5 (old_hand)

726          56 LOAD_FAST                2 (nums_to_reroll)
             58 LOAD_CONST               4 ('all')
             60 COMPARE_OP               2 (==)
             62 POP_JUMP_IF_FALSE       98

727          64 LOAD_CONST               5 ('')
             66 STORE_FAST               2 (nums_to_reroll)

728          68 SETUP_LOOP              76 (to 146)
             70 LOAD_FAST                1 (hand)
             72 GET_ITER
        >>   74 FOR_ITER                18 (to 94)
             76 STORE_FAST               6 (num)

729          78 LOAD_FAST                2 (nums_to_reroll)
             80 LOAD_CONST               6 ('{},')
             82 LOAD_ATTR                5 (format)
             84 LOAD_FAST                6 (num)
             86 CALL_FUNCTION            1
             88 BINARY_ADD
             90 STORE_FAST               2 (nums_to_reroll)
             92 JUMP_ABSOLUTE           74
        >>   94 POP_BLOCK
             96 JUMP_FORWARD            48 (to 146)

730     >>   98 LOAD_FAST                2 (nums_to_reroll)
            100 LOAD_CONST               7 ('cancel')
            102 COMPARE_OP               2 (==)
            104 POP_JUMP_IF_FALSE      112

731         106 LOAD_CONST               1 (True)
            108 STORE_FAST               3 (cancelled)
            110 JUMP_FORWARD            34 (to 146)

732     >>  112 LOAD_FAST                2 (nums_to_reroll)
            114 LOAD_CONST               8 ('help')
            116 COMPARE_OP               2 (==)
            118 POP_JUMP_IF_TRUE       128
            120 LOAD_FAST                2 (nums_to_reroll)
            122 LOAD_CONST               9 ('h')
            124 COMPARE_OP               2 (==)
            126 POP_JUMP_IF_FALSE      146

733     >>  128 LOAD_FAST                0 (self)
            130 LOAD_ATTR                6 (show_help)
            132 CALL_FUNCTION            0
            134 POP_TOP

734         136 LOAD_FAST                0 (self)
            138 LOAD_ATTR                7 (re_roll)
            140 LOAD_FAST                1 (hand)
            142 CALL_FUNCTION            1
            144 RETURN_VALUE

736     >>  146 LOAD_GLOBAL              8 (regex_sub)
            148 LOAD_CONST              10 ('\\s')
            150 LOAD_CONST               5 ('')
            152 LOAD_FAST                2 (nums_to_reroll)
            154 CALL_FUNCTION            3
            156 LOAD_ATTR                9 (split)
            158 LOAD_CONST              11 (',')
            160 CALL_FUNCTION            1
            162 STORE_FAST               2 (nums_to_reroll)

738         164 LOAD_FAST                3 (cancelled)
            166 EXTENDED_ARG             1
            168 POP_JUMP_IF_TRUE       294

739         170 SETUP_LOOP              72 (to 244)
            172 LOAD_GLOBAL             10 (range)
            174 LOAD_GLOBAL             11 (len)
            176 LOAD_FAST                2 (nums_to_reroll)
            178 CALL_FUNCTION            1
            180 CALL_FUNCTION            1
            182 GET_ITER
        >>  184 FOR_ITER                56 (to 242)
            186 STORE_FAST               7 (i)

740         188 SETUP_EXCEPT            20 (to 210)

741         190 LOAD_GLOBAL             12 (int)
            192 LOAD_FAST                2 (nums_to_reroll)
            194 LOAD_FAST                7 (i)
            196 BINARY_SUBSCR
            198 CALL_FUNCTION            1
            200 LOAD_FAST                2 (nums_to_reroll)
            202 LOAD_FAST                7 (i)
            204 STORE_SUBSCR
            206 POP_BLOCK
            208 JUMP_ABSOLUTE          184

742     >>  210 DUP_TOP
            212 LOAD_GLOBAL             13 (ValueError)
            214 COMPARE_OP              10 (exception match)
            216 POP_JUMP_IF_FALSE      238
            218 POP_TOP
            220 POP_TOP
            222 POP_TOP

743         224 LOAD_FAST                2 (nums_to_reroll)
            226 LOAD_ATTR               14 (pop)
            228 LOAD_FAST                7 (i)
            230 CALL_FUNCTION            1
            232 POP_TOP
            234 POP_EXCEPT
            236 JUMP_ABSOLUTE          184
        >>  238 END_FINALLY
            240 JUMP_ABSOLUTE          184
        >>  242 POP_BLOCK

745     >>  244 SETUP_LOOP              48 (to 294)
            246 LOAD_FAST                2 (nums_to_reroll)
            248 GET_ITER
        >>  250 FOR_ITER                40 (to 292)
            252 STORE_FAST               6 (num)

746         254 LOAD_FAST                6 (num)
            256 LOAD_FAST                5 (old_hand)
            258 COMPARE_OP               6 (in)
            260 EXTENDED_ARG             1
            262 POP_JUMP_IF_FALSE      276

747         264 LOAD_FAST                5 (old_hand)
            266 LOAD_ATTR               15 (remove)
            268 LOAD_FAST                6 (num)
            270 CALL_FUNCTION            1
            272 POP_TOP
            274 JUMP_ABSOLUTE          250

749     >>  276 LOAD_GLOBAL             16 (print)
            278 LOAD_CONST              12 ("I'm sorry it appears you've entered a number not found in your hand.\n Let's try again.")
            280 CALL_FUNCTION            1
            282 POP_TOP

750         284 LOAD_CONST               1 (True)
            286 STORE_FAST               4 (error)

751         288 BREAK_LOOP
            290 JUMP_ABSOLUTE          250
        >>  292 POP_BLOCK

753     >>  294 LOAD_FAST                4 (error)
            296 EXTENDED_ARG             1
            298 POP_JUMP_IF_FALSE      312

754         300 LOAD_FAST                0 (self)
            302 LOAD_ATTR                7 (re_roll)
            304 LOAD_FAST                1 (hand)
            306 CALL_FUNCTION            1
            308 POP_TOP
            310 JUMP_FORWARD            96 (to 408)

755     >>  312 LOAD_FAST                3 (cancelled)
            314 EXTENDED_ARG             1
            316 POP_JUMP_IF_FALSE      330

756         318 LOAD_FAST                0 (self)
            320 LOAD_ATTR               17 (choose_score)
            322 LOAD_FAST                1 (hand)
            324 CALL_FUNCTION            1
            326 POP_TOP
            328 JUMP_FORWARD            78 (to 408)

758     >>  330 LOAD_CONST              13 (5)
            332 LOAD_GLOBAL             11 (len)
            334 LOAD_FAST                5 (old_hand)
            336 CALL_FUNCTION            1
            338 BINARY_SUBTRACT
            340 STORE_FAST               8 (new_dice_needed)

759         342 LOAD_FAST                5 (old_hand)
            344 STORE_FAST               9 (new_hand)

761         346 SETUP_LOOP              30 (to 378)
            348 LOAD_GLOBAL             10 (range)
            350 LOAD_FAST                8 (new_dice_needed)
            352 CALL_FUNCTION            1
            354 GET_ITER
        >>  356 FOR_ITER                18 (to 376)
            358 STORE_FAST              10 (_)

762         360 LOAD_FAST                9 (new_hand)
            362 LOAD_ATTR               18 (append)
            364 LOAD_GLOBAL             19 (D6)
            366 CALL_FUNCTION            0
            368 CALL_FUNCTION            1
            370 POP_TOP
            372 EXTENDED_ARG             1
            374 JUMP_ABSOLUTE          356
        >>  376 POP_BLOCK

764     >>  378 LOAD_FAST                9 (new_hand)
            380 LOAD_ATTR               20 (sort)
            382 CALL_FUNCTION            0
            384 POP_TOP

765         386 LOAD_FAST                0 (self)
            388 LOAD_ATTR                2 (print_hand)
            390 LOAD_FAST                9 (new_hand)
            392 LOAD_CONST               1 (True)
            394 CALL_FUNCTION            2
            396 POP_TOP

766         398 LOAD_FAST                0 (self)
            400 LOAD_ATTR               17 (choose_score)
            402 LOAD_FAST                9 (new_hand)
            404 CALL_FUNCTION            1
            406 POP_TOP
        >>  408 LOAD_CONST               0 (None)
            410 RETURN_VALUE

Disassembly of roll_action:
702           0 LOAD_GLOBAL              0 (YatzyHand)
              2 CALL_FUNCTION            0
              4 STORE_FAST               1 (hand)

703           6 LOAD_FAST                0 (self)
              8 LOAD_ATTR                1 (print_hand)
             10 LOAD_FAST                1 (hand)
             12 LOAD_CONST               1 (False)
             14 CALL_FUNCTION            2
             16 POP_TOP

704          18 LOAD_FAST                0 (self)
             20 LOAD_ATTR                2 (prompt_to_roll_again_and_score)
             22 LOAD_FAST                1 (hand)
             24 CALL_FUNCTION            1
             26 POP_TOP
             28 LOAD_CONST               0 (None)
             30 RETURN_VALUE

Disassembly of show_help:
633           0 LOAD_CONST               1 (True)
              2 LOAD_FAST                0 (self)
              4 STORE_ATTR               0 (help_shown_last)

634           6 LOAD_GLOBAL              1 (print)

683           8 LOAD_CONST               2 ('\n    "help" or "h": opens this menu\n    "roll" or "r": rolls five dice\n    "quit" or "q": quits the game\n    -----------------------\n    SCORING:\n    -----------------------\n    To choose where to place\n    your score you must match\n    a word or phrase from the\n    scorecard:\n\n    ----------------------------|----------------------------\n       Upper Section            |   Lower Section\n    ----------------------------|----------------------------\n    This section this scored    |  I\'ve listed the points\n    by adding the number of dice|  for each in this part below\n    in your hand which match    |\n    the description.            |  (total = total of dice)\n                                |\n    ones:                       |  three of a kind: total\n    twos:                       |  four of a kind: total\n    threes:                     |  full house: 25\n    fours:                      |  small straight: 30\n    fives:                      |  large straight: 40\n    sixes:                      |  yatzy: 50\n    total:                      |  chance: total\n    (35 bonus if total >= 63)   |  (each additional yatzy = 100)\n    bonus:                      |  yatzy bonus: see above\n    upper total:                |  lower total:\n    ---------------------------------------------------------\n        Total:\n    ---------------------------------------------------------\n\n    Example: (user input follows ">>  ")\n\n    Welcome to script yatzy!\n    Type \'roll\' or \'r\' to begin playing!\n    >>  roll\n    You rolled 1 1 4 3 5\n    Would you like to roll again? Y/N\n    >> y\n    Please indicate which numbers you\'d like to roll again, separating them with commas\n    OR type \'all\' or \'cancel\'\n    >>  4,3,5\n    Your new hand is 1 1 1 6 6\n    Please indicate which part of your scorecard you\'d like to fill in.\n    >> full houseSorry you\'ve already used this portion of your scorecard\n\n        ')
             10 CALL_FUNCTION            1
             12 POP_TOP

684          14 LOAD_GLOBAL              2 (input)
             16 LOAD_CONST               3 ("Hit the enter key when you're ready to return to the game.\n>>  ")
             18 CALL_FUNCTION            1
             20 POP_TOP

685          22 LOAD_FAST                0 (self)
             24 LOAD_ATTR                3 (clear_screen)
             26 CALL_FUNCTION            0
             28 POP_TOP

686          30 LOAD_GLOBAL              1 (print)
             32 LOAD_CONST               4 ('Turn resumed.')
             34 CALL_FUNCTION            1
             36 POP_TOP
             38 LOAD_CONST               0 (None)
             40 RETURN_VALUE


Disassembly of YatzyHand:
Disassembly of __append__:
 82           0 LOAD_GLOBAL              0 (print)
              2 LOAD_CONST               1 ('')
              4 LOAD_ATTR                1 (format)
              6 LOAD_GLOBAL              2 (type)
              8 LOAD_FAST                0 (self)
             10 CALL_FUNCTION            1
             12 CALL_FUNCTION            1
             14 CALL_FUNCTION            1
             16 POP_TOP

 83          18 LOAD_FAST                0 (self)
             20 LOAD_ATTR                3 (append)
             22 LOAD_FAST                1 (item)
             24 CALL_FUNCTION            1
             26 POP_TOP

 84          28 LOAD_GLOBAL              0 (print)
             30 LOAD_FAST                0 (self)
             32 CALL_FUNCTION            1
             34 POP_TOP
             36 LOAD_CONST               0 (None)
             38 RETURN_VALUE

Disassembly of __init__:
 79           0 LOAD_GLOBAL              0 (super)
              2 CALL_FUNCTION            0
              4 LOAD_ATTR                1 (__init__)
              6 LOAD_FAST                1 (args)
              8 LOAD_CONST               1 (5)
             10 LOAD_GLOBAL              2 (D6)
             12 LOAD_CONST               2 (('size', 'die_class'))
             14 BUILD_CONST_KEY_MAP      2
             16 LOAD_FAST                2 (kwargs)
             18 BUILD_MAP_UNPACK_WITH_CALL     2
             20 CALL_FUNCTION_EX         1
             22 POP_TOP
             24 LOAD_CONST               0 (None)
             26 RETURN_VALUE


Disassembly of YatzyScore:
Disassembly of __init__:
157           0 LOAD_FAST                1 (name)
              2 LOAD_FAST                0 (self)
              4 STORE_ATTR               0 (player_name)
              6 LOAD_CONST               0 (None)
              8 RETURN_VALUE

Disassembly of _print_a_state:
183           0 LOAD_GLOBAL              0 (isinstance)
              2 LOAD_FAST                1 (state)
              4 LOAD_GLOBAL              1 (int)
              6 CALL_FUNCTION            2
              8 STORE_FAST               3 (is_int)

184          10 LOAD_FAST                2 (upper)
             12 POP_JUMP_IF_FALSE       54

185          14 LOAD_FAST                3 (is_int)
             16 POP_JUMP_IF_FALSE       48

186          18 LOAD_GLOBAL              2 (len)
             20 LOAD_GLOBAL              3 (str)
             22 LOAD_FAST                1 (state)
             24 CALL_FUNCTION            1
             26 CALL_FUNCTION            1
             28 LOAD_CONST               1 (1)
             30 COMPARE_OP               4 (>)
             32 POP_JUMP_IF_FALSE       38
             34 LOAD_FAST                1 (state)
             36 RETURN_VALUE
        >>   38 LOAD_CONST               2 (' {}')
             40 LOAD_ATTR                4 (format)
             42 LOAD_FAST                1 (state)
             44 CALL_FUNCTION            1
             46 RETURN_VALUE

188     >>   48 LOAD_CONST               3 ('  ')
             50 RETURN_VALUE
             52 JUMP_FORWARD            12 (to 66)

190     >>   54 LOAD_FAST                3 (is_int)
             56 POP_JUMP_IF_FALSE       62
             58 LOAD_FAST                1 (state)
             60 RETURN_VALUE
        >>   62 LOAD_CONST               3 ('  ')
             64 RETURN_VALUE
        >>   66 LOAD_CONST               0 (None)
             68 RETURN_VALUE

Disassembly of _score_set:
275           0 LOAD_CONST               1 (0)
              2 BUILD_LIST               1
              4 STORE_FAST               3 (scores)

276           6 LOAD_CONST               1 (0)
              8 BUILD_LIST               1
             10 STORE_FAST               4 (numbers)

277          12 SETUP_LOOP              54 (to 68)
             14 LOAD_FAST                1 (hand)
             16 LOAD_ATTR                0 (_sets)
             18 LOAD_ATTR                1 (items)
             20 CALL_FUNCTION            0
             22 GET_ITER
        >>   24 FOR_ITER                40 (to 66)
             26 UNPACK_SEQUENCE          2
             28 STORE_FAST               5 (worth)
             30 STORE_FAST               6 (count)

278          32 LOAD_FAST                6 (count)
             34 LOAD_FAST                2 (set_size)
             36 COMPARE_OP               2 (==)
             38 POP_JUMP_IF_FALSE       24

279          40 LOAD_FAST                3 (scores)
             42 LOAD_ATTR                2 (append)
             44 LOAD_FAST                5 (worth)
             46 LOAD_FAST                2 (set_size)
             48 BINARY_MULTIPLY
             50 CALL_FUNCTION            1
             52 POP_TOP

280          54 LOAD_FAST                4 (numbers)
             56 LOAD_ATTR                2 (append)
             58 LOAD_FAST                5 (worth)
             60 CALL_FUNCTION            1
             62 POP_TOP
             64 JUMP_ABSOLUTE           24
        >>   66 POP_BLOCK

281     >>   68 LOAD_GLOBAL              3 (max)
             70 LOAD_FAST                3 (scores)
             72 CALL_FUNCTION            1
             74 LOAD_GLOBAL              3 (max)
             76 LOAD_FAST                4 (numbers)
             78 CALL_FUNCTION            1
             80 BUILD_TUPLE              2
             82 RETURN_VALUE

Disassembly of determine_3_in_sequence:
312           0 LOAD_CONST               1 (1)
              2 LOAD_CONST               2 (2)
              4 LOAD_CONST               3 (3)
              6 BUILD_SET                3

313           8 LOAD_CONST               1 (1)
             10 LOAD_CONST               2 (2)
             12 LOAD_CONST               3 (3)
             14 LOAD_CONST               4 (5)
             16 LOAD_CONST               5 (6)
             18 BUILD_SET                5

314          20 LOAD_CONST               1 (1)
             22 LOAD_CONST               2 (2)
             24 LOAD_CONST               3 (3)
             26 LOAD_CONST               4 (5)
             28 BUILD_SET                4

315          30 LOAD_CONST               1 (1)
             32 LOAD_CONST               2 (2)
             34 LOAD_CONST               3 (3)
             36 LOAD_CONST               5 (6)
             38 BUILD_SET                4

316          40 LOAD_CONST               2 (2)
             42 LOAD_CONST               3 (3)
             44 LOAD_CONST               6 (4)
             46 BUILD_SET                3

317          48 LOAD_CONST               2 (2)
             50 LOAD_CONST               3 (3)
             52 LOAD_CONST               6 (4)
             54 LOAD_CONST               5 (6)
             56 BUILD_SET                4

318          58 LOAD_CONST               3 (3)
             60 LOAD_CONST               6 (4)
             62 LOAD_CONST               4 (5)
             64 BUILD_SET                3

319          66 LOAD_CONST               1 (1)
             68 LOAD_CONST               3 (3)
             70 LOAD_CONST               6 (4)
             72 LOAD_CONST               4 (5)
             74 BUILD_SET                4

320          76 LOAD_CONST               6 (4)
             78 LOAD_CONST               4 (5)
             80 LOAD_CONST               5 (6)
             82 BUILD_SET                3

321          84 LOAD_CONST               1 (1)
             86 LOAD_CONST               6 (4)
             88 LOAD_CONST               4 (5)
             90 LOAD_CONST               5 (6)
             92 BUILD_SET                4

322          94 LOAD_CONST               1 (1)
             96 LOAD_CONST               2 (2)
             98 LOAD_CONST               6 (4)
            100 LOAD_CONST               4 (5)
            102 LOAD_CONST               5 (6)
            104 BUILD_SET                5

323         106 LOAD_CONST               2 (2)
            108 LOAD_CONST               6 (4)
            110 LOAD_CONST               4 (5)
            112 LOAD_CONST               5 (6)
            114 BUILD_SET                4
            116 BUILD_LIST              12
            118 STORE_FAST               2 (pass_conditions)

325         120 LOAD_GLOBAL              0 (set)
            122 LOAD_CONST               7 (<code object <listcomp> at 0x10a307540, file "/Users/winniepalangpour/git/winrox.github.io/src/yatzy.py", line 325>)
            124 LOAD_CONST               8 ('YatzyScore.determine_3_in_sequence.<locals>.<listcomp>')
            126 MAKE_FUNCTION            0
            128 LOAD_FAST                1 (hand)
            130 GET_ITER
            132 CALL_FUNCTION            1
            134 CALL_FUNCTION            1
            136 STORE_FAST               3 (set_hand)

326         138 LOAD_FAST                3 (set_hand)
            140 LOAD_FAST                2 (pass_conditions)
            142 COMPARE_OP               6 (in)
            144 EXTENDED_ARG             0
            146 POP_JUMP_IF_FALSE      250

327         148 LOAD_FAST                2 (pass_conditions)
            150 LOAD_ATTR                1 (index)
            152 LOAD_FAST                3 (set_hand)
            154 CALL_FUNCTION            1
            156 STORE_FAST               4 (index)

328         158 BUILD_LIST               0
            160 STORE_FAST               5 (win)

330         162 LOAD_FAST                4 (index)
            164 LOAD_CONST              17 ((0, 1, 2, 3))
            166 COMPARE_OP               6 (in)
            168 POP_JUMP_IF_FALSE      182

331         170 LOAD_CONST               1 (1)
            172 LOAD_CONST               2 (2)
            174 LOAD_CONST               3 (3)
            176 BUILD_LIST               3
            178 STORE_FAST               5 (win)
            180 JUMP_FORWARD            60 (to 242)

332     >>  182 LOAD_FAST                4 (index)
            184 LOAD_CONST              18 ((4, 5))
            186 COMPARE_OP               6 (in)
            188 POP_JUMP_IF_FALSE      202

333         190 LOAD_CONST               2 (2)
            192 LOAD_CONST               3 (3)
            194 LOAD_CONST               6 (4)
            196 BUILD_LIST               3
            198 STORE_FAST               5 (win)
            200 JUMP_FORWARD            40 (to 242)

334     >>  202 LOAD_FAST                4 (index)
            204 LOAD_CONST              19 ((6, 7))
            206 COMPARE_OP               6 (in)
            208 POP_JUMP_IF_FALSE      222

335         210 LOAD_CONST               3 (3)
            212 LOAD_CONST               6 (4)
            214 LOAD_CONST               4 (5)
            216 BUILD_LIST               3
            218 STORE_FAST               5 (win)
            220 JUMP_FORWARD            20 (to 242)

336     >>  222 LOAD_FAST                4 (index)
            224 LOAD_CONST              20 ((8, 9, 10, 11))
            226 COMPARE_OP               6 (in)
            228 EXTENDED_ARG             0
            230 POP_JUMP_IF_FALSE      242

337         232 LOAD_CONST               6 (4)
            234 LOAD_CONST               4 (5)
            236 LOAD_CONST               5 (6)
            238 BUILD_LIST               3
            240 STORE_FAST               5 (win)

339     >>  242 LOAD_CONST              15 (True)
            244 LOAD_FAST                5 (win)
            246 BUILD_TUPLE              2
            248 RETURN_VALUE

341     >>  250 LOAD_CONST              16 (False)
            252 BUILD_LIST               0
            254 BUILD_TUPLE              2
            256 RETURN_VALUE
            258 LOAD_CONST               0 (None)
            260 RETURN_VALUE

Disassembly of determine_3_of_kind:
367           0 LOAD_FAST                0 (self)
              2 LOAD_ATTR                0 (_score_set)
              4 LOAD_FAST                1 (hand)
              6 LOAD_CONST               1 (3)
              8 CALL_FUNCTION            2
             10 STORE_FAST               2 (score_data)

368          12 LOAD_FAST                0 (self)
             14 LOAD_ATTR                1 (get_of_a_kind_points)
             16 LOAD_FAST                1 (hand)
             18 LOAD_FAST                2 (score_data)
             20 CALL_FUNCTION            2
             22 STORE_FAST               3 (points)

370          24 LOAD_FAST                2 (score_data)
             26 LOAD_CONST               2 (0)
             28 BINARY_SUBSCR
             30 LOAD_CONST               2 (0)
             32 COMPARE_OP               4 (>)
             34 POP_JUMP_IF_FALSE       64
             36 LOAD_FAST                2 (score_data)
             38 LOAD_CONST               3 (1)
             40 BINARY_SUBSCR
             42 LOAD_CONST               2 (0)
             44 COMPARE_OP               4 (>)
             46 POP_JUMP_IF_FALSE       64

371          48 LOAD_CONST               4 (True)
             50 LOAD_FAST                3 (points)
             52 LOAD_FAST                2 (score_data)
             54 LOAD_CONST               3 (1)
             56 BINARY_SUBSCR
             58 BUILD_TUPLE              2
             60 BUILD_TUPLE              2
             62 RETURN_VALUE

373     >>   64 LOAD_CONST               5 (False)
             66 LOAD_CONST               2 (0)
             68 LOAD_FAST                2 (score_data)
             70 LOAD_CONST               3 (1)
             72 BINARY_SUBSCR
             74 BUILD_TUPLE              2
             76 BUILD_TUPLE              2
             78 RETURN_VALUE
             80 LOAD_CONST               0 (None)
             82 RETURN_VALUE

Disassembly of determine_4_of_a_kind:
387           0 LOAD_FAST                0 (self)
              2 LOAD_ATTR                0 (_score_set)
              4 LOAD_FAST                1 (hand)
              6 LOAD_CONST               1 (4)
              8 CALL_FUNCTION            2
             10 LOAD_CONST               2 (1)
             12 BINARY_SUBSCR
             14 STORE_FAST               2 (num)

388          16 LOAD_FAST                2 (num)
             18 LOAD_CONST               3 (0)
             20 COMPARE_OP               4 (>)
             22 POP_JUMP_IF_FALSE       32

389          24 LOAD_CONST               4 (True)
             26 LOAD_FAST                2 (num)
             28 BUILD_TUPLE              2
             30 RETURN_VALUE

391     >>   32 LOAD_CONST               5 (False)
             34 LOAD_FAST                2 (num)
             36 BUILD_TUPLE              2
             38 RETURN_VALUE
             40 LOAD_CONST               0 (None)
             42 RETURN_VALUE

Disassembly of determine_full_house:
408           0 LOAD_FAST                0 (self)
              2 LOAD_ATTR                0 (score_one_pair)
              4 LOAD_FAST                1 (hand)
              6 CALL_FUNCTION            1
              8 STORE_FAST               2 (pair)

409          10 LOAD_FAST                0 (self)
             12 LOAD_ATTR                1 (determine_3_of_kind)
             14 LOAD_FAST                1 (hand)
             16 CALL_FUNCTION            1
             18 STORE_FAST               3 (three)

412          20 LOAD_FAST                2 (pair)
             22 LOAD_CONST               1 (0)
             24 BINARY_SUBSCR
             26 POP_JUMP_IF_FALSE       64
             28 LOAD_FAST                3 (three)
             30 LOAD_CONST               1 (0)
             32 BINARY_SUBSCR
             34 POP_JUMP_IF_FALSE       64
             36 LOAD_FAST                2 (pair)
             38 LOAD_CONST               2 (1)
             40 BINARY_SUBSCR
             42 LOAD_CONST               2 (1)
             44 BINARY_SUBSCR
             46 LOAD_FAST                3 (three)
             48 LOAD_CONST               2 (1)
             50 BINARY_SUBSCR
             52 LOAD_CONST               2 (1)
             54 BINARY_SUBSCR
             56 COMPARE_OP               3 (!=)
             58 POP_JUMP_IF_FALSE       64

413          60 LOAD_CONST               3 (True)
             62 RETURN_VALUE

415     >>   64 LOAD_CONST               4 (False)
             66 RETURN_VALUE
             68 LOAD_CONST               0 (None)
             70 RETURN_VALUE

Disassembly of determine_large_straight:
462           0 LOAD_CONST               1 (1)
              2 LOAD_CONST               2 (2)
              4 LOAD_CONST               3 (3)
              6 LOAD_CONST               4 (4)
              8 LOAD_CONST               5 (5)
             10 BUILD_SET                5

463          12 LOAD_CONST               2 (2)
             14 LOAD_CONST               3 (3)
             16 LOAD_CONST               4 (4)
             18 LOAD_CONST               5 (5)
             20 LOAD_CONST               6 (6)
             22 BUILD_SET                5
             24 BUILD_LIST               2
             26 STORE_FAST               2 (wins)

465          28 LOAD_CONST               7 (False)
             30 STORE_FAST               3 (win_found)

466          32 LOAD_GLOBAL              0 (set)
             34 CALL_FUNCTION            0
             36 STORE_FAST               4 (set_hand)

468          38 SETUP_LOOP              26 (to 66)
             40 LOAD_FAST                1 (hand)
             42 GET_ITER
        >>   44 FOR_ITER                18 (to 64)
             46 STORE_FAST               5 (die)

469          48 LOAD_FAST                4 (set_hand)
             50 LOAD_ATTR                1 (add)
             52 LOAD_GLOBAL              2 (int)
             54 LOAD_FAST                5 (die)
             56 CALL_FUNCTION            1
             58 CALL_FUNCTION            1
             60 POP_TOP
             62 JUMP_ABSOLUTE           44
        >>   64 POP_BLOCK

471     >>   66 LOAD_FAST                4 (set_hand)
             68 LOAD_FAST                2 (wins)
             70 COMPARE_OP               6 (in)
             72 POP_JUMP_IF_FALSE       78

472          74 LOAD_CONST               8 (True)
             76 STORE_FAST               3 (win_found)

474     >>   78 LOAD_FAST                3 (win_found)
             80 RETURN_VALUE

Disassembly of determine_small_straight:
429           0 LOAD_CONST               1 (1)
              2 LOAD_CONST               2 (2)
              4 LOAD_CONST               3 (3)
              6 LOAD_CONST               4 (4)
              8 BUILD_SET                4

430          10 LOAD_CONST               1 (1)
             12 LOAD_CONST               2 (2)
             14 LOAD_CONST               3 (3)
             16 LOAD_CONST               4 (4)
             18 LOAD_CONST               5 (5)
             20 BUILD_SET                5

431          22 LOAD_CONST               1 (1)
             24 LOAD_CONST               2 (2)
             26 LOAD_CONST               3 (3)
             28 LOAD_CONST               4 (4)
             30 LOAD_CONST               6 (6)
             32 BUILD_SET                5

432          34 LOAD_CONST               2 (2)
             36 LOAD_CONST               3 (3)
             38 LOAD_CONST               4 (4)
             40 LOAD_CONST               5 (5)
             42 BUILD_SET                4

433          44 LOAD_CONST               2 (2)
             46 LOAD_CONST               3 (3)
             48 LOAD_CONST               4 (4)
             50 LOAD_CONST               5 (5)
             52 LOAD_CONST               6 (6)
             54 BUILD_SET                5

434          56 LOAD_CONST               3 (3)
             58 LOAD_CONST               4 (4)
             60 LOAD_CONST               5 (5)
             62 LOAD_CONST               6 (6)
             64 BUILD_SET                4

435          66 LOAD_CONST               1 (1)
             68 LOAD_CONST               3 (3)
             70 LOAD_CONST               4 (4)
             72 LOAD_CONST               5 (5)
             74 LOAD_CONST               6 (6)
             76 BUILD_SET                5

436          78 LOAD_CONST               2 (2)
             80 LOAD_CONST               3 (3)
             82 LOAD_CONST               4 (4)
             84 LOAD_CONST               5 (5)
             86 LOAD_CONST               6 (6)
             88 BUILD_SET                5
             90 BUILD_LIST               8
             92 STORE_FAST               2 (wins)

438          94 LOAD_CONST               7 (False)
             96 STORE_FAST               3 (win_found)

439          98 LOAD_GLOBAL              0 (set)
            100 CALL_FUNCTION            0
            102 STORE_FAST               4 (set_hand)

441         104 SETUP_LOOP              26 (to 132)
            106 LOAD_FAST                1 (hand)
            108 GET_ITER
        >>  110 FOR_ITER                18 (to 130)
            112 STORE_FAST               5 (num)

442         114 LOAD_FAST                4 (set_hand)
            116 LOAD_ATTR                1 (add)
            118 LOAD_GLOBAL              2 (int)
            120 LOAD_FAST                5 (num)
            122 CALL_FUNCTION            1
            124 CALL_FUNCTION            1
            126 POP_TOP
            128 JUMP_ABSOLUTE          110
        >>  130 POP_BLOCK

444     >>  132 LOAD_FAST                4 (set_hand)
            134 LOAD_FAST                2 (wins)
            136 COMPARE_OP               6 (in)
            138 POP_JUMP_IF_FALSE      144

445         140 LOAD_CONST               8 (True)
            142 STORE_FAST               3 (win_found)

447     >>  144 LOAD_FAST                3 (win_found)
            146 RETURN_VALUE

Disassembly of determine_two_of_a_kind:
351           0 LOAD_FAST                0 (self)
              2 LOAD_ATTR                0 (find_duplicates)
              4 LOAD_FAST                1 (hand)
              6 CALL_FUNCTION            1
              8 STORE_FAST               2 (duplicates)

352          10 LOAD_GLOBAL              1 (len)
             12 LOAD_FAST                2 (duplicates)
             14 CALL_FUNCTION            1
             16 STORE_FAST               3 (length)

354          18 LOAD_FAST                3 (length)
             20 LOAD_CONST               1 (0)
             22 COMPARE_OP               4 (>)
             24 POP_JUMP_IF_FALSE      112
             26 LOAD_GLOBAL              1 (len)
             28 LOAD_FAST                2 (duplicates)
             30 CALL_FUNCTION            1
             32 LOAD_CONST               2 (1)
             34 COMPARE_OP               2 (==)
             36 POP_JUMP_IF_FALSE      112

355          38 BUILD_LIST               0
             40 STORE_FAST               4 (hand_without_duplicates)

356          42 SETUP_LOOP              34 (to 78)
             44 LOAD_FAST                1 (hand)
             46 GET_ITER
        >>   48 FOR_ITER                26 (to 76)
             50 STORE_FAST               5 (num)

357          52 LOAD_FAST                5 (num)
             54 LOAD_FAST                2 (duplicates)
             56 LOAD_CONST               1 (0)
             58 BINARY_SUBSCR
             60 COMPARE_OP               3 (!=)
             62 POP_JUMP_IF_FALSE       48

358          64 LOAD_FAST                4 (hand_without_duplicates)
             66 LOAD_ATTR                2 (append)
             68 LOAD_FAST                5 (num)
             70 CALL_FUNCTION            1
             72 POP_TOP
             74 JUMP_ABSOLUTE           48
        >>   76 POP_BLOCK

359     >>   78 LOAD_GLOBAL              1 (len)
             80 LOAD_FAST                4 (hand_without_duplicates)
             82 CALL_FUNCTION            1
             84 LOAD_CONST               3 (3)
             86 COMPARE_OP               2 (==)
             88 POP_JUMP_IF_FALSE      102

360          90 LOAD_CONST               4 (True)
             92 LOAD_FAST                2 (duplicates)
             94 LOAD_CONST               1 (0)
             96 BINARY_SUBSCR
             98 BUILD_TUPLE              2
            100 RETURN_VALUE

362     >>  102 LOAD_CONST               5 (False)
            104 LOAD_FAST                2 (duplicates)
            106 BUILD_TUPLE              2
            108 RETURN_VALUE
            110 JUMP_FORWARD             8 (to 120)

364     >>  112 LOAD_CONST               5 (False)
            114 LOAD_FAST                2 (duplicates)
            116 BUILD_TUPLE              2
            118 RETURN_VALUE
        >>  120 LOAD_CONST               0 (None)
            122 RETURN_VALUE

Disassembly of determine_two_pair:
344           0 LOAD_FAST                0 (self)
              2 LOAD_ATTR                0 (find_duplicates)
              4 LOAD_FAST                1 (hand)
              6 CALL_FUNCTION            1
              8 STORE_FAST               2 (duplicates)

345          10 LOAD_GLOBAL              1 (len)
             12 LOAD_FAST                2 (duplicates)
             14 CALL_FUNCTION            1
             16 LOAD_CONST               1 (2)
             18 COMPARE_OP               2 (==)
             20 POP_JUMP_IF_FALSE       30

346          22 LOAD_CONST               2 (True)
             24 LOAD_FAST                2 (duplicates)
             26 BUILD_TUPLE              2
             28 RETURN_VALUE

348     >>   30 LOAD_CONST               3 (False)
             32 LOAD_FAST                2 (duplicates)
             34 BUILD_TUPLE              2
             36 RETURN_VALUE
             38 LOAD_CONST               0 (None)
             40 RETURN_VALUE

Disassembly of determine_yatzy:
488           0 LOAD_GLOBAL              0 (set)
              2 CALL_FUNCTION            0
              4 STORE_FAST               2 (set_hand)

490           6 SETUP_LOOP              26 (to 34)
              8 LOAD_FAST                1 (hand)
             10 GET_ITER
        >>   12 FOR_ITER                18 (to 32)
             14 STORE_FAST               3 (die)

491          16 LOAD_FAST                2 (set_hand)
             18 LOAD_ATTR                1 (add)
             20 LOAD_GLOBAL              2 (int)
             22 LOAD_FAST                3 (die)
             24 CALL_FUNCTION            1
             26 CALL_FUNCTION            1
             28 POP_TOP
             30 JUMP_ABSOLUTE           12
        >>   32 POP_BLOCK

493     >>   34 LOAD_GLOBAL              3 (len)
             36 LOAD_FAST                2 (set_hand)
             38 CALL_FUNCTION            1
             40 LOAD_CONST               1 (1)
             42 COMPARE_OP               2 (==)
             44 POP_JUMP_IF_FALSE       50

494          46 LOAD_CONST               2 (True)
             48 RETURN_VALUE

496     >>   50 LOAD_CONST               3 (False)
             52 RETURN_VALUE
             54 LOAD_CONST               0 (None)
             56 RETURN_VALUE

Disassembly of find_duplicates:
301           0 BUILD_LIST               0
              2 STORE_FAST               2 (duplicates)

302           4 BUILD_LIST               0
              6 STORE_FAST               3 (nums_found)

303           8 SETUP_LOOP              42 (to 52)
             10 LOAD_FAST                1 (hand)
             12 GET_ITER
        >>   14 FOR_ITER                34 (to 50)
             16 STORE_FAST               4 (num)

304          18 LOAD_FAST                4 (num)
             20 LOAD_FAST                3 (nums_found)
             22 COMPARE_OP               6 (in)
             24 POP_JUMP_IF_FALSE       38

305          26 LOAD_FAST                2 (duplicates)
             28 LOAD_ATTR                0 (append)
             30 LOAD_FAST                4 (num)
             32 CALL_FUNCTION            1
             34 POP_TOP
             36 JUMP_ABSOLUTE           14

307     >>   38 LOAD_FAST                3 (nums_found)
             40 LOAD_ATTR                0 (append)
             42 LOAD_FAST                4 (num)
             44 CALL_FUNCTION            1
             46 POP_TOP
             48 JUMP_ABSOLUTE           14
        >>   50 POP_BLOCK

308     >>   52 LOAD_FAST                2 (duplicates)
             54 RETURN_VALUE

Disassembly of get_of_a_kind_points:
291           0 BUILD_LIST               0
              2 STORE_FAST               3 (hand_without_set)

292           4 LOAD_FAST                2 (score_data)
              6 LOAD_CONST               1 (0)
              8 BINARY_SUBSCR
             10 STORE_FAST               4 (points)

293          12 SETUP_LOOP              34 (to 48)
             14 LOAD_FAST                1 (hand)
             16 GET_ITER
        >>   18 FOR_ITER                26 (to 46)
             20 STORE_FAST               5 (num)

294          22 LOAD_FAST                5 (num)
             24 LOAD_FAST                2 (score_data)
             26 LOAD_CONST               2 (1)
             28 BINARY_SUBSCR
             30 COMPARE_OP               3 (!=)
             32 POP_JUMP_IF_FALSE       18

295          34 LOAD_FAST                3 (hand_without_set)
             36 LOAD_ATTR                0 (append)
             38 LOAD_FAST                5 (num)
             40 CALL_FUNCTION            1
             42 POP_TOP
             44 JUMP_ABSOLUTE           18
        >>   46 POP_BLOCK

296     >>   48 SETUP_LOOP              20 (to 70)
             50 LOAD_FAST                3 (hand_without_set)
             52 GET_ITER
        >>   54 FOR_ITER                12 (to 68)
             56 STORE_FAST               5 (num)

297          58 LOAD_FAST                4 (points)
             60 LOAD_FAST                5 (num)
             62 INPLACE_ADD
             64 STORE_FAST               4 (points)
             66 JUMP_ABSOLUTE           54
        >>   68 POP_BLOCK

298     >>   70 LOAD_FAST                4 (points)
             72 RETURN_VALUE

Disassembly of get_state:
167           0 LOAD_FAST                0 (self)
              2 LOAD_ATTR                0 (ones)

168           4 LOAD_FAST                0 (self)
              6 LOAD_ATTR                1 (twos)

169           8 LOAD_FAST                0 (self)
             10 LOAD_ATTR                2 (threes)

170          12 LOAD_FAST                0 (self)
             14 LOAD_ATTR                3 (fours)

171          16 LOAD_FAST                0 (self)
             18 LOAD_ATTR                4 (fives)

172          20 LOAD_FAST                0 (self)
             22 LOAD_ATTR                5 (sixes)

173          24 LOAD_FAST                0 (self)
             26 LOAD_ATTR                6 (three_of_a_kind)

174          28 LOAD_FAST                0 (self)
             30 LOAD_ATTR                7 (four_of_a_kind)

175          32 LOAD_FAST                0 (self)
             34 LOAD_ATTR                8 (full_house)

176          36 LOAD_FAST                0 (self)
             38 LOAD_ATTR                9 (small_straight)

177          40 LOAD_FAST                0 (self)
             42 LOAD_ATTR               10 (large_straight)

178          44 LOAD_FAST                0 (self)
             46 LOAD_ATTR               11 (yatzy)

179          48 LOAD_FAST                0 (self)
             50 LOAD_ATTR               12 (chance)
             52 LOAD_CONST               1 (('ones', 'twos', 'threes', 'fours', 'fives', 'sixes', 'three_of_a_kind', 'four_of_a_kind', 'full_house', 'small_straight', 'large_straight', 'yatzy', 'chance'))
             54 BUILD_CONST_KEY_MAP     13
             56 RETURN_VALUE

Disassembly of print_score:
193           0 LOAD_GLOBAL              0 (print)

212           2 LOAD_CONST               1 ('\n    -----------------------------------------------------\n        YATZY ___{}___\n    ----------------------------|------------------------\n       Upper Section            |   Lower Section\n    ----------------------------|------------------------\n    ones: {}                    | three of a kind: {}\n    twos: {}                    | four of a kind: {}\n    threes: {}                  | full house: {}\n    fours: {}                   | small straight: {}\n    fives: {}                   | large straight: {}\n    sixes: {}                   | yatzy: {}\n    total: {}                   | chance: {}\n    (35 bonus if total >= 63)   | (each additional yatzy = 100)\n    bonus: {}                   | yatzy bonus: {}\n    upper total: {}             | lower total: {}\n    -----------------------------------------------------\n        Total: {}\n    -----------------------------------------------------\n        ')
              4 LOAD_ATTR                1 (format)

213           6 LOAD_FAST                0 (self)
              8 LOAD_ATTR                2 (player_name)

214          10 LOAD_FAST                0 (self)
             12 LOAD_ATTR                3 (_print_a_state)
             14 LOAD_FAST                0 (self)
             16 LOAD_ATTR                4 (ones)
             18 LOAD_CONST               2 (True)
             20 CALL_FUNCTION            2

215          22 LOAD_FAST                0 (self)
             24 LOAD_ATTR                3 (_print_a_state)
             26 LOAD_FAST                0 (self)
             28 LOAD_ATTR                5 (three_of_a_kind)
             30 LOAD_CONST               3 (False)
             32 CALL_FUNCTION            2

216          34 LOAD_FAST                0 (self)
             36 LOAD_ATTR                3 (_print_a_state)
             38 LOAD_FAST                0 (self)
             40 LOAD_ATTR                6 (twos)
             42 LOAD_CONST               2 (True)
             44 CALL_FUNCTION            2

217          46 LOAD_FAST                0 (self)
             48 LOAD_ATTR                3 (_print_a_state)
             50 LOAD_FAST                0 (self)
             52 LOAD_ATTR                7 (four_of_a_kind)
             54 LOAD_CONST               3 (False)
             56 CALL_FUNCTION            2

218          58 LOAD_FAST                0 (self)
             60 LOAD_ATTR                3 (_print_a_state)
             62 LOAD_FAST                0 (self)
             64 LOAD_ATTR                8 (threes)
             66 LOAD_CONST               2 (True)
             68 CALL_FUNCTION            2

219          70 LOAD_FAST                0 (self)
             72 LOAD_ATTR                3 (_print_a_state)
             74 LOAD_FAST                0 (self)
             76 LOAD_ATTR                9 (full_house)
             78 LOAD_CONST               3 (False)
             80 CALL_FUNCTION            2

220          82 LOAD_FAST                0 (self)
             84 LOAD_ATTR                3 (_print_a_state)
             86 LOAD_FAST                0 (self)
             88 LOAD_ATTR               10 (fours)
             90 LOAD_CONST               2 (True)
             92 CALL_FUNCTION            2

221          94 LOAD_FAST                0 (self)
             96 LOAD_ATTR                3 (_print_a_state)
             98 LOAD_FAST                0 (self)
            100 LOAD_ATTR               11 (small_straight)
            102 LOAD_CONST               3 (False)
            104 CALL_FUNCTION            2

222         106 LOAD_FAST                0 (self)
            108 LOAD_ATTR                3 (_print_a_state)
            110 LOAD_FAST                0 (self)
            112 LOAD_ATTR               12 (fives)
            114 LOAD_CONST               2 (True)
            116 CALL_FUNCTION            2

223         118 LOAD_FAST                0 (self)
            120 LOAD_ATTR                3 (_print_a_state)
            122 LOAD_FAST                0 (self)
            124 LOAD_ATTR               13 (large_straight)
            126 LOAD_CONST               3 (False)
            128 CALL_FUNCTION            2

224         130 LOAD_FAST                0 (self)
            132 LOAD_ATTR                3 (_print_a_state)
            134 LOAD_FAST                0 (self)
            136 LOAD_ATTR               14 (sixes)
            138 LOAD_CONST               2 (True)
            140 CALL_FUNCTION            2

225         142 LOAD_FAST                0 (self)
            144 LOAD_ATTR                3 (_print_a_state)
            146 LOAD_FAST                0 (self)
            148 LOAD_ATTR               15 (yatzy)
            150 LOAD_CONST               3 (False)
            152 CALL_FUNCTION            2

226         154 LOAD_FAST                0 (self)
            156 LOAD_ATTR                3 (_print_a_state)
            158 LOAD_FAST                0 (self)
            160 LOAD_ATTR               16 (total)
            162 LOAD_CONST               3 (False)
            164 CALL_FUNCTION            2

227         166 LOAD_FAST                0 (self)
            168 LOAD_ATTR                3 (_print_a_state)
            170 LOAD_FAST                0 (self)
            172 LOAD_ATTR               17 (chance)
            174 LOAD_CONST               3 (False)
            176 CALL_FUNCTION            2

228         178 LOAD_FAST                0 (self)
            180 LOAD_ATTR                3 (_print_a_state)
            182 LOAD_FAST                0 (self)
            184 LOAD_ATTR               18 (bonus)
            186 LOAD_CONST               2 (True)
            188 CALL_FUNCTION            2

229         190 LOAD_FAST                0 (self)
            192 LOAD_ATTR                3 (_print_a_state)
            194 LOAD_FAST                0 (self)
            196 LOAD_ATTR               19 (yatzy_bonus)
            198 LOAD_CONST               3 (False)
            200 CALL_FUNCTION            2

230         202 LOAD_FAST                0 (self)
            204 LOAD_ATTR                3 (_print_a_state)
            206 LOAD_FAST                0 (self)
            208 LOAD_ATTR               20 (upper_total)
            210 LOAD_CONST               2 (True)
            212 CALL_FUNCTION            2

231         214 LOAD_FAST                0 (self)
            216 LOAD_ATTR                3 (_print_a_state)
            218 LOAD_FAST                0 (self)
            220 LOAD_ATTR               21 (lower_total)
            222 LOAD_CONST               3 (False)
            224 CALL_FUNCTION            2

232         226 LOAD_FAST                0 (self)
            228 LOAD_ATTR                3 (_print_a_state)
            230 LOAD_FAST                0 (self)
            232 LOAD_ATTR               22 (grand_total)
            234 LOAD_CONST               3 (False)
            236 CALL_FUNCTION            2
            238 CALL_FUNCTION           20
            240 CALL_FUNCTION            1
            242 POP_TOP
            244 LOAD_CONST               0 (None)
            246 RETURN_VALUE

Disassembly of score_chance:
511           0 LOAD_CONST               1 (0)
              2 STORE_FAST               2 (score)

512           4 SETUP_LOOP              24 (to 30)
              6 LOAD_FAST                1 (hand)
              8 GET_ITER
        >>   10 FOR_ITER                16 (to 28)
             12 STORE_FAST               3 (die)

513          14 LOAD_FAST                2 (score)
             16 LOAD_GLOBAL              0 (int)
             18 LOAD_FAST                3 (die)
             20 CALL_FUNCTION            1
             22 INPLACE_ADD
             24 STORE_FAST               2 (score)
             26 JUMP_ABSOLUTE           10
        >>   28 POP_BLOCK

515     >>   30 LOAD_FAST                2 (score)
             32 LOAD_FAST                0 (self)
             34 STORE_ATTR               1 (chance)

516          36 LOAD_FAST                0 (self)
             38 LOAD_ATTR                2 (update_total)
             40 LOAD_FAST                2 (score)
             42 CALL_FUNCTION            1
             44 POP_TOP

517          46 LOAD_FAST                2 (score)
             48 RETURN_VALUE

Disassembly of score_fives:
263           0 LOAD_GLOBAL              0 (sum)
              2 LOAD_FAST                1 (hand)
              4 LOAD_ATTR                1 (fives)
              6 CALL_FUNCTION            1
              8 STORE_FAST               2 (score)

264          10 LOAD_FAST                2 (score)
             12 LOAD_FAST                0 (self)
             14 STORE_ATTR               1 (fives)

265          16 LOAD_FAST                0 (self)
             18 LOAD_ATTR                2 (update_total)
             20 LOAD_FAST                2 (score)
             22 CALL_FUNCTION            1
             24 POP_TOP

266          26 LOAD_FAST                2 (score)
             28 RETURN_VALUE

Disassembly of score_four_of_a_kind:
394           0 LOAD_FAST                0 (self)
              2 LOAD_ATTR                0 (_score_set)
              4 LOAD_FAST                1 (hand)
              6 LOAD_CONST               1 (4)
              8 CALL_FUNCTION            2
             10 STORE_FAST               2 (score_data)

395          12 LOAD_CONST               2 (0)
             14 STORE_FAST               3 (points)

396          16 LOAD_FAST                2 (score_data)
             18 LOAD_CONST               2 (0)
             20 BINARY_SUBSCR
             22 LOAD_CONST               2 (0)
             24 COMPARE_OP               3 (!=)
             26 POP_JUMP_IF_FALSE       40

397          28 LOAD_FAST                0 (self)
             30 LOAD_ATTR                1 (get_of_a_kind_points)
             32 LOAD_FAST                1 (hand)
             34 LOAD_FAST                2 (score_data)
             36 CALL_FUNCTION            2
             38 STORE_FAST               3 (points)

399     >>   40 LOAD_FAST                3 (points)
             42 LOAD_FAST                0 (self)
             44 STORE_ATTR               2 (four_of_a_kind)

400          46 LOAD_FAST                0 (self)
             48 LOAD_ATTR                3 (update_total)
             50 LOAD_FAST                3 (points)
             52 CALL_FUNCTION            1
             54 POP_TOP

402          56 LOAD_FAST                2 (score_data)
             58 LOAD_CONST               2 (0)
             60 BINARY_SUBSCR
             62 LOAD_CONST               2 (0)
             64 COMPARE_OP               4 (>)
             66 POP_JUMP_IF_FALSE       88
             68 LOAD_FAST                2 (score_data)
             70 LOAD_CONST               3 (1)
             72 BINARY_SUBSCR
             74 LOAD_CONST               2 (0)
             76 COMPARE_OP               4 (>)
             78 POP_JUMP_IF_FALSE       88

403          80 LOAD_CONST               4 (True)
             82 LOAD_FAST                2 (score_data)
             84 BUILD_TUPLE              2
             86 RETURN_VALUE

405     >>   88 LOAD_CONST               5 (False)
             90 LOAD_CONST               2 (0)
             92 LOAD_FAST                2 (score_data)
             94 LOAD_CONST               3 (1)
             96 BINARY_SUBSCR
             98 BUILD_TUPLE              2
            100 BUILD_TUPLE              2
            102 RETURN_VALUE
            104 LOAD_CONST               0 (None)
            106 RETURN_VALUE

Disassembly of score_fours:
257           0 LOAD_GLOBAL              0 (sum)
              2 LOAD_FAST                1 (hand)
              4 LOAD_ATTR                1 (fours)
              6 CALL_FUNCTION            1
              8 STORE_FAST               2 (score)

258          10 LOAD_FAST                2 (score)
             12 LOAD_FAST                0 (self)
             14 STORE_ATTR               1 (fours)

259          16 LOAD_FAST                0 (self)
             18 LOAD_ATTR                2 (update_total)
             20 LOAD_FAST                2 (score)
             22 CALL_FUNCTION            1
             24 POP_TOP

260          26 LOAD_FAST                2 (score)
             28 RETURN_VALUE

Disassembly of score_full_house:
418           0 LOAD_FAST                0 (self)
              2 LOAD_ATTR                0 (determine_full_house)
              4 LOAD_FAST                1 (hand)
              6 CALL_FUNCTION            1
              8 STORE_FAST               2 (is_full_house)

419          10 LOAD_FAST                2 (is_full_house)
             12 POP_JUMP_IF_FALSE       32

420          14 LOAD_CONST               1 (25)
             16 LOAD_FAST                0 (self)
             18 STORE_ATTR               1 (full_house)

421          20 LOAD_FAST                0 (self)
             22 LOAD_ATTR                2 (update_total)
             24 LOAD_CONST               1 (25)
             26 CALL_FUNCTION            1
             28 POP_TOP
             30 JUMP_FORWARD             6 (to 38)

423     >>   32 LOAD_CONST               2 (0)
             34 LOAD_FAST                0 (self)
             36 STORE_ATTR               1 (full_house)

425     >>   38 LOAD_FAST                0 (self)
             40 LOAD_ATTR                1 (full_house)
             42 LOAD_CONST               2 (0)
             44 COMPARE_OP               4 (>)
             46 RETURN_VALUE

Disassembly of score_large_straight:
477           0 LOAD_FAST                0 (self)
              2 LOAD_ATTR                0 (determine_large_straight)
              4 LOAD_FAST                1 (hand)
              6 CALL_FUNCTION            1
              8 STORE_FAST               2 (win_found)

479          10 LOAD_FAST                2 (win_found)
             12 POP_JUMP_IF_FALSE       32

480          14 LOAD_CONST               1 (40)
             16 LOAD_FAST                0 (self)
             18 STORE_ATTR               1 (large_straight)

481          20 LOAD_FAST                0 (self)
             22 LOAD_ATTR                2 (update_total)
             24 LOAD_CONST               1 (40)
             26 CALL_FUNCTION            1
             28 POP_TOP
             30 JUMP_FORWARD             6 (to 38)

483     >>   32 LOAD_CONST               2 (0)
             34 LOAD_FAST                0 (self)
             36 STORE_ATTR               1 (large_straight)

485     >>   38 LOAD_FAST                2 (win_found)
             40 RETURN_VALUE

Disassembly of score_one_pair:
284           0 LOAD_FAST                0 (self)
              2 LOAD_ATTR                0 (_score_set)
              4 LOAD_FAST                1 (hand)
              6 LOAD_CONST               1 (2)
              8 CALL_FUNCTION            2
             10 STORE_FAST               2 (score_data)

285          12 LOAD_FAST                2 (score_data)
             14 LOAD_CONST               2 (0)
             16 BINARY_SUBSCR
             18 LOAD_CONST               2 (0)
             20 COMPARE_OP               4 (>)
             22 POP_JUMP_IF_FALSE       44
             24 LOAD_FAST                2 (score_data)
             26 LOAD_CONST               3 (1)
             28 BINARY_SUBSCR
             30 LOAD_CONST               2 (0)
             32 COMPARE_OP               4 (>)
             34 POP_JUMP_IF_FALSE       44

286          36 LOAD_CONST               4 (True)
             38 LOAD_FAST                2 (score_data)
             40 BUILD_TUPLE              2
             42 RETURN_VALUE

288     >>   44 LOAD_CONST               5 (False)
             46 LOAD_FAST                2 (score_data)
             48 BUILD_TUPLE              2
             50 RETURN_VALUE
             52 LOAD_CONST               0 (None)
             54 RETURN_VALUE

Disassembly of score_ones:
239           0 LOAD_GLOBAL              0 (sum)
              2 LOAD_FAST                1 (hand)
              4 LOAD_ATTR                1 (ones)
              6 CALL_FUNCTION            1
              8 STORE_FAST               2 (score)

240          10 LOAD_FAST                2 (score)
             12 LOAD_FAST                0 (self)
             14 STORE_ATTR               1 (ones)

241          16 LOAD_FAST                0 (self)
             18 LOAD_ATTR                2 (update_total)
             20 LOAD_FAST                2 (score)
             22 CALL_FUNCTION            1
             24 POP_TOP

242          26 LOAD_FAST                2 (score)
             28 RETURN_VALUE

Disassembly of score_sixes:
269           0 LOAD_GLOBAL              0 (sum)
              2 LOAD_FAST                1 (hand)
              4 LOAD_ATTR                1 (sixes)
              6 CALL_FUNCTION            1
              8 STORE_FAST               2 (score)

270          10 LOAD_FAST                2 (score)
             12 LOAD_FAST                0 (self)
             14 STORE_ATTR               1 (sixes)

271          16 LOAD_FAST                0 (self)
             18 LOAD_ATTR                2 (update_total)
             20 LOAD_FAST                2 (score)
             22 CALL_FUNCTION            1
             24 POP_TOP

272          26 LOAD_FAST                2 (score)
             28 RETURN_VALUE

Disassembly of score_small_straight:
450           0 LOAD_FAST                0 (self)
              2 LOAD_ATTR                0 (determine_small_straight)
              4 LOAD_FAST                1 (hand)
              6 CALL_FUNCTION            1
              8 STORE_FAST               2 (win_found)

452          10 LOAD_FAST                2 (win_found)
             12 POP_JUMP_IF_FALSE       32

453          14 LOAD_CONST               1 (30)
             16 LOAD_FAST                0 (self)
             18 STORE_ATTR               1 (small_straight)

454          20 LOAD_FAST                0 (self)
             22 LOAD_ATTR                2 (update_total)
             24 LOAD_CONST               1 (30)
             26 CALL_FUNCTION            1
             28 POP_TOP
             30 JUMP_FORWARD             6 (to 38)

456     >>   32 LOAD_CONST               2 (0)
             34 LOAD_FAST                0 (self)
             36 STORE_ATTR               1 (small_straight)

458     >>   38 LOAD_FAST                2 (win_found)
             40 RETURN_VALUE

Disassembly of score_three_of_a_kind:
376           0 LOAD_FAST                1 (hand)
              2 POP_JUMP_IF_FALSE       50

377           4 LOAD_FAST                0 (self)
              6 LOAD_ATTR                0 (determine_3_of_kind)
              8 LOAD_FAST                1 (hand)
             10 CALL_FUNCTION            1
             12 STORE_FAST               2 (data)

379          14 LOAD_FAST                2 (data)
             16 LOAD_CONST               1 (1)
             18 BINARY_SUBSCR
             20 LOAD_CONST               2 (0)
             22 BINARY_SUBSCR
             24 LOAD_FAST                0 (self)
             26 STORE_ATTR               1 (three_of_a_kind)

380          28 LOAD_FAST                0 (self)
             30 LOAD_ATTR                2 (update_total)
             32 LOAD_FAST                2 (data)
             34 LOAD_CONST               1 (1)
             36 BINARY_SUBSCR
             38 LOAD_CONST               2 (0)
             40 BINARY_SUBSCR
             42 CALL_FUNCTION            1
             44 POP_TOP

382          46 LOAD_FAST                2 (data)
             48 RETURN_VALUE

384     >>   50 LOAD_CONST               0 (None)
             52 RETURN_VALUE

Disassembly of score_threes:
251           0 LOAD_GLOBAL              0 (sum)
              2 LOAD_FAST                1 (hand)
              4 LOAD_ATTR                1 (threes)
              6 CALL_FUNCTION            1
              8 STORE_FAST               2 (score)

252          10 LOAD_FAST                2 (score)
             12 LOAD_FAST                0 (self)
             14 STORE_ATTR               1 (threes)

253          16 LOAD_FAST                0 (self)
             18 LOAD_ATTR                2 (update_total)
             20 LOAD_FAST                2 (score)
             22 CALL_FUNCTION            1
             24 POP_TOP

254          26 LOAD_FAST                2 (score)
             28 RETURN_VALUE

Disassembly of score_twos:
245           0 LOAD_GLOBAL              0 (sum)
              2 LOAD_FAST                1 (hand)
              4 LOAD_ATTR                1 (twos)
              6 CALL_FUNCTION            1
              8 STORE_FAST               2 (score)

246          10 LOAD_FAST                2 (score)
             12 LOAD_FAST                0 (self)
             14 STORE_ATTR               1 (twos)

247          16 LOAD_FAST                0 (self)
             18 LOAD_ATTR                2 (update_total)
             20 LOAD_FAST                2 (score)
             22 CALL_FUNCTION            1
             24 POP_TOP

248          26 LOAD_FAST                2 (score)
             28 RETURN_VALUE

Disassembly of score_yatzy:
499           0 LOAD_FAST                0 (self)
              2 LOAD_ATTR                0 (determine_yatzy)
              4 LOAD_FAST                1 (hand)
              6 CALL_FUNCTION            1
              8 STORE_FAST               2 (is_yatzy)

500          10 LOAD_CONST               1 (0)
             12 STORE_FAST               3 (score)

502          14 LOAD_FAST                2 (is_yatzy)
             16 POP_JUMP_IF_FALSE       30
             18 LOAD_FAST                0 (self)
             20 LOAD_ATTR                1 (yatzy)
             22 UNARY_NOT
             24 POP_JUMP_IF_FALSE       30

503          26 LOAD_CONST               2 (50)
             28 STORE_FAST               3 (score)

505     >>   30 LOAD_FAST                3 (score)
             32 LOAD_FAST                0 (self)
             34 STORE_ATTR               1 (yatzy)

506          36 LOAD_FAST                3 (score)
             38 LOAD_CONST               1 (0)
             40 COMPARE_OP               4 (>)
             42 POP_JUMP_IF_FALSE       54

507          44 LOAD_FAST                0 (self)
             46 LOAD_ATTR                2 (update_total)
             48 LOAD_FAST                3 (score)
             50 CALL_FUNCTION            1
             52 POP_TOP

508     >>   54 LOAD_FAST                3 (score)
             56 RETURN_VALUE

Disassembly of set_name:
160           0 LOAD_FAST                1 (name)
              2 LOAD_CONST               1 ('')
              4 COMPARE_OP               3 (!=)
              6 POP_JUMP_IF_FALSE       16

161           8 LOAD_FAST                1 (name)
             10 LOAD_FAST                0 (self)
             12 STORE_ATTR               0 (player_name)
             14 JUMP_FORWARD             6 (to 22)

163     >>   16 LOAD_CONST               2 ('player1')
             18 LOAD_FAST                0 (self)
             20 STORE_ATTR               0 (player_name)
        >>   22 LOAD_CONST               0 (None)
             24 RETURN_VALUE

Disassembly of set_score:
521           0 LOAD_CONST               1 (<code object empty at 0x10a307f60, file "/Users/winniepalangpour/git/winrox.github.io/src/yatzy.py", line 521>)
              2 LOAD_CONST               2 ('YatzyScore.set_score.<locals>.empty')
              4 MAKE_FUNCTION            0
              6 STORE_FAST               4 (empty)

527           8 LOAD_FAST                0 (self)
             10 LOAD_ATTR                0 (determine_yatzy)
             12 LOAD_FAST                1 (hand)
             14 CALL_FUNCTION            1
             16 POP_JUMP_IF_FALSE       68
             18 LOAD_FAST                4 (empty)
             20 LOAD_FAST                0 (self)
             22 LOAD_ATTR                1 (yatzy)
             24 CALL_FUNCTION            1
             26 UNARY_NOT
             28 POP_JUMP_IF_FALSE       68

528          30 LOAD_FAST                0 (self)
             32 LOAD_ATTR                2 (yatzy_bonus)
             34 POP_JUMP_IF_FALSE       62

529          36 LOAD_FAST                0 (self)
             38 DUP_TOP
             40 LOAD_ATTR                2 (yatzy_bonus)
             42 LOAD_CONST               3 (100)
             44 INPLACE_ADD
             46 ROT_TWO
             48 STORE_ATTR               2 (yatzy_bonus)

530          50 LOAD_FAST                0 (self)
             52 LOAD_ATTR                3 (update_total)
             54 LOAD_CONST               3 (100)
             56 CALL_FUNCTION            1
             58 POP_TOP
             60 JUMP_FORWARD             6 (to 68)

532     >>   62 LOAD_CONST               3 (100)
             64 LOAD_FAST                0 (self)
             66 STORE_ATTR               2 (yatzy_bonus)

534     >>   68 LOAD_FAST                2 (category)
             70 LOAD_CONST               4 ('ones')
             72 COMPARE_OP               2 (==)
             74 POP_JUMP_IF_FALSE      100
             76 LOAD_FAST                4 (empty)
             78 LOAD_FAST                0 (self)
             80 LOAD_ATTR                4 (ones)
             82 CALL_FUNCTION            1
             84 POP_JUMP_IF_FALSE      100

535          86 LOAD_FAST                0 (self)
             88 LOAD_ATTR                5 (score_ones)
             90 LOAD_FAST                1 (hand)
             92 CALL_FUNCTION            1
             94 POP_TOP
             96 EXTENDED_ARG             1
             98 JUMP_FORWARD           438 (to 538)

536     >>  100 LOAD_FAST                2 (category)
            102 LOAD_CONST               5 ('twos')
            104 COMPARE_OP               2 (==)
            106 POP_JUMP_IF_FALSE      132
            108 LOAD_FAST                4 (empty)
            110 LOAD_FAST                0 (self)
            112 LOAD_ATTR                6 (twos)
            114 CALL_FUNCTION            1
            116 POP_JUMP_IF_FALSE      132

537         118 LOAD_FAST                0 (self)
            120 LOAD_ATTR                7 (score_twos)
            122 LOAD_FAST                1 (hand)
            124 CALL_FUNCTION            1
            126 POP_TOP
            128 EXTENDED_ARG             1
            130 JUMP_FORWARD           406 (to 538)

538     >>  132 LOAD_FAST                2 (category)
            134 LOAD_CONST               6 ('threes')
            136 COMPARE_OP               2 (==)
            138 POP_JUMP_IF_FALSE      164
            140 LOAD_FAST                4 (empty)
            142 LOAD_FAST                0 (self)
            144 LOAD_ATTR                8 (threes)
            146 CALL_FUNCTION            1
            148 POP_JUMP_IF_FALSE      164

539         150 LOAD_FAST                0 (self)
            152 LOAD_ATTR                9 (score_threes)
            154 LOAD_FAST                1 (hand)
            156 CALL_FUNCTION            1
            158 POP_TOP
            160 EXTENDED_ARG             1
            162 JUMP_FORWARD           374 (to 538)

540     >>  164 LOAD_FAST                2 (category)
            166 LOAD_CONST               7 ('fours')
            168 COMPARE_OP               2 (==)
            170 POP_JUMP_IF_FALSE      196
            172 LOAD_FAST                4 (empty)
            174 LOAD_FAST                0 (self)
            176 LOAD_ATTR               10 (fours)
            178 CALL_FUNCTION            1
            180 POP_JUMP_IF_FALSE      196

541         182 LOAD_FAST                0 (self)
            184 LOAD_ATTR               11 (score_fours)
            186 LOAD_FAST                1 (hand)
            188 CALL_FUNCTION            1
            190 POP_TOP
            192 EXTENDED_ARG             1
            194 JUMP_FORWARD           342 (to 538)

542     >>  196 LOAD_FAST                2 (category)
            198 LOAD_CONST               8 ('fives')
            200 COMPARE_OP               2 (==)
            202 POP_JUMP_IF_FALSE      228
            204 LOAD_FAST                4 (empty)
            206 LOAD_FAST                0 (self)
            208 LOAD_ATTR               12 (fives)
            210 CALL_FUNCTION            1
            212 POP_JUMP_IF_FALSE      228

543         214 LOAD_FAST                0 (self)
            216 LOAD_ATTR               13 (score_fives)
            218 LOAD_FAST                1 (hand)
            220 CALL_FUNCTION            1
            222 POP_TOP
            224 EXTENDED_ARG             1
            226 JUMP_FORWARD           310 (to 538)

544     >>  228 LOAD_FAST                2 (category)
            230 LOAD_CONST               9 ('sixes')
            232 COMPARE_OP               2 (==)
            234 JUMP_IF_FALSE_OR_POP   244
            236 LOAD_FAST                4 (empty)
            238 LOAD_FAST                0 (self)
            240 LOAD_ATTR               14 (sixes)
            242 CALL_FUNCTION            1
        >>  244 EXTENDED_ARG             1
            246 POP_JUMP_IF_FALSE      262

545         248 LOAD_FAST                0 (self)
            250 LOAD_ATTR               15 (score_sixes)
            252 LOAD_FAST                1 (hand)
            254 CALL_FUNCTION            1
            256 POP_TOP
            258 EXTENDED_ARG             1
            260 JUMP_FORWARD           276 (to 538)

547     >>  262 LOAD_FAST                2 (category)
            264 LOAD_CONST              10 ('three of a kind')
            266 COMPARE_OP               2 (==)
            268 EXTENDED_ARG             1
            270 POP_JUMP_IF_TRUE       282
            272 LOAD_FAST                2 (category)
            274 LOAD_CONST              11 ('3 of a kind')
            276 COMPARE_OP               2 (==)
            278 EXTENDED_ARG             1
            280 POP_JUMP_IF_FALSE      306

548     >>  282 LOAD_FAST                4 (empty)
            284 LOAD_FAST                0 (self)
            286 LOAD_ATTR               16 (three_of_a_kind)
            288 CALL_FUNCTION            1
            290 EXTENDED_ARG             1
            292 POP_JUMP_IF_FALSE      306

550         294 LOAD_FAST                0 (self)
            296 LOAD_ATTR               17 (score_three_of_a_kind)
            298 LOAD_FAST                1 (hand)
            300 CALL_FUNCTION            1
            302 POP_TOP
            304 JUMP_FORWARD           232 (to 538)

552     >>  306 LOAD_FAST                2 (category)
            308 LOAD_CONST              12 ('four of a kind')
            310 COMPARE_OP               2 (==)
            312 EXTENDED_ARG             1
            314 POP_JUMP_IF_TRUE       326
            316 LOAD_FAST                2 (category)
            318 LOAD_CONST              13 ('4 of a kind')
            320 COMPARE_OP               2 (==)
            322 EXTENDED_ARG             1
            324 POP_JUMP_IF_FALSE      350

553     >>  326 LOAD_FAST                4 (empty)
            328 LOAD_FAST                0 (self)
            330 LOAD_ATTR               18 (four_of_a_kind)
            332 CALL_FUNCTION            1
            334 EXTENDED_ARG             1
            336 POP_JUMP_IF_FALSE      350

555         338 LOAD_FAST                0 (self)
            340 LOAD_ATTR               19 (score_four_of_a_kind)
            342 LOAD_FAST                1 (hand)
            344 CALL_FUNCTION            1
            346 POP_TOP
            348 JUMP_FORWARD           188 (to 538)

556     >>  350 LOAD_FAST                2 (category)
            352 LOAD_CONST              14 ('full house')
            354 COMPARE_OP               2 (==)
            356 EXTENDED_ARG             1
            358 POP_JUMP_IF_FALSE      384
            360 LOAD_FAST                4 (empty)
            362 LOAD_FAST                0 (self)
            364 LOAD_ATTR               20 (full_house)
            366 CALL_FUNCTION            1
            368 EXTENDED_ARG             1
            370 POP_JUMP_IF_FALSE      384

557         372 LOAD_FAST                0 (self)
            374 LOAD_ATTR               21 (score_full_house)
            376 LOAD_FAST                1 (hand)
            378 CALL_FUNCTION            1
            380 POP_TOP
            382 JUMP_FORWARD           154 (to 538)

558     >>  384 LOAD_FAST                2 (category)
            386 LOAD_CONST              15 ('small straight')
            388 COMPARE_OP               2 (==)
            390 EXTENDED_ARG             1
            392 POP_JUMP_IF_FALSE      418
            394 LOAD_FAST                4 (empty)
            396 LOAD_FAST                0 (self)
            398 LOAD_ATTR               22 (small_straight)
            400 CALL_FUNCTION            1
            402 EXTENDED_ARG             1
            404 POP_JUMP_IF_FALSE      418

559         406 LOAD_FAST                0 (self)
            408 LOAD_ATTR               23 (score_small_straight)
            410 LOAD_FAST                1 (hand)
            412 CALL_FUNCTION            1
            414 POP_TOP
            416 JUMP_FORWARD           120 (to 538)

560     >>  418 LOAD_FAST                2 (category)
            420 LOAD_CONST              16 ('large straight')
            422 COMPARE_OP               2 (==)
            424 EXTENDED_ARG             1
            426 POP_JUMP_IF_FALSE      452
            428 LOAD_FAST                4 (empty)
            430 LOAD_FAST                0 (self)
            432 LOAD_ATTR               24 (large_straight)
            434 CALL_FUNCTION            1
            436 EXTENDED_ARG             1
            438 POP_JUMP_IF_FALSE      452

561         440 LOAD_FAST                0 (self)
            442 LOAD_ATTR               25 (score_large_straight)
            444 LOAD_FAST                1 (hand)
            446 CALL_FUNCTION            1
            448 POP_TOP
            450 JUMP_FORWARD            86 (to 538)

562     >>  452 LOAD_FAST                2 (category)
            454 LOAD_CONST              17 ('chance')
            456 COMPARE_OP               2 (==)
            458 EXTENDED_ARG             1
            460 POP_JUMP_IF_FALSE      486
            462 LOAD_FAST                4 (empty)
            464 LOAD_FAST                0 (self)
            466 LOAD_ATTR               26 (chance)
            468 CALL_FUNCTION            1
            470 EXTENDED_ARG             1
            472 POP_JUMP_IF_FALSE      486

563         474 LOAD_FAST                0 (self)
            476 LOAD_ATTR               27 (score_chance)
            478 LOAD_FAST                1 (hand)
            480 CALL_FUNCTION            1
            482 POP_TOP
            484 JUMP_FORWARD            52 (to 538)

565     >>  486 LOAD_FAST                2 (category)
            488 LOAD_CONST              18 ('yatzy')
            490 COMPARE_OP               2 (==)
            492 EXTENDED_ARG             1
            494 POP_JUMP_IF_TRUE       506
            496 LOAD_FAST                2 (category)
            498 LOAD_CONST              19 ('yachtzee')
            500 COMPARE_OP               2 (==)
            502 EXTENDED_ARG             2
            504 POP_JUMP_IF_FALSE      530

566     >>  506 LOAD_FAST                4 (empty)
            508 LOAD_FAST                0 (self)
            510 LOAD_ATTR                1 (yatzy)
            512 CALL_FUNCTION            1
            514 EXTENDED_ARG             2
            516 POP_JUMP_IF_FALSE      530

568         518 LOAD_FAST                0 (self)
            520 LOAD_ATTR               28 (score_yatzy)
            522 LOAD_FAST                1 (hand)
            524 CALL_FUNCTION            1
            526 POP_TOP
            528 JUMP_FORWARD             8 (to 538)

570     >>  530 LOAD_FAST                3 (invalid_choice)
            532 LOAD_FAST                1 (hand)
            534 CALL_FUNCTION            1
            536 POP_TOP

574     >>  538 LOAD_FAST                4 (empty)
            540 LOAD_FAST                0 (self)
            542 LOAD_ATTR               29 (upper_total)
            544 CALL_FUNCTION            1
            546 EXTENDED_ARG             2
            548 POP_JUMP_IF_FALSE      726

575         550 LOAD_FAST                4 (empty)
            552 LOAD_FAST                0 (self)
            554 LOAD_ATTR                4 (ones)
            556 CALL_FUNCTION            1
            558 UNARY_NOT
            560 EXTENDED_ARG             2
            562 POP_JUMP_IF_FALSE      726

576         564 LOAD_FAST                4 (empty)
            566 LOAD_FAST                0 (self)
            568 LOAD_ATTR                6 (twos)
            570 CALL_FUNCTION            1
            572 UNARY_NOT
            574 EXTENDED_ARG             2
            576 POP_JUMP_IF_FALSE      726

577         578 LOAD_FAST                4 (empty)
            580 LOAD_FAST                0 (self)
            582 LOAD_ATTR                8 (threes)
            584 CALL_FUNCTION            1
            586 UNARY_NOT
            588 EXTENDED_ARG             2
            590 POP_JUMP_IF_FALSE      726

578         592 LOAD_FAST                4 (empty)
            594 LOAD_FAST                0 (self)
            596 LOAD_ATTR               10 (fours)
            598 CALL_FUNCTION            1
            600 UNARY_NOT
            602 EXTENDED_ARG             2
            604 POP_JUMP_IF_FALSE      726

579         606 LOAD_FAST                4 (empty)
            608 LOAD_FAST                0 (self)
            610 LOAD_ATTR               12 (fives)
            612 CALL_FUNCTION            1
            614 UNARY_NOT
            616 EXTENDED_ARG             2
            618 POP_JUMP_IF_FALSE      726

580         620 LOAD_FAST                4 (empty)
            622 LOAD_FAST                0 (self)
            624 LOAD_ATTR               14 (sixes)
            626 CALL_FUNCTION            1
            628 UNARY_NOT
            630 EXTENDED_ARG             2
            632 POP_JUMP_IF_FALSE      726

588         634 LOAD_FAST                0 (self)
            636 LOAD_ATTR                4 (ones)
            638 LOAD_FAST                0 (self)
            640 LOAD_ATTR                6 (twos)
            642 BINARY_ADD
            644 LOAD_FAST                0 (self)
            646 LOAD_ATTR                8 (threes)
            648 BINARY_ADD
            650 LOAD_FAST                0 (self)
            652 LOAD_ATTR               10 (fours)
            654 BINARY_ADD
            656 LOAD_FAST                0 (self)
            658 LOAD_ATTR               12 (fives)
            660 BINARY_ADD
            662 LOAD_FAST                0 (self)
            664 LOAD_ATTR               14 (sixes)
            666 BINARY_ADD
            668 STORE_FAST               5 (upper_total)

590         670 LOAD_FAST                5 (upper_total)
            672 LOAD_FAST                0 (self)
            674 STORE_ATTR              30 (total)

591         676 LOAD_FAST                5 (upper_total)
            678 LOAD_CONST              20 (63)
            680 COMPARE_OP               4 (>)
            682 EXTENDED_ARG             2
            684 POP_JUMP_IF_FALSE      704

592         686 LOAD_CONST              21 (35)
            688 LOAD_FAST                0 (self)
            690 STORE_ATTR              31 (bonus)

593         692 LOAD_FAST                0 (self)
            694 LOAD_ATTR                3 (update_total)
            696 LOAD_CONST              21 (35)
            698 CALL_FUNCTION            1
            700 POP_TOP
            702 JUMP_FORWARD             6 (to 710)

595     >>  704 LOAD_CONST              22 (0)
            706 LOAD_FAST                0 (self)
            708 STORE_ATTR              31 (bonus)

596     >>  710 LOAD_FAST                5 (upper_total)
            712 LOAD_FAST                0 (self)
            714 LOAD_ATTR               31 (bonus)
            716 INPLACE_ADD
            718 STORE_FAST               5 (upper_total)

597         720 LOAD_FAST                5 (upper_total)
            722 LOAD_FAST                0 (self)
            724 STORE_ATTR              29 (upper_total)

600     >>  726 LOAD_FAST                4 (empty)
            728 LOAD_FAST                0 (self)
            730 LOAD_ATTR               32 (lower_total)
            732 CALL_FUNCTION            1
            734 EXTENDED_ARG             3
            736 POP_JUMP_IF_FALSE      890

601         738 LOAD_FAST                4 (empty)
            740 LOAD_FAST                0 (self)
            742 LOAD_ATTR               16 (three_of_a_kind)
            744 CALL_FUNCTION            1
            746 UNARY_NOT
            748 EXTENDED_ARG             3
            750 POP_JUMP_IF_FALSE      890

602         752 LOAD_FAST                4 (empty)
            754 LOAD_FAST                0 (self)
            756 LOAD_ATTR               18 (four_of_a_kind)
            758 CALL_FUNCTION            1
            760 UNARY_NOT
            762 EXTENDED_ARG             3
            764 POP_JUMP_IF_FALSE      890

603         766 LOAD_FAST                4 (empty)
            768 LOAD_FAST                0 (self)
            770 LOAD_ATTR               20 (full_house)
            772 CALL_FUNCTION            1
            774 UNARY_NOT
            776 EXTENDED_ARG             3
            778 POP_JUMP_IF_FALSE      890

604         780 LOAD_FAST                4 (empty)
            782 LOAD_FAST                0 (self)
            784 LOAD_ATTR               22 (small_straight)
            786 CALL_FUNCTION            1
            788 UNARY_NOT
            790 EXTENDED_ARG             3
            792 POP_JUMP_IF_FALSE      890

605         794 LOAD_FAST                4 (empty)
            796 LOAD_FAST                0 (self)
            798 LOAD_ATTR               24 (large_straight)
            800 CALL_FUNCTION            1
            802 UNARY_NOT
            804 EXTENDED_ARG             3
            806 POP_JUMP_IF_FALSE      890

606         808 LOAD_FAST                4 (empty)
            810 LOAD_FAST                0 (self)
            812 LOAD_ATTR                1 (yatzy)
            814 CALL_FUNCTION            1
            816 UNARY_NOT
            818 EXTENDED_ARG             3
            820 POP_JUMP_IF_FALSE      890

607         822 LOAD_FAST                4 (empty)
            824 LOAD_FAST                0 (self)
            826 LOAD_ATTR               26 (chance)
            828 CALL_FUNCTION            1
            830 UNARY_NOT
            832 EXTENDED_ARG             3
            834 POP_JUMP_IF_FALSE      890

617         836 LOAD_FAST                0 (self)
            838 LOAD_ATTR               16 (three_of_a_kind)
            840 LOAD_FAST                0 (self)
            842 LOAD_ATTR               18 (four_of_a_kind)
            844 BINARY_ADD
            846 LOAD_FAST                0 (self)
            848 LOAD_ATTR               20 (full_house)
            850 BINARY_ADD
            852 LOAD_FAST                0 (self)
            854 LOAD_ATTR               22 (small_straight)
            856 BINARY_ADD
            858 LOAD_FAST                0 (self)
            860 LOAD_ATTR               24 (large_straight)
            862 BINARY_ADD
            864 LOAD_FAST                0 (self)
            866 LOAD_ATTR                1 (yatzy)
            868 BINARY_ADD
            870 LOAD_FAST                0 (self)
            872 LOAD_ATTR               26 (chance)
            874 BINARY_ADD
            876 LOAD_FAST                0 (self)
            878 LOAD_ATTR                2 (yatzy_bonus)
            880 BINARY_ADD
            882 STORE_FAST               6 (lower_total)

619         884 LOAD_FAST                6 (lower_total)
            886 LOAD_FAST                0 (self)
            888 STORE_ATTR              32 (lower_total)
        >>  890 LOAD_CONST               0 (None)
            892 RETURN_VALUE

Disassembly of update_total:
236           0 LOAD_FAST                0 (self)
              2 DUP_TOP
              4 LOAD_ATTR                0 (grand_total)
              6 LOAD_FAST                1 (newly_added_score)
              8 INPLACE_ADD
             10 ROT_TWO
             12 STORE_ATTR               0 (grand_total)
             14 LOAD_CONST               0 (None)
             16 RETURN_VALUE


Disassembly of randint:
221           0 LOAD_FAST                0 (self)
              2 LOAD_ATTR                0 (randrange)
              4 LOAD_FAST                1 (a)
              6 LOAD_FAST                2 (b)
              8 LOAD_CONST               1 (1)
             10 BINARY_ADD
             12 CALL_FUNCTION            2
             14 RETURN_VALUE

Disassembly of regex_sub:
191           0 LOAD_GLOBAL              0 (_compile)
              2 LOAD_FAST                0 (pattern)
              4 LOAD_FAST                4 (flags)
              6 CALL_FUNCTION            2
              8 LOAD_ATTR                1 (sub)
             10 LOAD_FAST                1 (repl)
             12 LOAD_FAST                2 (string)
             14 LOAD_FAST                3 (count)
             16 CALL_FUNCTION            3
             18 RETURN_VALUE

