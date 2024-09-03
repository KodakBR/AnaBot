import pyttsx3

# Inicializando o motor de fala
engine = pyttsx3.init()

def speak(text):
    """
    Função para o bot falar o texto fornecido.
    """
    engine.say(text)
    engine.runAndWait()