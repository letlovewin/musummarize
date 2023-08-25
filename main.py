import os
import tkinter as tk
from tkinter import ttk,filedialog,messagebox

from PIL import Image
from pytesseract import pytesseract

window = tk.Tk()
window.title("MuSummarize")
window.minsize(500,280)

style = ttk.Style(window)
style.theme_use('alt')

image_path = None

def open_file():
    def analyze_text():
        if image_path!=None:
            img = Image.open(image_path)
          
            # Passing the image object to image_to_string() function
            # This function will extract the text from the image
            text = pytesseract.image_to_string(img)
              
            # Displaying the extracted text
            print(text[:-1])
        else:
            messagebox.showinfo("Analysis failed", "You need to insert an image!")
        
    file = filedialog.askopenfile(mode='r', filetypes=[('Image files', '*.png'),('Image files','*.jpg')])
    if file:
        filepath = os.path.abspath(file.name)
        analyze_button = tk.Button(text="Analyze Notes",command=analyze_text).pack()



info = tk.Label(text="Lightweight note summarization and management application.").pack()
button = tk.Button(text="Browse",command=open_file).pack()


window.mainloop()

