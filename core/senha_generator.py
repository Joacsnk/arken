from main import main
import string
from secrets import choice
from pyperclip import copy
class senha_generator(main):
    def __init__(self):
        pass
    
    def inicio(self):
        self.selecao(self.interface())  
        self.selecao_senha(self.mostrar_senha())
        
    def interface(self):
        print("● — — — — — ◦Níveis de senha◦ — — — — — ●\n\n")
        print("[1] - Nível 1 (8 digitos, com números)\n\n[2] - Nível 2 (10 digitos, com letras minúsculas)\n")
        print("[3] - Nível 3 (12 digitos, com letras minúsculas e maiúsculas)\n")
        print("[4] - Nível 4 (16 digitos, com letras minúsculas, maiúsculas e números)\n")
        print("[5] - Nível 5 (18 digitos, com letras minúsculas, maiúsculas, números e caracteres especiais)\n")
        print("[6] - Personalizar senha\n")
        print("[7] - Sair\n")
        return str(input("Digite a opção desejada: "))
    def selecao(self, opcao):
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
                print("Personalizar senha selecionado")
            case "7":
                self.limpar_terminal()
                self.tempo(0.7)
                self.inicio()
            case _:
                self.opcao_inválida()
                self.inicio()

    def mostrar_senha(self):
        self.limpar_terminal()
        self.tempo(0.7)
        print(f"Senha gerada: {self.senha}\n\n")
        print("[1] - Copiar senha\n[2] - Gerar nova senha\n[3] - Sair\n")
        return str(input("Digite a opção desejada: "))
    
    def selecao_senha(self, opcao):
        match opcao:
            case "1":
                copy(self.senha)
                self.limpar_terminal()
                print("Senha copiada com sucesso!")
                self.limpar_terminal()
                self.tempo(0.7)
                self.inicio()
            case "2":
                self.limpar_terminal()
                self.tempo(0.7)
                self.inicio()
            case "3":
                self.limpar_terminal()
                self.tempo(0.7)
                self.inicio()
            case _:
                self.opcao_invalida()
                self.mostrar_senha()
        

    def gerador_senha(self, tamanho, numero, Lmaiusculas, Lminusculas, simbolos):
        fonte_caracteres = ''
        if numero:
            fonte_caracteres += string.digits
        if Lmaiusculas:
            fonte_caracteres += string.ascii_uppercase
        if Lminusculas:
            fonte_caracteres += string.ascii_lowercase
        if simbolos:
            fonte_caracteres += string.punctuation
        senha = ''.join(choice(fonte_caracteres) for _ in range(tamanho))
        return senha