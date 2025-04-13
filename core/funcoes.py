from os import system as sy #importando o sistema para acessar o terminal
from time import sleep as sl #importando o tempo para fazer uma espera
from pyperclip import copy #importando a biblioteca pyperclip para copiar o conteudo
from string import ascii_uppercase, digits, ascii_lowercase, punctuation #importando os caracteres que serão utilizados na senha
from secrets import choice #importando a biblioteca secrets para gerar senhas seguras
class FuncoesGerais(): #classe que contém as funções gerais do programa
    
    def __init__(self): #construtor da classe
        pass #inicializando o construtor da classe
    
    def limpar_terminal(self): #função que limpa o terminal
        sy("cls") #comando para limpar o terminal no windows
    
    def tempo_espera(self, tempo_espera):   #função que faz uma espera de x segundos
        sl(tempo_espera) #tempo de espera em segundos
        
    def explicacao_erro(self, tipo_erro): #função que explica o erro
        self.limpar_terminal() #limpa o terminal
        self.tempo_espera(0.5) #espera 0.5 segundos
        if tipo_erro == 1: #se o erro for 1
            print("Erro 1. Opção inválida. Verifique se digitou corretamente.") # Opção fora do escopo
        elif tipo_erro == 2:
            print("Erro 2. Tamanho inválido. O tamanho deve ser entre 4 e 20.") # Tamanho fora do escopo
        elif tipo_erro == 3:
            print("Erro 3. Tamanho inválido. O tamanho deve ser um número inteiro.") # Tamanho não é um número inteiro
        elif tipo_erro == 4:
            print("Erro 4. Tamanho inválido. O tamanho deve ser definido.") # Tamanho não definido
        elif tipo_erro == 5:
            print("Erro 5. Opcão inválida. Nenhum caractere foi selecionado.") # Nenhum caractere foi selecionado
        self.tempo_espera(2) #espera 2 segundos
        self.limpar_terminal() #limpa o terminal novamente
        
    def copiar_conteudo(self, conteudo): #função que copia o conteudo para a área de transferência
        copy(conteudo) #copia o conteudo para a área de transferência
        
    def titulo_visivel(self, titulo, tempo_espera): #função que mostra o titulo na tela
        self.limpar_terminal() #limpa o terminal
        print(titulo) #mostra o titulo na tela
        self.tempo_espera(tempo_espera) #espera o tempo definido
        self.limpar_terminal() #limpa o terminal novamente
        
    def ligar_desligar_opcao(self, opcao): #função que liga ou desliga uma opção
        if opcao == False: #se a opção estiver desligada
            opcao = True #liga a opção
        else: #se a opção estiver ligada
            opcao = False #desliga a opção
        return opcao #retorna o valor da opção
        
    def gerador_senha(self, tamanho_senha, com_numero, com_letras_maiusculas, com_letras_minusculas, com_simbolos): #função que gera a senha
        conteudo_fonte_senha = '' #variável que contém os caracteres que serão utilizados na senha
        if com_numero: #se a opção de números estiver ligada
            conteudo_fonte_senha += digits #adiciona números à variável
        if com_letras_maiusculas: #se a opção de letras maiúsculas estiver ligada
            conteudo_fonte_senha += ascii_uppercase #adiciona letras maiúsculas à variável
        if com_letras_minusculas: #se a opção de letras minúsculas estiver ligada
            conteudo_fonte_senha += ascii_lowercase #adiciona letras minúsculas à variável
        if com_simbolos: #se a opção de símbolos estiver ligada
            excluir_simbolos_problematicos = '''""#$&'(),/:;<>@[\]^`{|}~''' #definindo os símbolos que serão excluídos
            simbolos_filtrados = ''.join(i for i in punctuation if i not in excluir_simbolos_problematicos) #filtrando os símbolos
            conteudo_fonte_senha += simbolos_filtrados #adiciona os símbolos filtrados à variável
        senha = ''.join(choice(conteudo_fonte_senha) for _ in range(tamanho_senha)) #gerando a senha
        return senha #retorna a senha gerada