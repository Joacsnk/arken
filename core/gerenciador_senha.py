from core.funcoes import FuncoesGerais # Importando a classe FuncoesGerais
import os # Importando a biblioteca os para manipulação de arquivos
import json # Importando a biblioteca json para manipulação de arquivos json
class GerenciadorSenha(FuncoesGerais): # Herança da classe FuncoesGerais
    
    def __init__(self): # Método construtor
        self.verificar_arquivo_json() # Verifica se o arquivo json existe e cria se não existir
    
    def inicio(self): # Método de início
        self.opcao_interface(self.interface()) # Chamando a interface inicial
    
    def interface(self): # Interface inicial
        print("● — — — — — ◦Gerenciador de Senhas◦ — — — — — ●\n\n") # Título
        print("[1] - Adicionar\n") # Opção 1: adicionar senha
        print("[2] - Listar\n") # Opção 2: mostrar os nomes das senhas
        print("[3] - Buscar\n") # Opção 3
        print("[4] - Remover\n")
        print("[5] - Sair\n")
        return str(input("Digite a opção desejada: "))

    def opcao_interface(self, opcao):
        match opcao:
            case "1":
                self.adicionar_senha()
            case "2":
                self.listar_nomes_senhas()
            case "3":
                self.buscar_senha()
            case "4":
                self.remover_senha()
            case "5":
                self.limpar_terminal()
                from main import MenuPrincipal
                MenuPrincipal().inicio()
            case _:
                self.explicacao_erro(1)
                self.inicio()
                
    def verificar_arquivo_json(self):
        self.caminho_json = r'C:\Users\Usuario\Desktop\Projetos\Andamento\arken\data\senhas.json'
        if not os.path.exists(self.caminho_json) or os.stat(self.caminho_json).st_size == 0:
            os.makedirs(os.path.dirname(self.caminho_json), exist_ok=True)
            with open(self.caminho_json, 'w') as f:
                json.dump({}, f)
                
    def adicionar_senha(self):
        self.limpar_terminal()
        nome_senha = str(input("Digite o nome da senha: "))
        senha = str(input("Digite a senha: "))
        descricao_senha = str(input("Digite a descrição da senha: "))
        if not nome_senha or not senha or not descricao_senha:
            self.explicacao_erro(6)
            self.inicio()
        elif nome_senha in conjunto_senhas:
            self.explicacao_erro(7)
            self.inicio()
        else:
            with open(self.caminho_json, 'r') as f:
                conjunto_senhas = json.load(f)
                conjunto_senhas[nome_senha] = {
                    'senha': senha,
                    'descricao': descricao_senha
                }
            with open(self.caminho_json, 'w') as f:
                json.dump(conjunto_senhas, f, indent=4)
            self.titulo_visivel("Senha adicionada com sucesso!", 2)
            self.inicio()
        
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
                while True:
                    str(input("\nPressione enter para continuar..."))
                    self.limpar_terminal()
                    self.inicio()
    
    def buscar_senha(self):
        self.limpar_terminal()
        nome_senha = str(input("Digite o nome da senha: "))
        with open(self.caminho_json, 'r') as f:
            conjunto_senhas = json.load(f)
            if nome_senha in conjunto_senhas:
                while True:
                    self.limpar_terminal()
                    senha = conjunto_senhas[nome_senha]['senha']
                    descricao = conjunto_senhas[nome_senha]['descricao']
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
                                'senha': senha,
                                'descricao': descricao
                            }
                            with open(self.caminho_json, 'w') as f:
                                json.dump(conjunto_senhas, f, indent=4)
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
    
    def remover_senha(self):
        self.limpar_terminal()
        nome_senha = str(input("Digite o nome da senha que deseja remover: "))
        with open(self.caminho_json, 'r') as f:
            conjunto_senhas = json.load(f)
            if nome_senha in conjunto_senhas:
                while True:
                    self.limpar_terminal()
                    print(f"Nome da senha: {nome_senha}\nSenha: {conjunto_senhas[nome_senha]['senha']}\nDescrição: {conjunto_senhas[nome_senha]['descricao']}")
                    print(f"\nDeseja realmente remover {nome_senha}?\n\n[1] - Sim\n[2] - Não")
                    opcao = str(input("\nDigite a opção desejada: "))
                    if opcao == "1":
                        del conjunto_senhas[nome_senha]
                        with open(self.caminho_json, 'w') as f:
                            json.dump(conjunto_senhas, f, indent=4)
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
    
    
