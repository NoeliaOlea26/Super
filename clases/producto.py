from db import productos_db
class Producto:
    def __init__(self):
        self.__nombre = ""
        self.__detalle = ""
        self.__stock = 0
        self.__precio = 0
    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def detalle(self):
        return self.__detalle

    @detalle.setter
    def detalle(self, detalle):
        self.__detalle = detalle
    
    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, stock):
        self.__stock = stock
    
    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    def crear_producto(self, nombre, detalle, stock, precio):
        self.__nombre = nombre
        self.__detalle = detalle
        self.__stock = stock
        self.__precio = precio
        productos_db.insertar_producto(self.__nombre, self.__detalle, self.__stock, self.__precio)
    
    def eliminar_producto(self, codigo):
        productos_db.eliminar_producto(codigo)
    
    def editar_producto(self, nombre, detalle, stock, precio, codigo):
        productos_db.editar_producto(nombre, detalle, stock, precio, codigo)
    
    def ver_producto(self, codigo):
        return productos_db.ver_producto(codigo)
    
    def ver_todo(self):
        return productos_db.ver_todos()
    
    def incrementar_stock(self, idProducto, cantidad):
        return productos_db.incrementar_stock(idProducto, cantidad)
    
    def decrementar_stock(self, idProducto, cantidad):
        return productos_db.decrementar_stock(idProducto, cantidad)