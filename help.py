from shutil import get_terminal_size as gts
from math import floor, ceil

h = """Правила игры:

    
Список команд:  


    """



def show_help():
    print(h)


def show_message(text):
    width = gts()[0] -1
    half_width = (width - len(text) - 2)/ 2
    m = f"""{'#'* width}
    {'#'* (width-2) + '#'}
    {'#' + ' '* (ceil(half_width) + 'text.upper() + ' '* (floor(half_width)+'#'}
    {'#'* (width-2) + '#'}
    {'#'* width}"""
    print('#'*width)
    print(m, end ='\n\n')
    pass
