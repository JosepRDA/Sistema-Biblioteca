import tkinter as tk
from tkinter import messagebox
from biblioteca import iniciarBiblioteca
from funcoes import validarUsuario

def iniciarLogin():
    loginWindow = tk.Tk()
    loginWindow.title("Login Biblioteca")
    loginWindow.geometry("250x250")

    tk.Label(loginWindow, text ="Usuario:").pack(pady=5)
    entradaUsuario= tk.Entry(loginWindow)
    entradaUsuario.pack(pady=5)

    tk.Label(loginWindow, text="Senha:").pack(pady=5)
    entradaSenha = tk.Entry(loginWindow, show="*")
    entradaSenha.pack(pady=5)

    def realizarLogin():
        usuario = entradaUsuario.get()
        senha = entradaSenha.get()
        if validarUsuario(usuario,senha):
            loginWindow.destroy()
            iniciarBiblioteca()
        else:
            messagebox.showerror("Erro","Usuario ou senha incorretos")
    tk.Button(loginWindow, text="Login", command=realizarLogin).pack(pady=20)
    loginWindow.mainloop()