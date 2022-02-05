info = {
    'Amal' : '1111111111' ,
    'Mohammed' : '2222222222' ,
    'Khadija'  : '3333333333' ,
    'Abdullah'  : '4444444444' ,
    'Rawan'  : '5555555555',
    'Faisal' : '6666666666' ,
    'Layla' : '7777777777'
}

def getOwner(dic , number):
    if number.isdigit() and len(number) == 10:
        for name, number in dic.items():
            if user_input == number:
                print(name)
                break
        else:
            print("Sorry the number is not found!")
    else:
        print("This is invalid number")


def getNumber(dic , name):
    for name, number in dic.items():
        if user_input == name:
            print(number)
            break
    else:
        print("Sorry the name is bot found!")

def addNewUser(dic):
    name = input("Enter the name of the new: ")
    number = input("Enter the number of the new : ")
    dic[name] = number
    return dic


i = int(input(
    'The phone book welcomes you.'
        '\nSearch by number Click 1'
        ' \nSearch by name Click  2 '
        '\nTo add a new name and number to the phone Click 3' 
		'\nexit Click 4 :'))
while i != 4:
    if i == 1:
        user_input = input('Enter the number : ')
        getOwner(info, user_input)
    elif i == 2:
        user_input = input('Enter the name : ')
        getNumber(info, user_input)
    elif i == 3:
        print(addNewUser(info))

    else:
        print(" You must choose one of '1-2-3-4' ")
        break

    i = int(input(
			'The phone book welcomes you.'
			'\nSearch by number Click 1'
			' \nSearch by name Click  2 '
			'\nTo add a new name and number to the phone Click 3'
			'\nexit Click 4 :'))
