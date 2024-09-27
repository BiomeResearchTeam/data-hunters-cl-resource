import os
from os import system, name
from rich.panel import Panel
from rich.text import Text
from rich.console import Console
from rich.columns import Columns
from rich.align import Align
console = Console()

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux
    else:
        _ = system('clear')


def center_text(text):
    #centrare il testo. utile soprattutto con input()
    terminal_width = os.get_terminal_size().columns
    padding = (terminal_width - len(text)) // 2
    centered_text = " " * padding + text
    return centered_text


def main_box(title, text, width, height):
    #box viola con testo giustificato al centro, di cui specificare titolo, testo, larghezza e altezza
    text_title = Text.assemble(title)
    text_content = Text.assemble(text, style=None, justify="center")
    main_box = Panel(text_content, title=text_title, border_style="magenta1", padding=(0, 1), width=width, height=height)
    return main_box

def options_box(options, colors):
    #crea i pulsanti delle opzioni; bisogna fornire le opzioni e il colore del bordo dei rettangoli 
    #(colore del testo è da specificare prima di questa def)
    choice = [Panel(opt, expand=True, border_style=color) for opt, color in zip(options, colors)]
    columns = Columns(choice, equal=True)
    return columns