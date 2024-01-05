import os

managerFile = 'manager.txt'

def showData():
    global managerFile
    try:
        managerFile = open(managerFile)
        managerFile2 = [i for i in managerFile]
        managerFile.close()
        allData = ''
        for data in managerFile2:
            allData += f'{data}\n'
        print(allData)
    except FileNotFoundError:
        print('Nothing show')  


def newData():
    global managerFile
    counter = 0
    title = input('Title for login and password: ')
    login = input('\nLogin: ')
    password = input('\nPassword: ')
    try:
        file_total = open(managerFile, 'r')
        file_total2 = [i for i in file_total]
        file_total.close()
        if file_total2:
            for i in range(0, len(file_total2), 3):
                counter += 1
    except FileNotFoundError:
        counter = 0
    with open(managerFile, '+a') as file:
        file.write(f'{counter+1}. {title}\n{login}\n{password}\n')
    print("Data add!")

# # error, nocorrect remove of password
def deleteData():
    global managerFile
    counter = 0
    try:
        file_total = open(managerFile)
        file_total2 = [i for i in file_total]
        file_total.close()
        if file_total2:
            for i in range(0, len(file_total2), 3):
                counter += 1
    except FileNotFoundError:
        print("Nothing removes")
        return
    user = input(f"Select data for remove (1-{counter}): ")
    file_total2.pop(counter-1)
    digital = 0
    total = 0
    newFile = ''
    for data in file_total2:
        if total <= counter-1:
            try:
                for num in data:
                        if int(num):
                            digital += 1
            except ValueError:
                pass
            data = data.replace(data[:digital], str(int(data[0:digital])-1))
            newFile += f'{data}'
            digital = 0
            continue
        newFile += f'{data}'
    with open(managerFile, 'w') as file:
        file.write(newFile)

def main():
    while True:
        user = input("Select action: (show - 1, new password - 2, delete password - 3, exit - 4)\n")
        if user == '1':
            showData()
        elif user == '2':
            newData()
        elif user == '3':
            deleteData()
        elif user == '4':
            print("Good bye!")
            break
        else:
            print("Error, action not correct")

if __name__ in '__main__':
    main()