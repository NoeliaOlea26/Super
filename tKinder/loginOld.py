import tkinter as tk
from tkinter import ttk, messagebox

class LoginVentana(tk.Tk):
    def __init__(self):
        super().__init__()
        # ventana principal
        self.geometry('300x150')
        self.title('Login')
        self.resizable(0,0)
        # configuración del grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        # Creamos los componentes
        self._crear_componentes()

    # Definir el método crear_componentes
    def _crear_componentes(self):
        # usuario
        usuario_etiqueta = ttk.Label(self, text='Ingrese DNI:')
        usuario_etiqueta.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self.usuario_entrada = ttk.Entry(self)
        self.usuario_entrada.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        # boton Login
        login_boton = ttk.Button(self, text='Siguiente', command=self.verificacion)
        login_boton.grid(row=3, column=0, columnspan=2)

        # Omitir
        omitir_boton = ttk.Button(self, text='Omitir', command=self.verificacion)
        omitir_boton.grid(row=4, column=0, columnspan=2)

    def verificacion(self):
        # Si es admin debe ingresar clave
        if self.usuario_entrada.get() == '12345': #Se puede colocar una clave fija o autogenerada
            return self.password()
        
        # Si es cliente debe pasar verificacion
        elif self.usuario_entrada.get() == '11111': # Se puede consultar a la base de datos el nombre y que verifique identidad
            return self.verif_datos()
        
        # Si no es cliente solo ingresa DNI
        else:
            password_etiqueta = ttk.Label(self, text='Usted Ingresó como invitado')
            password_etiqueta.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        
        

    def password(self):
        # password
        password_etiqueta = ttk.Label(self, text='Contraseña:')
        password_etiqueta.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        self.password_entrada = ttk.Entry(self, show='*')
        self.password_entrada.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

    def verif_datos(self):
        # password
        password_etiqueta = ttk.Label(self, text='¿Usted es Rodrigo Gonza?:')
        password_etiqueta.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        #self.password_entrada = ttk.Entry(self, show='*')
        #self.password_entrada.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        identif_boton = ttk.Button(self, text='Sí')
        identif_boton.grid(row=2, column=0)
        identif2_boton = ttk.Button(self, text='No')
        identif2_boton.grid(row=2, column=1)

    def _login(self):
        messagebox.showinfo('Datos Login',
            f'usuario: {self.usuario_entrada.get()}, Password: {self.password_entrada.get()}')

# Ejecutar la ventana
if __name__ == '__main__':
    login_ventana = LoginVentana()
    login_ventana.mainloop()