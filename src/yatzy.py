from random import randint
from time import sleep
from os import system as os_system, name as os_name
from re import sub as regex_sub

class Dice:
    def __init__(self, sides=2, value=0):
        if not sides >= 2:
            raise ValueError("Must have at least 2 sides")
        if not isinstance(sides, int):
            raise ValueError("Sides must be a whole number")
        if not isinstance(value, int):
            raise ValueError("Value must be a whole number")

        self.value = value or randint(1, sides)

    def __int__(self):
        return self.value

    def __eq__(self, other):
        return int(self) == other

    def __ne__(self, other):
        return int(self) != other

    def __gt__(self, other):
        return int(self) > other

    def __lt__(self, other):
        return int(self) < other

    def __ge__(self, other):
        this = int(self)
        return this > other or this == other

    def __le__(self, other):
        this = int(self)
        return this < other or this == other

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return int(self) + other

    def __repr__(self):
        return str(self.value)


class D6(Dice):
    def __init__(self, value=0):
        super().__init__(sides=6, value=value)


class Hand(list):
    def __init__(self, size=0, die_class=None, *args, **kwargs):
        if not die_class:
            raise ValueError("You must provide a die class!")
        super().__init__()

        for _ in range(size):
            self.append(die_class())
        self.sort()

    def _by_value(self, value):
        dice = []
        for die in self:
            if die == value:
                dice.append(die)
        return dice

    @classmethod
    def roll(Hand, die_type=D6, size=5):
        return Hand(size, die_class=die_type)


class YatzyHand(Hand):
    def __init__(self, *args, **kwargs):
        super().__init__(size=5, die_class=D6, *args, **kwargs)

    def __append__(self, item):
        print("".format(type(self)))
        self.append(item)
        print(self)

    @property
    def ones(self):
        return self._by_value(1)

    @property
    def twos(self):
        return self._by_value(2)

    @property
    def threes(self):
        return self._by_value(3)

    @property
    def fours(self):
        return self._by_value(4)

    @property
    def fives(self):
        return self._by_value(5)

    @property
    def sixes(self):
        return self._by_value(6)

    @property
    def _sets(self):
        return {
            1: len(self.ones),
            2: len(self.twos),
            3: len(self.threes),
            4: len(self.fours),
            5: len(self.fives),
            6: len(self.sixes)
        }


