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
        self.create_widgets()
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

    def fIncrementar(self):
        cantidad = self.txtModificarStock.get()
        self.productos.incrementar_stock(int(self.txtCodigo.get()), cantidad)
        self.limpiaGrid()
        self.llenaDatos()

    def fDecrementar(self):
        cantidad = self.txtModificarStock.get()
        self.productos.decrementar_stock(int(self.txtCodigo.get()), cantidad)
        self.limpiaGrid()
        self.llenaDatos()

    def create_widgets(self):
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

if __name__ == '__main__':
    login_ventana = Ventana()
    login_ventana.mainloop()  