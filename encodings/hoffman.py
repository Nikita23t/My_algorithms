import tkinter as tk

def hoffman_encoding(string):
    base_string = string.lower()
    elems = {}
    sorted_elems = []
    k = 0
    
    for i in base_string:
        if i not in elems:
            for j in base_string:
                if j==i:
                    k+=1
            elems[i]= k
            k=0

    sorted_elems = sorted(elems.items(), key=lambda x: x[1],)
    
    while len(sorted_elems) > 1:
        left = sorted_elems[0]
        right = sorted_elems[1]

        node = (left[0], right[0]), (left[1] + right[1])
        sorted_elems = sorted_elems[2:]
        sorted_elems.append((node, node[1]))
        sorted_elems = sorted(sorted_elems, key=lambda x: x[1])

    codes = {}
    
    def build_codes(node, code=""):
        if isinstance(node, tuple):
            build_codes(node[0], code+"0")
            build_codes(node[1], code+"1")
        else:
            if node in elems:
                codes[node] = code
    
    build_codes(sorted_elems[0][0])
    
    encoded_string = ""
    for char in base_string:
        encoded_string += codes[char]
    
    return elems, codes, encoded_string

def display_result():
    string = input_box.get()
    elems, codes, encoded_string = hoffman_encoding(string)
    
    elems_listbox.delete(0, tk.END)
    for char, freq in elems.items():
        elems_listbox.insert(tk.END, f"{char}: {freq}")
    
    codes_listbox.delete(0, tk.END)
    for char, code in codes.items():
        codes_listbox.insert(tk.END, f"{char}: {code}")
    
    encoded_text.delete("1.0", tk.END)
    encoded_text.insert(tk.END, encoded_string)

window = tk.Tk()
window.title("Алгоритм Хаффмана")


input_box = tk.Entry(window, width=40) 
input_box.pack(side=tk.TOP)

clear_button = tk.Button(window, text="Очистить", command=lambda: input_box.delete(0, tk.END))
clear_button.pack(side=tk.BOTTOM)

encode_button = tk.Button(window, text="Закодировать", command=display_result)
encode_button.pack(side=tk.BOTTOM)

result_frame = tk.Frame(window)
result_frame.pack()

elems_frame = tk.Frame(result_frame)
elems_frame.pack(side=tk.LEFT)

elems_listbox = tk.Listbox(elems_frame, height=10)
elems_listbox.pack()

codes_frame = tk.Frame(result_frame)
codes_frame.pack(side=tk.LEFT)

codes_listbox = tk.Listbox(codes_frame, height=10)
codes_listbox.pack()

encoded_frame = tk.Frame(window, width=50)
encoded_frame.pack()

encoded_text = tk.Text(encoded_frame, height=10, width=40)
encoded_text.pack()

window.mainloop()
