import os, json, time, pyperclip, help


fileData = 'data.json'

def clearDisplay():
    os.system('cls' if os.name == 'nt' else 'clear')

def showData(dataUser):
    # shows the names of the blocks, if they exist
    with open(fileData, 'r') as file:
        data = json.load(file)

    if data['datas'] == {}:
        print("The data blocks do not exist.\nTip: Start by adding blocks")
        start()
    with open(fileData, 'r') as file:
        data = json.load(file)
        
    order = 1
    listBlocks = data['datas'].keys()
    print(f'————————————————— Titles {20*'—'}')
    for key in listBlocks:
        print(f'{order}.', key)
        order += 1
    print(f'{45*'—'}')
    selectBlock = input('Write the name or number to view: ').strip()
    order = 0
    try:
        for key in listBlocks:
            if int(selectBlock)-1 == order:
                print(f'—————————————————{20*'—'}')
                print(f'{key}:', ''.join(data['datas'][key]))
                print(f'—————————————————{20*'—'}')
                start()
            order += 1
    except ValueError:
        try:
            if data['datas'][selectBlock]:
                print(f'—————————————————{20*'—'}')
                print(f'{selectBlock}:',''.join(data['datas'][selectBlock]))
                print(f'—————————————————{20*'—'}')
        except KeyError:        
            start()

        
def addData(dataUser):
    with open(fileData, 'r') as file:
        base = json.load(file)

    if dataUser[0] in base['datas']:   
        print('The block name already exists!')
        start()
    elif len(dataUser) > 1:
        new_block = {f'{dataUser[0]}': " ".join(dataUser[1:])}
        base['datas'].update(new_block)

        with open(fileData, 'w') as file:
            json.dump(base, file)
        start()
    else:
        print("The data for the block is empty!")
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
        'show': showData,
        'add': addData,
        'del': delData,
        'edit': editData
    }

def start():
    while True:
        userChoice = input("Commands' list (l): ").strip().split() 
        try:
            if userChoice[0].lower() == 'exit':
                break
            selection[userChoice[0].lower()](userChoice[1:])
        except (KeyError, IndexError):
            print(help.helper)
            

start()
