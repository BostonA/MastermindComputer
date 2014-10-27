import random, time, easygui
TitleText = "Mastermind Scorer"
def Choose_1_random_color():
    #Choses random color (For Code)
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
def InteractionAtBeganing(TitleText):
    TermsOfSevace = "Terms of Sevace \n \n  By Using this program you agree to not report an invalid bug, and to allow Boston Abrams and others,to use the data that you perduse, your email  adress and your name. "
    
    easygui.msgbox(msg = TermsOfSevace, title = TitleText +  " Terms of sevace", ok_button = "I agree")            
    easygui.msgbox(msg = "I have chosen a code for you to break", title = TitleText +  " Intoduction", ok_button = "Next")
    easygui.msgbox(msg = "There is no way you can guess it", title = TitleText +  " Intoduction", ok_button = "Next")

    easygui.msgbox(msg = "But I will give you a try", title = TitleText +  " Intoduction", ok_button = "Next")
    easygui.enterbox(msg = "Enter Your nic-name (what you want to be called by in the game)", title = TitleText)

def UserPlay():
    easygui.buttonbox(msg = "Pick the color for the color of your leftmost hole", title = "Play Mastermind (By Boston Abrams)Copyright 2014 Boston Abrams", choices = ("Blue", "Green", "White", "Red", "Yellow", "Orange"))
    

def AskUserWhatTheyWantToPlay():
    #Red and White are the color of the small pegs
    Red = raw_input("How many red Pegs: ")
    White = raw_input("How many White Pegs: ")
    return Red, White
Code = [Choose_1_random_color(), Choose_1_random_color(),Choose_1_random_color(),Choose_1_random_color()]
InteractionAtBeganing(TitleText)
UserPlay()

