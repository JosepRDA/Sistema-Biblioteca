# biblioteca.py
import tkinter as tk
from funcoes import listarLivros, adicionarLivro, excluirLivro, exibirLivroDetalhes, alterarLivro

def iniciarBiblioteca():
    global bibliotecaWindow, frameConteudo
    bibliotecaWindow = tk.Tk()  # Corrigido aquibibli
    bibliotecaWindow.title("Biblioteca")

        # Definindo a janela para ocupar toda a tela, mas mantendo os controles
    largura = bibliotecaWindow.winfo_screenwidth()
    altura = bibliotecaWindow.winfo_screenheight()
    bibliotecaWindow.geometry(f"{largura}x{altura}")  # Define a geometria da janela

    # Menu Principal
    menuPrincipal = tk.Menu(bibliotecaWindow)

    # Menu Cadastro
    menuCadastro = tk.Menu(menuPrincipal, tearoff=0)
    menuCadastro.add_command(label="Cadastrar Livro", command=abrirCadastroLivro)
    menuPrincipal.add_cascade(label="Cadastro", menu=menuCadastro)

    # Menu de Listagem
    menuListagem = tk.Menu(menuPrincipal, tearoff=0)
    menuListagem.add_command(label="Listar Livros", command=exibirLivros)
    menuPrincipal.add_cascade(label="Listar", menu=menuListagem)

    bibliotecaWindow.config(menu=menuPrincipal)

    # Frame de Conteúdo principal
    frameConteudo = tk.Frame(bibliotecaWindow)
    frameConteudo.pack(fill="both", expand=True)

    exibirLivros()  # Exibe a lista de livros no início
    bibliotecaWindow.mainloop()

def exibirLivros():
    limparFrame()
    tk.Label(frameConteudo, text="Livros Cadastrados", font=("Arial", 16)).pack(pady=10)
    livros = listarLivros()

    if livros:  # Verifica se a lista de livros não está vazia
        for idx, livro in enumerate(livros):
            frameLivro = tk.Frame(frameConteudo)
            frameLivro.pack(fill="x", pady=5)

            # Label de livro
            tk.Label(frameLivro, text=livro['Título'], anchor="w").pack(side="left")

            # Botão de Exibir
            tk.Button(frameLivro, text="Exibir", command=lambda idx=idx: exibirLivroDetalhes(idx)).pack(side="right", padx=5)

            # Botão Excluir
            tk.Button(frameLivro, text="Excluir", command=lambda idx=idx: excluirLivro(idx, exibirLivros)).pack(side="right", padx=5)

            # Botão Alterar
            tk.Button(frameLivro, text="Alterar", command=lambda idx=idx: abrirAlterarLivro(idx)).pack(side="right", padx=5)
    else:
        tk.Label(frameConteudo, text="Nenhum livro cadastrado.").pack(pady=10)

# Demais funções permanecem inalteradas...

def abrirCadastroLivro():
    limparFrame()
    tk.Label(frameConteudo, text="Cadastro de Livro", font=("Arial", 16)).pack(pady=10)

    campos = [
        "Título", "Autor", "Editora", "Ano", "Gênero",
        "Idioma", "ISBN", "Páginas", "Formato", "Localização"
    ]

    entradas = {}  # Dicionário para armazenar as entradas
    for campo in campos:
        tk.Label(frameConteudo, text=f"{campo}:").pack(pady=5)
        entrada = tk.Entry(frameConteudo)
        entrada.pack(pady=5)
        entradas[campo] = entrada  # Armazena a entrada no dicionário

    def salvarLivro():
        dadosLivro = {campo: entradas[campo].get() for campo in campos}  # Recupera valores das entradas
        adicionarLivro(dadosLivro)
        exibirLivros()

    tk.Button(frameConteudo, text="Salvar Livro", command=salvarLivro, font=("Arial", 16)).pack(pady=10)


def abrirAlterarLivro(idx):
    limparFrame()
    tk.Label(frameConteudo, text="Alterar Livro", font=("Arial", 16)).pack(pady=10)

    # Recupera os dados do livro que será alterado
    livro = listarLivros()[idx]

    campos = [
        "Título", "Autor", "Editora", "Ano", "Gênero",
        "Idioma", "ISBN", "Páginas", "Formato", "Localização"
    ]

    entradas = {}  # Dicionário para armazenar as entradas
    for campo in campos:
        tk.Label(frameConteudo, text=f"{campo}:").pack(pady=5)
        entrada = tk.Entry(frameConteudo)
        entrada.pack(pady=5)
        entrada.insert(0, livro.get(campo, ""))  # Insere o valor atual do livro, se existir
        entradas[campo] = entrada  # Armazena a entrada no dicionário

    def salvarAlteracoes():
        novosDados = {campo: entradas[campo].get() for campo in campos}  # Recupera novos valores
        alterarLivro(idx, novosDados)
        exibirLivros()

    tk.Button(frameConteudo, text="Salvar Alterações", command=salvarAlteracoes, font=("Arial", 16)).pack(pady=10)

    
def salvarAlteracoes(idx, entradas):
    novosDados = {campo: entrada.get() for campo, entrada in entradas.items()}
    alterarLivro(idx, novosDados)
    exibirLivros()

def limparFrame():
    for widget in frameConteudo.winfo_children():
        widget.destroy()


