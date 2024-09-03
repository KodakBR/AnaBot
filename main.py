from Recognizer_speech import recognize_speech_from_microphone
from mysql_program import adicionar_programa, obter_caminho_programa, executar_programa_por_comando
from motor_fala import speak
from arduino_rele import alternar_rele, reles_config
import configparser

def carregar_comandos():
    config = configparser.ConfigParser()
    config.read('comandos.ini')
    comandos = {}
    for section in config.sections():
        comandos[section] = dict(config.items(section))
        # print("Comandos carregados:", comandos)  # print para verificar os comandos carregados
    return comandos

def processar_comando(voice_command):
    comandos = carregar_comandos() 
    # print("Comando de voz recebido:", voice_command)  #print para verificar o comando recebido
    for cmd_name, cmd_info in comandos.items():
        if voice_command in cmd_info['comando'].split(", "):
            return cmd_info
    print("Nenhum comando correspondente encontrado.")  # Se não encontrou nenhum comando
    return None

def executar_acao(comando, voice_command):
    tipo = comando['tipo']
    if tipo == 'texto':
        if comando['acao'] == 'printar':
            print(comando['mensagem'])
        elif comando['acao'] == 'falar':
            speak(comando['mensagem'])
    elif tipo == 'programa':
        caminho = obter_caminho_programa(comando['nome_programa'])
        if caminho:
            speak(f"Abrindo {comando['nome_programa']}")
            executar_programa_por_comando(comando['nome_programa'])
            speak(f"{comando['nome_programa']} aberto")
    elif tipo == 'novo':
        if comando:
            nome = input("Qual o nome do programa: ")
            caminho = input("Qual o caminho do programa: ")
            adicionar_programa(nome, caminho)
    elif tipo == 'arduino':
        numero_rele = comando['numero'] # usa o numero do rele no arquivo reles.ini
        for nome_rele, config in reles_config.items():
            if numero_rele == config['numero']:
                resposta = alternar_rele(nome_rele, numero_rele)
                speak(f"{config['nome']} {resposta}")
                break

        else:
            speak("Comando de rele nao encontrado!")


def command_bot():
    while True:
        try:
            voice_command = recognize_speech_from_microphone()

            if voice_command and voice_command.startswith("ana"):
                speak("Ola mestre, como posso ajudar o senhor")
                comando = recognize_speech_from_microphone()  # Aguardar o próximo comando imediatamente
                
                if comando:
                    comando_processado = processar_comando(comando)
                    if comando_processado:
                        executar_acao(comando_processado, comando)
                    else:
                        speak("Comando não encontrado!")
                else:
                    speak("Desculpe, não consegui entender o comando.")

        except KeyboardInterrupt:
            print("Programa encerrado.")
            break

if __name__ == "__main__":
    command_bot()
