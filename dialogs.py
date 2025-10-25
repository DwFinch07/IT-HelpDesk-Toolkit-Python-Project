import customtkinter as ctk

def ask_password():
    dialog = ctk.CTkInputDialog(text="Root Password Is Required:", title="Root Password")
    return dialog.get_input()
