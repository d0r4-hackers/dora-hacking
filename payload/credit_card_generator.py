try:
    import creditcard
    import pyfiglet
    import random
    from pyfiglet import Figlet
    from creditcard import CreditCard as cc
except:
    import os
    os.system('pip3 install creditcard & pip3 install pyfiglet')

def lg_cc():
    fonts = Figlet(font='slant')
    print(fonts.renderText('Credit Card'))
def generator(num):
    n = 0
    for gens in range(num):
        cvv = random.randint(1, 999)
        mm = str(random.randint(1, 12))
        yy = str(random.randint(24, 32))
        id = random.randint(4000000000000000, 5999999999999999)
        check = cc(id, mm, yy, cvv)
        if check.is_valid:
            brand = check.brand
            n += 1
            if num == n:
                exit('Generator Complete')
                
            print(f"""
    card num: {id}
    expires : {mm}/{yy}
    cvv : {cvv}
    brand : {brand}
    pipe : {id}|{mm}/{yy}|{cvv}
    """)
        else:
            pass