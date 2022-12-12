# import tkinter as tk
# from tkinter import messagebox

# def validarAdm():
#     if entradaCont.get()=="admin":
#         abrirVtnaAdm()
#     else:
#         messagebox.warning("contraseña incorrecta")


from tkinter import  Tk, Button, Entry, Label, messagebox, ttk, PhotoImage
from tkinter import  StringVar,END,HORIZONTAL,Frame,Toplevel
import os, platform, time
from db.conexion import Conexion
from clases import persona, producto
from db import persona_db
import ticket_factura

class Login(Frame):
	def __init__(self, master=None):
		super().__init__( master)
		self.user_marcar = "Ingrese su dni"
		self.fila1  = ''
		self.datos = Conexion
		self.widgets()
	
	def salir(self):
		self.master.destroy()
		self.master.quit()

	def habilitarCajas(self,estado):
        self.txtNombre.configure(state=estado)
        self.txtStock.configure(state=estado)
        self.txtPrecio.configure(state=estado)
        self.txtDetalle.configure(state=estado)
        
    def habilitarBtnOper(self,estado):
        self.btnNuevo.configure(state=estado)                
        self.btnModificar.configure(state=estado)
        self.btnEliminar.configure(state=estado)
        
    def habilitarBtnGuardar(self,estado):
        self.btnGuardar.configure(state=estado)                
        self.btnCancelar.configure(state=estado)                
        
    def limpiarCajas(self):
        self.txtStock.delete(0,END)
        self.txtPrecio.delete(0,END)
        self.txtNombre.delete(0,END)
        self.txtDetalle.delete(0,END)
        
    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)


    def llenaDatos(self):
        datos = self.productos.ver_todo()        
        for row in datos:            
            self.grid.insert("",END,text=row[0], values=(row[1],row[2], row[3],row[4]))
        
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set( self.grid.get_children()[0] )

    def fBuscar(self): #hacer funcion para que busque cierto codigo. Habria que especificar si se desea buscar persona o producto
        idProducto = self.txtCodigo.get()
        self.limpiaGrid()
        row = self.productos.ver_producto(int(idProducto))
        print(row)
        self.grid.insert("",END,text=row[0], values=(row[1],row[2], row[3],row[4]))
        
    def fNuevo(self):         
        self.habilitarCajas("normal")  
        self.habilitarBtnOper("disabled")
        self.habilitarBtnGuardar("normal")
        self.limpiarCajas()        
        self.txtNombre.focus()
    
    def fGuardar(self): 
        if self.id ==-1:       
            self.productos.crear_producto(self.txtNombre.get(),self.txtDetalle.get(),self.txtStock.get(),self.txtPrecio.get())            
            messagebox.showinfo("Insertar", 'Elemento insertado correctamente.')
        else:
            self.productos.editar_producto(self.txtNombre.get(),self.txtDetalle.get(),self.txtStock.get(),self.txtPrecio.get(), self.id)
            messagebox.showinfo("Modificar", 'Elemento modificado correctamente.')
            self.id = -1            
        self.limpiaGrid()
        self.llenaDatos() 
        self.limpiarCajas() 
        self.habilitarBtnGuardar("disabled")      
        self.habilitarBtnOper("normal")
        self.habilitarCajas("disabled")
                    
    def fModificar(self):        
        selected = self.grid.focus()                               
        clave = self.grid.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Modificar", 'Debes seleccionar un elemento.')            
        else:            
            self.id = clave  
            self.habilitarCajas("normal")                         
            valores = self.grid.item(selected,'values')
            self.limpiarCajas()            
            self.txtNombre.insert(0,valores[0])
            self.txtDetalle.insert(0,valores[1])
            self.txtStock.insert(0,valores[2])
            self.txtPrecio.insert(0,valores[3])            
            self.habilitarBtnOper("disabled")
            self.habilitarBtnGuardar("normal")
            self.txtNombre.focus()
                                        
    def fEliminar(self):
        selected = self.grid.focus()                               
        clave = self.grid.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Eliminar", 'Debes seleccionar un elemento.')            
        else:                           #Aqui hay algo raro
            valores = self.grid.item(selected,'values')
            data = str(clave) + ", " + valores[0] + ", " + valores[1]
            r = messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n" + data)            
            if r == messagebox.YES:
                n = self.paises.elimina_pais(clave)
                if n == 1:
                    messagebox.showinfo("Eliminar", 'Elemento eliminado correctamente.')
                    self.limpiaGrid()
                    self.llenaDatos()
                else:
                    messagebox.showwarning("Eliminar", 'No fue posible eliminar el elemento.')
                            
    def fCancelar(self):
        r = messagebox.askquestion("Calcelar", "Esta seguro que desea cancelar la operación actual")
        if r == messagebox.YES:
            self.limpiarCajas() 
            self.habilitarBtnGuardar("disabled")      
            self.habilitarBtnOper("normal")
            self.habilitarCajas("disabled")

	def acceder_ventana_dos(self):
		
		self.master.withdraw()
		self.ventana_dos = Toplevel()
		self.ventana_dos.title('Segunda Ventana')
		self.ventana_dos.geometry('500x500+400+80')
		self.ventana_dos.protocol("WM_DELETE_WINDOW", self.salir)
		self.ventana_dos.config(bg= 'white')
		self.pack()
        # self.create_widgets()
        self.llenaDatos()
        self.habilitarCajas("disabled")  
        self.habilitarBtnOper("normal")
        self.habilitarBtnGuardar("disabled")  
        self.id=-1      
		
		# Label(self.ventana_dos, text='VENTANA DOS', font='Arial 40', bg= 'white').pack(expand=True)
		# Button(self.ventana_dos, text='Salir', font='Arial 10', bg= 'red', command= self.salir).pack(expand=True)

		frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0,y=0,width=93, height=360)        
        # self.btnNuevo=Button(frame1,text="Nuevo", bg="blue", fg="white")
        # self.btnNuevo.place(x=5,y=50,width=80, height=30 )        
        self.btnModificar=Button(frame1,text="Modificar", bg="blue", fg="white")
        self.btnModificar.place(x=5,y=90,width=80, height=30)                
        self.btnEliminar=Button(frame1,text="Eliminar", bg="blue", fg="white")
        self.btnEliminar.place(x=5,y=130,width=80, height=30)        
        frame2 = Frame(self,bg="#d3dde3" )
        frame2.place(x=95,y=0,width=150, height=360) 

        lbl1 = Label(frame2,text="Ingrese Codigo: ")
        lbl1.place(x=3,y=5)        #+50 -20
        self.txtCod=Entry(frame2)
        self.txtCod.place(x=3,y=25,width=50, height=20)  #+20- 30

        lbl2 = Label(frame2,text="Ingrese cantidad: ")
        lbl2.place(x=3,y=55)        #-20
        self.txtCtdad=Entry(frame2)
        self.txtCtdad.place(x=3,y=75,width=100, height=20)     #-30

        self.btnGuardar=Button(frame2,text="Cargar", bg="#9ACD32", fg="black")
        self.btnGuardar.place(x=10,y=105,width=60, height=30)
        self.btnCancelar=Button(frame2,text="Cancelar",  bg="orange", fg="black")
        self.btnCancelar.place(x=80,y=105,width=60, height=30)    

        # lbl3 = Label(frame2,text="Capital: ")
        # lbl3.place(x=3,y=105)        
        # self.txtStock=Entry(frame2)
        # self.txtStock.place(x=3,y=125,width=100, height=20) 

        # lbl4 = Label(frame2,text="Currency Code: ")
        # lbl4.place(x=3,y=155)        
        # self.txtPrecio=Entry(frame2)
        # self.txtPrecio.place(x=3,y=175,width=50, height=20)    
        lbl3 = Label(frame2,text="Total: ")
        lbl3.place(x=25,y=180)        #-20
        self.txtTotal=Entry(frame2)
        self.txtTotal.place(x=25,y=205,width=100, height=20)     #-30
