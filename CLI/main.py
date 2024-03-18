import os, json, time, pyperclip


fileData = 'data.json'

def clearDisplay():
    os.system('cls' if os.name == 'nt' else 'clear')

def showData():
    # shows the names of the blocks, if they exist
    with open(fileData, 'r') as file:
        data = json.load(file)

    if data['datas'] == {}:
        clearDisplay()
        ('————————— Error —————————————————————')
        print('The data does not exist!')
        ('—————————————————————————————————————')
        time.sleep(2)
        start()
    else:
        with open(fileData, 'r') as file:
            data = json.load(file)
        
        order = 1
        titleData = data['datas'].keys()
        print(f'————————————————— Titles {20*'—'}')
        for key in titleData:
            print(f'{order}.', key)
            order += 1
        print(f'{45*'—'}')
        userChoice = input('Select the name of the data (x): ').strip()
        clearDisplay()
        if userChoice.lower() == 'x':
            start()
        else:
            print(f'———————————————— {userChoice} {20*'—'}')
            try:
                now_data = ' '.join(data['datas'][userChoice])
            except KeyError:
                clearDisplay()
                print("There's no such name.")
                time.sleep(1)
                start()
            print(now_data)
            print(f'{(38+len(userChoice))*'—'}')
            question = input('Copy to clipboard? (x/y): ').lower().strip()
            if question == 'y' or question == '':
                clearDisplay()
                order = input(f'Which one or all of them? (1-{len(data['datas'])}/all): ').lower().strip()
                if order == 'all':
                    pyperclip.copy(now_data)
                else:
                    pyperclip.copy(data['datas'][userChoice][int(order)-1])
                start()
            else:
                start()

def addData():
    with open(fileData, 'r') as file:
        data = json.load(file)

    print(f'—————————— New name for the block {20*'—'}')
    titleOfData = input('Name for the data block (x): ').strip()
    print(f'{54*'—'}')

    if titleOfData in data['datas'] or not(titleOfData):
        clearDisplay()
        ('————————— Error —————————————————————')
        print("ERROR! The name already exists")
        time.sleep(1)
        ('—————————————————————————————————————')
        start()
    elif titleOfData.lower() == 'x':
        start()
    else:
        print(f'{54*'—'}')
        parameters = input('Login, password, etc., separated by a space (x): ')
        print(f'{54*'—'}')
        if not(parameters):
            clearDisplay()
            ('————————— Error —————————————————————')
            print('ERROR! The field is empty')
            ('—————————————————————————————————————')
            time.sleep(1)
            start()
        elif parameters.lower() == 'x':
            start()
        new_data = {f'{titleOfData}': parameters.split()}
        data['datas'].update(new_data)

        with open(fileData, 'w') as file:
            json.dump(data, file)
        
        start()


def delData():
    with open(fileData, 'r') as file:
        data = json.load(file)

    if data['datas'] == {}:
        ('————————— Error —————————————————————')
        print('The data does not exist!')
        ('—————————————————————————————————————')
        time.sleep(1)
        start()
    else:

        order = 1
        titleData = data['datas'].keys()

        print(f'———————————————— Titles {20*'—'}')
        for key in titleData:
            print(f'{order}.', key)
            order += 1
        print(f'{45*'—'}')

        userChoice = input('Delete all passwords or a specific one? (All/One/x): ').lower()

        if userChoice == 'all':
            print(f'———————————————— Code word {20*'—'}')
            codeWord = input('Enter the code word: ')
            print(f'{47*'—'}')
            if data['code_word'] == codeWord:
                data['datas'] = {}
                with open(fileData, 'w') as file:
                    json.dump(data, file)
                start()
            else:
                clearDisplay()
                ('————————— Error —————————————————————')
                print('The code word is incorrect!')
                ('—————————————————————————————————————')
                time.sleep(1)
                start()
        elif userChoice == 'x':
            start()

        clearDisplay()
        order = 1
        titleData = data['datas'].keys()
        print(f'———————————————— Titles {20*'—'}')
        for key in titleData:
            print(f'{order}.', key)
            order += 1
        print(f'{44*'—'}')

        nameOfTitle = input('Select the name of the data to delete (x): ')

        if nameOfTitle in data['datas']:
            print(f'————————————————— {nameOfTitle.strip()}{20*'—'}')
            print(' '.join(data['datas'][nameOfTitle]))
            print(f'{(38+len(nameOfTitle.strip()))*'—'}')
            if input('Delete? (Y): ') == 'Y':
                data['datas'].pop(nameOfTitle)
                with open(fileData, 'w') as file:
                    json.dump(data, file)
                start()
            else:
                clearDisplay()
                ('————————— Error —————————————————————')
                print('Deletion error.')
                ('—————————————————————————————————————')
                time.sleep(1)
                start()
        elif nameOfTitle == 'x':
            start()
        else:
            clearDisplay()
            ('————————— Error —————————————————————')
            print('There is no such name')
            ('—————————————————————————————————————')
            time.sleep(1)
            start()

def editData():
    with open(fileData, 'r') as file:
        data = json.load(file)
    
    if data['datas'] == {}:
        clearDisplay()
        ('————————— Error —————————————————————')
        print('The data does not exist!')
        ('—————————————————————————————————————')
        time.sleep(1)
        start()
    else:
        order = 1
        titleData = data['datas'].keys()
        print(f'———————————————— Titles {20*'—'}')
        for key in titleData:
            print(f'{order}.', key)
            order += 1
        print(f'{44*'—'}')
        userTitle = input('Select a title to edit: ')
        if userTitle.strip() not in data['datas']:
            clearDisplay()
            ('————————— Error —————————————————————')
            print("There's no such name!")
            ('—————————————————————————————————————')
            time.sleep(1)
            start()
        else:
            clearDisplay()
            print(f'————————— Old version {20*'—'}')
            print(' '.join(data['datas'][userTitle]))
            print(f'{42*'—'}')
            print(f'\n———————— New version {20*'—'}')
            userChoice = input('Write in the changes: ')
            if userChoice.lower().strip() == 'x':
                start()
            print(f'{42*'—'}')
            data['datas'][userTitle] = userChoice.split()
            with open(fileData, 'w') as file:
                    json.dump(data, file)
            start()

selection = {
        '1': showData,
        '2': addData,
        '3': delData,
        '4': editData
    }

def start():
    clearDisplay()

    while True:
        userChoice = input('Show (1) / Add (2) / Remove (3) / Edit (4) / Exit (5): ') 
        if userChoice.lower().strip() == '5':
            break
        try:
            clearDisplay() # clear
            selection[userChoice]()
        except KeyError:
            print('No action detected!')
            time.sleep(2)
            clearDisplay()
            continue

start()
