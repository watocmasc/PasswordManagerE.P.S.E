CONFIG_MENU = """
config:
    Window:
        styles:
            set_title: '[2]{item}'
            border: '[white]{item}'
            corner: '[white]{item}'

    Button:
        styles:
            label: '[@white black bold]{item}'
            highlight: '[@#794699 white bold]{item}'

"""

CONFIG_REGLOGWINDOW = '''
config:
    Window:
        min_width: 60
        width: 60
        styles:
            title: '[2]{item}'
            border: '[white]{item}'
            corner: '[white]{item}'   

    InputField:
        styles:
            prompt: '[white bold]{item}' 
            value: '[5]{item}'
            
    Button:
        styles:
            label: '[@white black bold]{item}'
            highlight: '[@#5eb54a white bold]{item}'

'''