import fitz  # PyMuPDF
import json
import os
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
from io import StringIO
from sympy import sympify, SympifyError
import tkinter as tk
from tkinter import filedialog, messagebox

def pdf_to_text_with_math(pdf_path):
    output_string = StringIO()
    with open(pdf_path, 'rb') as f:
        extract_text_to_fp(f, output_string, laparams=LAParams())
    return output_string.getvalue()

def is_likely_math_expression(line):
    math_symbols = {'+', '-', '*', '/', '=', '(', ')', '[', ']', '{', '}', '^', '_'}
    return any(symbol in line for symbol in math_symbols)

def parse_math_expressions(text):
    expressions = []
    lines = text.split('\n')
    for line in lines:
        if is_likely_math_expression(line):
            try:
                expr = sympify(line)
                expressions.append(expr)
            except (SympifyError, SyntaxError):
                continue
    return expressions

def save_text_to_json(text, expressions, json_path):
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    data = {
        "text": text,
        "expressions": [str(expr) for expr in expressions]
    }
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        try:
            text = pdf_to_text_with_math(file_path)
            expressions = parse_math_expressions(text)
            json_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
            if json_path:
                save_text_to_json(text, expressions, json_path)
                messagebox.showinfo("Success", f"File processed and saved to {json_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("PDF to Text and Math Expressions")
root.geometry("400x200")

# Create and place the upload button
upload_button = tk.Button(root, text="Upload PDF", command=upload_file, width=20, height=2)
upload_button.pack(pady=50)

# Run the Tkinter event loop
root.mainloop()
    