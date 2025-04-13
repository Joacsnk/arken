from core.funcoes import FuncoesGerais # Importando a classe FuncoesGerais do módulo funcoes.py
class GeradorSenha(FuncoesGerais): # Herança da classe FuncoesGerais
    def __init__(self): # Inicializando a classe GeradorSenha
        pass # Método construtor
    
    def inicio(self): # Método de início
        self.opcao_interface(self.interface()) # Chamando a interface inicial 
        self.opcao_interface_mostrando_senha(self.interface_mostrando_senha()) # Chamando a interface mostrando a senha gerada
        
    def interface(self): # Método da interface inicial
        print("● — — — — — ◦Níveis de senha◦ — — — — — ●\n\n") # Título do programa
        # Opções do menu:
        print("[1] - Nível 1 (8 digitos, com números)\n\n[2] - Nível 2 (10 digitos, com letras minúsculas)\n") 
        print("[3] - Nível 3 (12 digitos, com letras minúsculas e maiúsculas)\n")
        print("[4] - Nível 4 (16 digitos, com letras minúsculas, maiúsculas e números)\n")
        print("[5] - Nível 5 (18 digitos, com letras minúsculas, maiúsculas, números e caracteres especiais)\n")
        print("[6] - Personalizar senha\n") # Opção de personalização
        print("[7] - Sair\n") # Opção de sair
        return str(input("Digite a opção desejada: ")) # Retorna a opção escolhida pelo usuário
    
    def opcao_interface(self, opcao): # Método para tratar a opção escolhida
        match opcao: # Usando o match para tratar a opção escolhida
            case "1": # Caso opção 1
                self.senha = self.gerador_senha(8, True, False, False, False) # Gerando senha de 8 digitos com números
            case "2": # Caso opção 2
                self.senha = self.gerador_senha(10, False, False, True, False) # Gerando senha de 10 digitos com letras minúsculas
            case "3": # Caso opção 3
                self.senha = self.gerador_senha(12, False, True, True, False) # Gerando senha de 12 digitos com letras minúsculas e maiúsculas
            case "4": # Caso opção 4
                self.senha = self.gerador_senha(16, True, True, True, False) # Gerando senha de 16 digitos com letras minúsculas, maiúsculas e números
            case "5": # Caso opção 5
                self.senha = self.gerador_senha(18, True, True, True, True) # Gerando senha de 18 digitos com letras minúsculas, maiúsculas, números e caracteres especiais
            case "6": # Caso opção 6
                self.tamanho_senha = None # Inicializando a variável tamanho_senha
                self.com_numero = False # Inicializando a variável com_numero
                self.com_letras_maiusculas = False # Inicializando a variável com_letras_maiusculas
                self.com_letras_minusculas = False  # Inicializando a variável com_letras_minusculas
                self.com_simbolos = False # Inicializando a variável com_simbolos
                self.senha_personalizada() # Chamando a função de personalização
            case "7": # Caso opção 7
                self.limpar_terminal() # Limpando o terminal
                from main import MenuPrincipal # Importando a classe MenuPrincipal
                MenuPrincipal().inicio() # Chamando o método de início da classe MenuPrincipal
            case _: # Caso opção inválida
                self.explicacao_erro(1) # Chamando o método de erro
                self.inicio() # Chamando o método de início novamente

    def interface_mostrando_senha(self): # Método da interface mostrando a senha gerada
        self.limpar_terminal() # Limpando o terminal
        self.tempo_espera(0.5)  # Espera 0.5 segundos
        print(f"Senha gerada: {self.senha}\n\n") # Mostrando a senha gerada
        print("[1] - Copiar senha\n[2] - Gerar nova senha\n[3] - Sair\n") # Opções do menu
        return str(input("Digite a opção desejada: ")) # Retorna a opção escolhida pelo usuário
    
    def opcao_interface_mostrando_senha(self, opcao): # Método para tratar a opção escolhida
        match opcao: # Usando o match para tratar a opção escolhida
            case "1": # Caso opção 1
                self.copiar_conteudo(self.senha) # Copiando a senha para a área de transferência
                self.titulo_visivel("Senha copiada com sucesso!", 0.7) # Mostrando mensagem de sucesso
                self.inicio() # Chamando o método de início novamente
            case "2": # Caso opção 2
                self.limpar_terminal() # Limpando o terminal
                self.inicio() # Chamando o método de início novamente
            case "3": # Caso opção 3
                self.limpar_terminal() # Limpando o terminal
                from main import MenuPrincipal # Importando a classe MenuPrincipal
                MenuPrincipal().inicio() # Chamando o método de início da classe MenuPrincipal                
            case _: # Caso opção inválida
                self.explicacao_erro(1) # Chamando o método de erro 
                self.opcao_interface_mostrando_senha(self.interface_mostrando_senha()) # Chamando a função de interface mostrando a senha gerada novamente
        
    def senha_personalizada(self): # Método de personalização da senha
        self.limpar_terminal() # Limpando o terminal
        print("● — — — — — ◦Personalização◦ — — — — — ●\n\n") # Título do programa
        # Opções do menu:
        print(f"[1] - Tamanho da senha ({self.tamanho_senha})\n\n[2] - Números ({self.com_numero})\n") #Tamanho da senha e números
        print(f"[3] - Letras maiúsculas ({self.com_letras_maiusculas})\n\n[4] - Letras minúsculas ({self.com_letras_minusculas})\n") # Letras maiúsculas e minúsculas
        print(f"[5] - Caracteres especiais ({self.com_simbolos})\n\n[6] - Finalizar\n\n[7] - Voltar\n") # Caracteres especiais, finalizar e voltar
        match str(input("Digite a opção desejada: ")): # Retorna a opção escolhida pelo usuário
            case "1": # Caso opção 1
                self.limpar_terminal() # Limpando o terminal
                self.tamanho_senha = str(input("Digite o tamanho da senha: ")).strip() # Pedindo o tamanho da senha
                if self.tamanho_senha.isdigit(): # Verificando se o tamanho da senha é um número
                    self.tamanho_senha = int(self.tamanho_senha) # Convertendo o tamanho da senha para inteiro
                    if self.tamanho_senha < 4 or self.tamanho_senha > 20: # Verificando se o tamanho da senha está dentro do escopo
                        self.explicacao_erro(2) # Chamando o método de erro
                        self.tamanho_senha = None # Inicializando a variável tamanho_senha
                        self.senha_personalizada() # Chamando a função de personalização novamente
                    else: # Se o tamanho da senha estiver dentro do escopo
                        self.senha_personalizada() # Chamando a função de personalização novamente
                else: # Se o tamanho da senha não for um número
                    self.explicacao_erro(3) # Chamando o método de erro
                    self.tamanho_senha = None # Inicializando a variável tamanho_senha
                    self.senha_personalizada() # Chamando a função de personalização novamente
            case "2": # Caso opção 2
                self.com_numero = self.ligar_desligar_opcao(self.com_numero) # Ligando ou desligando a opção de números
                self.senha_personalizada() # Chamando a função de personalização novamente
            case "3": # Caso opção 3
                self.com_letras_maiusculas = self.ligar_desligar_opcao(self.com_letras_maiusculas) # Ligando ou desligando a opção de letras maiúsculas
                self.senha_personalizada() # Chamando a função de personalização novamente
            case "4": # Caso opção 4
                self.com_letras_minusculas = self.ligar_desligar_opcao(self.com_letras_minusculas) # Ligando ou desligando a opção de letras minúsculas
                self.senha_personalizada() # Chamando a função de personalização novamente
            case "5": # Caso opção 5
                self.com_simbolos = self.ligar_desligar_opcao(self.com_simbolos) # Ligando ou desligando a opção de caracteres especiais
                self.senha_personalizada() # Chamando a função de personalização novamente
            case "6": # Caso opção 6
                if self.tamanho_senha is None: # Verificando se o tamanho da senha foi definido
                    self.explicacao_erro(4) # Chamando o método de erro
                    self.senha_personalizada() # Chamando a função de personalização novamente
                elif self.com_letras_maiusculas == False and self.com_letras_minusculas == False and self.com_simbolos == False: # Verificando se nenhuma opção foi selecionada
                    self.explicacao_erro(5) # Chamando o método de erro
                    self.senha_personalizada() # Chamando a função de personalização novamente
                else: # Se todas as opções foram selecionadas
                    self.limpar_terminal() # Limpando o terminal
                    self.tempo_espera(0.5) # Espera 0.5 segundos
                    self.senha = self.gerador_senha(self.tamanho_senha, self.com_numero, self.com_letras_maiusculas, self.com_letras_minusculas, self.com_simbolos) # Gerando a senha personalizada
                    self.opcao_interface_mostrando_senha(self.interface_mostrando_senha()) # Chamando a função de interface mostrando a senha personalizada
            case "7": # Caso opção 7
                self.limpar_terminal() # Limpando o terminal
                self.inicio() # Chamando o método de início novamente
            case _:
                self.explicacao_erro(1) # Chamando o método de erro
                self.senha_personalizada()  # Chamando a função de personalização novamente       