import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Configuración de la conexión a la base de datos
def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='edi200316',
            database='cliente',
        )
        return conexion
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"No se pudo conectar a la base de datos: {e}")
        return None

# Función para guardar datos en la base de datos
def guardar_datos():
    if not all([cedula.get(), nombre.get(), apellido.get(), telefono.get(), direccion.get(), correo.get()]):
        messagebox.showerror('Error', 'Todos los campos son obligatorios')
        return

    conexion = conectar_bd()
    if conexion is None:
        return

    try:
        cursor = conexion.cursor()
        query = """
        INSERT INTO gestion_cliente (cedula, nombre, apellido, direccion, telefono, correo)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (cedula.get(), nombre.get(), apellido.get(), direccion.get(), telefono.get(), correo.get()))
        conexion.commit()
        messagebox.showinfo('Correcto', 'Datos guardados correctamente')
    except mysql.connector.Error as e:
        messagebox.showerror('Error', f'Error al guardar los datos en la base de datos: {e}')
    finally:
        cursor.close()
        conexion.close()

# Función para borrar datos del formulario
def borrar_datos():
    cedula.set('')
    nombre.set('')
    apellido.set('')
    direccion.set('')
    telefono.set('')
    correo.set('')
    messagebox.showinfo('Correcto', 'Datos borrados correctamente')

# Construir ventana
ventana = tk.Tk()
ventana.title('Sistema de registro de clientes')
ventana.geometry('400x300')

# Crear variables
cedula = tk.StringVar()
nombre = tk.StringVar()
apellido = tk.StringVar()
telefono = tk.StringVar()
direccion = tk.StringVar()
correo = tk.StringVar()

# Crear etiquetas
etiqueta_cedula = tk.Label(ventana, text='Cédula:')
etiqueta_nombre = tk.Label(ventana, text='Nombre:')
etiqueta_apellido = tk.Label(ventana, text='Apellido:')
etiqueta_telefono = tk.Label(ventana, text='Teléfono:')
etiqueta_direccion = tk.Label(ventana, text='Dirección:')
etiqueta_correo = tk.Label(ventana, text='Correo:')

# Crear entradas
entrada_cedula = tk.Entry(ventana, textvariable=cedula)
entrada_nombre = tk.Entry(ventana, textvariable=nombre)
entrada_apellido = tk.Entry(ventana, textvariable=apellido)
entrada_telefono = tk.Entry(ventana, textvariable=telefono)
entrada_direccion = tk.Entry(ventana, textvariable=direccion)
entrada_correo = tk.Entry(ventana, textvariable=correo)

# Crear botones
boton_guardar = tk.Button(ventana, text='Guardar', command=guardar_datos)
boton_borrar = tk.Button(ventana, text='Borrar', command=borrar_datos)

# Posicionar etiquetas
etiqueta_cedula.grid(row=0, column=0, padx=5, pady=5)
etiqueta_nombre.grid(row=1, column=0, padx=5, pady=5)
etiqueta_apellido.grid(row=2, column=0, padx=5, pady=5)
etiqueta_telefono.grid(row=3, column=0, padx=5, pady=5)
etiqueta_direccion.grid(row=4, column=0, padx=5, pady=5)
etiqueta_correo.grid(row=5, column=0, padx=5, pady=5)

# Posicionar entradas
entrada_cedula.grid(row=0, column=1, padx=5, pady=5)
entrada_nombre.grid(row=1, column=1, padx=5, pady=5)
entrada_apellido.grid(row=2, column=1, padx=5, pady=5)
entrada_telefono.grid(row=3, column=1, padx=5, pady=5)
entrada_direccion.grid(row=4, column=1, padx=5, pady=5)
entrada_correo.grid(row=5, column=1, padx=5, pady=5)

# Posicionar botones
boton_guardar.grid(row=6, column=0, columnspan=2, pady=10)
boton_borrar.grid(row=7, column=0, columnspan=2, pady=10)

# Ejecutar ventana principal
ventana.mainloop()


                              
                              
    


