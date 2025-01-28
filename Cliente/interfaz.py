import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

# Función para conectar a la base de datos
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

# Función para guardar datos en la BD
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

# Función para borrar datos de la BD
def borrar_datos():
    if not cedula.get():
        messagebox.showerror('Error', 'La cédula es obligatoria para eliminar un registro')
        return
    conexion = conectar_bd()
    if conexion is None:
        return
    try:
        cursor = conexion.cursor()
        query = "DELETE FROM gestion_cliente WHERE cedula = %s"
        cursor.execute(query, (cedula.get(),))
        if cursor.rowcount > 0:
            conexion.commit()
            messagebox.showinfo('Correcto', 'Registro eliminado correctamente')
            borrar_campos()
        else:
            messagebox.showwarning('Atención', 'No se encontró un registro con esa cédula')
    except mysql.connector.Error as e:
        messagebox.showerror('Error', f'Error al eliminar el registro: {e}')
    finally:
        cursor.close()
        conexion.close()

# Función para actualizar datos
def actualizar_datos():
    if not all([cedula.get(), nombre.get(), apellido.get(), telefono.get(), direccion.get(), correo.get()]):
        messagebox.showerror('Error', 'Todos los campos son obligatorios para actualizar un registro')
        return
    conexion = conectar_bd()
    if conexion is None:
        return
    try:
        cursor = conexion.cursor()
        query = """
        UPDATE gestion_cliente SET nombre = %s, apellido = %s, direccion = %s, telefono = %s, correo = %s
        WHERE cedula = %s
        """
        cursor.execute(query, (nombre.get(), apellido.get(), direccion.get(), telefono.get(), correo.get(), cedula.get()))
        if cursor.rowcount > 0:
            conexion.commit()
            messagebox.showinfo('Correcto', 'Registro actualizado correctamente')
        else:
            messagebox.showwarning('Atención', 'No se encontró un registro con esa cédula')
    except mysql.connector.Error as e:
        messagebox.showerror('Error', f'Error al actualizar el registro: {e}')
    finally:
        cursor.close()
        conexion.close()

# Función para ver datos
def ver_datos():
    conexion = conectar_bd()
    if conexion is None:
        return
    try:
        cursor = conexion.cursor()
        query = "SELECT * FROM gestion_cliente"
        cursor.execute(query)
        registros = cursor.fetchall()
        ventana_ver = tk.Toplevel(ventana)
        ventana_ver.title("Registros")
        ventana_ver.geometry("600x400")
        tree = ttk.Treeview(ventana_ver, columns=("cedula", "nombre", "apellido", "direccion", "telefono", "correo"), show="headings")
        tree.heading("cedula", text="Cédula")
        tree.heading("nombre", text="Nombre")
        tree.heading("apellido", text="Apellido")
        tree.heading("direccion", text="Dirección")
        tree.heading("telefono", text="Teléfono")
        tree.heading("correo", text="Correo")
        for registro in registros:
            tree.insert("", tk.END, values=registro)
        tree.pack(expand=True, fill=tk.BOTH)
    except mysql.connector.Error as e:
        messagebox.showerror('Error', f'Error al obtener los datos: {e}')
    finally:
        cursor.close()
        conexion.close()

# Función para borrar campos de entrada
def borrar_campos():
    for variable in [cedula, nombre, apellido, direccion, telefono, correo]:
        variable.set('')

ventana = tk.Tk()
ventana.title('Sistema de registro de clientes')
ventana.geometry('500x600')
ventana.configure(bg='#f4f4f4')
ventana.eval('tk::PlaceWindow . center')

frame_contenido = ttk.Frame(ventana, padding=(20, 10))
frame_contenido.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

cedula = tk.StringVar()
nombre = tk.StringVar()
apellido = tk.StringVar()
telefono = tk.StringVar()
direccion = tk.StringVar()
correo = tk.StringVar()

campos = [("Cédula", cedula), ("Nombre", nombre), ("Apellido", apellido), ("Teléfono", telefono), ("Dirección", direccion), ("Correo", correo)]

for i, (texto, variable) in enumerate(campos):
    ttk.Label(frame_contenido, text=texto + ':').grid(row=i, column=0, sticky=tk.W, pady=5, padx=5)
    ttk.Entry(frame_contenido, textvariable=variable, width=35, font=('Arial', 12)).grid(row=i, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)

botones = [("Guardar", guardar_datos, "#4CAF50"), ("Borrar Campos", borrar_campos, "#f44336"), ("Eliminar", borrar_datos, "#FF5733"), ("Actualizar", actualizar_datos, "#FFC300"), ("Ver Datos", ver_datos, "#3498DB")]

for i, (texto, comando, color) in enumerate(botones):
    btn = tk.Button(frame_contenido, text=texto, command=comando, bg=color, fg='white', font=('Arial', 12, 'bold'), width=20, height=2)
    btn.grid(row=len(campos) + i, column=0, columnspan=2, pady=8)

ventana.mainloop()


                              
                              
    


