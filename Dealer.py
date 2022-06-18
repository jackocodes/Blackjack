class Dealer: 
    def __init__(self):
        self.cards = []

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

        
        print("The dealers cards add up to: " + str(total))
        return total

    def addCard(self, card, option):
        self.cards.append(card)
        if option == True: 
            print("The dealers first card is: " + str(card))
        else: 
            print("The dealers card was a: " + str(card))
       
        

