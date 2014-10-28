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
    easygui.msgbox(msg = TermsOfSevace, title = TitleText +  " Terms of sevace", ok_button = "I Agree")            
    easygui.msgbox(msg = "I have chosen a code for you to break", title = TitleText +  " Intoduction", ok_button = "Next")
    easygui.msgbox(msg = "There is no way you can guess it", title = TitleText +  " Intoduction", ok_button = "Next")
    easygui.msgbox(msg = "But I will give you a try", title = TitleText +  " Intoduction", ok_button = "Next")
    Name = easygui.enterbox(msg = "Enter Your nic-name (what you want to be called by in the game)", title = TitleText)
    Email = easygui.enterbox(msg = "Enter your email address", title = Name + " " + TitleText + " Email Address.")

def UserPlay(TitleText):
    #Propts the user enter their guess
    ColorChosen = []
    easygui.msgbox(msg = "Enter Your Guesses in the boxes that follow ", title = TitleText +  " Guessing", ok_button = "Next")
    ColorChosen[0] = easygui.buttonbox(msg = "Pick the color for your 1st hole", title = TitleText + " Guessing", choices = ("Blue", "Green", "White", "Red", "Yellow", "Orange"))
    ColorChosen[1] = easygui.buttonbox(msg = "Pick the color for your 2nd hole", title = TitleText + " Guessing", choices = ("Blue", "Green", "White", "Red", "Yellow", "Orange"))
    ColorChosen[3] = easygui.buttonbox(msg = "Pick the color for your 3nd hole", title = TitleText + " Guessing", choices = ("Blue", "Green", "White", "Red", "Yellow", "Orange"))
    ColorChosen[4] = easygui.buttonbox(msg = "Pick the color for your 4nd hole", title = TitleText + " Guessing", choices = ("Blue", "Green", "White", "Red", "Yellow", "Orange"))
    return ColorChosen
def HowManyPegs(ColorsOfUsersGuess, MasterCode):
    Counter = 0 # counts number of ColorsOfUsersGuess's to match the Master Code
    #Figures out how many pegs
    Red = 0 #How many reds
    White = 0 #how many Whites
    while counter > 5:
        if ColorsOfUsersGuess[0] == MasterCode[counter]:
            pass
def MakeUserStatFile(PlayerEmail, PlayerName, WhoWon):
    things = open(PlayerName + " Mastermind Stat doc.txt", "a")
    things.write("During Game 1 " + WhoWon + " Won")
    things.close()

Code = [Choose_1_random_color(), Choose_1_random_color(),Choose_1_random_color(),Choose_1_random_color()]
InteractionAtBeganing(TitleText)
Colors = UserPlay()
HowManyRedPegs(Colors, Code)
