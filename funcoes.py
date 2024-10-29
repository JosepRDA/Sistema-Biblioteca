from tkinter import messagebox

livros = []

def listarLivros() -> list:
    return livros

def adicionarLivro(livro) -> None:
    livros.append(livro)

def excluirLivro(idx, callback) -> None:
    if 0 <= idx <= len(livros):
        del livros[idx]
        callback()
    
def exibirLivroDetalhes(idx) -> None:
    if 0 <= idx <= len(livros):
        livro = livros[idx]
        detalhes = "\n".join(f"{campo} : {valor}" for campo, valor in livro.items())
        messagebox.showinfo("Detalhes do Livro", detalhes)

def validarUsuario(usuario, senha) -> bool:
    return usuario == "eu" and senha == "123"

def alterarLivro(idx, novosDados):
    if 0 <= idx < len(livros):
        livros[idx].update(novosDados)