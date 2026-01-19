import tkinter as tk
from tkinter import simpledialog, messagebox

# ---------------- FUNCIONES ----------------
def division():
    a = simpledialog.askfloat("División", "Ingrese el numerador:")
    b = simpledialog.askfloat("División", "Ingrese el denominador:")
    if b == 0:
        messagebox.showerror("Error", "No se puede dividir entre cero")
    else:
        messagebox.showinfo("Resultado", f"Resultado: {a / b}")

def factorial():
    n = simpledialog.askinteger("Factorial", "Ingrese un número:")
    if n is None or n < 0:
        messagebox.showerror("Error", "Número inválido")
        return
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    messagebox.showinfo("Resultado", f"{n}! = {fact}")

def tabla():
    n = simpledialog.askinteger("Tabla", "Ingrese un número (1-10):")
    if n is None or not 1 <= n <= 10:
        messagebox.showerror("Error", "Número fuera de rango")
        return
    texto = ""
    for i in range(1, 11):
        texto += f"{n} x {i} = {n*i}\n"
    messagebox.showinfo("Tabla", texto)

def potencias():
    n = simpledialog.askfloat("Potencias", "Ingrese un número:")
    messagebox.showinfo("Resultado", f"Cuadrado: {n*2}\nCubo: {n*3}"
                            
# ---------------- Suma y producto -----------
def suma_numeros():
    n = simpledialog.askinteger("Suma", "¿Cuántos números desea sumar?")
    if not n or n <= 0:
        return
    total = 0
    for i in range(n):
        total += simpledialog.askfloat("Suma", f"Ingrese el número {i+1}:")
    messagebox.showinfo("Resultado", f"La suma es: {total}")

def producto_numeros():
    n = simpledialog.askinteger("Producto", "¿Cuántos números desea multiplicar?")
    if not n or n <= 0:
        return
    producto = 1
    for i in range(n):
        producto *= simpledialog.askfloat("Producto", f"Ingrese el número {i+1}:")
    messagebox.showinfo("Resultado", f"El producto es: {producto}")

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
