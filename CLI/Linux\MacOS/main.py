import os, json, time, help
from termcolor import colored as cd


fileData = 'data.json'

def clearDisplay():
    os.system('cls' if os.name == 'nt' else 'clear')

def showData(dataUser):
    # shows the names of the blocks, if they exist
    with open(fileData, 'r') as file:
        data = json.load(file)

    if data['datas'] == {}:
        print(cd("The data blocks do not exist.", 'red'))
        print(cd("Tip: Start by adding blocks", 'green'))
        start()
    with open(fileData, 'r') as file:
        data = json.load(file)
        
    order = 1
    listBlocks = data['datas'].keys()
    print(f'{20*"—"} Titles {20*"—"}')
    for key in listBlocks:
        print(f'{order}.', key)
        order += 1
    print(f'{48*"—"}')
    selectBlock = input('Write the name or number to view: ').strip()
    order = 0
    status = None
    try:
        for key in listBlocks:
            if int(selectBlock)-1 == order:
                status = f"{key}: {''.join(data['datas'][key])}"
                break
            order += 1
        if status:
            print(f'{48*"—"}')
            print(cd(status, 'green'))
            print(f'{48*"—"}')
        else:
            print(cd('Error!', 'red'))
        start()     
    except ValueError:
        try:
            if data['datas'][selectBlock]:
                print(f'{48*"—"}')
                print(cd(f"{selectBlock}: {''.join(data['datas'][selectBlock])}", 'green'))
                print(f'{48*"—"}')
            else:
                print(cd('Error!', 'red'))
            start()
        except KeyError:        
            start()

        
def addBlock(dataUser):
    with open(fileData, 'r') as file:
        base = json.load(file)

    if dataUser[0] in base['datas']:   
        print(cd('The block name already exists!', 'red'))
        start()
    elif len(dataUser) > 1:
        new_block = {f'{dataUser[0]}': " ".join(dataUser[1:])}
        base['datas'].update(new_block)

        with open(fileData, 'w') as file:
            json.dump(base, file)
        print(cd('The data block was successfully added.', 'green'))
        start()
    else:
        print(cd("The data for the block is empty!", 'red'))
        start()

def delBlock(dataUser):
    with open(fileData, 'r') as file:
        data = json.load(file)

    if data['datas'] == {}:
        print(cd('The data does not exist!', 'red'))
        start()
    else:
        order = 1
        listBlocks = data['datas'].keys()

        print(f'{20*"—"} Titles {20*"—"}')
        for key in listBlocks:
            print(f'{order}.', key)
            order += 1
        print(f'{48*"—"}')

        selectBlock = input('Write the name or number to view: ').strip()
        order = 0
        delBlock = None
        try:
            for key in listBlocks:
                if int(selectBlock)-1 == order:
                    delBlock = key
                    break
                order += 1
            if delBlock:
                print(f'{48*"—"}')
                print(cd(f"{delBlock}: {data['datas'][delBlock]}", 'red'))
                print(f'{48*"—"}')
                choice = input(f"Delete a block of data? ({cd('Y', 'green')}/{cd('n', 'red')}): ")
                if choice == 'Y':
                    data['datas'].pop(key)
                    with open(fileData, 'w') as file:
                        json.dump(data, file)
            else:
                print(cd('Error!', 'red'))
            start() 
        except ValueError:
            try:
                if selectBlock in data['datas']:
                    print(f'{48*"—"}')
                    print(cd(f'{selectBlock}: {data["datas"][selectBlock]}', 'red'))
                    print(f'{48*"—"}')
                    choice = input(f"Delete a block of data? ({cd('Y', 'green')}/{cd('n', 'red')}): ")
                    if choice == 'Y':
                        data['datas'].pop(selectBlock)
                        with open(fileData, 'w') as file:
                            json.dump(data, file)
                else:
                    print(cd('Error!', 'red'))
                start()
            except KeyError:        
                start()
'''
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
'''
selection = {
        'show': showData,
        'add': addBlock,
        'delete': delBlock,
        #'edit': editBlock
    }

def start():
    with open(fileData, 'r') as file:
        base = json.load(file)
    for i in range(5):
        if base['code_word'] == '':
            print(cd("Code words are needed to log into your database!", 'red'))
            code_word = input(cd("Come up with 5 code words: ", 'green')).strip()
            if len(code_word.split()) == 5:
                base['code_word'] = code_word
                with open(fileData, 'w') as file:
                    json.dump(base, file)
                break
            else:
                print(cd("The number of code words is not equal to 5!", 'red'))
        else:
            break
    if base['code_word'] == '':
        print("ERROR! Try again.")
    else:
        while True:
            userChoice = input(cd("Commands' list (l): ", 'yellow')).strip().split() 
            try:
                if userChoice[0].lower() == 'exit':
                    break
                selection[userChoice[0].lower()](userChoice[1:])
            except (KeyError, IndexError):
                print(help.helper)
            
if __name__ == '__main__':
    start()
