from decimal import Decimal
import os
os.system("clear")
# EVENTS OF THE PROGRAM
def Dollar():
    final_currency_dollar = input ("\n New Currency ---> ")
    final_currency_dollar = float(final_currency_dollar)
        
    if final_currency_dollar == 2:
        initial = input("\n $")
        initial = float(initial)
        final = initial * 0.92
        print("\n €", final)

    elif final_currency_dollar == 3:
        initial = input("\n $")
        initial = float(initial)
        final = initial * 108.2
        print("\n JAP¥", final)
    
    elif final_currency_dollar == 4:
        initial = input("\n $")
        initial = float(initial)
        final = initial * 7.1
        print("\n CHN¥", final)
    
    elif final_currency_dollar == 5:
        initial = input("\n $")
        initial = float(initial)
        final = initial * 23.39
        print("\n MXN$", final)
    
    elif final_currency_dollar == 6:
        initial = input("\n $")
        initial = float(initial)
        final = initial * 0.8
        print("\n £", final)
    
    elif final_currency_dollar == 7:
        initial = input("\n $")
        initial = float(initial)
        final = initial * 0.00016
        print("\n ฿", final)
    
    else:
        print("You didn't choose an available currency, try again!")
        quit = input("Do you want to quit the program ? (y/n)")
        if quit == "y":
            print("End of the Program...")
        
        else:
            Dollar()

def Euro():
    final_currency_euro = input ("\n New Currency ---> ")
    final_currency_euro = float(final_currency_euro)
        
    if final_currency_euro == 1:
        initial = input("\n €")
        initial = float(initial)
        final = initial * 1.12
        print("\n $", final)

    elif final_currency_euro == 3:
        initial = input("\n €")
        initial = float(initial)
        final = initial * 120.52
        print("\n JAP¥", final)
    
    elif final_currency_euro == 4:
        initial = input("\n €")
        initial = float(initial)
        final = initial * 7.93
        print("\n CHN¥", final)
    
    elif final_currency_euro == 5:
        initial = input("\n €")
        initial = float(initial)
        final = initial * 26.12
        print("\n MXN$", final)
    
    elif final_currency_euro == 6:
        initial = input("\n €")
        initial = float(initial)
        final = initial * 0.9
        print("\n £", final)
    
    elif final_currency_euro == 7:
        initial = input("\n €")
        initial = float(initial)
        final = initial * 0.00018
        print("\n ฿", final)
    
    else:
        print("You didn't choose an available currency, try again!")
        quit = input("Do you want to quit the program ? (y/n)")
        if quit == "y":
            print("End of the Program...")
        
        else:
            Euro()

def Yen():
    final_currency_yen = input ("\n New Currency ---> ")
    final_currency_yen = float(final_currency_yen)
        
    if final_currency_yen == 1:
        initial = input("\n JAP¥")
        initial = float(initial)
        final = initial * 0.0093
        print("\n $", final)

    elif final_currency_yen == 2:
        initial = input("\n JAP¥")
        initial = float(initial)
        final = initial * 0.0083
        print("\n €", final)
    
    elif final_currency_yen == 4:
        initial = input("\n JAP¥")
        initial = float(initial)
        final = initial * 0.066
        print("\n CHN¥", final)
    
    elif final_currency_yen == 5:
        initial = input("\n JAP¥")
        initial = float(initial)
        final = initial * 0.22
        print("\n MXN$", final)
    
    elif final_currency_yen == 6:
        initial = input("\n JAP¥")
        initial = float(initial)
        final = initial * 0.0074
        print("\n £", final)
    
    elif final_currency_yen == 7:
        initial = input("\n JAP¥")
        initial = float(initial)
        final = initial * 0.0000015
        print("\n ฿", final)
    
    else:
        print("You didn't choose an available currency, try again!")
        quit = input("Do you want to quit the program ? (y/n)")
        if quit == "y":
            print("End of the Program...")
        
        else:
            Yen()

def Yuan():
    final_currency_yuan = input ("\n New Currency ---> ")
    final_currency_yuan = float(final_currency_yuan)
        
    if final_currency_yuan == 1:
        initial = input("\n CHN¥")
        initial = float(initial)
        final = initial * 0.14
        print("\n $", final)

    elif final_currency_yuan == 2:
        initial = input("\n CHN¥")
        initial = float(initial)
        final = initial * 0.13
        print("\n €", final)
    
    elif final_currency_yuan == 3:
        initial = input("\n CHN¥")
        initial = float(initial)
        final = initial * 15.21
        print("\n JAP¥", final)
    
    elif final_currency_yuan == 5:
        initial = input("\n CHN¥")
        initial = float(initial)
        final = initial * 3.3
        print("\n MXN$", final)
    
    elif final_currency_yuan == 6:
        initial = input("\n CHN¥")
        initial = float(initial)
        final = initial * 0.11
        print("\n £", final)
    
    elif final_currency_yuan == 7:
        initial = input("\n CHN¥")
        initial = float(initial)
        final = initial * 0.000023
        print("\n ฿", final)
    
    else:
        print("You didn't choose an available currency, try again!")
        quit = input("Do you want to quit the program ? (y/n)")
        if quit == "y":
            print("End of the Program...")
        
        else:
            Yuan()

