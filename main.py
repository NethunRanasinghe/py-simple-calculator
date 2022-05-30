#-----------------------Calculation-Start-----------------------
def addition(values):
    sum = 0
    for i in values:
        sum += i
    print("\nAnswer :: " + str(sum) + "\n\n")
    again()

def substraction(values):
    sum  = values[0]
    new_values = values[1:]

    for i in new_values:
        sum -= i
    
    print("\nAnswer :: " + str(sum) + "\n\n")
    again()

def division(values):
    sum  = values[0]
    new_values = values[1:]

    for i in new_values:
        sum /= i

    print("\nAnswer :: " + str(sum) + "\n\n")
    again()

def multiplication(values):
    sum = 1
    for i in values:
        sum *= i
    print("\nAnswer :: " + str(sum) + "\n\n")
    again()

#-----------------------Calculation-End-----------------------

def choose():
    print("\n1 - Addition")
    print("2 - Substraction")
    print("3 - Division")
    print("4 - Multiplication")

    print()

    while True:
        op = int(input("Choose an operation to continue:- "))
        if op != "":
            break


    if op in range(1,5):
        if(op == 1):
            userInput("add",1)
        elif(op == 2):
            userInput("substract",2)
        elif(op == 3):
            userInput("divide",3)
        else:
            userInput("multiply",4)

    else:
        print("\nInvalid input !")
        print()
        choose()


def userInput(choice,num):
    print("\nEnter the numbers you want to {}.".format(choice))
    print("Enter 'x' to finish.\n")

    try:
        values = []
        i = 1
        while True:
            number = input("Number "+str(i)+" :- ")
            if number == 'x' or number == 'X':
                break

            values.append(int(number))
            i+=1
        
        if num == 1:
            addition(values)
        elif num == 2:
            substraction(values)
        elif num ==3:
            division(values)
        else:
            multiplication(values)

    except ValueError:
        print("\nOnly enter numbers !")
        userInput(choice,num)

    except Exception as e:
        print(e)
        userInput(choice,num)    
    
   


def again():
    ui = input("Want to do another calculation ? (y/n) :- ")

    if(ui == "y" or ui == "Y"):
        choose()
    elif(ui == "n" or ui == "N"):
        exit
    else:
        print("Invalid input !\n")
        again()
    

choose()
