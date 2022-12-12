from io import BufferedIOBase
from tkinter import *
from tkinter import ttk
#from clases import *
from clases.producto import Producto
#from db.productos_db import ProductosDb
from tkinter import messagebox


class Ventana(Frame):

    productos = Producto()
       
    def __init__(self, master=None):
        super().__init__(master,width=680, height=359)
        self.master = master
        self.pack()
        self.create_widgets2()
        self.llenaDatos()
        self.habilitarCajas("disabled")  
        self.habilitarBtnOper("normal")
        self.habilitarBtnGuardar("disabled")  
        self.id=-1      
                   
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
            self.id= clave  
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
        else:                           
            valores = self.grid.item(selected,'values')
            data = str(clave) + ", " + valores[0] + ", " + valores[1]
            r = messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n" + data)            
            if r == messagebox.YES:
                n = self.productos.eliminar_producto(clave) #No entiendo porque n debe ser igual a 1
                messagebox.showinfo("Eliminar", 'Elemento eliminado correctamente.')
                self.limpiaGrid()
                self.llenaDatos() 
                            
    def fCancelar(self):
        r = messagebox.askquestion("Calcelar", "Esta seguro que desea cancelar la operación actual")
        if r == messagebox.YES:
            self.limpiarCajas() 
            self.habilitarBtnGuardar("disabled")      
            self.habilitarBtnOper("normal")
            self.habilitarCajas("disabled")

    def fIncrementar(self):
        selected = self.grid.focus()                               
        clave = self.grid.item(selected,'text')  
        cantidad = self.txtModificarStock.get()      
        if clave == '':
            messagebox.showwarning("Actualizar Stock", 'Debes seleccionar un elemento.')            
        else:                           
            self.productos.incrementar_stock(int(clave), cantidad)
            messagebox.showinfo("Actualizar Stock", 'Stock Actualizado Correctamente.')
            self.limpiaGrid()
            self.llenaDatos() 

    def fDecrementar(self):
        selected = self.grid.focus()                               
        clave = self.grid.item(selected,'text')  
        cantidad = self.txtModificarStock.get()      
        if clave == '':
            messagebox.showwarning("Actualizar Stock", 'Debes seleccionar un elemento.')            
        else:                           
            self.productos.decrementar_stock(int(clave), cantidad)
            messagebox.showinfo("Actualizar Stock", 'Stock Actualizado Correctamente.')
            self.limpiaGrid()
            self.llenaDatos()

    def create_widgets2(self):
        frame1 = Frame(self, bg="#bfdaff") #Color de fondo de un fragmento de la ventana
        frame1.place(x=0,y=0,width=100, height=359)     
        lbl0 = Label(frame1,text="Ingrese codigo: ")
        lbl0.place(x=0,y=5)        
        #self.txtNombre=Entry(frame2,textvariable = self.ISO3)
        self.txtCodigo=Entry(frame1) #En el primer fragmento ingreso una caja de texto
        self.txtCodigo.place(x=5,y=25,width=75, height=20)  
        self.btnBuscar=Button(frame1,text="Buscar", command=self.fBuscar, bg="pink", fg="black")
        self.btnBuscar.place(x=5,y=50,width=80, height=30 )     
        self.btnNuevo=Button(frame1,text="Nuevo", command=self.fNuevo, bg="blue", fg="white")
        self.btnNuevo.place(x=5,y=130,width=80, height=30 )        
        self.btnModificar=Button(frame1,text="Modificar", command=self.fModificar, bg="blue", fg="white")
        self.btnModificar.place(x=5,y=170,width=80, height=30)                
        self.btnEliminar=Button(frame1,text="Eliminar", command=self.fEliminar, bg="blue", fg="white")
        self.btnEliminar.place(x=5,y=210,width=80, height=30)        
        frame2 = Frame(self,bg="#d3dde3" ) #Segundo fragmento de la ventana, de color gris
        frame2.place(x=101,y=0,width=150, height=359)                        
        lbl1 = Label(frame2,text="Nombre: ")
        lbl1.place(x=3,y=5)        
        #self.txtNombre=Entry(frame2,textvariable = self.ISO3)
        self.txtNombre=Entry(frame2) #Nombre
        self.txtNombre.place(x=3,y=25,width=75, height=20)                
        
        lbl2 = Label(frame2,text="Detalle: ")
        lbl2.place(x=3,y=55)        
        self.txtDetalle=Entry(frame2)
        self.txtDetalle.place(x=3,y=75,width=100, height=20)        
        
        lbl3 = Label(frame2,text="Stock: ")
        lbl3.place(x=3,y=105)        
        self.txtStock=Entry(frame2)
        self.txtStock.place(x=3,y=125,width=100, height=20)        
        
        lbl4 = Label(frame2,text="Precio: ")
        lbl4.place(x=3,y=155)        
        self.txtPrecio=Entry(frame2)
        self.txtPrecio.place(x=3,y=175,width=50, height=20)        
        
        self.btnGuardar=Button(frame2,text="Guardar", command=self.fGuardar, bg="green", fg="white")
        self.btnGuardar.place(x=10,y=210,width=60, height=30)
        
        self.btnCancelar=Button(frame2,text="Cancelar", command=self.fCancelar, bg="red", fg="white")
        self.btnCancelar.place(x=80,y=210,width=60, height=30) 

        lbl22 = Label(frame2,text="Modificar Stock: ")
        lbl22.place(x=3,y=275)        #-20
        self.txtModificarStock=Entry(frame2)
        self.txtModificarStock.place(x=3,y=295,width=100, height=20)     #-30

        self.btnSumar=Button(frame2,text="Sumar", command = self.fIncrementar, bg="#9ACD32", fg="black")
        self.btnSumar.place(x=10,y=325,width=60, height=30)
        self.btnRestar=Button(frame2,text="Restar", command = self.fDecrementar, bg="orange", fg="black")
        self.btnRestar.place(x=80,y=325,width=60, height=30)  
        # frame4 = Frame(self,bg="pink" )
        # frame4.place(x=0,y=260,width=450, height=150)                        
        #lbl5 = Label(frame4,text="Precio: ")
        #lbl5.place(x=3,y=280)        
        # self.txtCurrency2=Entry(frame4)
        # self.txtCurrency2.place(x=3,y=300,width=50, height=20)        
        # self.btnSumar=Button(frame4,text="Guardar", command="", bg="green", fg="white")
        # self.btnSumar.place(x=10,y=330,width=60, height=30)        
        frame3 = Frame(self,bg="yellow" )
        frame3.place(x=247,y=0,width=420, height=359)                      
        self.grid = ttk.Treeview(frame3, columns=("col1","col2","col3","col4"))        
        self.grid.column("#0",width=60)
        self.grid.column("col1",width=70, anchor=CENTER)
        self.grid.column("col2",width=90, anchor=CENTER)
        self.grid.column("col3",width=90, anchor=CENTER)
        self.grid.column("col4",width=90, anchor=CENTER)        
        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="Nombre", anchor=CENTER)
        self.grid.heading("col2", text="Detalle", anchor=CENTER)
        self.grid.heading("col3", text="Stock", anchor=CENTER)
        self.grid.heading("col4", text="Precio", anchor=CENTER)                
        self.grid.pack(side=LEFT,fill = Y)        
        sb = Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT, fill = Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)
        self.grid['selectmode']='browse' 

if __name__ == '__main__':
    login_ventana = Ventana()
    login_ventana.mainloop()  