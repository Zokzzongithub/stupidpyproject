import tkinter as tk
from tkinter import messagebox
import random
import json
import os

saved_file = "saved_passwords.json"
if not os.path.exists(saved_file):
    with open(saved_file, 'w') as f:
        json.dump([], f)

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.length_var = tk.IntVar(value=8)
        self.password_var = tk.StringVar()
        self.spec_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Choose password length (1-25):").pack(pady=5)
        tk.Spinbox(self.root, from_=1, to=25, textvariable=self.length_var, width=5).pack(pady=5)
        tk.Button(self.root, text="Generate Password", command=self.generate_password).pack(pady=5)
        tk.Entry(self.root, textvariable=self.password_var, font=("Helvetica", 14), width=30, state='readonly').pack(pady=5)
        tk.Label(self.root, text="Specification (e.g., email, social media, etc.):").pack(pady=5)
        tk.Entry(self.root, textvariable=self.spec_var, width=30).pack(pady=5)
        tk.Button(self.root, text="Save Password", command=self.save_password).pack(pady=5)

    def generate_password(self):
        length = self.length_var.get()
        if not (1 <= length <= 25):
            messagebox.showerror("Error", "Please choose a number between 1 and 25.")
            return
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_var.set(password)

    def save_password(self):
        password = self.password_var.get()
        specification = self.spec_var.get()
        if not password:
            messagebox.showerror("Error", "No password to save.")
            return
        if not specification:
            messagebox.showerror("Error", "Please specify what the password is for.")
            return
        with open(saved_file, 'r') as f:
            saved_passwords = json.load(f)
        saved_passwords.append({"password": password, "specification": specification})
        with open(saved_file, 'w') as f:
            json.dump(saved_passwords, f)
        messagebox.showinfo("Success", "Password saved successfully.")
        self.password_var.set("")
        self.spec_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
