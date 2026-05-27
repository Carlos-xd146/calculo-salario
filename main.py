import customtkinter as ctk

from bancoDados import criar_banco




funcionario = ctk.CTkLabel(janela, text="Funcionario: Carlos Eduardo")
funcionario.pack(pady=10)

def tela_pontos():



# def excluir_ponto():

# def calcular_total():

def main():
    
    janela = ctk.CTk()
    janela.title("Minha Janela")
    janela.geometry("400x300")
    criar_banco()
    janela.mainloop()


if __name__ == "__main__":
    main()






















