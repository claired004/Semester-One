#init

#function
def quiz():
    print("Welcome to Which Chick Flick Movie Are You")
    print("Answer these questions to find out Chick Flick")
    answer=input("Would you rather spend your day hiking or at a spa?")
    if answer=="hiking" or answer=="hike" or answer=="h":
        answer=input("Do you prefer summer or winter?")
        if answer=="summer" or answer=="s":
            answer=input("Do you prefer a dinner date or a night drive?")
            if answer=="dinner date":
                print("The Notebook")
            else:
                print("The Princess Diaries")
        if answer=="winter" or answer=="w":
            answer=input("Dancing or Movie Marathon?")
            if answer=="dancing" or answer=="d":
                print("10 Things I Hate About You")
            else:
                print("Clueless")
    if answer=="spa day" or answer=="spa" or answer=="s":
        answer=input("Do you prefer casual jeans or flowy dresses?")
        if answer=="casual jeans" or answer=="jeans" or answer=="j":
            answer=input("Do you prefer going to karaoke or an art gallery?")
            if answer=="karaoke":
                print("Mean Girls")
            else:
                print("13 Going on 30")
        if answer=="flowy dresses" or answer=="dress" or answer=="flowy dress":
            answer=input("Road Trip or Live Music?")
            if answer=="road trip" or answer=="r":
                print("Legally Blonde")
            else:
                print("How to Lose a Guy in 10 Days")

#Main
quiz()

