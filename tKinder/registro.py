import tkinter as tk
from tkinter import Frame, ttk, messagebox, IntVar, Radiobutton

class LoginVentana(tk.Tk):
    def __init__(self):
        super().__init__()
        # ventana principal
        self.geometry('400x400')
        self.title('Registro')
        #self.iconbitmap('GUI/image/icons/tienda.ico')
        self.var_op = IntVar()
        #self.resizable(0,0)
        #self['bg']= '#14E7E7'

        # configuración del grid
        #self.columnconfigure(0, weight=1)
        #self.rowconfigure(0, weight=1)
        #self.columnconfigure(1, weight=2)
        # Creamos los componentes
        self._crear_componentes()
        #self.pack()

    # Definir el método crear_componentes
    def _crear_componentes(self):
        # caja =Frame(self, width=150,height=200,bg="yellow")
        # caja.place(x=4, y=5)
        # boc1 =Frame(caja, width=50, height =200,bg="blue")
        # boc1.grid(row=0, column=0)
        # self.lbl1=ttk.Label(boc1,text="ejecutar")
        # self.lbl1.pack(side="left")

        lbl1 =ttk.Label(self,text="Registro", font="Arial 25")
        lbl1.grid(row=0, column=1,padx=0, pady=5)
        # nombre
        nombre_etiqueta = ttk.Label(self, text='Nombre:')
        nombre_etiqueta.grid(row=2, column=0,sticky=tk.E, padx=5, pady=5)
        self.nombre_entrada = ttk.Entry(self)
        self.nombre_entrada.grid(row=2, column=1,  columnspan=2, sticky=tk.W, padx=5, pady=5)

        # apellido
        apellido_etiqueta = ttk.Label(self, text='Apellido:')
        apellido_etiqueta.grid(row=3, column=0,sticky=tk.E, padx=5, pady=5)
        self.apellido_entrada = ttk.Entry(self)
        self.apellido_entrada.grid(row=3, column=1,  columnspan=2, sticky=tk.W, padx=5, pady=5)

        # dni
        dni_etiqueta = ttk.Label(self, text='Dni:')
        dni_etiqueta.grid(row=4, column=0,sticky=tk.E, padx=5, pady=5)
        self.dni_entrada = ttk.Entry(self)
        self.dni_entrada.grid(row=4, column=1,  columnspan=2, sticky=tk.W, padx=5, pady=5)

        # condicion
        condicion_etiqueta = ttk.Label(self, text='Seleccione:')
        condicion_etiqueta.grid(row=5, column=0, sticky=tk.E, padx=5, pady=5)


        opciones={"Usuario":0, "Admin":1}
        posy=200
        for (t,v) in opciones.items():
            Radiobutton(self, text=t, value=v, variable = self.var_op).place(x=100,y=posy)
            posy=posy+25        
        # password
        password_etiqueta = ttk.Label(self, text='Contraseña:')
        password_etiqueta.grid(row=13, column=0, sticky=tk.E, padx=5, pady=5)
        self.password_entrada = ttk.Entry(self, show='*')
        self.password_entrada.grid(row=13, column=1, sticky=tk.W, padx=5, pady=35)

        # validacion /habilitar para que sea admin
        validacion_etiqueta = ttk.Label(self, text='Codigo Verificación (Adm):')
        validacion_etiqueta.grid(row=14, column=0, sticky=tk.E, padx=5, pady=5)
        self.validacion_entrada = ttk.Entry(self, show='*')
        self.validacion_entrada.grid(row=14, column=1, sticky=tk.W, padx=5, pady=5)

        # boton Login
        login_boton = ttk.Button(self, text='Cancelar', command=self._login)
        login_boton.grid(row=1, column=2, padx=0, pady=5)

        omit_boton = ttk.Button(self, text='Aceptar',command=self._login)
        omit_boton.grid(row=15, column=0,padx=35, pady=10)

    def _login(self):
        messagebox.showinfo('Datos Login',
            f'usuario: {self.usuario_entrada.get()}, Password: {self.password_entrada.get()}')

# Ejecutar la ventana
if __name__ == '__main__':
    login_ventana = LoginVentana()
    login_ventana.mainloop()