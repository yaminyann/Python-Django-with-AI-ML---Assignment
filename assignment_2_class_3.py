# Clss -3
# Assignment - 2
# Bank Management system , like CRUD application

bank_user = { 'yamin': 400,
              'rasel': 800,
              'nasim': 300,

    }
print('Welcome to The BANK')
while True:
    print('What do you like to do ? ')
    print(' '+'1. View Balence')
    print(' ' +'2. View all bank info  ')
    print(' ' +'3. Update balence ')
    print(' ' +'4. Delete user .')
    print(' ' + '5. Exit')

    disition = input()

    if disition == '1':
        print('Enter Your Name : ')
        k = input()
        if k in bank_user.keys():
            print('Your Bank Balence is : '+str(bank_user[k]))
        else:
            print('The user cannot found. Would you like to add this user to the account?')
            disition = input()
            if disition == 'yes':
                k = input('Enter your name please ___ ')
                v = input('enter your balence please ___')
                bank_user.update({k:v})

            else:
                print('Would Like to EXIT ?')
                disition = input()
                if disition == 'yes':
                    break


    elif disition == '2':
        for k,v in bank_user.items():
            print('username  '+str(k)+'  BANK Balence '+str(v))



    elif disition == '3':
        print('Enter Your name please : ')
        k = input()
        if k in bank_user.keys():
            print('do you want add or subtract from your savings ??')
            disition = input()
            if disition == 'add':
                temp_balence = bank_user[k]
                extra = input('Enter the ammount you want to add :  ')
                bank_user[k] = temp_balence+int(extra)
                print(bank_user[k])
            elif disition == 'subtract':
                temp_balence = bank_user[k]
                extra = input('Enter The ammount you want to subtract --')
                bank_user[k] = temp_balence - int(extra)
                print('balence Update . It is ___')
                print(bank_user[k])

            else:
                print('there is no such accont in the bank database .')
        else:
            print('USER Cannot FOUND . please Try Again! ')



    elif disition == '4':
        print('Whoes account you want to delete ? ')
        disition_user = input()
        if disition_user in bank_user.keys():
            print('USER Found , Still you need to Delete this user ',)
            d = input()
            if d == 'yes':
                del (bank_user[disition_user])

        else:
            print('User not found , please Try Again')





    elif disition == '5':
        break

    else:
        print("YOU PRESS WRONG KEY, PLEASE TRY AGAIN ! ")