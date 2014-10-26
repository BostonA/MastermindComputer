import random
def Choose_1_random_color():
    #Choses random color (For First turn)
    TheColorNum = random.randint(1, 6)
    #TheColorNum is the number before it is switched to a string and a color
    #(Blue, Green...)
    if (TheColorNum == 1):
        TheColor = "Blue"
    elif (TheColorNum == 2):
        TheColor = "Green"
    elif (TheColorNum == 3):
        TheColor = "Yellow"
    elif (TheColorNum == 4):
        TheColor = "White"
    elif (TheColorNum == 5):
        TheColor = "Orange"
    elif (TheColorNum == 6):
        TheColor = "Green"
    else:
        #Bug Check
        TheColor = "BUG HERE STOP"
    #That made the .randit into a string (color)
    #TheColor = The color is chosen
    return TheColor
    
    

#BODY BELOW
print Choose_1_random_color()
