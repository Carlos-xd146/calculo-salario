import customtkinter as ctk

from bancoDados import criar_banco, pegar_todos_pontos

janela = tela_atual = None

def tela_pontos():
    global tela_atual
    
    tela_atual = ctk.CTkFrame(janela)
    tela_atual.pack(fill="both", expand=True, padx= 10, pady=10)

    header = ctk.CTkFrame(tela_atual)
    header.pack(fill="x", pady=10)

    ctk.CTkLabel(
        header,
        text="Tabela de Horarios",
        font=("Arial", 24, "bold"),
    ).pack(side="left")

    # filtro = ctk.StringVar()

    # ctk.CTkEntry(
    #     tela_atual,
    #     textvariable=filtro,
    #     placeholder_text="🔍 Filtrar...",
    # ).pack(fill="x", pady=5)

    lista = ctk.CTkScrollableFrame(tela_atual)
    lista.pack(fill="both", expand=True)



    soma_total = ctk.CTkLabel(
        tela_atual,
        text= f"Soma total = {calcular_total()} min",
        font=("Arial", 20),
    ).pack(pady=12)

    

    for ponto in pegar_todos_pontos():
        card = ctk.CTkFrame(lista, corner_radius=10)
        card.pack(fill="x", padx=5, pady=5)

        ctk.CTkLabel(
            card,
            text=f"{ponto['_data']} - Horas {ponto['horas']} Hrs",
            font=("Arial", 12),
        ).pack(side="left", padx=10, pady=8)

        ctk.CTkButton(
            card,
            text="🗑 Excluir",
            width=100,
            command = lambda c=card: c.destroy()
        ).pack(side="right",padx=5, pady=5)
    


# def excluir_ponto():
   

def calcular_total():
    horario = 0

    for horas in pegar_todos_pontos():
        horario += (horas['horas'])*60

    return(horario)


def main():
    global janela
    janela = ctk.CTk()
    janela.title("Minha Janela")
    janela.geometry("800x600")
    criar_banco()
    tela_pontos()
    janela.mainloop() 

if __name__ == "__main__":
    main()






















