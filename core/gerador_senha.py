from core.funcoes import FuncoesGerais # Importando funções gerais
class GeradorSenha(FuncoesGerais): 
    
    def __init__(self): # Init padrão
        pass 
    
    def inicio(self):  # Função principal para iniciar o arquivo completo
        self.opcao_interface(self.interface())  
        self.opcao_interface_mostrando_senha(self.interface_mostrando_senha())
        
    def interface(self):  # Interface gráfica que retorna a opção do usuário
        print("\n" + "═" * 60)
        print("●        ◦◦◦ NÍVEIS DE SENHA DISPONÍVEIS ◦◦◦        ●")
        print("═" * 60 + "\n")
        
        print("  [1] Nível 1  →  8 dígitos (números)")
        print("  [2] Nível 2  → 10 dígitos (letras minúsculas)")
        print("  [3] Nível 3  → 12 dígitos (letras minúsculas e maiúsculas)")
        print("  [4] Nível 4  → 16 dígitos (letras, números)")
        print("  [5] Nível 5  → 18 dígitos (letras, números, especiais)")
        print("  [6] Personalizar senha")
        print("  [7] Sair\n")
        
        return input("Digite a opção desejada ➤  ")
   
    ''' 
    Opções da interfaçe:
    
    - Todos os parâmetros do tempo do hacker descobrir é utilizando um  brute force como exemplo
    
    1 - 8 caracteres e somente número. É uma senha fraca e quase imediatamente consegue ser descoberta
    
    2 - 10 caracteres e somente letras minúsculas. Senha fraca também, porém demora cerga de 60 minutos de ser descoberta
    
    3 - 12 caracteres, maiúsculas e minúsculas. Senha forte, demoraria uns 300 anos
    
    4 - 16 caracteres, maiúsculas, minúsculas e números. Senha fortíssima, demoraria 37 bilhões de anos para ser descoberta
    
    5 - 18 caracteres, maiúsculas, minúsculas, números e símbolos. Opção mais forte não customizável. Demoraria aproximadamente 7.10 elevado a 48 ANOS. 
    
    6 - Irá para a opção personalizada, onde você poderá customizar o tamanho e suas fontes
    
    7 - Voltar para o menu inicial
    '''
    def opcao_interface(self, opcao): 
        match opcao: 
            case "1": 
                self.senha = self.gerador_senha(8, True, False, False, False) 
            case "2": 
                self.senha = self.gerador_senha(10, False, False, True, False)  
            case "3": 
                self.senha = self.gerador_senha(12, False, True, True, False)
            case "4": 
                self.senha = self.gerador_senha(16, True, True, True, False) 
            case "5":
                self.senha = self.gerador_senha(18, True, True, True, True) 
            case "6":
                self.senha_personalizada() 
            case "7": 
                self.limpar_terminal() 
                from main import MenuPrincipal 
                MenuPrincipal().inicio() 
            case _: 
                self.explicacao_erro(1) 
                self.inicio() 

    def interface_mostrando_senha(self):  # Interface para mostrar a senha gerada
        self.limpar_terminal()

        print("\n" + "═" * 50)
        print("           ● SENHA GERADA COM SUCESSO ●")
        print("═" * 50 + "\n")

        print(f"Senha ➤  {self.senha}\n")

        print("  [1] Copiar senha")
        print("  [2] Gerar nova senha")
        print("  [3] Sair\n")

        return input("Digite a opção desejada ➤  ")
 
    def opcao_interface_mostrando_senha(self, opcao): 
        match opcao: 
            case "1": # Copia senha e retorna para o menu de geração
                self.copiar_conteudo(self.senha) 
                self.titulo_visivel("Senha copiada com sucesso!", 0.7) 
                self.inicio() 
            case "2": # Volta para o menu de geração
                self.limpar_terminal() 
                self.inicio() 
            case "3": # Volta para o menu inicial de Main.py
                self.limpar_terminal() 
                from main import MenuPrincipal 
                MenuPrincipal().inicio()                
            case _: 
                self.explicacao_erro(1)  
                self.opcao_interface_mostrando_senha(self.interface_mostrando_senha()) 
        
    '''
    A senha personalizada é uma opção para uma senha mais específica, seja por causa do software ou do próprio usuário
    Você pode criar uma senha com letras maiúsculas, letras minúsculas, números e/ou símbolos, de 4 até 20 caracteres
    
    A função redefine assim que executada todas as variáveis, assim que executa
    Logo após entra num while onde vai criar a interface
    
    [1] Define o tamanho da senha. Dará erro se for menor que 4, maior que 20 ou não for um número inteiro
    [2] Liga / Desliga opção de números na senha
    [3] Liga / Desliga opção de letras maiúsculas na senha
    [4] Liga / Desliga opção de letras minúsculas na senha
    [5] Liga / Desliga opção de símbolos na senha
    
    Caso queira voltar, aperte [7]
    
    Se o tamanho da senha já foi definida e pelo menos uma das opções de caracteres está ligada, ele gerará a senha
    '''
    def senha_personalizada(self): 
        tamanho_senha = None 
        com_numero = False 
        com_letras_maiusculas = False 
        com_letras_minusculas = False  
        com_simbolos = False 
        while True: # Menu com funções de ligado ou desligado (True / False)
            self.limpar_terminal() 

            print("\n" + "═" * 58)
            print("         ● ◦◦◦ MENU DE PERSONALIZAÇÃO DE SENHA ◦◦◦ ●")
            print("═" * 58 + "\n")

            print(f"  [1] Tamanho da senha .............. ({tamanho_senha})")
            print(f"  [2] Incluir números ............... ({com_numero})")
            print(f"  [3] Letras maiúsculas ............. ({com_letras_maiusculas})")
            print(f"  [4] Letras minúsculas ............. ({com_letras_minusculas})")
            print(f"  [5] Caracteres especiais .......... ({com_simbolos})")
            print(f"  [6] Finalizar personalização")
            print(f"  [7] Voltar ao menu anterior\n")

            match str(input("Digite a opção desejada ➤  ")):

                case "1": # Verificação caso não for dígito ou fora do escopo
                    self.limpar_terminal() 
                    tamanho_senha = str(input("Digite o tamanho da senha ➤  ")).strip() 
                    tamanho_senha = self.verificar_tamanho_senha(tamanho_senha)
                case "2": 
                    com_numero = self.ligar_desligar_opcao(com_numero) 
                case "3": 
                    com_letras_maiusculas = self.ligar_desligar_opcao(com_letras_maiusculas) 
                case "4": 
                    com_letras_minusculas = self.ligar_desligar_opcao(com_letras_minusculas) 
                case "5": 
                    com_simbolos = self.ligar_desligar_opcao(com_simbolos) 
                case "6": # Verifica caso não tenha tamanho ou não tenha as fontes de caracteres
                    if tamanho_senha is None: 
                        self.explicacao_erro(4) 
                    elif not any([com_letras_maiusculas, com_letras_minusculas, com_simbolos, com_numero]):
                        self.explicacao_erro(5) 
                    else: 
                        self.limpar_terminal() 
                        self.tempo_espera(0.5)
                        self.senha = self.gerador_senha(tamanho_senha, com_numero, com_letras_maiusculas, com_letras_minusculas, com_simbolos) 
                        self.opcao_interface_mostrando_senha(self.interface_mostrando_senha()) 
                case "7": 
                    self.limpar_terminal()
                    self.inicio() 
                case _:
                    self.explicacao_erro(1) 

    def verificar_tamanho_senha(self, tamanho_senha): # Verifica se está no padrão de senhas comum
        if tamanho_senha.isdigit():
            tamanho_senha = int(tamanho_senha)
            if tamanho_senha >= 4 and tamanho_senha <= 20: 
                self.titulo_visivel(f'Tamanho de senha definida com sucesso!', 1.5)
            else:
                self.explicacao_erro(2) 
                tamanho_senha = None 
        else: 
            self.explicacao_erro(3) 
            tamanho_senha = None 
        return tamanho_senha
        
        
if __name__ == "__main__":
    GeradorSenha().inicio()