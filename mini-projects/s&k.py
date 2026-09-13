import random
print('Snake And Ladder')


def rolldice():
   roll = random.randint(1,6)
   return roll

class Player:



    def __init__(self):
        self.currentPos = 0
        self.snake ={30:7,47:13,56:19,73:51,82:42,92:75,98:55}
        self.ladder={4:25,21:39,26:67,43:76,59:80,71:89}
        


    def move(self,dice):
        if self.currentPos == 0:
            if dice == 1:
                self.currentPos = self.currentPos + dice
                return self.currentPos
            else:
                return self.currentPos
        

        else:
            self.currentPos = self.currentPos + dice
            return self.currentPos

    def snakeBite(self,newPos):
        newPos = self.snake[newPos]
        return newPos
    

    def ladderClimb(self,currentPos):
        if currentPos in self.ladder:
            self.currentPos = self.ladder[currentPos]
        return self.currentPos


p1 = Player()
p2 = Player()

turn = 1


while True:
    print(f'[Player 1: {p1.currentPos}]\t')
    print(f'[Player 2: {p2.currentPos}]\n')

    if turn == 1:
        print("Player 1's turn.... ")
        comm = input('click enter to roll the dice: \n')
        dice = rolldice()
        print(f'You rolled {dice}!')

        newPos = p1.move(dice)

        # to check winning status
        if p2.move(dice)< 100:
            newPos = p2.move(dice)
        elif p2.move(dice)== 100:
            print("Player 2 has WON!!!")
            break

        if newPos in p1.snake:
            newPos = p1.snakeBite(newPos)
        elif newPos in p1.ladder:
            newPos = p1.ladderClimb(newPos)
             

        print(f'Player 1 moved from {p1.currentPos} to {newPos}\n')
        turn =2
    else:
        print("Player 2's turn.... ")
        comm = input('click enter to roll the dice: \n')
        dice = rolldice()
        print(f'You rolled {dice}!\n')


        # to check winning status
        if p2.move(dice)< 100:
            newPos = p2.move(dice)
        elif p2.move(dice)== 100:
            print("Player 2 has WON!!!")
            break

        # to chck for ladder or snake
        if newPos in p2.snake:
            newPos = p2.snakeBite(newPos)
        elif newPos in p2.ladder:
            newPos = p2.ladderClimb(newPos)


        print(f'Player 2 moved from {p2.currentPos} to {newPos}\n\n')
        turn = 1
        
           





    

