
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


caminho_optins = r'C:\Users\PC\Downloads\Tkinter-Designer-master\Tkinter-Designer-master\build\gui.py'
comando = ["python", caminho_optins]


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\PC\Downloads\pythorn\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x720")
window.configure(bg = "#D2D0C8")


canvas = Canvas(
    window,
    bg = "#D2D0C8",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    bg = "#D2D0C8",
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=536.0,
    y=255.0,
    width=210.0,
    height=210.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    bg = "#D2D0C8",
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=1228.0,
    y=20.0,
    width=30.0,
    height=30.0
)

canvas.create_text(
    528.0,
    549.0,
    anchor="nw",
    text="CLIQUE NO BOTÃO PARA INICIAR",
    fill="#000000",
    font=("CrimsonText Regular", 15 * -1)
)
window.resizable(False, False)
window.mainloop()