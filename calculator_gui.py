import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import sympy as sp
import math
import cmath
import networkx as nx

# ── GUI Setup ──────────────────────────────────────────
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("650x750")
root.configure(bg="#1e1e1e")

# ── Styling ────────────────────────────────────────────
LABEL_STYLE = {"bg": "#1e1e1e", "fg": "white", "font": ("Arial", 11)}
ENTRY_STYLE = {"bg": "#2d2d2d", "fg": "white", "insertbackground": "white", "font": ("Arial", 11)}
BTN_STYLE   = {"bg": "#0078d7", "fg": "white", "font": ("Arial", 11, "bold"), "relief": "flat", "cursor": "hand2"}

# ── Input Fields ───────────────────────────────────────
tk.Label(root, text="Number 1:", **LABEL_STYLE).pack(pady=(15, 2))
num1_entry = tk.Entry(root, width=40, **ENTRY_STYLE)
num1_entry.pack()

tk.Label(root, text="Number 2 (if needed):", **LABEL_STYLE).pack(pady=(10, 2))
num2_entry = tk.Entry(root, width=40, **ENTRY_STYLE)
num2_entry.pack()

tk.Label(root, text="Set A (comma-separated, if needed):", **LABEL_STYLE).pack(pady=(10, 2))
setA_entry = tk.Entry(root, width=40, **ENTRY_STYLE)
setA_entry.pack()

tk.Label(root, text="Set B (comma-separated, if needed):", **LABEL_STYLE).pack(pady=(10, 2))
setB_entry = tk.Entry(root, width=40, **ENTRY_STYLE)
setB_entry.pack()

# ── Operation Dropdown ─────────────────────────────────
tk.Label(root, text="Select Operation:", **LABEL_STYLE).pack(pady=(10, 2))
operations = [
    "1  - Add",
    "2  - Subtract",
    "3  - Multiply",
    "4  - Divide",
    "5  - Power",
    "6  - Square Root",
    "7  - Logarithm (base 10)",
    "8  - Sin",
    "9  - Cos",
    "10 - Tan",
    "11 - Factorial",
    "12 - GCD",
    "13 - LCM",
    "14 - Prime Check",
    "15 - Prime Factors",
    "16 - Derivative",
    "17 - Integral",
    "18 - Set Union & Intersection",
    "19 - Complex Number",
    "20 - Graph Edges",
    "21 - Value of Pi",
    "22 - Show History",
    "23 - Clear Output",
]
selected_op = tk.StringVar()
dropdown = ttk.Combobox(root, values=operations, textvariable=selected_op,
                        width=38, font=("Arial", 11))
dropdown.pack()
dropdown.current(0)

# ── Output Area ────────────────────────────────────────
tk.Label(root, text="Output:", **LABEL_STYLE).pack(pady=(10, 2))
output_box = scrolledtext.ScrolledText(root, height=12, width=75,
                                       bg="#2d2d2d", fg="#00ff99",
                                       font=("Courier", 11), relief="flat")
output_box.pack(padx=10)

# ── History ────────────────────────────────────────────
history = []

# ── Helper ─────────────────────────────────────────────
def show(text):
    output_box.insert(tk.END, str(text) + "\n")
    output_box.see(tk.END)

def get_nums():
    n1 = num1_entry.get().strip()
    n2 = num2_entry.get().strip()
    return n1, n2

