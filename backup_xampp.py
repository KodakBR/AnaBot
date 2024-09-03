import mysql.connector
import configparser
import os
from datetime import datetime

def conectar_banco_xampp():
    config = configparser.ConfigParser()
    config.read('db_config.ini')
    
    db_config = config['DatabaseBackup']
    
    return mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database']
    )

def criar_tabelas_backup(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS programas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255),
        caminho VARCHAR(255)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS comandos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        tipo VARCHAR(50),
        modo VARCHAR(50),
        comando TEXT,
        terminal TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reles (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255),
        numero INT
    )
    """)

def realizar_backup():
    db_backup = conectar_banco_xampp()
    cursor_backup = db_backup.cursor()
    
    criar_tabelas_backup(cursor_backup)
    
    cursor_backup.execute("DELETE FROM programas")
    cursor_backup.execute("INSERT INTO programas SELECT * FROM annybot.programas")
    
    cursor_backup.execute("DELETE FROM comandos")
    cursor_backup.execute("INSERT INTO comandos SELECT * FROM annybot.comandos")

    cursor_backup.execute("DELETE FROM reles")
    cursor_backup.execute("INSERT INTO reles SELECT * FROM annybot.reles")
    
    db_backup.commit()
    
    # Backup dos arquivos .ini
    os.system("cp comandos.ini reles.ini /path/to/xampp/backup/folder/")  # Altere o caminho conforme necessário

    cursor_backup.close()
    db_backup.close()

    print("Backup realizado com sucesso.")
