name = input("what is your name ")
nameL =len(name)

if nameL < 3:
    print ("name must be at least 3 characters")
elif nameL > 50:
    print ("name can be a maximum of 50 characters")
else:
    print ("name looks good!")
