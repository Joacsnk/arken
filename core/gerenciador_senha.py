import json # Manipulação em json
from core.funcoes import FuncoesGerais # Funções gerais...dhuuu
from core.ferramentas_crypto import FerramentasCrypto as FC # Funções gerais
from backup.local import Backup_Local as BL
class GerenciadorSenha(FuncoesGerais): 
    '''
    O GerenciadorSenha tem a função de gerenciar suas senhas de forma maleável e que seja fácil de manipular. Precisa buscar, excluir ou adicionar uma senha? Precisa editar uma senha? Aqui é o lugar
    
    Para começar, definimos um objeto, pedimos o acesso com 'self.crypto.senha_acesso()' e verificamos se o arquivo json existe. Depois definimos o caminho padrão
    '''
    def __init__(self): 
        self.crypto = FC()
        self.crypto.senha_acesso()
        self.caminho_json = BL().verificar_arquivos()
        self.caminho_json = 'data/senhas.json'
    
    def inicio(self): 
        self.opcao_interface(self.interface()) # Inciando interface com escolha
    
    def interface(self):
        print("\n" + "═" * 60)
        print("       ● ◦◦◦ MENU DO GERENCIADOR DE SENHAS ◦◦◦ ●")
        print("═" * 60 + "\n")

        print("  [1] Adicionar nova senha")
        print("  [2] Listar todas as senhas")
        print("  [3] Buscar por uma senha")
        print("  [4] Remover senha")
        print("  [5] Sair\n")

        return input("Digite a opção desejada ➤  ")

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
                from main import MenuPrincipal # Volta para o menu
                MenuPrincipal().inicio()
            case _:
                self.explicacao_erro(1)
                self.inicio()
                 
    '''
    adicionar_senha define o nome da senha, a senha em si e a descrição. O nome facilita a pesquisa, a senha é a parte que interessamos né e a descricão ajuda na hora de saber suas aplicações e facilita os usos (ele dá erro se nenhum for preenchido). Nisso, ele faz uma pesquisa para ver se existe uma senha com o mesmo nome, se existir ele impede o usuário de usar a mesma senha, para não haver conflito. Se atender essas condições, ele criptografa as informações (menos o nome), faz o backup e guarda no json
    '''
    def adicionar_senha(self):
        self.limpar_terminal()
        nome_senha = str(input("Digite o nome da senha ➤  "))
        senha = str(input("Digite a senha ➤  "))
        descricao_senha = str(input("Digite a descrição da senha ➤  "))
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
                print("\n" + "═" * 50)
                print("        ● SENHAS CADASTRADAS ●")
                print("═" * 50 + "\n")
                for nome_senha in conjunto_senhas:
                    print(f"  ➤  {nome_senha}")
                input("\n  ↳ Pressione Enter para continuar...\n")
                self.limpar_terminal()
                self.inicio()
     
    '''
    buscar_senha primeiro faz uma busca pelo nome da senha. E então ele faz uma leitura (caso ele não exista, ele aponta o erro e volta para o menu). Se existir, ele mostra a senha descriptografada e verifica a opção. Caso 1, ele copia e volta. Caso 2, ele edita a senha, faz um backup e guarda novamente. Caso 3, ele retorna normalmente
    '''
    def buscar_senha(self):
        self.limpar_terminal()
        nome_senha = str(input("Digite o nome da senha ➤  "))
        with open(self.caminho_json, 'r') as f:
            conjunto_senhas = json.load(f)
            if nome_senha in conjunto_senhas:
                while True:
                    self.limpar_terminal()
                    senha = self.crypto.descriptografar_data(conjunto_senhas[nome_senha]['senha'])
                    descricao = self.crypto.descriptografar_data(conjunto_senhas[nome_senha]['descricao'])
                    print("\n" + "═" * 50)
                    print("        ● DETALHES DA SENHA ●")
                    print("═" * 50 + "\n")

                    print(f"Nome ➤  {nome_senha}")
                    print(f"Senha ➤  {senha}")
                    print(f"Descrição ➤  {descricao}\n")

                    print("  [1] Copiar senha")
                    print("  [2] Editar senha")
                    print("  [3] Voltar\n")
                    opcao = input("Digite a opção desejada ➤  ")
                    if opcao == "1":
                        self.copiar_conteudo(senha)
                        self.titulo_visivel("Senha copiada com sucesso!", 2)
                        self.limpar_terminal()
                        self.inicio()
                    elif opcao == "2":
                        self.limpar_terminal()
                        senha = str(input("Digite a nova senha ➤  "))
                        descricao = str(input("Digite a nova descrição ➤  "))
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
    remover_senha faz a busca do nome da senha que quer ser excluída. Caso encontrada, ele descriptografa os dados e pergunta se deseja realmente remover. Caso sim, ele remove e faz o backup novamente
    '''
    def remover_senha(self):
        self.limpar_terminal()
        nome_senha = str(input("Digite o nome da senha que deseja remover ➤  "))
        with open(self.caminho_json, 'r') as f:
            conjunto_senhas = json.load(f)
            if nome_senha in conjunto_senhas:
                senha = self.crypto.descriptografar_data(conjunto_senhas[nome_senha]['senha'])
                descricao = self.crypto.descriptografar_data(conjunto_senhas[nome_senha]['descricao'])
                while True:
                    self.limpar_terminal()
                    print("\n" + "═" * 50)
                    print("        ● CONFIRMAÇÃO DE REMOÇÃO ●")
                    print("═" * 50 + "\n")
                    print(f"Nome ➤  {nome_senha}")
                    print(f"Senha ➤  {senha}")
                    print(f"Descrição  ➤ {descricao}\n")
                    print(f"⚠️  Deseja realmente remover \"{nome_senha}\"?\n")
                    print("  [1] Sim")
                    print("  [2] Não\n")
                    opcao = input("Digite a opção desejada ➤  ")
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
    
    
if __name__ == "__main__":
    GerenciadorSenha().inicio()