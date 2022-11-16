import random

class Dice:
    def __init__(self,veces,caras,modificadores):
        self.veces=veces
        self.caras=caras
        self.mods=modificadores

    def rollDices(self): #Tirada multiple
        x=(self.veces)+1
        dices=[]
        for dice in range(1,x):
            dice=(random.randint(1,self.caras))
            dices.append(dice)
        return f"El resultado es: {dices} + {self.mods}."

    def rollDice(self):  #Tirada simple
        dice=(random.randint(1,self.caras))
        return f"El resultado es: {dice} + {self.mods} "

    def rollSum(self):  #Tirara sumatoria
        x=(self.veces)+1
        dices=[]
        for dice in range(1,x):
            dice=(random.randint(1,self.caras))
            dices.append(dice)
        print(dices)
        return f"El resultado es: {sum(dices)} + {self.mods} "

class tenDice():        #Pull de d10 para VtM
    def __init__(self,success,veces):
        self.success=success
        self.veces=veces

    def roll10dice(self): 
        pifias=[] 
        success_rolls=[]
        failed_rolls=[]
        for dice in range(1,self.veces):
            dice=random.randint(1,10)
            if dice==1:
                pifias.append(dice)
            elif dice<self.success:
                failed_rolls.append(dice)
            elif dice>=self.success:
                success_rolls.append(dice)
            else:
                pass
        return f"Éxitos: {success_rolls}\nFallos: {failed_rolls}\nPifias: {pifias}" 


dado1=Dice(10,6,0)
print(dado1.rollDices())

dado2=Dice(1,100,0)
print(dado2.rollDice())

dado3=Dice(5,6,0)
print(dado3.rollSum())

dado4=tenDice(7,10)
print(dado4.roll10dice())