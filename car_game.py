command = ''
stared = False  # cat is stopped


while command != 'quit':
    command = input("Your command >").lower()
    if command == 'start':

        if stared:
            print('Car is already started !')

        else:
            print('Car started')
            stared = True

    elif command == 'stop':

        if not stared:
            print('Car is already stopped !')
        else:
            print('Car stopped')

    elif command == 'help':
        print('''
start - to start to car
stop - to stop to car
quit - to quit
        
        ''')
    elif command == 'quit':
        break
    else:
        print("sorry, I don't understand that")