class YatzyScore:

    player_name = None
    # ------------------------
    #   Upper Section
    # ------------------------
    ones = None
    twos = None
    threes = None
    fours = None
    fives = None
    sixes = None
    total = None
    # bonus applies if total above is >= 63
    bonus = None
    upper_total = None
    # ------------------------
    #   Lower Section
    # ------------------------
    three_of_a_kind = None
    four_of_a_kind = None
    full_house = None
    small_straight = None
    large_straight = None
    yatzy = None
    chance = None
    # each additional yatzy beyond 1 is worth 100 points
    yatzy_bonus = 0
    lower_total = None
    # ------------------------
    #   Total
    # ------------------------
    grand_total = 0

    def __init__(self, name=None):
        self.player_name = name

    def set_name(self, name):
        if name != "":
            self.player_name = name
        else:
            self.player_name = "player1"

    def get_state(self):
        return {
            "ones": self.ones,
            "twos": self.twos,
            "threes": self.threes,
            "fours": self.fours,
            "fives": self.fives,
            "sixes": self.sixes,
            "three_of_a_kind": self.three_of_a_kind,
            "four_of_a_kind": self.four_of_a_kind,
            "full_house": self.full_house,
            "small_straight": self.small_straight,
            "large_straight": self.large_straight,
            "yatzy": self.yatzy,
            "chance": self.chance
        }

    def _print_a_state(self, state, upper):
        is_int = isinstance(state, int)
        if upper:
            if is_int:
                return (state if len(str(state)) > 1 else " {}".format(state))
            else:
                return "  "
        else:
            return state if is_int else "  "

    def print_score(self):
        print("""
    -----------------------------------------------------
        YATZY ___{}___
    ----------------------------|------------------------
       Upper Section            |   Lower Section
    ----------------------------|------------------------
    ones: {}                    | three of a kind: {}
    twos: {}                    | four of a kind: {}
    threes: {}                  | full house: {}
    fours: {}                   | small straight: {}
    fives: {}                   | large straight: {}
    sixes: {}                   | yatzy: {}
    total: {}                   | chance: {}
    (35 bonus if total >= 63)   | (each additional yatzy = 100)
    bonus: {}                   | yatzy bonus: {}
    upper total: {}             | lower total: {}
    -----------------------------------------------------
        Total: {}
    -----------------------------------------------------
        """.format(
            self.player_name,
            self._print_a_state(self.ones, True),
            self._print_a_state(self.three_of_a_kind, False),
            self._print_a_state(self.twos, True),
            self._print_a_state(self.four_of_a_kind, False),
            self._print_a_state(self.threes, True),
            self._print_a_state(self.full_house, False),
            self._print_a_state(self.fours, True),
            self._print_a_state(self.small_straight, False),
            self._print_a_state(self.fives, True),
            self._print_a_state(self.large_straight, False),
            self._print_a_state(self.sixes, True),
            self._print_a_state(self.yatzy, False),
            self._print_a_state(self.total, False),
            self._print_a_state(self.chance, False),
            self._print_a_state(self.bonus, True),
            self._print_a_state(self.yatzy_bonus, False),
            self._print_a_state(self.upper_total, True),
            self._print_a_state(self.lower_total, False),
            self._print_a_state(self.grand_total, False)
         ))

    def update_total(self, newly_added_score):
        self.grand_total += newly_added_score

    def score_ones(self, hand):
        score = sum(hand.ones)
        self.ones = score
        self.update_total(score)
        return score

    def score_twos(self, hand):
        score = sum(hand.twos)
        self.twos = score
        self.update_total(score)
        return score

    def score_threes(self, hand):
        score = sum(hand.threes)
        self.threes = score
        self.update_total(score)
        return score

    def score_fours(self, hand):
        score = sum(hand.fours)
        self.fours = score
        self.update_total(score)
        return score

    def score_fives(self, hand):
        score = sum(hand.fives)
        self.fives = score
        self.update_total(score)
        return score

    def score_sixes(self, hand):
        score = sum(hand.sixes)
        self.sixes = score
        self.update_total(score)
        return score

    def _score_set(self, hand, set_size):
        scores = [0]
        numbers = [0]
        for worth, count in hand._sets.items():
            if count == set_size:
                scores.append(worth * set_size)
                numbers.append(worth)
        return (max(scores), max(numbers))

    def score_one_pair(self, hand):
        score_data = self._score_set(hand, 2)
        if score_data[0] > 0 and score_data[1] > 0:
            return (True, score_data)
        else:
            return (False, score_data)

    def get_of_a_kind_points(self, hand, score_data):
        hand_without_set = []
        points = score_data[0]
        for num in hand:
            if num != score_data[1]:
                hand_without_set.append(num)
        for num in hand_without_set:
            points += num
        return points

    def find_duplicates(self, hand):
        duplicates = []
        nums_found = []
        for num in hand:
            if num in nums_found:
                duplicates.append(num)
            else:
                nums_found.append(num)
        return duplicates

    def determine_3_in_sequence(self, hand):
        pass_conditions = [
            {1, 2, 3},
            {1, 2, 3, 5, 6},
            {1, 2, 3, 5},
            {1, 2, 3, 6},
            {2, 3, 4},
            {2, 3, 4, 6},
            {3, 4, 5},
            {1, 3, 4, 5},
            {4, 5, 6},
            {1, 4, 5, 6},
            {1, 2, 4, 5, 6},
            {2, 4, 5, 6}
        ]
        set_hand = set([num.value for num in hand])
        if set_hand in pass_conditions:
            index = pass_conditions.index(set_hand)
            win = []

            if index in [0, 1, 2, 3]:
                win = [1, 2, 3]
            elif index in [4, 5]:
                win = [2, 3, 4]
            elif index in [6, 7]:
                win = [3, 4, 5]
            elif index in [8, 9, 10, 11]:
                win = [4, 5, 6]

            return (True, win)
        else:
            return (False, [])

    def determine_two_pair(self, hand):
        duplicates = self.find_duplicates(hand)
        if len(duplicates) == 2:
            return (True, duplicates)
        else:
            return (False, duplicates)

    def determine_two_of_a_kind(self, hand):
        duplicates = self.find_duplicates(hand)
        length = len(duplicates)

        if length > 0 and len(duplicates) == 1:
            hand_without_duplicates = []
            for num in hand:
                if num != duplicates[0]:
                    hand_without_duplicates.append(num)
            if len(hand_without_duplicates) == 3:
                return (True, duplicates[0])
            else:
                return (False, duplicates)
        else:
            return (False, duplicates)

    def determine_3_of_kind(self, hand):
        score_data = self._score_set(hand, 3)
        points = self.get_of_a_kind_points(hand, score_data)

        if score_data[0] > 0 and score_data[1] > 0:
            return (True, (points, score_data[1]))
        else:
            return (False, (0, score_data[1]))

    def score_three_of_a_kind(self, hand=None):
        if hand:
            data = self.determine_3_of_kind(hand)

            self.three_of_a_kind = data[1][0]
            self.update_total(data[1][0])

            return data
        else:
            pass

    def determine_4_of_a_kind(self, hand):
        num = self._score_set(hand, 4)[1]
        if num > 0:
            return True, num
        else:
            return False, num

    def score_four_of_a_kind(self, hand):
        score_data = self._score_set(hand, 4)
        points = 0
        if score_data[0] != 0:
            points = self.get_of_a_kind_points(hand, score_data)

        self.four_of_a_kind = points
        self.update_total(points)

        if score_data[0] > 0 and score_data[1] > 0:
            return (True, score_data)
        else:
            return (False, (0, score_data[1]))

    def determine_full_house(self, hand):
        pair = self.score_one_pair(hand)
        three = self.determine_3_of_kind(hand)
        # if you have 3 of a kind and a pair AND
        # those 2 numbers are different, you've got a full house
        if pair[0] and three[0] and pair[1][1] != three[1][1]:
            return True
        else:
            return False

    def score_full_house(self, hand):
        is_full_house = self.determine_full_house(hand)
        if is_full_house:
            self.full_house = 25
            self.update_total(25)
        else:
            self.full_house = 0

        return self.full_house > 0

    def determine_small_straight(self, hand):
        wins = [
            {1, 2, 3, 4},
            {1, 2, 3, 4, 5},
            {1, 2, 3, 4, 6},
            {2, 3, 4, 5},
            {2, 3, 4, 5, 6},
            {3, 4, 5, 6},
            {1, 3, 4, 5, 6},
            {2, 3, 4, 5, 6}
        ]
        win_found = False
        set_hand = set()

        for num in hand:
            set_hand.add(int(num))

        if set_hand in wins:
            win_found = True

        return win_found

    def score_small_straight(self, hand):
        win_found = self.determine_small_straight(hand)

        if win_found:
            self.small_straight = 30
            self.update_total(30)
        else:
            self.small_straight = 0

        return win_found

    def determine_large_straight(self, hand):
        wins = [
            {1, 2, 3, 4, 5},
            {2, 3, 4, 5, 6}
        ]
        win_found = False
        set_hand = set()

        for die in hand:
            set_hand.add(int(die))

        if set_hand in wins:
            win_found = True

        return win_found

    def score_large_straight(self, hand):
        win_found = self.determine_large_straight(hand)

        if win_found:
            self.large_straight = 40
            self.update_total(40)
        else:
            self.large_straight = 0

        return win_found

    def determine_yatzy(self, hand):
        set_hand = set()

        for die in hand:
            set_hand.add(int(die))

        if len(set_hand) == 1:
            return True
        else:
            return False

    def score_yatzy(self, hand):
        is_yatzy = self.determine_yatzy(hand)
        score = 0

        if is_yatzy and not self.yatzy:
            score = 50

        self.yatzy = score
        if score > 0:
            self.update_total(score)
        return score

    def score_chance(self, hand):
        score = 0
        for die in hand:
            score += int(die)

        self.chance = score
        self.update_total(score)
        return score

    def set_score(self, hand, category, invalid_choice):

        def empty(score):
            if score is None:
                return True
            else:
                return False

        if self.determine_yatzy(hand) and not empty(self.yatzy):
            if self.yatzy_bonus:
                self.yatzy_bonus += 100
                self.update_total(100)
            else:
                self.yatzy_bonus = 100

        if category == 'ones' and empty(self.ones):
            self.score_ones(hand)
        elif category == 'twos' and empty(self.twos):
            self.score_twos(hand)
        elif category == 'threes' and empty(self.threes):
            self.score_threes(hand)
        elif category == 'fours' and empty(self.fours):
            self.score_fours(hand)
        elif category == 'fives' and empty(self.fives):
            self.score_fives(hand)
        elif category == 'sixes' and empty(self.sixes):
            self.score_sixes(hand)
        elif (
            (category == 'three of a kind' or category == '3 of a kind')
            and empty(self.three_of_a_kind)
        ):
            self.score_three_of_a_kind(hand)
        elif (
            (category == 'four of a kind' or category == '4 of a kind')
            and empty(self.four_of_a_kind)
        ):
            self.score_four_of_a_kind(hand)
        elif category == 'full house' and empty(self.full_house):
            self.score_full_house(hand)
        elif category == 'small straight' and empty(self.small_straight):
            self.score_small_straight(hand)
        elif category == 'large straight' and empty(self.large_straight):
            self.score_large_straight(hand)
        elif category == 'chance' and empty(self.chance):
            self.score_chance(hand)
        elif (
            (category == 'yatzy' or category == 'yachtzee')
            and empty(self.yatzy)
        ):
            self.score_yatzy(hand)
        else:
            invalid_choice(hand)


        if (
            empty(self.upper_total)
            and not empty(self.ones)
            and not empty(self.twos)
            and not empty(self.threes)
            and not empty(self.fours)
            and not empty(self.fives)
            and not empty(self.sixes)
        ):
            upper_total = (
                self.ones
                + self.twos
                + self.threes
                + self.fours
                + self.fives
                + self.sixes
            )
            self.total = upper_total
            if upper_total > 63:
                self.bonus = 35
                self.update_total(35)
            else:
                self.bonus = 0
            upper_total += self.bonus
            self.upper_total = upper_total

        if (
            empty(self.lower_total)
            and not empty(self.three_of_a_kind)
            and not empty(self.four_of_a_kind)
            and not empty(self.full_house)
            and not empty(self.small_straight)
            and not empty(self.large_straight)
            and not empty(self.yatzy)
            and not empty(self.chance)
        ):
            lower_total = (
                self.three_of_a_kind
                + self.four_of_a_kind
                + self.full_house
                + self.small_straight
                + self.large_straight
                + self.yatzy
                + self.chance
                + self.yatzy_bonus
            )
            self.lower_total = lower_total


