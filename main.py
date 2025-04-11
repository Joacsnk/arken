from os import system as sy
from time import sleep as sl
class main():
    
    def inicio(self):
        self.limpar_terminal()
        self.selecao(self.interface())
    
    def limpar_terminal(self):
        sy("cls")
    
    def opcao_inválida(self):
        self.limpar_terminal()
        sl(1)
        print("Erro 1. Opção inválida. Verifique se digitou corretamente.")
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
                self.opcao_inválida()
                self.inicio()
                
            
    
if __name__ == "__main__":
    app = main()
    app.inicio()