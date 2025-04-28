import os
from shutil import copy2
from datetime import datetime
class Backup_Local:
    
    def __init__(self):
        os.makedirs('backup', exist_ok=True)
    
    def backup_arquivo(self, arquivo):
        data_hora = datetime.now().strftime("%Y-%m-%d")
        nome, extensao = arquivo.split('.')
        origem = f'data/{arquivo}'
        if arquivo == 'salt.salt':
            os.makedirs('backup/backup_salt', exist_ok=True)
            destino = f'backup/backup_salt/{nome}_backup_{data_hora}.{extensao}'
        elif arquivo == 'chave.key':
            os.makedirs('backup/backup_key', exist_ok=True)
            destino = f'backup/backup_key/{nome}_backup_{data_hora}.{extensao}'
        elif arquivo == 'senhas.json':
            os.makedirs('backup/backup_json', exist_ok=True)
            destino = f'backup/backup_json/{nome}_backup_{data_hora}.{extensao}'
        copy2(origem, destino)