from core.funcoes import FuncoesGerais # importando funções para usar como herança
class MenuPrincipal(FuncoesGerais):
    ''' 
    Menu principal é o inicio do programa. É aqui que vamos para o gerenciador ou para o gerador de senhas.
    
    
    
    '''
    
    def __init__(self): 
        pass
    
    def inicio(self): # Def principal para iniciar o Main.py
        self.limpar_terminal() 
        self.opcao_interface_inicial(self.interface_inicial()) 
    
    def interface_inicial(self): # Interface de opções graficamente simples, desenvolvido para terminal
        print("✦  — — — — — ARKEN — — — — —  ✦\n\n") 
        print("[1] - Criar senha\n[2] - Gerenciar senha\n[3] - Sair\n") 
        return str(input("Digite a opção desejada: ")) # Retorna a opçao escolhida
    
    def opcao_interface_inicial(self, opcao): # Processa e executa a opção
        match opcao:
            case "1": # Importa e inicia o painel do gerador de senha
                self.limpar_terminal() 
                from core.gerador_senha import GeradorSenha 
                GeradorSenha().inicio() 
            case "2": # Importa e inicia o painel do gerenciador de senha
                self.limpar_terminal() 
                from core.gerenciador_senha import GerenciadorSenha 
                GerenciadorSenha().inicio() 
            case "3": # Sai do programa
                self.limpar_terminal() 
                exit() 
            case _: # Retorna novamente caso opção diferente
                self.explicacao_erro(1) 
                self.inicio() 
                              
if __name__ == "__main__": # Se o main for iniciado diretamente por ele, ele vai para o 'def inicio'
    MenuPrincipal().inicio() 
    