class PlayYatzy:
    playing = True
    score = YatzyScore()
    comp_score = YatzyScore('computer')
    help_shown_last = False
    turn = 1

    def clear_screen(self):
        os_system("cls" if os_name == "nt" else "clear")

    def show_help(self):
        self.help_shown_last = True
        print("""
    "help" or "h": opens this menu
    "roll" or "r": rolls five dice
    "quit" or "q": quits the game
    -----------------------
    SCORING:
    -----------------------
    To choose where to place
    your score you must match
    a word or phrase from the
    scorecard:

    ----------------------------|----------------------------
       Upper Section            |   Lower Section
    ----------------------------|----------------------------
    This section this scored    |  I've listed the points
    by adding the number of dice|  for each in this part below
    in your hand which match    |
    the description.            |  (total = total of dice)
                                |
    ones:                       |  three of a kind: total
    twos:                       |  four of a kind: total
    threes:                     |  full house: 25
    fours:                      |  small straight: 30
    fives:                      |  large straight: 40
    sixes:                      |  yatzy: 50
    total:                      |  chance: total
    (35 bonus if total >= 63)   |  (each additional yatzy = 100)
    bonus:                      |  yatzy bonus: see above
    upper total:                |  lower total:
    ---------------------------------------------------------
        Total:
    ---------------------------------------------------------

    Example: (user input follows ">>  ")

    Welcome to script yatzy!
    Type 'roll' or 'r' to begin playing!
    >>  roll
    You rolled 1 1 4 3 5
    Would you like to roll again? Y/N
    >> y
    Please indicate which numbers you'd like to roll again, separating them with commas
    OR type 'all' or 'cancel'
    >>  4,3,5
    Your new hand is 1 1 1 6 6
    Please indicate which part of your scorecard you'd like to fill in.
    >> full houseSorry you've already used this portion of your scorecard

        """)
        input("Hit the enter key when you're ready to return to the game.\n>>  ")
        self.clear_screen()
        print("Turn resumed.")

    def prompt_to_roll_again_and_score(self, hand):
        if self.help_shown_last:
            self.print_hand(hand, False)
            self.help_shown_last = False
        roll_again = input("Would you like to roll again? Y/N\n>>  ").lower().strip()
        if roll_again == 'help' or roll_again == 'h':
            self.show_help()
            return self.prompt_to_roll_again_and_score(hand)
        elif roll_again == 'y' or roll_again == 'yes':
            self.re_roll(hand)
        else:
            self.choose_score(hand)

    def roll_action(self):
        hand = YatzyHand()
        self.print_hand(hand, False)
        self.prompt_to_roll_again_and_score(hand)

    def print_hand(self, hand, new):
        re_rolled = "new " if new else ""
        print("Your {}hand is {} {} {} {} {}".format(re_rolled, hand[0], hand[1], hand[2], hand[3], hand[4]))

    def re_roll(self, hand):
        if self.help_shown_last:
            self.clear_screen()
            self.print_hand(hand, True)
            self.help_shown_last = False

        nums_to_reroll = input(
            """Please indicate which numbers you'd like to roll again
by separating them with commas (example: 1,2,3)
OR type 'all', 'cancel' or 'help'
>>  """
        ).lower()
        cancelled = False
        error = False
        old_hand = hand

        if nums_to_reroll == 'all':
            nums_to_reroll = ""
            for num in hand:
                nums_to_reroll = nums_to_reroll + "{},".format(num)
        elif nums_to_reroll == 'cancel':
            cancelled = True
        elif nums_to_reroll == 'help' or nums_to_reroll == "h":
            self.show_help()
            return self.re_roll(hand)

        nums_to_reroll = regex_sub(r'\s', '', nums_to_reroll).split(',')

        if not cancelled:
            for i in range(len(nums_to_reroll)):
                try:
                    nums_to_reroll[i] = int(nums_to_reroll[i])
                except ValueError:
                    nums_to_reroll.pop(i)

            for num in nums_to_reroll:
                if num in old_hand:
                    old_hand.remove(num)
                else:
                    print("I'm sorry it appears you've entered a number not found in your hand.\n Let's try again.")
                    error = True
                    break

        if error:
            self.re_roll(hand)
        elif cancelled:
            self.choose_score(hand)
        else:
            new_dice_needed = 5 - len(old_hand)
            new_hand = old_hand

            for _ in range(new_dice_needed):
                new_hand.append(D6())

            new_hand.sort()
            self.print_hand(new_hand, True)
            self.choose_score(new_hand)

    def invalid_choice(self, hand):
        print("Sorry you've already used this portion of your scorecard\nOR your choice didn't match an item on the scorecard.\nPlease try again.\n")
        self.choose_score(hand)
        self.turn -= 1

    def end_game(self):
        self.clear_screen()
        print("\nGAME OVER\nHere are the final scorecards:\n")
        self.comp_score.print_score()
        sleep(1)
        self.score.print_score()
        print(f"\n\nYou scored {self.score.grand_total} points")
        sleep(1)
        print(f"The computer scored {self.comp_score.grand_total} points")
        if self.score.grand_total > self.comp_score.grand_total:
            print("Congratulations, you won!!! 🎉 ")
        elif self.score.grand_total == self.comp_score.grand_total:
            print("Yuck, looks like you and the computer tie.")
        else:
            print("Darn! The computer beat you this time.")
        sleep(1)
        print("See you next time 👋 ")
        sleep(2)
        self.playing = False

    def choose_score(self, hand):
        score = self.score
        old_score = score.get_state()
        if self.help_shown_last:
            score.print_score()
            self.print_hand(hand, False)
            self.help_shown_last = False

        category = input("Please indicate which part of your scorecard you'd like to fill in by typing a matching category.\n(example: three of a kind OR twos)\n>>  ").lower().strip()

        if category == 'help' or category == "h":
            self.show_help()
            return self.choose_score(hand)
        else:
            self.score.set_score(hand, category, self.invalid_choice)

        if score.lower_total != None and score.upper_total != None and self.turn % 2 == 0:
            self.clear_screen()
            print("\nGAME OVER\nHere are the final scorecards:\n")
            self.comp_score.print_score()
            sleep(1)
            score.print_score()
            print(f"\n\nYou scored {score.grand_total} points")
            sleep(1)
            print(f"The computer scored {self.comp_score.grand_total} points")
            if score.grand_total > self.comp_score.grand_total:
                print("Congratulations, you won!!! 🎉 ")
            elif score.grand_total == self.comp_score.grand_total:
                print("Yuck, looks like you and the computer tie.")
            else:
                print("Darn! The computer beat you this time.")
            sleep(1)
            print("See you next time 👋 ")
            sleep(2)
            self.playing = False

        # check for score diff before ending hand, otherwise try again
        new_score = score.get_state()
        if not new_score.items() - old_score.items():
            print("Error encountered.\nSorry, but I'll have to ask again.")
            self.print_hand(hand, False)
            self.choose_score(hand)
        else:
            self.turn += 1
            return new_score

    def comp_determine_reroll(self, possibilities, hand):
        nums_to_reroll = list()
        comp_score = self.comp_score
        # figure out which die or dice to re-roll
        if possibilities["small_str"]:
            # determine the out of sequence number and append it to nums_to_reroll
            set_hand = set([die.value for die in hand])
            sym_diff = set()

            if len(set_hand - {1,2,3,4}) == 0:
                sym_diff = set_hand ^ {1,2,3,4}
            elif len(set_hand - {2,3,4,5}) == 0:
                sym_diff= set_hand ^ {2,3,4,5}
            elif len(set_hand - {3,4,5,6}) == 0:
                sym_diff = set_hand ^ {3,4,5,6}

            if len(sym_diff) > 0:
                nums_to_reroll.append(sym_diff.pop())
            else:
                reroll = comp_score.find_duplicates(hand)
                nums_to_reroll.append(reroll)
        elif possibilities["four_of_a"][0]:
            for num in hand:
                if num.value != possibilities["four_of_a"][1]:
                    nums_to_reroll.append(num.value)
        elif possibilities["three_of_a"][0]:
            for num in hand:
               if num.value != possibilities["three_of_a"][1][1]:
                    nums_to_reroll.append(num.value)
        elif possibilities["two_pair"][0] and comp_score.full_house == None:
            for num in hand:
               if num.value != possibilities["two_pair"][1][0] and num != possibilities["two_pair"][1][1]:
                    nums_to_reroll.append(num.value)
        elif possibilities["three_seq"][0] and (comp_score.small_straight == None or comp_score.large_straight == None):
            nums_not_to_roll = possibilities["three_seq"][1]
            for num in hand:
                if num.value not in nums_not_to_roll:
                    nums_to_reroll.append(num.value)
                else:
                    nums_not_to_roll.remove(num)
        elif possibilities["two_of_a"][0]:
            for num in hand:
               if num.value != possibilities["two_of_a"][1]:
                    nums_to_reroll.append(num.value)
        elif 1 in hand and comp_score.ones == None:
            for num in hand:
               if num.value != 1:
                    nums_to_reroll.append(num.value)
        elif 2 in hand and comp_score.twos == None:
            for num in hand:
               if num.value != 2:
                    nums_to_reroll.append(num.value)
        elif 3 in hand and comp_score.threes == None:
            for num in hand:
               if num.value != 3:
                    nums_to_reroll.append(num.value)
        elif 4 in hand and comp_score.fours == None:
            for num in hand:
               if num.value != 4:
                    nums_to_reroll.append(num.value)
        elif 5 in hand and comp_score.fives == None:
            for num in hand:
               if num.value != 5:
                    nums_to_reroll.append(num.value)
        elif 6 in hand and comp_score.sixes == None:
            for num in hand:
               if num.value != 6:
                    nums_to_reroll.append(num.value)
        else:
            nums_to_reroll = hand.copy()

        return nums_to_reroll

    def comp_choose_score(self, possibilities, new_hand):
        comp_score = self.comp_score
        chosen_score = None
        current_upper_scores = [
            (False, ""), # need placeholder for 0 index, cannot roll 0
            (comp_score.ones == None, "ones"),
            (comp_score.twos == None, "twos"),
            (comp_score.threes == None, "threes"),
            (comp_score.fours == None, "fours"),
            (comp_score.fives == None, "fives"),
            (comp_score.sixes == None, "sixes")
        ]
        ones = len(list(filter(lambda x: x == 1, new_hand)))
        twos = len(list(filter(lambda x: x == 2, new_hand)))
        threes = len(list(filter(lambda x: x == 3, new_hand)))
        fours = len(list(filter(lambda x: x == 4, new_hand)))
        fives = len(list(filter(lambda x: x == 5, new_hand)))
        sixes = len(list(filter(lambda x: x == 6, new_hand)))

        # if possibilities["yat"] and comp_score.yatzy != None:
        #     computer_score.yatzy_bonus += 100

        if possibilities["yat"] and comp_score.yatzy == None:
            chosen_score = "yatzy"
        elif possibilities["large_str"] and comp_score.large_straight == None:
            chosen_score = "large straight"
        elif possibilities["small_str"] and comp_score.small_straight == None:
            chosen_score = "small straight"
        elif comp_score.sixes == None and len(list(filter(lambda x: x == 6, new_hand))) >= 3:
            chosen_score = "sixes"
        elif possibilities["four_of_a"][0] and comp_score.four_of_a_kind == None:
            num = possibilities["four_of_a"][1]
            if current_upper_scores[num][0] and num != 0:
                chosen_score = current_upper_scores[num][1]
            else:
                chosen_score = "four of a kind"
        elif possibilities["full_ho"] and comp_score.full_house == None:
            chosen_score = "full house"
        elif possibilities["three_of_a"][0] and comp_score.three_of_a_kind == None:
            num = possibilities["three_of_a"][1][1]
            if current_upper_scores[num][0] and num != 0:
                chosen_score = current_upper_scores[num][1]
            else:
                chosen_score = "three of a kind"
        elif comp_score.fives == None and fives >= 3:
            chosen_score = "fives"
        elif comp_score.fours == None and fours >= 3:
            chosen_score = "fours"
        elif comp_score.threes == None and threes >= 3:
            chosen_score = "threes"
        elif comp_score.twos == None and twos >= 3:
            chosen_score = "twos"
        elif comp_score.ones == None and ones >= 3:
            chosen_score = "ones"
        elif comp_score.sixes == None and sixes == 2:
            chosen_score = "sixes"
        elif comp_score.fives == None and fives == 2:
            chosen_score = "fives"
        elif comp_score.fours == None and fours == 2:
            chosen_score = "fours"
        elif comp_score.threes == None and threes == 2:
            chosen_score = "threes"
        elif comp_score.twos == None and twos == 2:
            chosen_score = "twos"
        elif comp_score.ones == None and ones == 2:
            chosen_score = "ones"
        elif comp_score.ones == None and ones == 1:
            chosen_score = "ones"
        elif comp_score.twos == None and twos == 1:
            chosen_score = "twos"
        elif comp_score.threes == None and threes == 1:
            chosen_score = "threes"
        elif comp_score.fours == None and fours == 1:
            chosen_score = "fours"
        elif comp_score.fives == None and fives == 1:
            chosen_score = "fives"
        elif comp_score.sixes == None and sixes == 1:
            chosen_score = "sixes"
        elif comp_score.chance == None:
            chosen_score = "chance"
        elif comp_score.ones == None:
            chosen_score = "ones"
        elif comp_score.twos == None:
            chosen_score = "twos"
        elif comp_score.threes == None:
            chosen_score = "threes"
        elif comp_score.fours == None:
            chosen_score = "fours"
        elif comp_score.fives == None:
            chosen_score = "fives"
        elif comp_score.three_of_a_kind == None:
            chosen_score = "three_of_a_kind"
        elif comp_score.four_of_a_kind == None:
            chosen_score = "four of a kind"
        elif comp_score.sixes == None:
            chosen_score = "sixes"
        elif comp_score.full_house == None:
            chosen_score = "full house"
        elif comp_score.small_straight == None:
            chosen_score = "small straight"
        elif comp_score.large_straight == None:
            chosen_score = "large straight"
        elif comp_score.yatzy == None:
            chosen_score = "yatzy"

        return chosen_score

    def computer_turn(self):
        comp_score = self.comp_score
        old_comp_score = comp_score
        hand = YatzyHand()
        print("\n* Computer's score is {}".format(self.comp_score.grand_total))
        print("* Computer rolls {} {} {} {} {}".format(hand[0], hand[1], hand[2], hand[3], hand[4]))

        def set_possibilities(hand):
            return {
                "yat": comp_score.determine_yatzy(hand),
                "large_str": comp_score.determine_large_straight(hand),
                "full_ho": comp_score.determine_full_house(hand), #😆
                "three_seq": comp_score.determine_3_in_sequence(hand),
                "small_str": comp_score.determine_small_straight(hand),
                "four_of_a": comp_score.determine_4_of_a_kind(hand),
                "three_of_a": comp_score.determine_3_of_kind(hand),
                "two_pair": comp_score.determine_two_pair(hand),
                "two_of_a": comp_score.determine_two_of_a_kind(hand)
            }

        possibilities = set_possibilities(hand)

        def comp_invalid_choice(hand):
            print("ERROR in computer player logic when setting the score\nDEBUG ME")

        # if large straight, yatzy, or full house and any of those categories
        # are blank, then don't roll again and choose one of those scores.
        if possibilities["yat"] and comp_score.yatzy == None:
            comp_score.set_score(hand, 'yatzy', comp_invalid_choice)
            print("* YATZY!\n")
        elif possibilities["large_str"] and comp_score.large_straight == None:
            comp_score.set_score(hand, 'large straight', comp_invalid_choice)
            print("* Computer chooses large straight")
        elif possibilities["full_ho"] and comp_score.full_house == None:
            comp_score.set_score(hand, 'full house', comp_invalid_choice)
            print("* Computer chooses full house")
        elif possibilities["small_str"] and comp_score.small_straight == None and comp_score.large_straight != None:
            comp_score.set_score(hand, 'small straight', comp_invalid_choice)
            print("* Computer chooses small straight")
        else:
            old_hand = hand
            nums_to_reroll = self.comp_determine_reroll(possibilities, hand)
            nums = ", ".join([str(num) for num in nums_to_reroll])
            print(f"* Computer re-rolls {nums}.")
            # Re-roll the chosen die/dice
            for num in nums_to_reroll:
                if num in old_hand:
                    old_hand.remove(num)
            new_dice_needed = 5 - len(old_hand)
            new_hand = old_hand

            for _ in range(new_dice_needed):
                new_hand.append(D6())

            new_hand.sort()
            print(f"* Computer's new hand is {new_hand[0]} {new_hand[1]} {new_hand[2]} {new_hand[3]} {new_hand[4]}")
            chosen_score = self.comp_choose_score(set_possibilities(new_hand), new_hand)

            if chosen_score != None:
                comp_score.set_score(new_hand, chosen_score, comp_invalid_choice)
                print(f'* Computer chooses {chosen_score}')
            else:
                throw("ERROR chosen_score is unset!!!")

        # print computer score and end turn
        if old_comp_score.yatzy_bonus != comp_score.yatzy_bonus:
            print(f"* Computer scores yatzy bonus +100")
        elif old_comp_score.bonus != comp_score.bonus:
            print(f"* Computer scores upper section bonus +35")
        print(f"* Computer's new score is {self.comp_score.grand_total}")
        self.turn += 1

    def play(self):
        comp_turn = (self.turn % 2) == 0
        if self.score.lower_total != None and self.score.upper_total != None and self.comp_score.lower_total != None and self.comp_score.upper_total != None:
            self.end_game()
        elif not comp_turn and not self.help_shown_last and self.turn != 1:
            print("\nIt's your turn now {}. Type 'roll' to continue.".format(self.score.player_name))
        elif self.help_shown_last and self.score.player_name != None:
            print("Please type 'roll' to continue.")
            self.help_shown_last = False
        elif self.help_shown_last and self.score.player_name == None:
            self.help_shown_last = False

        if self.turn == 1 and self.score.player_name == None:
            print("Welcome to script yatzy!")
            name = input("What is your name?\n>>  ")
            if name == 'h' or name == 'help':
                self.show_help()
                return self.play()
            else:
                self.score.set_name(name)

            print("""
    Hi {}.

    You'll be playing against one other computer player.
    When you are done rolling fill in your scorecard by
    typing a matching category from the scorecard below.

    Type 'help' if you get lost.""".format(name))
            self.score.print_score()
            print("\nType 'roll' or 'r' to begin playing 😀")

        if comp_turn:
            self.computer_turn()
        else:
            if self.turn != 1:
                self.score.print_score()

            action = input(">>  ").lower().strip()

            if action == 'roll' or action == 'r':
                self.roll_action()
            elif action == 'quit' or action == 'q':
                self.clear_screen()
                self.playing = False
            elif action == 'help' or action == "h":
                self.show_help()
            else:
                print("I'm sorry your choice wasn't recognized.\nPlease type one of the following next time: 'roll', 'help', or 'quit'\nYour turn will now restart.")


game = PlayYatzy()
game.clear_screen()

while game.playing:
    game.play()


# TODO 'h' shortcut for help and make sure the computer's turn does not get skipped!
