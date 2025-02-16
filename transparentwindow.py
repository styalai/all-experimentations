import tkinter as tk

def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    root.geometry(f"{width}x{height}+{x}+{y}")

root = tk.Tk()
root.overrideredirect(True)  # Supprime la barre de titre
root.attributes('-topmost', True)  # Garde la fenêtre au premier plan
center_window(root, 6, 6)  # Taille ajustée pour environ 10mm
root.configure(bg='#FFFFFF')  # Vert fluo

root.mainloop()
