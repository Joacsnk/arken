from os import system as sy # limpar terminal
from time import sleep as sl # delay intencional
from pyperclip import copy # Copiar conteúdo
from string import ascii_uppercase, digits, ascii_lowercase, punctuation # Conjunto de strings para o gerador de senhas
from secrets import choice # Escolha aleatória de caracteres para o gerador
class FuncoesGerais(): 
    ''' 
    FuncoesGerais serve especificamente para auxiliar outros arquivos com funções gerais e que irão usar.
    Para facilitar, juntei todas as funções que serão (ou possivelmente) reutilizáveis. Facilita na hora de 
    limpar um terminal ou explicar um erro
    '''
    
    def __init__(self): 
        pass 
    
    def limpar_terminal(self): # Limpa o terminal
        sy("cls") 
    
    def tempo_espera(self, tempo_espera): # Delay intencional, seja para dar tempo de ler algum conteúdo ou perfomance
        sl(tempo_espera) # Utiliza o tempo como parâmetro em segundos para definir o delay
        
    def explicacao_erro(self, tipo_erro): 
        ''' 
        Erros evitáveis e simples o suficiente para serem identificados e notificados para o usuário. 
        Divido em: Nº do erro; Resumo; Correção rápida. Ex: Erro 585. Usuário não encontrado. Busque um usuário válido 
        Utiliza como parâmetro o número do erro para seleciona-lo
        '''
        self.limpar_terminal() 
        self.tempo_espera(0.5) 
        if tipo_erro == 1: 
            print("Erro 1. Opção inválida. Verifique se digitou corretamente.") # Opção fora de escopo
        elif tipo_erro == 2:
            print("Erro 2. Tamanho da senha inválida. O tamanho deve ser entre 4 e 20.") # Tamanho mínimo ou máximo ultrapassado
        elif tipo_erro == 3:
            print("Erro 3. Tamanho inválido. O tamanho deve ser um número inteiro.") # Float não suportado
        elif tipo_erro == 4:
            print("Erro 4. Tamanho inválido. O tamanho deve ser definido.") # Tamanho não definido. Óbvio
        elif tipo_erro == 5:
            print("Erro 5. Opcão inválida. Nenhum caractere foi selecionado.")  # Sem strings para a alimentação da senha
        elif tipo_erro == 6:
            print("Erro 6. Seleção inválida. Nome inexistente.")  # Nome não encontrado nesse conjunto
        elif tipo_erro == 7:
            print("Erro 7. Seleção inválida. Nome já existente.") # Nome já existente em um conjunto
        elif tipo_erro == 8:
            print("Erro 8. Senhas diferentes. Repita a senha para confirmar") # Senha 1 diferente da Senha 2
        elif tipo_erro == 9:
            print("Erro 9. Senha incorreta. Digite a senha corretamente")
        self.tempo_espera(2) 
        self.limpar_terminal() 
        
    def copiar_conteudo(self, conteudo): # Copia o conteúdo para a área de transferência
        copy(conteudo) 
        
    def titulo_visivel(self, titulo, tempo_espera): # Título simples, como "senha adicionada" ou "backup feito com êxito"
        self.limpar_terminal() 
        print(titulo) 
        self.tempo_espera(tempo_espera) # tempo de delay como parâmetro
        self.limpar_terminal() 
        
    def ligar_desligar_opcao(self, opcao): # Transformar a variável em True ou False, como um ligado/desligado. 
        if opcao == False: # Utiliza a própria variável como parâmetro
            opcao = True 
        else: 
            opcao = False 
        return opcao 
        
    def gerador_senha(self, tamanho_senha, com_numero, com_letras_maiusculas, com_letras_minusculas, com_simbolos): 
        ''' 
        Def específico para gerar senhas de acordo com seus parâmetros
        PARÂMETROS:
        
        'Tamanho_senha' = Quantidade de caracteres da senha né. ex: 'senha123' tem 8 caracteres, sendo assim seu tamanho
        'com_numero' = Caso verdadeiro, adiciona números à senha
        'com_letras_maiusculas' = Caso verdadeiro, adiciona letras maiúsculas
        'com_letras_minusculas' = Caso verdadeiro, adiciona letras minúsculas
        'com_simbolos' = Caso verdadeiro, adiciona símbolos (não problemáticos, já explico)
        
        Ele funcioada da seguinte forma: 
        
        - Cria uma variável para auxiliar chamada 'conteudo_fonte_senha'. Ela guardará os caracteres que serão usados para a criação da senha
        
        - Verifica cada parâmetro. Caso verdadeiro, ele adiciona no 'conteudo_fonte_senha'
        
        - Caso o parâmetro 'com_simbolos' seja verdadeiro, primeiro ele seleciona todos os símbolos que podem ocasionar problemas na hora de registrar com senha. Ex: '#' é muito usada para comments em algumas linguagens. Depois ele junta todos os símbolos na 'simbolos_filtrados' EXCETO as que estão na variável 'excluir_simbolos_problematicos' por meio da iteração
        
        - 'senha' vai receber, aleatoriamente, o número de caracteres da lista de 'conteudo_fonte_senha' de acordo com o 'tamanho_senha'
        
        '''
        conteudo_fonte_senha = '' 
        if com_numero: 
            conteudo_fonte_senha += digits 
        if com_letras_maiusculas: 
            conteudo_fonte_senha += ascii_uppercase 
        if com_letras_minusculas: 
            conteudo_fonte_senha += ascii_lowercase 
        if com_simbolos: 
            excluir_simbolos_problematicos = '''""#$&'(),/:;<>@[\]^`{|}~''' 
            simbolos_filtrados = ''.join(i for i in punctuation if i not in excluir_simbolos_problematicos)
            conteudo_fonte_senha += simbolos_filtrados 
        senha = ''.join(choice(conteudo_fonte_senha) for _ in range(tamanho_senha))
        return senha 