from core.funcoes import FuncoesGerais # importando funções gerais
class MenuPrincipal(FuncoesGerais):
    ''' 
    Menu principal é o inicio do programa. É aqui que vamos para o gerenciador ou gerador de senhas. Caso queira sair do sistema, esse é o caminho também. O MenuPrincipal é o porta voz do programa. É por esse arquvio que tudo começa
    '''
    
    def __init__(self): # Init padrão para evitar problemas de compatibilidade
        pass
    
    def inicio(self): # Def principal para iniciar o Main.py
        self.limpar_terminal() 
        self.opcao_interface_inicial(self.interface_inicial()) 
    
    def interface_inicial(self): # Interfaçe gráfica
        print("\n" + "=" * 34)
        print("✦      — — — ARKEN — — —      ✦")
        print("=" * 34 + "\n")
        
        print("  [1] Criar senha")
        print("  [2] Gerenciar senha")
        print("  [3] Sair\n")
        
        return input("Digite a opção desejada ➤  ")
    
    def opcao_interface_inicial(self, opcao): # Processa e executa a opção do usuário
        self.limpar_terminal()
        match opcao:
            case "1": # Importa e inicia o painel do gerador de senha
                from core.gerador_senha import GeradorSenha 
                GeradorSenha().inicio() 
            case "2": # Importa e inicia o painel do gerenciador de senha
                from core.gerenciador_senha import GerenciadorSenha 
                GerenciadorSenha().inicio() 
            case "3": # Sai do programa
                exit() 
            case _: # Apresenta erro e retorna ao início
                self.explicacao_erro(1) 
                self.inicio() 
                              
if __name__ == "__main__": # Se o main for iniciado diretamente por ele, ele inicia o programa pela def 'inicio'
    MenuPrincipal().inicio() 
    