# ── Calculate ──────────────────────────────────────────
def calculate():
    choice = selected_op.get().split(" - ")[0].strip()
    n1, n2 = get_nums()

    try:
        # Basic operations that need two numbers
        if choice in ["1","2","3","4","5","12","13"]:
            num1, num2 = float(n1), float(n2)

        # Single number operations
        if choice in ["6","7","8","9","10","11","14","15"]:
            num1 = float(n1)

        if choice == "1":
            result = num1 + num2
            show(f"Addition: {num1} + {num2} = {result}")
            history.append(f"{num1} + {num2} = {result}")

        elif choice == "2":
            result = num1 - num2
            show(f"Subtraction: {num1} - {num2} = {result}")
            history.append(f"{num1} - {num2} = {result}")

        elif choice == "3":
            result = num1 * num2
            show(f"Multiplication: {num1} x {num2} = {result}")
            history.append(f"{num1} x {num2} = {result}")

        elif choice == "4":
            if num2 == 0:
                show("Error: Cannot divide by zero!")
            else:
                result = num1 / num2
                show(f"Division: {num1} / {num2} = {result}")
                history.append(f"{num1} / {num2} = {result}")

        elif choice == "5":
            result = math.pow(num1, num2)
            show(f"Power: {num1} ^ {num2} = {result}")
            history.append(f"{num1} ^ {num2} = {result}")

        elif choice == "6":
            result = math.sqrt(num1)
            show(f"Square Root of {num1} = {result}")
            history.append(f"sqrt({num1}) = {result}")

        elif choice == "7":
            result = math.log10(num1)
            show(f"Log10({num1}) = {result}")
            history.append(f"log10({num1}) = {result}")

        elif choice == "8":
            result = math.sin(math.radians(num1))
            show(f"Sin({num1}°) = {result}")
            history.append(f"sin({num1}) = {result}")

        elif choice == "9":
            result = math.cos(math.radians(num1))
            show(f"Cos({num1}°) = {result}")
            history.append(f"cos({num1}) = {result}")

        elif choice == "10":
            result = math.tan(math.radians(num1))
            show(f"Tan({num1}°) = {result}")
            history.append(f"tan({num1}) = {result}")

        elif choice == "11":
            result = math.factorial(int(num1))
            show(f"{int(num1)}! = {result}")
            history.append(f"{int(num1)}! = {result}")

        elif choice == "12":
            result = math.gcd(int(num1), int(num2))
            show(f"GCD({int(num1)}, {int(num2)}) = {result}")
            history.append(f"GCD = {result}")

        elif choice == "13":
            result = math.lcm(int(num1), int(num2))
            show(f"LCM({int(num1)}, {int(num2)}) = {result}")
            history.append(f"LCM = {result}")

        elif choice == "14":
            result = sp.isprime(int(num1))
            show(f"{int(num1)} is {'prime' if result else 'not prime'}")
            history.append(f"Prime check {int(num1)}: {result}")

        elif choice == "15":
            result = sp.factorint(int(num1))
            show(f"Prime factors of {int(num1)}: {result}")
            history.append(f"Factors of {int(num1)}: {result}")

        elif choice == "16":
            x = sp.Symbol('x')
            expr = sp.sympify(n1)
            result = sp.diff(expr, x)
            show(f"Derivative of {expr} = {result}")
            history.append(f"d/dx({expr}) = {result}")

        elif choice == "17":
            x = sp.Symbol('x')
            expr = sp.sympify(n1)
            result = sp.integrate(expr, x)
            show(f"Integral of {expr} = {result} + C")
            history.append(f"∫({expr})dx = {result}")

        elif choice == "18":
            a_raw = setA_entry.get().strip().strip('()')
            b_raw = setB_entry.get().strip().strip('()')
            A = sp.FiniteSet(*[sp.Integer(x.strip()) for x in a_raw.split(',')])
            B = sp.FiniteSet(*[sp.Integer(x.strip()) for x in b_raw.split(',')])
            show(f"Union: {sp.Union(A, B)}")
            show(f"Intersection: {sp.Intersection(A, B)}")
            history.append(f"Union={sp.Union(A,B)}, Intersection={sp.Intersection(A,B)}")

        elif choice == "19":
            cn = complex(float(n1), float(n2))
            show(f"Complex: {cn}")
            show(f"Magnitude: {abs(cn)}")
            show(f"Phase: {cmath.phase(cn)}")
            history.append(f"Complex {cn}")

        elif choice == "20":
            G = nx.Graph()
            G.add_edge(n1, n2)
            show(f"Graph edges: {list(G.edges())}")
            history.append(f"Graph edges: {list(G.edges())}")

        elif choice == "21":
            show(f"Value of Pi = {math.pi}")

        elif choice == "22":
            if not history:
                show("No history yet.")
            else:
                show("── History ──")
                for item in history:
                    show(item)

        elif choice == "23":
            output_box.delete("1.0", tk.END)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# ── Buttons ────────────────────────────────────────────
btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=15)

tk.Button(btn_frame, text="  Calculate  ", command=calculate,
          **BTN_STYLE).grid(row=0, column=0, padx=10)

tk.Button(btn_frame, text="  Clear  ",
          command=lambda: output_box.delete("1.0", tk.END),
          bg="#d9534f", fg="white", font=("Arial", 11, "bold"),
          relief="flat", cursor="hand2").grid(row=0, column=1, padx=10)

# ── Run ────────────────────────────────────────────────
root.mainloop()