#nombre, detalle, stock, precio
        lbl4 = Label(frame2,text="Estado de compra: ")
        lbl4.place(x=5,y=235)        #-20
        self.btnGuardar=Button(frame2,text="Terminar", bg="green", fg="white")
        self.btnGuardar.place(x=10,y=260,width=60, height=30)
        self.btnCancelar=Button(frame2,text="Cancelar",  bg="red", fg="white")
        self.btnCancelar.place(x=80,y=260,width=60, height=30)        
        self.grid = ttk.Treeview(self, columns=("col1","col2","col3","col4"))        
        self.grid.column("#0",width=50)
        self.grid.column("col1",width=60, anchor=CENTER)
        self.grid.column("col2",width=90, anchor=CENTER)
        self.grid.column("col3",width=90, anchor=CENTER)
        self.grid.column("col4",width=90, anchor=CENTER)        
        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="Nombre", anchor=CENTER)
        self.grid.heading("col2", text="Detalle", anchor=CENTER)
        self.grid.heading("col3", text="Cantidad", anchor=CENTER)
        self.grid.heading("col4", text="Precio", anchor=CENTER)        
        self.grid.place(x=247,y=0,width=420, height=360)


	def verificacion_users(self):
		self.indica1['text'] = ''
		users_entry = self.entry1.get()
		password_entry = self.entry2.get()

		if users_entry!= self.user_marcar or self.contra_marcar != password_entry:
			users_entry = str("'" + users_entry + "'")
			password_entry = str("'" + password_entry + "'")

			dato1 = self.datos.busca_users(users_entry)
			dato2 = self.datos.busca_password(password_entry)

			self.fila1 = dato1
			self.fila2 = dato2 

			if self.fila1 == self.fila2:	
				if dato1 == [] and dato2 ==[]:
					self.indica2['text'] = 'Contraseña incorrecta'
					self.indica1['text'] = 'Usuario incorrecto'
				else:

					if dato1 ==[]:
						self.indica1['text'] = 'Usuario incorrecto'
					else:
						dato1 = dato1[0][1]

					if dato2 ==[]:
						self.indica2['text'] = 'Contraseña incorrecta'
					else:
						dato2 = dato2[0][2]

					if dato1 != [] and dato2 != []:
						self.acceder_ventana_dos()
			else:
				self.indica1['text'] = 'Usuario incorrecto'
				self.indica2['text'] = 'Contraseña incorrecta'

