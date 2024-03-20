from termcolor import colored as cd
helper = \
f'''
{cd("The data consists of blocks, the blocks"
"have a name and content.", "green")}
{cd('Commands', 'red')}
    {cd('add', 'blue')} {cd('<title>', 'magenta')}  {cd('[additionally, .., ..]', 'magenta')} 
Adding a block with content.
[title] - the name of the block, serves 
    as the key to open the block data.
[additionally, .., ..] - the content of 
    the block can contain any data.
    {cd('delete', 'blue')} 
Deletes a data block by block name.   
    {cd('show', 'blue')}
Shows block data by name.   
    {cd('edit', 'blue')}
Edits the block data, by its name. 
    {cd('exit', 'blue')} 
Terminates the program.
'''