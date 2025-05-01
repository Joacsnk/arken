from core.funcoes import FuncoesGerais # Funções gerais...dhuuu
import os # Verificação do arquivo json
import json # Manipulação em json
from core.ferramentas_crypto import FerramentasCrypto as FC # Funções gerais
from backup.local import Backup_Local as BL
class GerenciadorSenha(FuncoesGerais): 
    '''
    O GerenciadorSenha tem a função de gerenciar suas senhas de forma maleável e que seja fácil de manipular. Precisa buscar, excluir ou adicionar uma senha? Precisa editar uma senha? Aqui é o lugar
    
    Para começar, definimos um objeto, pedimos o acesso com 'self.crypto.senha_acesso()' e verificamos se o arquivo json existe
    '''
    def __init__(self): 
        self.crypto = FC()
        self.crypto.senha_acesso()
        self.verificar_arquivo_json() 
    
    def inicio(self): 
        self.opcao_interface(self.interface()) # Inciando interface com escolha
    
    def interface(self): 
        print("● — — — — — ◦Gerenciador de Senhas◦ — — — — — ●\n\n") 
        print("[1] - Adicionar\n") 
        print("[2] - Listar\n") 
        print("[3] - Buscar\n") 
        print("[4] - Remover\n")
        print("[5] - Sair\n")
        return str(input("Digite a opção desejada: "))

    def opcao_interface(self, opcao):
        match opcao:
            case "1":
                self.adicionar_senha() # Adicionar uma nova senha
            case "2":
                self.listar_nomes_senhas() # Listar os nomes de suas senhas 
            case "3":
                self.buscar_senha() # Faz uma busca pela senha digitada e pode editar ou copiar
            case "4":
                self.remover_senha() # busca e remove a senha
            case "5":
                self.limpar_terminal() # Volta para o menu
                from main import MenuPrincipal
                MenuPrincipal().inicio()
            case _:
                self.explicacao_erro(1)
                self.inicio()
                
    '''
    verificar_arquivo_json verifica se o arquivo, que serve para guardar as senhas, existe. Ele define o caminho e se pergunta se existe. Se não, ele cria e o escreve com '{}'
    '''
    def verificar_arquivo_json(self):
        self.caminho_json = os.path.join('data', 'senhas.json')
        if not os.path.exists(self.caminho_json) or os.stat(self.caminho_json).st_size == 0:
            os.makedirs(os.path.dirname(self.caminho_json), exist_ok=True)
            with open(self.caminho_json, 'w') as f:
                json.dump({}, f)
    
    '''
    adicionar_senha define o nome da senha, a senha em si e a descrição. O nome facilita a pesquisa, a senha é a parte que interessamos né e a descricão ajuda na hora de saber suas aplicações e facilita os usos (ele dá erro se nenhum for preenchido). Nisso, ele faz uma pesquisa para ver se existe uma senha com o mesmo nome, se existir ele impede o usuário de usar a mesma senha, para não haver conflito. Se atender essas condições, ele criptografa as informações (menos o nome) e guarda no json
    '''
    def adicionar_senha(self):
        self.limpar_terminal()
        nome_senha = str(input("Digite o nome da senha: "))
        senha = str(input("Digite a senha: "))
        descricao_senha = str(input("Digite a descrição da senha: "))
        if not nome_senha or not senha or not descricao_senha:
            self.explicacao_erro(6)
            self.inicio()
        with open(self.caminho_json, 'r') as f:
                conjunto_senhas = json.load(f)
                if nome_senha in conjunto_senhas:
                    self.explicacao_erro(7)
                    self.inicio()
                else:
                    senha = self.crypto.criptografar_data(senha)
                    descricao_senha = self.crypto.criptografar_data(descricao_senha)
                    conjunto_senhas[nome_senha] = {
                        'senha': senha,
                        'descricao': descricao_senha
                    }
                with open(self.caminho_json, 'w') as f:
                    json.dump(conjunto_senhas, f, indent=4)
                BL().backup_arquivo(1)
                self.titulo_visivel("Senha adicionada com sucesso!", 2)
                self.inicio()
    
    '''
    listar_nomes_senhas confere, antes de tudo, se existe senhas. Se não existir, ele retorna erro. Caso tenha senhas, ele lista todos os nomes de senhas disponíveis
    '''
    
    def listar_nomes_senhas(self):
        self.limpar_terminal()
        with open(self.caminho_json, 'r') as f:
            conjunto_senhas = json.load(f)
            if not conjunto_senhas:
                self.titulo_visivel("Nenhuma senha cadastrada!", 1.5)
                self.inicio()
            else:
                print("Senhas cadastradas:\n\n")
                for nome_senha in conjunto_senhas:
                    print(f"{nome_senha}") 
                    str(input("\nPressione enter para continuar... "))
                    self.limpar_terminal()
                    self.inicio()
    
    
    '''
    buscar_senha primeiro faz uma busca pelo nome da senha. E então ele faz uma leitura (caso ele não exista, ele aponta o erro e volta para o menu). Se existir, ele mostra a senha descriptografada e verifica a opção. Caso 1, ele copia e volta. Caso 2, ele edita a senha e guarda novamente. Caso 3, ele retorna normalmente
    '''
    
    def buscar_senha(self):
        self.limpar_terminal()
        nome_senha = str(input("Digite o nome da senha: "))
        with open(self.caminho_json, 'r') as f:
            conjunto_senhas = json.load(f)
            if nome_senha in conjunto_senhas:
                while True:
                    self.limpar_terminal()
                    senha = self.crypto.descriptografar_data(conjunto_senhas[nome_senha]['senha'])
                    descricao = self.crypto.descriptografar_data(conjunto_senhas[nome_senha]['descricao'])
                    print(f"Nome da senha: {nome_senha}\nSenha: {senha}\nDescrição: {descricao}")
                    opcao = str(input("\n[1] - Copiar\n[2] - Editar\n[3] - Voltar\n\nDigite a opção desejada: "))
                    if opcao == "1":
                        self.copiar_conteudo(senha)
                        self.titulo_visivel("Senha copiada com sucesso!", 2)
                        self.limpar_terminal()
                        self.inicio()
                    elif opcao == "2":
                        self.limpar_terminal()
                        senha = str(input("Digite a nova senha: "))
                        descricao = str(input("Digite a nova descrição: "))
                        if not senha or not descricao:
                            self.explicacao_erro(6)
                            self.inicio()
                        else:
                            conjunto_senhas[nome_senha] = {
                                'senha': self.crypto.criptografar_data(senha),
                                'descricao': self.crypto.criptografar_data(descricao)
                            }
                            with open(self.caminho_json, 'w') as f:
                                json.dump(conjunto_senhas, f, indent=4)
                            BL().backup_arquivo(1)
                            self.titulo_visivel("Senha editada com sucesso!", 2)
                            self.inicio()
                    elif opcao == "3":
                        self.limpar_terminal()
                        self.inicio()
                    else:
                        self.explicacao_erro(1)
            else:
                self.titulo_visivel("Senha não encontrada!", 1.5)
                self.inicio()
    
    '''
    remover_senha faz a busca do nome da senha que quer ser excluída. Caso encontrada, ele descriptografa os dados e pergunta se deseja realmente remover. Caso sim, ele remove 
    '''
    
    def remover_senha(self):
        self.limpar_terminal()
        nome_senha = str(input("Digite o nome da senha que deseja remover: "))
        with open(self.caminho_json, 'r') as f:
            conjunto_senhas = json.load(f)
            if nome_senha in conjunto_senhas:
                senha = self.crypto.descriptografar_data(conjunto_senhas[nome_senha]['senha'])
                descricao = self.crypto.descriptografar_data(conjunto_senhas[nome_senha]['descricao'])
                while True:
                    self.limpar_terminal()
                    print(f"Nome da senha: {nome_senha}\nSenha: {senha}\nDescrição: {descricao}")
                    print(f"\nDeseja realmente remover {nome_senha}?\n\n[1] - Sim\n[2] - Não")
                    opcao = str(input("\nDigite a opção desejada: "))
                    if opcao == "1":
                        del conjunto_senhas[nome_senha]
                        with open(self.caminho_json, 'w') as f:
                            json.dump(conjunto_senhas, f, indent=4)
                        BL().backup_arquivo(1)
                        self.titulo_visivel("Senha removida com sucesso!", 1.5)
                        self.inicio()
                    elif opcao == "2":
                        self.limpar_terminal()
                        self.inicio()
                    else:
                        self.explicacao_erro(1)
            else:
                self.titulo_visivel("Senha não encontrada!", 1.5)
                self.inicio()
    
    
