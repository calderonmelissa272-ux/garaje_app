import tkinter as tk
from tkinter import messagebox
from modelos.vehiculo import Vehiculo
from servicios.garaje_servicio import GarajeServicio

class AppTkinter:

    def __init__(self, root):
        self.root = root
        self.root.title("Garaje App")

        self.servicio = GarajeServicio()

        tk.Label(root, text="Placa").grid(row=0, column=0)
        tk.Label(root, text="Marca").grid(row=1, column=0)
        tk.Label(root, text="Modelo").grid(row=2, column=0)

        self.entry_placa = tk.Entry(root)
        self.entry_marca = tk.Entry(root)
        self.entry_modelo = tk.Entry(root)

        self.entry_placa.grid(row=0, column=1)
        self.entry_marca.grid(row=1, column=1)
        self.entry_modelo.grid(row=2, column=1)

        btn_agregar = tk.Button(root, text="Agregar Vehículo", command=self.agregar_vehiculo)
        btn_agregar.grid(row=3, column=0, columnspan=2)

        self.lista = tk.Listbox(root, width=40)
        self.lista.grid(row=4, column=0, columnspan=2)

    def agregar_vehiculo(self):

        placa = self.entry_placa.get()
        marca = self.entry_marca.get()
        modelo = self.entry_modelo.get()

        if placa == "" or marca == "" or modelo == "":
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        vehiculo = Vehiculo(placa, marca, modelo)
        self.servicio.agregar_vehiculo(vehiculo)

        self.actualizar_lista()

        self.entry_placa.delete(0, tk.END)
        self.entry_marca.delete(0, tk.END)
        self.entry_modelo.delete(0, tk.END)

    def actualizar_lista(self):

        self.lista.delete(0, tk.END)

        for v in self.servicio.listar_vehiculos():
            self.lista.insert(tk.END, str(v))
