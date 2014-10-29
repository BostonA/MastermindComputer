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
    ColorChosen = ["","","",""]
    easygui.msgbox(msg = "Enter Your Guesses in the boxes that follow ", title = TitleText +  " Guessing", ok_button = "Next")
    ColorChosen[0] = easygui.buttonbox(msg = "Pick the color for your 1st hole", title = TitleText + " Guessing", choices = ("Blue", "Green", "White", "Red", "Yellow", "Orange"))
    ColorChosen[1] = easygui.buttonbox(msg = "Pick the color for your 2nd hole", title = TitleText + " Guessing", choices = ("Blue", "Green", "White", "Red", "Yellow", "Orange"))
    ColorChosen[2] = easygui.buttonbox(msg = "Pick the color for your 3nd hole", title = TitleText + " Guessing", choices = ("Blue", "Green", "White", "Red", "Yellow", "Orange"))
    ColorChosen[3] = easygui.buttonbox(msg = "Pick the color for your 4nd hole", title = TitleText + " Guessing", choices = ("Blue", "Green", "White", "Red", "Yellow", "Orange"))
    return ColorChosen

def HowManyPegs(ColorsOfUsersGuess, MasterCode):
    MasterCodeCounter = 0
    ColorsOfUsersGuessCounter = 0
    #Figures out how many pegs
    Red = 0 #How many reds
    White = 0 #how many Whites
    KeepGoing = True
    while MasterCodeCounter < 4:
        KeepGoing = True
        MasterCodeCounter = MasterCodeCounter + 1
        ColorsOfUsersGuessCounter = 0 #Reset
        while ColorsOfUsersGuessCounter < 4 and KeepGoing: #Fix Number of Whites
            ColorsOfUsersGuessCounter = ColorsOfUsersGuessCounter + 1
            if ColorsOfUsersGuess[ColorsOfUsersGuessCounter - 1] == MasterCode[MasterCodeCounter - 1]:
                if MasterCodeCounter == ColorsOfUsersGuessCounter:

                    Red = Red + 1
                    KeepGoing = False
                else:
                    White = White + 1
    print Red
    print White
    if Red == 4:
        return ["Won", "Won"]
    else:
        return [Red, White]
    
def TellUserScore (RedNo, WhiteNo, Title):
    return easygui.buttonbox(msg = "You Got " + str(RedNo) + " Red Pegs \n You Got " + str(WhiteNo) + " White Pegs", title = Title + "Peg Number.", choices = ("Next", "Quit", "Forfit", "New Game", "Send Feedback (or a bug)"))
def MakeUserStatFile(PlayerEmail, PlayerName, WhoWon):
    things = open(PlayerName + " Mastermind Stat doc.txt", "a")
    things.write("During Game 1 " + WhoWon + " Won")
    things.close()
def FiguresOutWhatTheUserWhatsToDo(WhatUserWantsToDo, TitleText):
    Go = False
    if WhatUserWantsToDo == "Next":
        Go = True
    elif WhatUserWantsToDo == "Send Feedback (or a bug)":
        Feedback(TitleText)
def Feedback(TitleText):
    Error = easygui.enterbox(msg = "What is your feedback?", title = TitleText + " FeedBack")
    things = open("FeedBack (Mastermind).txt", "a")
    things.write(Error + "\n")
    things.close()
#Code = ["Green", "Green","Green","Green"]
#print Code
#Colors = UserPlay(TitleText)
#REDWHITE = HowManyPegs(Colors, Code)
#RedPegs = REDWHITE[0]
#WhitePegs = REDWHITE[1]
#WhatUserWantsToDo = TellUserScore(RedPegs, WhitePegs, TitleText)
#FiguresOutWhatTheUserWhatsToDo(WhatUserWantsToDo)
FiguresOutWhatTheUserWhatsToDo("Send Feedback (or a bug)", TitleText)
