import random

print('Snake And Ladder')


def rolldice():
    roll = random.randint(1, 6)
    return roll


class Player:

    def __init__(self, name):
        self.name = name
        self.currentPos = 0
        self.snake = {30: 7, 47: 13, 56: 19, 73: 51, 82: 42, 92: 75, 98: 55}
        self.ladder = {4: 25, 21: 39, 26: 67, 43: 76, 59: 80, 71: 89}

    def move(self, dice):
        if self.currentPos == 0 and dice != 1:
            return self.currentPos

        newPos = self.currentPos + dice

        if newPos > 100:
            return self.currentPos

        self.currentPos = newPos
        return self.currentPos

    def snakeBite(self):
        if self.currentPos in self.snake:
            bitePos = self.currentPos
            self.currentPos = self.snake[bitePos]
            print(f'{self.name} got bitten by a 🐍 at {bitePos}, sliding down to {self.currentPos}!\n')
        return self.currentPos

    def ladderClimb(self):
        if self.currentPos in self.ladder:
            climbPos = self.currentPos
            self.currentPos = self.ladder[climbPos]
            print(f'{self.name} found a 🪜  at {climbPos}, climbing up to {self.currentPos}!\n')
        return self.currentPos

    def takeTurn(self):
        click = input('click enter to roll the dice 🎲: \n')
        dice = rolldice()
        print(f'You rolled {dice}!')
        oldPos = self.currentPos
        self.move(dice)
        movedTo = self.currentPos
        print(f'{self.name} moved from {oldPos} to {movedTo}')

        self.snakeBite()
        self.ladderClimb()


p1 = Player("Player 1")
p2 = Player("Player 2")
turn = 1

while True:
    print(f'[Player 1: {p1.currentPos}] [Player 2: {p2.currentPos}]\n')

    if turn == 1:
        print("Player 1's turn.... ")
        p1.takeTurn()
        if p1.currentPos == 100:
            print("Player 1 has WON!!!")
            break
        turn = 2
    else:
        print("Player 2's turn.... ")
        p2.takeTurn()
        if p2.currentPos == 100:
            print("Player 2 has WON!!!")
            break
        turn = 1