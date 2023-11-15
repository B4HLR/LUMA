import datetime
import webbrowser
from googletrans import Translator
import pyttsx3
import locale
import time
import sys
import speech_recognition as sr
import wikipedia
from plyer import notification
import re
import random

wikipedia.set_lang('pt')
now = datetime.datetime.now()
engine = pyttsx3.init()

piadas = [
    "Por que o esqueleto não brigou com ninguém? Porque ele não tem estômago para isso!",
    "O que um canibal vegetariano come? A mesma coisa que todo mundo, só que ele sente mais culpa.",
    "Por que o livro de matemática se deitou? Porque tinha problemas.",
    "Qual é o café mais perigoso do mundo? O ex-presso.",
    "O que a girafa disse para o camelo? Você demora muito pra tomar banho!",
    "Qual é a semelhança entre o sol e um par de peitos? Com óculos escuros podes olhar mais tempo.",
    "Eu tenho o corpo perfeito, mas está em casa no meu congelador.",
    "A filha perguntou ao pai como morrem as estrelas. ele responde “Normalmente de overdose”.",
    "Os meus familiares mais idosos gostavam de me provocar nos casamentos, dizendo: “Tu é o próximo”! Assim que comecei a fazer o mesmo com eles nos funerais, eles pararam logo.",
    "O meu ex teve um acidente grave recentemente. Eu disse aos médicos o tipo de sangue errado. Agora, ele vai realmente saber como é a rejeição.",
    "Meu avô derrubou mais de 35 aviões na segunda guerra, foi considerado o pior mecânico na guerra",
    "O que o teu pai tem em comum com Nemo? Os dois não podem ser encontrados",
    "Tu não és completamente inútil, sempre podes ser usado como um mau exemplo",
]

def obter_piada_aleatoria():
    if not piadas:
        return "Não tenho mais piadas para contar."
    piada_aleatoria = random.choice(piadas)
    piadas.remove(piada_aleatoria)
    return piada_aleatoria


def criar_lembrete(titulo, mensagem):
    notification.notify(
        title=titulo,
        message=mensagem,
        timeout=5  # Tempo em segundos que a notificação será exibida
    )

def speak(text):
    engine.say(text)
    engine.runAndWait()
def speak_en(text):
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    engine.say(text)
    engine.runAndWait()

def algoma():
    time.sleep(5)
    speak('algo mais?')
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Fale algo:")
        audio = recognizer.listen(source, timeout=5)
        texto = recognizer.recognize_google(audio, language="pt-BR")
        print(texto)
    if texto.lower() == "não":
        sys.exit()
    elif():
        pass


def assis_lemb():
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            audio = recognizer.listen(source, timeout=7)
            try:
                texto = recognizer.recognize_google(audio, language="pt-BR")
                speak('lembrete criado')
                return texto
                break
            except sr.UnknownValueError:
                speak("Não foi possível entender o áudio")
                pass
            except sr.RequestError as e:
                print("Erro ao solicitar resultados; {0}".format(e))


class SystemInfo:
    def __init__(self):
        pass

    @staticmethod
    def get_time():
        answer = "Sâo {} horas {} minutos e {} segundos.".format(now.hour, now.minute, now.second)
        speak(answer)
    def get_day():
        locale.setlocale(locale.LC_TIME, "pt_BR.utf8")
        resp = "Hoje é {} de {} de {}.".format(now.day, now.strftime("%B"), now.year) 
        speak(resp)
    def pesyou (texto):
        pepe = texto.lower().replace("reproduza" , "").replace("no youtube" , "").replace('abra',"").replace("reproduzir", "").replace("abrir","").strip()
        link = f"https://www.youtube.com/results?search_query={pepe}"
        webbrowser.open(link, new=2)
        algoma()
    def abrirpes (texto):
        url = f"https://www.google.com/search?q={texto}"
        webbrowser.open(url, new=2)
    def pesimage (texto):
        pesim = texto.lower().replace("me dê", "").replace("quero", "").replace("me mostre", "").strip()
        url = f"https://www.google.com/search?q={pesim}&tbm=isch"
        webbrowser.open(url, new=2)
    def tradutor(texto):
        texto = texto.replace("traduza para o inglês","").replace("como seria em inglês", "").strip()
        try:
            translator = Translator()
            tradução = translator.translate(texto, src="pt", dest="en")
            speak_en(tradução.text)
        except Exception as e:
            return str(e)
    def wiki(texto):
        try:
            tex = texto.lower().replace("procure por", "").replace("pesquise na wiki","").strip()
            resp = wikipedia.summary(tex, 2)
            speak(resp)
            algoma()
        except wikipedia.exceptions.PageError:
            SystemInfo.abrirpes(tex)
    def fechar():
        sys.exit()
    def email():
        webbrowser.open(f"https://mail.google.com", new=2)
    def lembrete(texto):

        padrao_horario = r'\d{1,2}:\d{2}'

        horarios_encontrados = re.findall(padrao_horario, texto)
        if horarios_encontrados:
            for horario in horarios_encontrados:
                horario_que = horario
                if len(horario_que) == 4:
                    horario_que = "0" + horario_que
        else:
            print("horário encontrado no texto.")
        print('qual seria o lembrete?')
        speak('qual seria o lembrete?')
        texto = assis_lemb()

        while True:
            agora = datetime.datetime.now()
            formato_12_horas = agora.strftime("%I:%M")
            print("Hora formatada em 12 horas:", formato_12_horas)
            if formato_12_horas == horario_que:
                criar_lembrete("Lembrete", texto)
                break
            # Adicionar um pequeno atraso entre as verificações para evitar uso excessivo da CPU
            time.sleep(60)  # Verifica a cada minuto (60 segundos
    def piada():
        piada_aleatoria = obter_piada_aleatoria()
        speak(piada_aleatoria)