def Pesos():
    final_currency_pesos = input ("\n New Currency ---> ")
    final_currency_pesos = float(final_currency_pesos)
        
    if final_currency_pesos == 1:
        initial = input("\n MXN$")
        initial = float(initial)
        final = initial * 0.043
        print("\n $", final)

    elif final_currency_pesos == 2:
        initial = input("\n MXN$")
        initial = float(initial)
        final = initial * 0.038
        print("\n €", final)
    
    elif final_currency_pesos == 3:
        initial = input("\n MXN$")
        initial = float(initial)
        final = initial * 4.61
        print("\n JAP¥", final)
    
    elif final_currency_pesos == 4:
        initial = input("\n MXN$")
        initial = float(initial)
        final = initial * 0.3
        print("\n CHN¥", final)
    
    elif final_currency_pesos == 6:
        initial = input("\n MXN$")
        initial = float(initial)
        final = initial * 0.034
        print("\n £", final)
    
    elif final_currency_pesos == 7:
        initial = input("\n MXN$")
        initial = float(initial)
        final = initial * 0.0000069
        print("\n ฿", final)
    
    else:
        print("You didn't choose an available currency, try again!")
        quit = input("Do you want to quit the program ? (y/n)")
        if quit == "y":
            print("End of the Program...")
        
        else:
            Pesos()

def Pound():
    final_currency_pound = input ("\n New Currency ---> ")
    final_currency_pound = float(final_currency_pound)
        
    if final_currency_pound == 1:
        initial = input("\n £")
        initial = float(initial)
        final = initial * 1.25
        print("\n $", final)

    elif final_currency_pound == 2:
        initial = input("\n £")
        initial = float(initial)
        final = initial * 1.12
        print("\n €", final)
    
    elif final_currency_pound == 3:
        initial = input("\n £")
        initial = float(initial)
        final = initial * 134.21
        print("\n JAP¥", final)
    
    elif final_currency_pound == 4:
        initial = input("\n £")
        initial = float(initial)
        final = initial * 8.84
        print("\n CHN¥", final)
    
    elif final_currency_pound == 5:
        initial = input("\n £")
        initial = float(initial)
        final = initial * 29.13
        print("\n MXN$", final)
    
    elif final_currency_pound == 7:
        initial = input("\n £")
        initial = float(initial)
        final = initial * 0.00020
        print("\n ฿", final)
    
    else:
        print("You didn't choose an available currency, try again!")
        quit = input("Do you want to quit the program ? (y/n)")
        if quit == "y":
            print("End of the Program...")
        
        else:
            Pound()

def Bitcoin():
    final_currency_bitcoin = input ("\n New Currency ---> ")
    final_currency_bitcoin = float(final_currency_bitcoin)
        
    if final_currency_bitcoin == 1:
        initial = input("\n ฿")
        initial = float(initial)
        final = initial * 6205.59
        print("\n $", final)

    elif final_currency_bitcoin == 2:
        initial = input("\n ฿")
        initial = float(initial)
        final = initial * 5556.33
        print("\n €", final)
    
    elif final_currency_bitcoin == 3:
        initial = input("\n ฿")
        initial = float(initial)
        final = initial * 669676.24
        print("\n JAP¥", final)
    
    elif final_currency_bitcoin == 4:
        initial = input("\n ฿")
        initial = float(initial)
        final = initial * 44037.35
        print("\n CHN¥", final)
    
    elif final_currency_bitcoin == 5:
        initial = input("\n ฿")
        initial = float(initial)
        final = initial * 143622.14
        print("\n MXN$", final)
    
    elif final_currency_bitcoin == 6:
        initial = input("\n ฿")
        initial = float(initial)
        final = initial * 4929.8
        print("\n £", final)
    
    else:
        print("You didn't choose an available currency, try again!")
        quit = input("Do you want to quit the program ? (y/n)")
        if quit == "y":
            print("End of the Program...")
        
        else:
            Bitcoin()

# PROGRAM ORGANIZATION

initial_currency = input ("\n Initial Currency (type a number): \n 1- dollar ($) \n 2- euro (€) \n 3- japanese yen (JAP¥) \n 4- chinese yuan (CHN¥) \n 5- pesos (MXN$) \n 6- pounds (£) \n 7- bitcoins (฿) \n ---> ")
initial_currency = float(initial_currency)


if initial_currency == 1:
    Dollar()

elif initial_currency == 2:
    Euro()

elif initial_currency == 3:
    Yen()

elif initial_currency == 4:
    Yuan()

elif initial_currency == 5:
    Pesos()

elif initial_currency == 6:
    Pound()

elif initial_currency == 7:
    Bitcoin()

else:
    print("\n You didn't choose an available currency, try again!")
    os.system("python3 ConvertingMoney.py")
