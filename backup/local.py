import os
from shutil import copy2
from datetime import datetime
class Backup_Local:
    
    def __init__(self):
        pass
        
    def backup_arquivo(self, modo):
        self.verificar_arquivos()
        data_hora = datetime.now().strftime("%Y-%m-%d")
        if modo == 1:
            origem = 'data/senhas.json'
            destino = f'backup/backup_json/senhas_backup_{data_hora}.json'
        elif modo == 2:
            origem = 'data/salt.salt'
            destino = f'backup/backup_salt/salt_backup_{data_hora}.salt'
            copy2(origem,destino)
            origem = 'data/chave.key'
            destino = f'backup/backup_key/chave_backup_{data_hora}.key'
        copy2(origem, destino) 
    
    def verificar_arquivos(self):
        os.makedirs('backup', exist_ok=True)
        os.makedirs('backup/backup_salt', exist_ok=True)
        os.makedirs('backup/backup_key', exist_ok=True)
        os.makedirs('backup/backup_json', exist_ok=True)
        
if __name__ == '__main__':
    Backup_Local().backup_arquivo('chave.key')