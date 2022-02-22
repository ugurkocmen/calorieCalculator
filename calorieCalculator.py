leghtList = []
weightList = []
ageList = []

def main():
    global selection
    while True:
        try: 
            selection = int(input("Welcome! Select Your Option... 1-Personal Information 2-Calorie Calculator 3-Change Information\n Answer : "))
            break
        except ValueError:
            print("Only Numbers Please!")
            continue

def informations():
    global leght, weight, age
    while True:
        try:
            if selection == 1:
                leght = int(input("Your Length (Cantimeter) : "))
                leghtList.insert(0, leght)

                weight = int(input("Your Weight (Kilogram) : "))
                weightList.insert(0,weight)

                age = int(input("Your Age : "))
                ageList.insert(0,age)
                main()
                break
        except ValueError:
            print("Only Numbers Please!")
            informations()
        break
            
def calculator():
    global leght, weight, age
    while True:
        try:
            if selection == 2:
                gender = int(input("Select Your Gender 1-Male 2-Female\n Answer : "))
                if gender == 1:
                    calorie = int(66+(13.7*leghtList[0]) + (5*weightList[0]) - (6.8*ageList[0]))
                    print(f"The Daily Calories You Need : {calorie}")
                    main()
                if gender == 2:
                    calorie = int(655+(9.6*leghtList[0]) + (1.8*weightList[0]) - (4.7*ageList[0]))
                    print(f"The Daily Calories You Need : {calorie}")
                    main()
        except ValueError:
            print("Only Numbers Please!")
            calculator()
            break
        except IndexError:
            print("Fill Your Personal Information Please!")
            main()
        break

def changeInformations():
    while True:
        try:
            if selection == 3 and leght in leghtList:
                newLeghts = int(input("Your Length (Cantimeter) : "))
                leghtList.pop(0) and leghtList.insert(0,newLeghts)

                newWeights = int(input("Your Weight (Kilogram) : "))
                weightList.pop(0) and weightList.insert(0,newWeights)

                newAge = int(input("Your Age : "))
                ageList.pop(0) and ageList.insert(0,newAge)
                main()
                continue
        except ValueError:
            print("Only Numbers Please!")
            changeInformations()
        except NameError:
            print("Fill Your Personal Information Before This Action!")
            main()
        continue

main(), informations(), calculator(), changeInformations()