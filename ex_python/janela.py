import tkinter as tk

# Cria a janela principal
janela = tk.Tk()
janela.title("Minha Janela")
janela.geometry("300x200")  # Define o tamanho da janela

# Adiciona um rótulo
rotulo = tk.Label(janela, text="Olá, Mundo!")
rotulo.pack(pady=20)

# Adiciona um botão para fechar a janela
botao = tk.Button(janela, text="Fechar", command=janela.quit)
botao.pack(pady=10)

# Inicia o loop da aplicação
janela.mainloop()
