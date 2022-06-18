class Player: 
    def __init__(self):
        self.cards = []
        self.bust = False

    def getOption(self): 
        option = input("Would you like to pickup or stay?")
        return option

    def calcValues(self):
        temp = []
        total = 0
        for value in self.cards: 
            if type(value) == int:
                temp.append(value)
            else: 
                if value != "Ace": 
                    temp.append(10)


        for eachValue in temp: 
            total += eachValue

        
        for value in self.cards: 
            if value == "Ace": 
                if (total + 11) > 21: 
                    total += 1
                else:
                    total + 11 


        print("Your cards add up to: " + str(total))
        return total

    def addCard(self, card, option):
        self.cards.append(card)
        if option == True: 
             print("The dealer dealt you your first card. It is: " + str(card))
        else: 
            print("You picked up: " + str(card))
       
        

