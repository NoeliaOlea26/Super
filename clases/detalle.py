import db.detalle_db as detalle_db
import db.productos_db as productos_db


class Detalle:
    def __init__(self):
        self.__idFactura = 0 
        self.__idProducto = 0
        self.__cantidad = 0
        self.__precio = 0
        self.__subtotal = 0
    
    @property
    def idFactura(self):
        return self.__idFactura

    @idFactura.setter
    def idFactura(self, idFactura):
        self.__idFactura = idFactura
    
    @property
    def idProducto(self):
        return self.__idProducto

    @idProducto.setter
    def id(self, idProducto):
        self.__idProducto = idProducto
    
    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        self.__precio = precio    
    
    @property
    def subtotal(self):
        return self.__subtotal

    @subtotal.setter
    def subtotal(self, subtotal):
        self.__subtotal = subtotal

    def crear_detalle(self, idFactura, idProducto, cantidad):
        self.__idFactura = idFactura #Se encapsula cada dato recibido
        self.__idProducto = idProducto
        self.__cantidad = cantidad
        dato = productos_db.recuperar_precio(idProducto) #recupera el precio de un producto
        self.__precio = dato[0] #Recupero el precio
        self.__subtotal = self.__cantidad * self.__precio # El subtotal es un campo calculado que luego se guarda en la base de datos
        detalle_db.insertar_detalle(self.__idFactura, self.__idProducto, self.__cantidad, self.__precio, self.__subtotal)
    
    def editar_detalle(self, idFactura, idProducto, cantidad, precio, codigo):
        detalle_db.editar_detalle(idFactura, idProducto, cantidad, precio, codigo)
    
    def eliminar_detalle(self, codigo):
        detalle_db.eliminar_detalle(codigo)
    
    def ver_detalle(self, idFactura):
        return detalle_db.ver_detalle(idFactura)