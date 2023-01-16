
option = input ('> ')
if option.lower() == 'help':
    print ('start = to start the car engine')
    print ('stop  = to stop the the car')
    print ('quit = end the game')
    option = input ('> ')
elif option.lower() == 'start':
        print('car started......Ready to go! ')
        option = input ('> ')
elif option.lower() == 'stop':
        print ('Car Stopped. ')
        option = input ('> ')
elif option.lower()== 'quit':
        print ('quit')
else:
        print ("i don't understand that...")
