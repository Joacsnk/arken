from os import system as sy
from time import sleep as sl
class main():
    
    def inicio(self):
        self.limpar_terminal()
        self.selecao(self.interface())
    
    def limpar_terminal(self):
        sy("cls")
    
    def erro(self, tipo):
        self.limpar_terminal()
        sl(1)
        if tipo == 1:
            print("Erro 1. Opção inválida. Verifique se digitou corretamente.")
        elif tipo == 2:
            print("Erro 2. Tamanho inválido. O tamanho deve ser entre 4 e 20.")
        elif tipo == 3:
            print("Erro 3. Tamanho inválido. O tamanho deve ser um número.")
        elif tipo == 4:
            print("Erro 4. Tamanho inválido. O tamanho deve ser definido.")
        elif tipo == 5:
            print("Erro 5. Nenhum caractere foi selecionado.")
        sl(2)
        self.limpar_terminal()
  
    def tempo(self, tempo):
        sl(tempo)
    
    def interface(self):
        print("✦  — — — — — ARKEN— — — — —  ✦\n\n")
        print("[1] - Criar senha\n[2] - Sair\n")
        return str(input("Digite a opção desejada: "))
    
    def selecao(self, opcao):
        match opcao:
            case "1":
                self.limpar_terminal()
                self.tempo(0.7)
                from core.senha_generator import senha_generator
                senha_generator().inicio()
            case "2":
                self.limpar_terminal()
                exit()
            case _:
                self.erro(1)
                self.inicio()
                
            
    
if __name__ == "__main__":
    app = main()
    app.inicio()