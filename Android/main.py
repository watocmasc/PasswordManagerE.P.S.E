from flet import *
import json, os

def on_add_block(e):
    pass

def on_delete_block(e):
    pass

def on_update_block(e):
    pass

def main(page):
    page.title = "EPSE"
    page.bgcolor = "#282828"

    with open(os.path.abspath('data.json'), 'r') as file:
        base = json.load(file)

    base_data = ListView(padding=20, auto_scroll=True)
    for i in base['datas'].keys():
        base_data.controls.append(TextButton(f"{i}"))

    add_block = IconButton(
        icon=icons.ADD,
        icon_size=30,
        tooltip="Add",
        on_click=on_add_block,
    )
    delete_block = IconButton(
        icon=icons.DELETE,
        icon_size=30,
        tooltip="Delete",
        on_click=on_delete_block,
    )
    update_blocks = IconButton(
        icon=icons.UPDATE,
        icon_size=30,
        tooltip="Update",
        on_click=on_update_block,
    )

    panel_btns = Row(
            controls=[
                add_block, delete_block, update_blocks
            ],
            alignment="center"
    )

    column = Column(
        controls=[
            base_data, panel_btns
        ],
        expand=True
    )

    page.window_width = 540
    page.window_height = 960
    page.add(column)

if __name__ == '__main__':
    app(main)