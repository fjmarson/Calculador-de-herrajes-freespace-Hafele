import tkinter as tk
from tkinter import messagebox

class CalculadoraHerrajes:
    def __init__(self):
        self.altura_peso_rangos = {
            225: {"B": (2.3, 4.3), "C": (3.8, 7.1), "D": (6.4, 9.3), "E": (9.2, 13.4), "F": (13.4, 19.1)},
            250: {"B": (1.9, 3.9), "C": (3.4, 6.4), "D": (5.8, 9.1), "E": (8.3, 12.6), "F": (12.1, 17.2)},
            275: {"B": (1.9, 3.5), "C": (3.1, 5.8), "D": (5.3, 8.2), "E": (7.5, 12.0), "F": (11.0, 15.6)},
            300: {"B": (1.7, 3.2), "C": (2.8, 5.3), "D": (4.8, 7.5), "E": (6.9, 10.0), "F": (10.1, 14.3)},
            325: {"B": (1.6, 3.0), "C": (2.6, 4.9), "D": (4.4, 7.0), "E": (6.4, 10.2), "F": (9.3, 13.2)},
            350: {"B": (1.5, 2.8), "C": (2.4, 4.6), "D": (4.1, 6.5), "E": (5.9, 9.5), "F": (8.6, 12.3)},
            375: {"B": (1.3, 2.6), "C": (2.2, 4.3), "D": (3.8, 6.0), "E": (5.5, 8.8), "F": (8.1, 11.4)},
            400: {"B": (1.2, 2.4), "C": (2.1, 4.0), "D": (3.6, 5.6), "E": (5.2, 8.3), "F": (7.6, 10.7)},
            425: {"B": (1.1, 2.3), "C": (2.0, 3.8), "D": (3.4, 5.3), "E": (4.9, 7.8), "F": (7.1, 10.1)},
            450: {"B": (1.0, 2.1), "C": (1.9, 3.5), "D": (3.2, 5.0), "E": (4.6, 7.3), "F": (6.7, 9.5)},
            475: {"B": (1.0, 2.0), "C": (1.8, 3.4), "D": (3.0, 4.7), "E": (4.3, 7.0), "F": (6.4, 9.0)},
            500: {"B": (0.9, 1.9), "C": (1.7, 3.2), "D": (2.9, 4.5), "E": (4.1, 6.6), "F": (6.0, 8.6)},
            525: {"B": (0.9, 1.8), "C": (1.6, 3.0), "D": (2.7, 4.3), "E": (3.9, 6.3), "F": (5.7, 8.2)},
            550: {"B": (0.8, 1.7), "C": (1.5, 2.9), "D": (2.6, 4.1), "E": (3.7, 6.0), "F": (5.5, 7.8)},
            570: {"B": (0.8, 1.7), "C": (1.4, 2.8), "D": (2.5, 3.9), "E": (3.6, 5.7), "F": (5.2, 7.4)},
            600: {"B": (0.8, 1.6), "C": (1.4, 2.7), "D": (2.4, 3.7), "E": (3.4, 5.7), "F": (5.0, 7.1)},
            625: {"B": (0.7, 1.5), "C": (1.3, 2.5), "D": (2.3, 3.6), "E": (3.3, 5.3), "F": (4.8, 6.8)},
            650: {"B": (0.7, 1.5), "C": (1.3, 2.4), "D": (2.2, 3.5), "E": (3.2, 5.1), "F": (4.6, 6.6)},
        }
        

    def calcular_peso_placa(self, altura, ancho):
        peso_placa = round(altura * ancho * 0.00001618, 2)
        return peso_placa

    def calcular_herraje_recomendado(self, altura, ancho):
        for rango_altura, herrajes in self.altura_peso_rangos.items():
            if altura <= rango_altura:
                peso_placa = self.calcular_peso_placa(altura, ancho)
                for herraje, rango_peso in herrajes.items():
                    if rango_peso[0] <= peso_placa <= rango_peso[1]:
                        return herraje

        return None

def calcular_click():
    try:
        altura = float(altura_entry.get())
        ancho = float(ancho_entry.get())

        calculadora = CalculadoraHerrajes()
        herraje_recomendado = calculadora.calcular_herraje_recomendado(altura, ancho)

        if herraje_recomendado:
            messagebox.showinfo("Resultado", f"El peso de la placa es: {calculadora.calcular_peso_placa(altura, ancho)} kg\n"
                                             f"Herraje recomendado: {herraje_recomendado}")
        else:
            messagebox.showinfo("Resultado", "No se encontró un herraje recomendado para las dimensiones proporcionadas.")
    except ValueError:
        messagebox.showerror("Error", "Ingresa un valor numérico válido para la altura y el ancho.")

# Crear la ventana
window = tk.Tk()
window.title("Cálculo de peso de placa y herraje recomendado")

# Establecer las dimensiones de la ventana
window.geometry("400x250")

# Etiqueta y entrada para la altura
altura_label = tk.Label(window, text="Altura (milímetros):")
altura_label.pack()
altura_entry = tk.Entry(window)
altura_entry.pack()

# Etiqueta y entrada para el ancho
ancho_label = tk.Label(window, text="Ancho (milímetros):")
ancho_label.pack()
ancho_entry = tk.Entry(window)
ancho_entry.pack()

# Botón de cálculo
calcular_button = tk.Button(window, text="Calcular", command=calcular_click)
calcular_button.pack()

# Ejecutar el bucle de eventos
window.mainloop()