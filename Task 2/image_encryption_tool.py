import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import numpy as np
import os

def encrypt_image(input_path, key):
    img = Image.open(input_path)
    arr = np.array(img)
    encrypted_arr = arr ^ key
    encrypted_img = Image.fromarray(encrypted_arr)
    output_path = "encrypted.png"
    encrypted_img.save(output_path)
    return output_path

def decrypt_image(input_path, key):
    img = Image.open(input_path)
    arr = np.array(img)
    decrypted_arr = arr ^ key
    decrypted_img = Image.fromarray(decrypted_arr)
    output_path = "decrypted.png"
    decrypted_img.save(output_path)
    return output_path

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    entry_path.delete(0, tk.END)
    entry_path.insert(0, file_path)

def encrypt_action():
    file_path = entry_path.get()
    key = int(entry_key.get())
    if not file_path or not os.path.exists(file_path):
        messagebox.showerror("Error", "Please select a valid image file")
        return
    output = encrypt_image(file_path, key)
    messagebox.showinfo("Success", f"Image Encrypted!\nSaved as {output}")

def decrypt_action():
    file_path = entry_path.get()
    key = int(entry_key.get())
    if not file_path or not os.path.exists(file_path):
        messagebox.showerror("Error", "Please select a valid image file")
        return
    output = decrypt_image(file_path, key)
    messagebox.showinfo("Success", f"Image Decrypted!\nSaved as {output}")


# -------- GUI --------
root = tk.Tk()
root.title("Image Encryption Tool")
root.geometry("400x250")

# File input
tk.Label(root, text="Select Image File:").pack(pady=5)
entry_path = tk.Entry(root, width=40)
entry_path.pack()
tk.Button(root, text="Browse", command=browse_file).pack(pady=5)

# Key input
tk.Label(root, text="Enter Secret Key (0-255):").pack(pady=5)
entry_key = tk.Entry(root, width=10)
entry_key.pack()

# Buttons
tk.Button(root, text="Encrypt Image", command=encrypt_action, bg="green", fg="white").pack(pady=10)
tk.Button(root, text="Decrypt Image", command=decrypt_action, bg="blue", fg="white").pack(pady=5)

root.mainloop()
