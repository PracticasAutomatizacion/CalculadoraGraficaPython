import tkinter as tk
from tkinter import simpledialog, messagebox

# ---------------- FUNCIONES ----------------



# ---------------- INTERFAZ ----------------

ventana = tk.Tk()
ventana.title("Calculadora Matemática")
ventana.geometry("420x520")
ventana.configure(bg="#f4f6f8")

# Título
tk.Label(
    ventana,
    text="Calculadora Matemática",
    font=("Segoe UI", 18, "bold"),
    bg="#f4f6f8",
    fg="#2c3e50"
).pack(pady=15)

frame = tk.Frame(ventana, bg="#f4f6f8")
frame.pack()

def crear_boton(texto, funcion, color):
    tk.Button(
        frame,
        text=texto,
        command=funcion,
        font=("Segoe UI", 11),
        width=28,
        bg=color,
        fg="white",
        activebackground="#34495e",
        relief="flat",
        pady=6
    ).pack(pady=4)

crear_boton("➕ Suma", suma_numeros, "#3498db")
crear_boton("✖ Producto", producto_numeros, "#9b59b6")
crear_boton("➗ División", division, "#1abc9c")
crear_boton("! Factorial", factorial, "#e67e22")
crear_boton("📊 TablaS de multiplicar", tabla, "#16a085")
crear_boton("⬛ Cuadrado y cubo", potencias, "#2ecc71")
crear_boton("📈 Promedio", promedio, "#f39c12")
crear_boton("🔼 Máximo y mínimo", max_min, "#e74c3c")

tk.Button(
    ventana,
    text="Salir",
    command=ventana.quit,
    font=("Segoe UI", 11, "bold"),
    width=20,
    bg="#34495e",
    fg="white",
    relief="flat",
    pady=6
).pack(pady=15)

ventana.mainloop()
