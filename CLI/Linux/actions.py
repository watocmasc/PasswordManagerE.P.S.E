import json
from main import *
from termcolor import colored as cd
import pytermgui as ptg

fileData = 'Linux/data.json'

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

