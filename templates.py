DICE_ONE = """-----------
|         |
|    0    |
|         |
-----------"""
DICE_TWO = """-----------
|  0      |
|         |
|      0  |
-----------"""
DICE_THREE = """-----------
|  0      |
|    0    |
|      0  |
-----------"""
DICE_FOUR = """-----------
|  0   0  |
|         |
|  0   0  |
-----------"""
DICE_FIVE = """-----------
|  0   0  |
|    0    |
|  0   0  |
-----------"""
DICE_SIX = """-----------
|  0   0  |
|  0   0  |
|  0   0  |
-----------"""

DICE_DICT = {
             1 : DICE_ONE,
             2 : DICE_TWO,
             3 : DICE_THREE,
             4 : DICE_FOUR,
             5 : DICE_FIVE,
             6 : DICE_SIX
            }

UPPER_COMBO_COMMANDS = {
                        'ones',
                        'twos',
                        'threes',
                        'fours',
                        'fives',
                        'sixes'
                       }

LOWER_COMBO_COMMANDS = {
                        'threeofakind',
                        'fourofakind',
                        'fullhouse',
                        'shortstraight',
                        'longstraight',
                        'yahtzee',
                        'chance'
                       }

COMBO_COMMANDS = UPPER_COMBO_COMMANDS.union(LOWER_COMBO_COMMANDS)

OTHER_COMMANDS = {
            'save',
            'exit',
            'roll',
            'keep',
            'block',
            'finish',
            'print'
           }

COMMANDS = OTHER_COMMANDS.union(COMBO_COMMANDS)

COMBO_OUTLINES = {
             'ones'             : '111**',
             'twos'             : '222**',
             'threes'           : '333**',
             'fours'            : '444**',
             'fives'            : '555**',
             'sixes'            : '666**',
             'threeofakind'     : 'aaa**',
             'fourofakind'      : 'aaaa*',
             'fullhouse'        : 'aaabb',
             'shortstraight'    : 'abcd*',
             'longstraight'     : 'abcde',
             'yahtzee'          : 'aaaaa',
             'chance'           : '*****'
            }

COMBO_INDICES = {
             'ones'             : 0,
             'twos'             : 1,
             'threes'           : 2,
             'fours'            : 3,
             'fives'            : 4,
             'sixes'            : 5,
             'threeofakind'     : 6,
             'fourofakind'      : 7,
             'fullhouse'        : 8,
             'shortstraight'    : 9,
             'longstraight'     : 10,
             'yahtzee'          : 11,
             'chance'           : 12
            }

SCOREBOARD = """-----------------|--------------|------------|------------|------------|------------|
Combo            | Score Type   | {:<10} | {:<10} | {:<10} | {:<10} |
-----------------|--------------|------------|------------|------------|------------|
#################|##############|############|############|############|############|
-----------------|--------------|------------|------------|------------|------------|
Upper Section - Sum dice of the specified type.
-----------------|--------------|------------|------------|------------|------------|
Ones             | Sum Ones     | {:>10} | {:>10} | {:>10} | {:>10} |
Twos             | Sum Twos     | {:>10} | {:>10} | {:>10} | {:>10} |
Threes           | Sum Threes   | {:>10} | {:>10} | {:>10} | {:>10} |
Fours            | Sum Fours    | {:>10} | {:>10} | {:>10} | {:>10} |
Fives            | Sum Fives    | {:>10} | {:>10} | {:>10} | {:>10} |
Sixes            | Sum Sixes    | {:>10} | {:>10} | {:>10} | {:>10} |
-----------------|--------------|------------|------------|------------|------------|
Subtotal         | Sum combos   | {:>10} | {:>10} | {:>10} | {:>10} |
-----------------|--------------|------------|------------|------------|------------|
Bonus - Add 35 points if Subtotal is 63 or more
-----------------|--------------|------------|------------|------------|------------|
Bonus            | 35 points    | {:>10} | {:>10} | {:>10} | {:>10} |
-----------------|--------------|------------|------------|------------|------------|
#################|##############|############|############|############|############|
-----------------|--------------|------------|------------|------------|------------|
Lower Section - Scoring varies between Combos
-----------------|--------------|------------|------------|------------|------------|
3 of a kind      | Sum all dice | {:>10} | {:>10} | {:>10} | {:>10} |
4 of a kind      | Sum all dice | {:>10} | {:>10} | {:>10} | {:>10} |
Full House       | 25 points    | {:>10} | {:>10} | {:>10} | {:>10} |
Short Straight   | 30 points    | {:>10} | {:>10} | {:>10} | {:>10} |
Long Straight    | 40 points    | {:>10} | {:>10} | {:>10} | {:>10} |
Yahtzee          | 50 points ea | {:>10} | {:>10} | {:>10} | {:>10} |
Chance           | Sum all dice | {:>10} | {:>10} | {:>10} | {:>10} |
-----------------|--------------|------------|------------|------------|------------|
Subtotal         | Sum combos   | {:>10} | {:>10} | {:>10} | {:>10} |
-----------------|--------------|------------|------------|------------|------------|
#################|##############|############|############|############|############|
-----------------|--------------|------------|------------|------------|------------|
Total            | Overall Sum  | {:>10} | {:>10} | {:>10} | {:>10} |
-----------------|--------------|------------|------------|------------|------------|
"""