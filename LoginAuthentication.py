import tkinter as tk
from tkinter import messagebox

# Simulated user database
user_database = {
    "user1": "password1",
    "user2": "password2",
    # Add more users and passwords
}

class AuthenticationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Authentication App")

        self.label_username = tk.Label(root, text="Username")
        self.label_password = tk.Label(root, text="Password")

        self.entry_username = tk.Entry(root)
        self.entry_password = tk.Entry(root, show="*")

        self.label_username.pack()
        self.entry_username.pack()
        self.label_password.pack()
        self.entry_password.pack()

        self.login_button = tk.Button(root, text="Login", command=self.authenticate)
        self.login_button.pack()

    def authenticate(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username in user_database and user_database[username] == password:
            messagebox.showinfo("Success", "Login successful!")
        else:
            messagebox.showerror("Error", "Invalid username or password")

if __name__ == "__main__":
    root = tk.Tk()
    app = AuthenticationApp(root)
    root.mainloop()
