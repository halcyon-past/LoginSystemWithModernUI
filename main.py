import customtkinter as tk
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("localhost",9999))


tk.set_appearance_mode("System")
tk.set_default_color_theme("dark-blue")

root = tk.CTk()

root.geometry("500x350")

root.title("Login System")
root.resizable(False,False)

def login():
    message = client.recv(1024).decode()
    client.send(entry1.get().encode())
    message = client.recv(1024).decode()
    client.send(entry2.get().encode())
    message = client.recv(1024).decode()
    print(message)

frame = tk.CTkFrame(master=root)
frame.pack(pady=20,padx=60,fill="both",expand=True)
label = tk.CTkLabel(master=frame,text="Login System",font=("Arial",20,"bold"))
label.pack(pady=12,padx=10)

entry1 = tk.CTkEntry(master=frame,placeholder_text="Username")
entry1.pack(pady=12,padx=10)

entry2 = tk.CTkEntry(master=frame,placeholder_text="Password",show="*")
entry2.pack(pady=12,padx=10)

button = tk.CTkButton(master=frame,text="Login",command=login)
button.pack(pady=12,padx=10)

checkbox = tk.CTkCheckBox(master=frame,text="Remember me")
checkbox.pack(pady=12,padx=10)

root.mainloop()
