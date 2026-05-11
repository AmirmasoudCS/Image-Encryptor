import tkinter as tk
from tkinter import filedialog,messagebox
from cryptography.fernet import Fernet,InvalidToken
def encryptImage():
    path = filedialog.askopenfilename()
    if not path:
        return
    key = Fernet.generate_key()
    cipher = Fernet(key)
    with open(path,'rb') as f:
        data = f.read()
    encrypted = cipher.encrypt(data)
    savePath = filedialog.asksaveasfilename(defaultextension='.enc')
    if savePath:
        with open(savePath,'wb') as f:
            f.write(encrypted)
    keyEntry.delete(0,tk.END)
    keyEntry.insert(0,key.decode())
    messagebox.showinfo("Key Generated","Save this key to decrypt the image!")
def decryptImage():
    path = filedialog.askopenfilename()
    if not path:
        return
    key = keyEntry.get().encode()
    cipher = Fernet(key)
    with open(path,'rb') as f:
        encrypted = f.read()
    try :
        decrypted = cipher.decrypt(encrypted)
    except InvalidToken:
        messagebox.showerror("Error","Invalid key or file!")
        return
    savePath = filedialog.asksaveasfilename(defaultextension=".png")
    if savePath:
        with open(savePath,'wb') as f:
            f.write(decrypted)
    messagebox.showinfo("Done","Image decrypted!")
root = tk.Tk()
root.title("Image Encryptor")
tk.Label(root,text="Encryption Key").pack()
keyEntry = tk.Entry(root,width=50)
keyEntry.pack()
tk.Button(root,text="Encrypt (Generate Key)",command=encryptImage).pack(pady=10)
tk.Button(root,text="Decrypt",command = decryptImage).pack(pady=10)
root.mainloop()