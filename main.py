from core.funcoes import FuncoesGerais # Importando a classe FuncoesGerais
class MenuPrincipal(FuncoesGerais): # Herança da classe FuncoesGerais
    
    def __init__(self): # Inicializando a classe MenuPrincipal
        pass
    
    def inicio(self): # Método de início
        self.limpar_terminal() # Limpando o terminal
        self.opcao_interface_inicial(self.interface_inicial()) # Chamando a interface inicial
    
    def interface_inicial(self): # Método da interface inicial
        print("✦  — — — — — ARKEN — — — — —  ✦\n\n") # Título do programa
        print("[1] - Criar senha\n[2] - Gerenciar senha\n[3] - Sair\n") # Opções do menu
        return str(input("Digite a opção desejada: ")) # Retorna a opção escolhida pelo usuário
    
    def opcao_interface_inicial(self, opcao): # Método para tratar a opção escolhida
        match opcao: # Usando o match para tratar a opção escolhida
            case "1": # Caso opção 1
                self.limpar_terminal() # Limpando o terminal
                from core.gerador_senha import GeradorSenha # Importando a classe GeradorSenha
                GeradorSenha().inicio() # Chamando o método de início da classe GeradorSenha
            case "2": # Caso opção 2
                self.limpar_terminal() # Limpando o terminal
                from core.gerenciador_senha import GerenciadorSenha # Importando a classe GerenciadorSenha
                GerenciadorSenha().inicio()
            case "3": # Caso opção 3
                self.limpar_terminal() # Limpando o terminal
                exit() # Saindo do programa
            case _: # Caso opção inválida
                self.explicacao_erro(1) # Chamando o método de erro
                self.inicio() # Chamando o método de início novamente para mostrar o menu
                              
if __name__ == "__main__": # Verificando se o arquivo está sendo executado diretamente
    MenuPrincipal().inicio() # Inicia o programa chamando o método de início da classe MenuPrincipal