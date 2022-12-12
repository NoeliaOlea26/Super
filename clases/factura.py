import db.detalle_db as detalle_db
import db.factura_db as factura_db
import db.persona_db as persona_db
from clases import detalle

class Factura:
    def __init__(self):
        self.__idFactura = 0
        self.__idPersona = 0
        # self.__fecha = fecha ---> no la coloco porque se coloca automaticamente
        self.__estado = ""
        self.__total = 0
    
    @property
    def idFactura(self):
        return self.__idFactura

    @idFactura.setter
    def idFactura(self, idFactura):
        self.__idFactura = idFactura

    @property
    def idPersona(self):
        return self.__idPersona

    @idPersona.setter
    def idPersona(self, idPersona):
        self.__idPersona = idPersona
    
    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado
    
    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, total):
        self.__total = total  
    
    def crear_factura(self, dni):
        if dni == 0:
            self.__idPersona = 0
        else:
            dp = persona_db.ver_persona(dni)
            self.__idPersona = dp[0]
        factura_db.insertar_factura(self.__idPersona)
    
    def editar_factura(self, idPersona, fecha, estado, codigo):
        factura_db.editar_factura(idPersona, fecha, estado, codigo)
    
    def editar_estado_total(self, estado, total, idFactura):
        factura_db.editar_estado_total(estado, total, idFactura)

    def eliminar_factura(self, codigo):
        factura_db.eliminar_factura(codigo)
    
    def ver_factura(self, idFactura):
        # Preguntar si desea pagar con efectivo o tarjeta
        op = input('Desea pagar con efectivo?')
        if op == 'si':
            self.editar_estado_total('efectivo', self.sum_total(idFactura), idFactura)
            return factura_db.ver_factura(idFactura)
    
    def ver_todas(self, idPersona):
        return factura_db.ver_todas(idPersona)
    
    def ver_todas_activas(self):
        return factura_db.ver_todas_activas()

    def sum_total(self, idFactura):
        datos = detalle_db.ver_detalle(idFactura)
        total = sum((dato[5]) for dato in datos) #Sirve para hacer grandes sumas
        return total
    
    def retornar_idFactura(self, idPersona):
        id = factura_db.recuperar_idFactura(idPersona) #Recupero id de factura idFactura
        self.__idFactura = int(id[0])
        return self.__idFactura
    
    def asignar_estado(self, estado):
        self.__estado = estado
    
    def cantidad_facturas(self, idPersona):
        datos = factura_db.ver_todas(idPersona)
        cantidad = 0
        for i in datos:
            cantidad += 1
        return cantidad
    
    def descuento(self, idPersona): #Entre mas compra de un cliente, mayor es el descuento
        descuento = 0
        cantidad = self.cantidad_facturas(idPersona)
        if cantidad <= 5:
            descuento = 0.10
        elif cantidad > 10 and cantidad < 20:
            descuento = 0.15
        elif cantidad > 30:
            descuento = 0.20
        return descuento