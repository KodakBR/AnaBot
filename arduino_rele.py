import serial
import time
import configparser

# Configuração inicial
arduino = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)  # Aguardar a inicialização do Arduino

def carregar_configuracao_reles():
    config = configparser.ConfigParser()
    config.read('reles.ini')
    reles = {}
    for section in config.sections():
        reles[section] = {
            'nome': config[section]['nome'],
            'numero': config[section]['numero']
        }
    return reles

def enviar_comando_arduino(comando):
    comando = comando + '\n'
    arduino.write(comando.encode())
    resposta = arduino.readline().decode('utf-8').strip()
    return resposta

def alternar_rele(nome_rele, numero_rele):
    comando = f"toggle {numero_rele}"
    resposta = enviar_comando_arduino(comando)
    return resposta

# Não mais restaurar estado, tudo inicia desligado
reles_config = carregar_configuracao_reles()
