from random import randint

def ran_char():
    symbol = ["!", "?", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-" "+", "=", "<", ">", "/"]
    number = [1, 2, 3, 4, 5, 6]
    letter = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]

    ran_num = number[randint(0, len(number)-1)]
    ran_sym = symbol[randint(0, len(symbol)-1)]
    ran_let = letter[randint(0, len(letter)-1)]

    ran_c = [ran_num, ran_sym, ran_let]
    ran_list = ran_c[randint(0, len(ran_c)-1)]
    return ran_list

answer = input('Do you want to make a password?')
if answer == 'yes' or 'Yes':
    length = int(input('How long do you want your password to be?'))
    password = []
    for x in range(length):
        password.append(ran_char())        
    print(password)
elif answer == 'No' or 'no':
    print('Have a nice day')

for x in password:
    print(x, end="")

    







    
