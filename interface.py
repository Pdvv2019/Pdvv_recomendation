import pandas as pd
tabela_carregada = pd.read_hdf('similaridade_cosseno.h5', key='df')
linhas, colunas = tabela_carregada.shape
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk


# configuration for the interface
root = tk.Tk()
root.title("Games Recomendation")
root.iconbitmap("C:\\Users\\Phili\\OneDrive\\Imagens\\PngToIco\\prota.png\\prota.ico", )
root.geometry('526x376')
root.resizable(False,False)
imagem_fundo = Image.open("C:\\imagens\\renderizacao-3d-de-fundo-de-textura-hexagonal_23-2150796421.png")  
imagem_fundo = ImageTk.PhotoImage(imagem_fundo)
label_fundo = Label(root, image=imagem_fundo)
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)


def recomendar_jogos():
    nome_jogo = barra__de___pesquisa.get()
    if nome_jogo not in tabela_carregada.columns:
        recomendacoes_label.config(text=f"O jogo '{nome_jogo}' não foi encontrado.")
        return []

    recomendacoes = tabela_carregada[nome_jogo].sort_values(ascending=False).head(6).index.tolist()
    recomendacoes.remove(nome_jogo)
    
    


    recomendacoes_label.config(text=f'{recomendacoes}')
   




# create of widget (Title)

png_title = Image.open("C:\\imagens\\Enter your Game.png").resize((250,45),)
png_title = ImageTk.PhotoImage(png_title)
Ask = Label(root, image=png_title, bd=0)
Ask.pack( pady=20)

# create of widget (barra__de___pesquisa)
barra__de___pesquisa = Entry(root, width=21, font=("Arial",14), bg="gray", bd=2)
barra__de___pesquisa.pack(pady=0)


# create of widget (button)
search = Image.open("C:\\imagens\\transferir-removebg.png").resize((75,30))
search = ImageTk.PhotoImage(search)

find = Button(root, image=search, bd=0, command=recomendar_jogos )
find.pack(pady=5)

# create of widget (text)

recomendacoes_label = Label(root, text="", font=("Arial",14), wraplength=300, bg="gray")
recomendacoes_label.pack(pady=20)



root.mainloop()