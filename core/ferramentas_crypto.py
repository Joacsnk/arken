import os # Funções do Operating System
from core.funcoes import FuncoesGerais # Funções gerais kkk
import base64 # Codificação de dados binários em texto
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC # Derivação de chave baseado na senha para chave criptos
from cryptography.hazmat.primitives import hashes # Uilizada para transformar dados em um conjunto fixo de caracteres
from cryptography.hazmat.backends import default_backend # Necessário para configurar o PBKDF2HMAC
from cryptography.fernet import Fernet, InvalidToken # Sistema principal de criptografia; Erro se senha_mestra for errada
from backup.local import Backup_Local as BL
class FerramentasCrypto(FuncoesGerais):
    '''
    Se você quer SABER o que FerramentasCrypto faz, é simples:
    
    É uma classe que administra as funcionalidades de criptografia. A criptografia é um fator importante no projeto pois, sem ela, alguém mal intencionado poderá conseguir roubar as senhas e causar grandes estragos. Por isso, utilizo a criptografia nas senhas, para que, mesmo que o hacker estivesse em posse do senhas.json ou da chave.key, ele não consiga fazer basicamente nada pois estão protegidas com uma senha que ele não tem como saber (Mais tarde direi sobre)
    
    Se você quer ENTENDER o que FerramentasCrypto faz, siga esses passos (principalmente se você não sabe criptografia): 
    
    Primeiro, compre um lanche ou prepare um café bem gostoso.
    Relaxe bem o corpo e a mente, principalmente a mente.
    Agora, pronto para o desafio, vamos entender abaixo: 
    
    obter_salt - 
        O 'salt' é um fator aleatório que é adicionada na hora da criptografia, basicamente um "tempero" a criptografia. Ela é importante tanto para que a criptografia seja mais segura quanto para que as criptografias sejam diferentes, mesmo se as senhas fossem as mesmas. Ex: se a senha do usuário 1 for 'senha123' e o do usuário 2 for "senha123' também, o salt vai criar criptografias diferentes, pois o salt será diferente também
        
        A função primeiro define um caminho para o arquivo que guardará o salt, cria o caminho do diretório (data/) se ele não existe (mas se existe, ele não dá erro) e verifica se o arquivo existe (data/salt.salt). Se ele não existe ainda, ele cria e gera um conjunto de 16 bytes aleatórios. Por fim, ele abre e retorna 
        
    derivar_chave - 
        A derivação de chave seria a criptografia da senha-mestre com o salt, para criar uma chave criptográfica única
    
        A função usa como parâmetros a 'senha_mestre' em string e o salt em bytes. Primeiro ele cria um objeto para o PBKDF2HMAC, permitindo a melhor manipulação. Para isso, ele utiliza alguns parâmetros:
        
        algorithm=hashes.SHA256 (Algoritmo SHA-256, proteção alta e muito utilizada por sua segurança)
        length=32 (Tamanho padrão do fernet, que é 32 bytes, ou 256 bits)
        salt=salt (Salt, obviamente)
        iterations=100_000 (Quantidades de iterações com o hash. Quanto maior, mais seguro e mais lento)
        backend=default_backend (Padrão para acessar a API do cryptograph)
        
        Após isso, ele retorna: 
        
        senha_mestre.encode() (Transformando a senha para bytes)
        kdf.derive() (Fazendoa derivação com a senha e o salt)
        base64.urlsafe_b64encode() (Codificação para melhor armazenamento)
    
    senha_acesso - 
        Essa, dentro todo o código desse arquivo, é a única que se conecta diretamente com usuário. A senha-mestra será definida a partir do input. Primeiro, ele verifica se a chave.key existe. Se existe, significa que a chave criptografica existe, ou seja, já foi acessado alguma vez. Se não existe, ele definirá a sua senha de acesso e pedirá uma confirmação da senha
    
        Depois disso, ele:
        
        - Busca o salt
        - Busca a chave derivada, usando a senha com o salt 
        - Busca a chave Fernet (explico mais tarde)
        - Cria um objeto com a chave Fernet como parâmetro
    
    obter_chave_fernet - 
        Então chegamos na chave fernet. A chave fernet é a nossa principal forma e a mais simples de se compreender. Ela é a chave que nos permite criptografar e descriptografar os dados que queremos (no nosso exemplo, senhas). ex: Imagina que a sua senha importante é um celular. A chave fernet, nesse exemplo, seria um PIN. Esse PIN pode tanto bloqueiar seu celular como desbloquear-lo.
        
        Voltando para a criptografia, se alguém mal intencionado pegar suas senhas, ele não poderá fazer nada pois estão todas criptografadas. O problema real é se a chave for roubada. Se a chave fernet for roubada, mesmo que as senhas estejam criptografadas, ele consegue descriptografar com essa chave. Por isso se faz importante criptografar a chave fernet, para que, mesmo que a chave for roubada, estará criptografada também, e somente será descriptografada com a senha-mestre, que não está armazenada em um hardware (pelo menos espero que não)
        
        A função verifica se a chave existe. Se sim, ela retorna a chave fernet descriptografada. Se não, ela gera uma chave fernet nova e criptografa
    
    criptografar_chave_fernet -
        Ela retornará a chave fernet criptografada. Bom, não tem tanta explicação, o dificil passou
        
        A função utiliza a chave fernet descriptografada (chamada de 'chave_fernet_descriptografada') e a chave derivada como parâmetros. Primeiro, ele cria um objeto para utilizar a chave derivada. Depois ele criptografa a chave fernet e salva na 'chave_fernet_criptografada'. Após isso, ele salva essa chave criptografada no chave.key
        
    descriptografar_chave_fernet -
        Depois de toda a leitura, esse também é simples, porém importante. Utilizando a chave_derivada como parâmetro, ele busca a chave fernet criptografada no arquivo 'chave.key'. Nisso, ele tentará descriptografar essa chave usando a chave derivada. Se a senha-mestra for igual, a (senha-mestra + salt = chave_derivada) também é igual e irá descriptografar tranquilamente. Caso a senha for errada, ele mostrará o erro e voltará para o menu inicial
    
    criptografar_data -
        Função que criptografa a bendita senha. Pegando o dado em str, ele primeiro transforma em bytes, criptografa e transforma (e retorna) em str novamente.
        
        (obs: Lembre-se que sempre quando for criptografar ou descriptografar, tem que ser em bytes, e não em str. Pelos menos para os dados)
    
    descriptografar_data -
        Função que descriptografa a senha. Pegando o dado em str, ele primeiro transforma em bytes, criptografa e transforma (e retorna) em str novamente.
        
    É isso. Parabéns para você que leu e entendeu. Para quem não entendeu, repita os passos novamente
    '''
    def obter_salt(self, caminho='data/salt.salt'):
        os.makedirs(os.path.dirname(caminho), exist_ok=True)
        if not os.path.exists(caminho):
            with open(caminho, 'wb') as f:
                f.write(os.urandom(16))  # gera 16 bytes aleatórios seguros
        with open(caminho, 'rb') as f:
            return f.read()
        
    def derivar_chave(self, senha_mestra: str, salt: bytes) -> bytes:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),  
            length=32,                   
            salt=salt,                   
            iterations=100_000,          
            backend=default_backend()
        )
        return base64.urlsafe_b64encode(kdf.derive(senha_mestra.encode()))

    def senha_acesso(self):
            self.limpar_terminal()
            if os.path.exists('data/chave.key'):
                senha_mestre = str(input('Senha de acesso: '))
            else:
                while True:
                    senha_mestre = str(input('Defina sua senha de acesso à suas senhas (Guarde essa senha em um lugar seguro): '))
                    self.limpar_terminal()
                    if str(input("Digite a senha novamente para confirmar: ")) == senha_mestre:
                        break
                    else:
                        self.explicacao_erro(8)              
            salt = self.obter_salt()
            chave_derivada = self.derivar_chave(senha_mestre, salt)
            chave_fernet = self.obter_chave_fernet(chave_derivada)
            self.fernet = Fernet(chave_fernet) # Definindo objeto para criptografia e descriptografia
            BL().backup_arquivo(2)
            os.system("cls")
    
    def obter_chave_fernet(self, chave_derivada: bytes, caminho='data/chave.key') -> bytes:
        if not os.path.exists(caminho):
            chave_fernet_descriptografada = Fernet.generate_key()
            self.criptografar_chave_fernet(chave_fernet_descriptografada, chave_derivada)
            return chave_fernet_descriptografada
        else:
            return self.descriptografar_chave_fernet(chave_derivada, caminho)

    def criptografar_chave_fernet(self, chave_fernet_descriptografada: bytes, chave_derivada: bytes, caminho='data/chave.key'):
        fernet = Fernet(chave_derivada)                        
        chave_fernet_criptografada = fernet.encrypt(chave_fernet_descriptografada)
        os.makedirs(os.path.dirname(caminho), exist_ok=True)    
        with open(caminho, 'wb') as f:                       
            f.write(chave_fernet_criptografada)                        

    def descriptografar_chave_fernet(self, chave_derivada: bytes, caminho='data/chave.key') -> bytes:
        with open(caminho, 'rb') as f:
            chave_fernet_criptografada = f.read()
        fernet = Fernet(chave_derivada)
        try:
            chave_fernet_descriptografada = fernet.decrypt(chave_fernet_criptografada)
            return chave_fernet_descriptografada
        except InvalidToken:
            self.explicacao_erro(9)
            from main import MenuPrincipal
            MenuPrincipal().inicio()
    
    def criptografar_data(self, data: str):
        criptografada = self.fernet.encrypt(data.encode()).decode()
        return criptografada

    def descriptografar_data(self, data: str):
        descriptografada = self.fernet.decrypt(data.encode()).decode()
        return descriptografada