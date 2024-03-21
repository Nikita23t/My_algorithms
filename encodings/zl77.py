import tkinter as tk
from tkinter import ttk


def lz77_encode():
    data = text1.get("1.0", "end").rstrip()  
    dictionary = ""
    code = []
    i = 0
    while i < len(data):
        length, offset = 0, 0
        for j in range(i):
            substring = data[i:i + j + 1]
            k = dictionary.rfind(substring)
            if k != -1 and i + k < len(data):
                length = j + 1
                offset = i - k
        code.append((offset, length, data[i + length]))
        dictionary += data[i:i + length + 1]
        i += length + 1
    result.insert('end', code)


def clean():
    text1.delete("1.0", "end")
    result.delete("1.0", "end")
    
win = tk.Tk()
win.title("Алгоритм LZ77")
win.geometry("420x330")


text1=tk.Text(win)
text1.place(x=10, y=30, width=400, height=100)

result=tk.Text(win)
result.place(x=10, y=220, width=400, height=100)

button = ttk.Button(win, text='Закодировать', command=lz77_encode)
button.place(x=100, y=150)

button_clean = ttk.Button(win, text='Очистить', command=clean)
button_clean.place(x=200, y=150)

win.mainloop()