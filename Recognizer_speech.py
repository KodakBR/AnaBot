import speech_recognition as sr
from motor_fala import speak
import unicodedata  # Importação adicional para normalização de texto

# # Inicializa o reconhecedor de fala
# recognizer = sr.Recognizer()

# # Captura o audio do microfone
# with sr.Microphone() as source:
#     print("Por favor, fale algo:")
#     audio = recognizer.listen(source)

# # Tenta reconhecer a fala usando o Google Web Speech API
# try:
#     print("Voce disse: " + recognizer.recognize_google(audio, language="pt-BR"))
# except sr.UnknownValueError:
#     print("Descupe, nao entendi o que voce disse.")
# except sr.RequestError as e:
#     print(f"Erro ao requisitar os resultados do servico de reconhecimento de fala; {e}")

def recognize_speech_from_microphone():
    """
    Captura áudio do microfone, tenta reconhecer a fala,
    e normaliza o texto para evitar problemas com maiúsculas/minúsculas ou acentuação.
    Retorna o texto normalizado ou None em caso de falha.
    """
    # Inicializa o reconhecedor de fala.
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Por favor, fale algo:")
        # speak("oque deseja: ")
        audio = recognizer.listen(source)

    try:
        # Tenta reconhecer a fala usando a API do Google
        text = recognizer.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {text}")
        
        # Normaliza o texto para evitar problemas de correspondência
        text = text.lower()  # Converte todo o texto para minúsculas
        text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')
        
        return text
    except sr.UnknownValueError:
        print("Desculpe, não consegui entender o que você disse.")
        return None
    except sr.RequestError as e:
        print(f"Erro ao requisitar os resultados do serviço de reconhecimento de fala; {e}")
        return None
    
