history = []
inputcalc = 0
inputcalc2 = 0
def welcomescreen():
    print("_________________________________________________________________________________________________")
    print("__________________________________Python Calculator ;____________________________________________")
    print("___[calculate : c]___[shutdown : s]___[answers history : h]______________________________________")
    print("[available operators : + (plus), - (minus), * (x) , %, & and / (divide) ]________________________")
    print("_________________________________________________________________________________________________")

def place():
    for i in range(150):
        print("                                                                                           ")
def errormessage():
    print("Synthax error : please retry")
    input("Press Enter to continue")
    place()
    main()

def main():
    place()
    welcomescreen()
    typing = input("Type a command ")
    if typing == "s":
     print("Shutdown : type s, Cancel : type c or any key")
     askexit = input("Type a command ")
     if askexit == "c":
        place()
        main()
     elif askexit == "s":
        exit()
     else :
         place()
         main()

    if typing == "c":
     print("Please type your command with the following operators : +, -, *, **, % or /")
     inputcalc = str(input(" "))
     try:
        inputcalc2 = eval(inputcalc)
     except NameError:  # this is because when a casting to int fails, it calls xxxError
         errormessage()
     inputcalc = eval(inputcalc)
     print(inputcalc)
     history.append(inputcalc)
     inputcalc = 0
     inputcalc2 = 0
     input("Press Enter to continue")
     place()
     main()

    if typing == "h":
        print("Answers History :")
        print(history)
        input("Press Enter to continue")
        place()
        main()

    if typing != "h" or "c" or "s" :
        errormessage()
main()
