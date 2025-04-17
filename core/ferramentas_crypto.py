import os
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet, InvalidToken
class FerramentasCrypto():
    
    def obter_salt(self, caminho='data/salt.salt'):
        os.makedirs(os.path.dirname(caminho), exist_ok=True)
        if not os.path.exists(caminho):
            with open(caminho, 'wb') as f:
                f.write(os.urandom(16))  # gera 16 bytes aleatórios seguros
        with open(caminho, 'rb') as f:
            return f.read()
        
    def derivar_chave(self, senha_mestra: str, salt: bytes) -> bytes:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),   # algoritmo de hash
            length=32,                   # tamanho da chave (bytes)
            salt=salt,                   # salt que você obteve antes
            iterations=100_000,          # número de iterações para dificultar força bruta
            backend=default_backend()
        )
        return base64.urlsafe_b64encode(kdf.derive(senha_mestra.encode()))

    def senha_acesso(self):
            os.system('cls')
            senha_mestre = str(input('Senha de acesso: '))
            salt = self.obter_salt()
            chave_derivada = self.derivar_chave(senha_mestre, salt)
            chave_fernet = self.preparar_chave_fernet(chave_derivada)
            self.fernet = Fernet(chave_fernet)
            os.system("cls")
    
    def preparar_chave_fernet(self, chave_derivada: bytes, caminho='data/chave.key') -> bytes:
        if not os.path.exists(caminho):
            chave_original = Fernet.generate_key()
            self.criptografar_chave_fernet(chave_original, chave_derivada)
            return chave_original
        else:
            return self.descriptografar_chave_fernet(chave_derivada, caminho)

    def criptografar_chave_fernet(self, chave_original: bytes, chave_derivada: bytes, caminho='data/chave.key'):
        fernet = Fernet(chave_derivada)                        
        chave_criptografada = fernet.encrypt(chave_original)
        os.makedirs(os.path.dirname(caminho), exist_ok=True)    
        with open(caminho, 'wb') as f:                       
            f.write(chave_criptografada)                        

    def descriptografar_chave_fernet(self, chave_derivada: bytes, caminho='data/chave.key') -> bytes:
        with open(caminho, 'rb') as f:
            chave_criptografada = f.read()
        fernet = Fernet(chave_derivada)
        try:
            chave_original = fernet.decrypt(chave_criptografada)
            return chave_original
        except InvalidToken:
            exit()
    
    def criptografar_data(self, data: str):
        criptografada = self.fernet.encrypt(data.encode()).decode()
        return criptografada

    def descriptografar_data(self, data: str):
        descriptografada = self.fernet.decrypt(data.encode()).decode()
        return descriptografada