def widgets(self):
		Label(self.master, text= 'Usuario', bg='DarkOrchid1', fg= 'black', font= ('Lucida Sans', 16, 'bold')).pack(pady=5)
		self.entry1 = Entry(self.master, font=('Comic Sans MS', 12),justify = 'center', fg='grey',highlightbackground = "#E65561", 
			highlightcolor= "green2", highlightthickness=5)
		self.entry1.insert(0, self.user_marcar)
		self.entry1.pack(pady=4)   

		self.indica1 = Label(self.master, bg='DarkOrchid1', fg= 'black', font= ('Arial', 8, 'bold'))
		self.indica1.pack(pady=2)                             

		# contraseña y entry
		Label(self.master, text= 'Contraseña', bg='DarkOrchid1', fg= 'black', font= ('Lucida Sans', 16, 'bold')).pack(pady=5)
		self.entry2 = Entry(self.master,font=('Comic Sans MS', 12),justify = 'center',  fg='grey',highlightbackground = "#E65561", 
			highlightcolor= "green2", highlightthickness=5)
		self.entry2.insert(0, self.contra_marcar)
		self.entry2.pack(pady=4)
		self.indica2 = Label(self.master, bg='DarkOrchid1', fg= 'black', font= ('Arial', 8, 'bold'))
		self.indica2.pack(pady=2)

		Button(self.master, text= 'Iniciar Sesion',  command = self.verificacion_users,activebackground='magenta', bg='#D64E40', font=('Arial', 12,'bold')).pack(pady=10)
		
		Button(self.master, text= 'Salir', bg='DarkOrchid1',activebackground='DarkOrchid1', bd=0, fg = 'black', font=('Lucida Sans', 15,'italic'),command= self.salir).pack(pady=10)

if __name__ == "__main__":
	ventana = Tk()
	ventana.config(bg='DarkOrchid1')
	ventana.geometry('350x500+500+50')
	ventana.overrideredirect(1)
	ventana.resizable(0,0)
	app = Login(ventana)
	app.mainloop()