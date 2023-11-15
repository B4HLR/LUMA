import webbrowser
import speech_recognition as sr
import core
from nlu.classifier import classfy
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
from tkinter import PhotoImage


recognizer = sr.Recognizer()
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\PC\Downloads\Tkinter-Designer-master\Tkinter-Designer-master\build\assets\frame0")



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



def ouvir_e_escrever():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Fale algo:")
        audio = recognizer.listen(source, timeout=5)

        try:
            texto = recognizer.recognize_google(audio, language="pt-BR")
            print("Você disse:", texto)
            entity = classfy(texto)
            print(entity)
            if entity == 'time\getTime':
              core.SystemInfo.get_time()
            if entity == 'open\pesquisa':
              core.SystemInfo.abrirpes(texto)
            if entity == 'open\YouTube':
              core.SystemInfo.pesyou(texto)
            if entity == 'time\getDate':
              core.SystemInfo.get_day()
            if entity == 'open\Transl':
              core.SystemInfo.tradutor(texto)
            if entity == 'exit\ss':
              core.SystemInfo.fechar()
            if entity == 'pesquisar\imagem':
              core.SystemInfo.pesimage(texto)
            if entity == 'pesquisar\wiki':
              core.SystemInfo.wiki(texto)
            if entity == 'lembrete\create':
              core.SystemInfo.lembrete(texto)
            if entity == 'open\email':
              core.SystemInfo.email()
            if entity == 'piada\\None':
              core.SystemInfo.piada()
        except sr.UnknownValueError:
            core.speak("Não foi possível entender o áudio")
            pass
        except sr.RequestError as e:
            print("Erro ao solicitar resultados; {0}".format(e))


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
image_1 = PhotoImage(file="build\\assets\\frame0\\button_1.png")
button_1 = Button(
    image=image_1,
    borderwidth=0,
    bg = "#D2D0C8",
    highlightthickness=0,
    command=lambda: ouvir_e_escrever(),
    relief="flat"
)
button_1.place(
    x=536.0,
    y=255.0,
    width=210.0,
    height=210.0
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
