import mysql.connector
import configparser
import os

def conectar_banco():
    config = configparser.ConfigParser()
    config.read('db_config.ini')
    
    db_config = config['DatabaseProgram']
    
    return mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database']
    )

def criar_tabela_programas():
    """
    Cria a tabela 'programas' no banco de dados se ela ainda não existir.
    """
    db = conectar_banco()
    cursor = db.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS programas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        caminho VARCHAR(255) NOT NULL
    )
    """)
    db.commit()
    cursor.close()
    db.close()

def adicionar_programa(nome, caminho):
    """
    Adiciona um novo programa à tabela 'programas'.
    """
    db = conectar_banco()
    cursor = db.cursor()
    cursor.execute("INSERT INTO programas (nome, caminho) VALUES (%s, %s)", (nome, caminho))
    db.commit()
    cursor.close()
    db.close()

def obter_caminho_programa(nome):
    """
    Obtém o caminho de um programa pelo nome.
    """
    db = conectar_banco()
    cursor = db.cursor()
    cursor.execute("SELECT caminho FROM programas WHERE nome = %s", (nome,))
    resultado = cursor.fetchone()
    cursor.close()
    db.close()
    return resultado[0] if resultado else None

def executar_programa_por_comando(voice_command):
    """
    Verifica se o comando de voz corresponde a um programa e, se sim, executa o programa.
    """
    caminho_programa = obter_caminho_programa(voice_command)
    if caminho_programa:
        os.startfile(caminho_programa)
        return f"Executando {voice_command}"
    else:
        return "Comando não encontrado no banco de dados."

# Testar as funções acima (no contexto real você chamaria essas funções de acordo com a lógica do bot)
# criar_tabela_programas()
# adicionar_programa("notepad", "C:\\Windows\\notepad.exe")
# resultado = executar_programa_por_comando("notepad")
# print(resultado)  # Esperado: "Executando notepad"

# Observação: Como estamos em um ambiente restrito, não podemos realmente testar a conexão com o banco de dados
# ou a execução de programas. Porém, o código acima deve funcionar em um ambiente local configurado corretamente.

