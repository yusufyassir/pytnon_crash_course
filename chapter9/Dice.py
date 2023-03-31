from random import randint
class Die:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        side = randint(0, self.sides)
        print(side)

dice_6 = Die()
#dice_6.roll_die()
dice_10 = Die(10)
dice_10.roll_die()