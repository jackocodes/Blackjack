from Cards import getRandomCard
import time
import os 
clear = lambda: os.system('cls')

class Game: 
    def __init__(self, player, dealer):
        self.player = player 
        self.dealer = dealer
        self.gameEnded = False

    def handleOption(self, option): 
        if option.lower() == "pickup": 
            self.player.addCard(getRandomCard(), False)
            playerTotal = self.player.calcValues()
            if playerTotal > 21: 
                print("You bust.")
                self.gameEnded = True
                

        if option.lower() == "stay":
            self.dealer.addCard(getRandomCard(), False)
            dealerTotal = self.dealer.calcValues()
            time.sleep(3)
            playerTotal = self.player.calcValues()

            if dealerTotal > 21: 
                print("You win!")
                self.gameEnded = True
            elif dealerTotal > playerTotal: 
                print("You lost.")
                self.gameEnded = True
            elif dealerTotal < playerTotal:
                print("You win.")
                self.gameEnded = True

    def startGame(self): 
        clear()
        self.dealer.addCard(getRandomCard(), True)
        time.sleep(3)
        self.player.addCard(getRandomCard(), True)
        time.sleep(1)

        while self.player.bust != True: 
            if self.gameEnded == True: 
                return 
            else: 
                playerOption = self.player.getOption()
                self.handleOption(playerOption)



        

