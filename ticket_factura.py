from io import open
import os
from datetime import datetime
import platform
import time
from clases.detalle import Detalle
from clases.factura import Factura
from clases.persona import Persona
from clases.producto import Producto

class Ticket:
    def __init__(self): #Se encapsulan los datos que considero mas importantes y que utilizaran en diferentes funciones
        self.__dni = 0
        self.__idPersona = 0
        self.__idFactura = 0
    #Se crean getter y setter de cada uno de los datos construidos
    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni
    
    @property
    def idPersona(self):
        return self.__idPersona

    @idPersona.setter
    def idPersona(self, idPersona):
        self.__idPersona = idPersona

    @property
    def idFactura(self):
        return self.__idFactura

    @idFactura.setter
    def idFactura(self, idFactura):
        self.__idFactura = idFactura

    def ver_facturas(self, dni): #Funcion que sirve para imprimir por pantalla todas las facturas de una persona determinada por su DNI
        per = Persona()
        id = per.ver_persona(dni) #Mediante el dni recupero el id de cliente
        datos = Factura().ver_todas(id[0]) #Esta es una funcion que consulta con la base de datos para recuperar las facturas de un cliente
        print('\n-------------------------------------')
        print('              FACTURAS                 ')
        print('---------------------------------------')
        print(' ID  |   FECHA   |   ESTADO   |  TOTAL ')
        print('---------------------------------------')
        for i in datos: #Se van ubicando los datos en sus correspondientes campos
            print(str(i[0]).center(5, ' ')+'|'+str(i[2]).ljust(11,' ')+'|'+str(i[3]).ljust(12, ' ')+'|'+str(i[4]).ljust(8,' ')+'\n')
            print('---------------------------------------')

    def imprimir_ticket(self): #funcion que imprime un ticket por pantalla
        per = Persona()
        fac = Factura()
        if self.__idPersona == 0: #Si una persona no es cliente entonces no tiene DNI por eso sus datos no existe
            dato_per = [0,'No Registrado','',0,'No Cliente']
        else:
            dato_per = per.ver_persona(self.__dni) #Se recupera los datos de un cliente
        det = Detalle()
        dato_det = det.ver_detalle(self.__idFactura) #Se recupera el detalle de productos de una factura determinada
        subtotal = 0
        pro = Producto()

        fichero = open('ticket.txt', 'w')

        fichero.write(f'-----------------------------------------------{os.linesep}')
        fichero.write(f'                                               {os.linesep}')
        fichero.write(f'                    SUPERMARK                  {os.linesep}')
        fichero.write(f'                                            {os.linesep}')
        fichero.write(f'                           {(datetime.now()).date()}   {(datetime.now()).hour}:{(datetime.now()).minute}{os.linesep}') #Con esta funcion se recupera la fecha y hora actual
        fichero.write(f'-----------------------------------------------{os.linesep}')
        fichero.write(f'                     CLIENTE                   {os.linesep}')
        fichero.write(f'-----------------------------------------------{os.linesep}')
        fichero.write(f'Cliente: {dato_per[2]} {dato_per[1]}         DNI: {dato_per[3]}{os.linesep}')
        fichero.write(f'-----------------------------------------------{os.linesep}')
        fichero.write(f'                     DETALLE                   {os.linesep}')
        fichero.write(f'-----------------------------------------------{os.linesep}')
        fichero.write(f' PRODUCTO |    DETALLE    | CANTIDAD | SUBTOTAL {os.linesep}')
        fichero.write(f'-----------------------------------------------{os.linesep}')
        for i in dato_det:
            producto = pro.ver_producto(i[2])
            subtotal += i[5]
            fichero.write(producto[1].ljust(10,' ')+'|'+producto[2].ljust(15, ' ')+'|'+str(i[3]).ljust(10,' ')+'|'+str(i[5]).ljust(10, ' ')+'\n')
        fichero.write(f'-----------------------------------------------{os.linesep}')
        fichero.write(f'                      TOTAL                    {os.linesep}')
        fichero.write(f'-----------------------------------------------{os.linesep}')
        fichero.write(f'                     Subtotal: $ {subtotal}      {os.linesep}')
        
        # Con este if estoy aplicando un descuento solo a clientes
        if self._idPersonas != 0:
            descuento = subtotal * fac.descuento(self.__idPersona)
            total = subtotal - descuento
        else:
            descuento = 0
            total = subtotal
        
        fichero.write(f'                    Descuento: $ {descuento}     {os.linesep}')
        fichero.write(f'       Su total a pagar es de: $ {total}         {os.linesep}')
        fichero.write(f'-----------------------------------------------{os.linesep}')
        fichero.write(f'-------------¡GRACIAS POR SU COMPRA!-----------{os.linesep}')
        fichero.write(f'-----------------------------------------------{os.linesep}')
        fichero.close()
    
    def cargar_ticket(self, carrito): #Esta funcion carga la lista de productos del carrito a la base de datos de detalle
        det = Detalle() #Instancio las clases que utilizaré
        fac = Factura()
        pro = Producto()
        carrito = carrito #Entra como parametro el carrito porque de alli necesito los datos para cargar el detalle

        for i in carrito: #Para cada persona se crea un detalle con los articulos del carrito
            det.crear_detalle(self.__idFactura, i[0], i[1]) #Se crea un detalle 
            pro.decrementar_stock(i[0], i[1]) #Se disminuye el stock 
        estado = 'pagado' #Como se confirma la compra, el detalle de la factura creada cambia a pagado
        total = fac.sum_total(self.__idFactura) #El total de la factura es un campo calculado que utiliza la funcion sum_total para recuperar todos los subtotales de los detalles y sumarlos
        fac.editar_estado_total(estado, total, self.__idFactura) #Esta funcion actualiza el estado de la factura a pagado


    def confirmar_compra(self, carrito):
        fac = Factura()
        print('\n¿Confirmar compra?') #Solicitud de confirmacion de compra
        op = input('Si o No: ') 
        if op.lower() == 'si': #Confirma la compra y se crea la factura
            fac.crear_factura(self.__dni) #Se crea la nueva factura con el DNI del cliente
            #Retornar ID de Factura
            self.__idFactura = fac.retornar_idFactura(self.__idPersona) #Se recupera el id de factura de determinado cliente
            self.cargar_ticket(carrito) 
            self.imprimir_ticket() #Se crea un archivo txt como si fuese una factura de compra
            print('Ticket Generado con Exito!')
        elif op.lower() == 'no':
            print('Compra cancelada')
            pass
        else:
            print('Opcion inválida')
            self.confirmar_compra(carrito)
    
    def confirmacion(self, carrito): #Funcion para que el usuario determine que desea hacer luego de llenar su carrito
        print('\n¿Que desea hacer?')
        print('(1) Agregar Otro Producto al carrito')
        print('(2) Quitar Producto del carrito')
        print('(3) Confirmar Compra')
        print('(4) Cancelar Compra')

        op1 = input('Opcion: ')
        if op1 == '1': #Si el usuario desea agregar otro producto al carrito, se le vuelve a mostrar los productos disponibles para cargar
            self.agregar_producto(carrito)
            self.vista_previa(carrito)
            self.confirmacion(carrito) #Se aplica recursividad para volver a preguntar que desea hacer el usuario

        elif op1 == '2': #Si el usuario desea quitar un producto se le pedira que ingrese un id del producto que desea eliminar
            self.quitar_producto(carrito)
            self.vista_previa(carrito)
            self.confirmacion(carrito) #Se aplica recursividad para volver a preguntar que desea hacer el usuario
        
        elif op1 == '3': #Se confirma la compra e imprime el ticket
            self.confirmar_compra(carrito)
            print('Compra Finalizada')
        
        elif op1 == '4': #Se cancela la compra
            print('Compra cancelada')
            pass
        else:
            print('Opcion inválida') #Si se ingresa un dato no valido se aplica recursividad
            self.confirmacion()
    
    def datos_compra(self, dni=0):
        per = Persona()
        self.__dni = dni #Se setea en 0 en caso de ser invitado
        #Retornar ID de Persona
        if self.__dni == 0:
            self.__idPersona = 0 #Como el DNI es igual a 0, su id tambien sera 0
        else:
            datos = per.ver_persona(self.__dni)
            self.__idPersona = datos[0] 
        
        carrito = [] #Se crea el carrito como una lista vacia que se irá cargando de los productos
        
        self.agregar_producto(carrito) #Se llama a la funcion agregar_producto
        self.clear() #Limpia la consola luego de que se cargue un producto
        print('\nVerifique su Detalle de Compra')
        self.vista_previa(carrito) #Muestra una vista previa antes de efectuar la compra del carrito y los productos seleccionados
        self.confirmacion(carrito) #Se solicita confirmacion al usuario si se desea comprar los articulos del carrito
        self.clear() #Limpiamos de vuelta consola para evitar tanta suciedad

    def agregar_producto(self, list=[]):
        carrito = list #Toma la lista "carrito" creado en la funcion datos compra.
        op = 'si'      #Se instancia op(opcion que ira cambiando segun el usuario)
        while op.lower() == 'si' or op.lower() == 's': #Para entrar al ciclo op siempre tiene que ser si. Si el usuario no quiere seguir cargando productos entonces op cambia a "no" y se corta el ciclo
            self.ver_productos() #Se hace una vista previa de los productos disponibles
            idProducto = int(input('Ingrese codigo de producto: ')) #Los productos se ingresan por id de producto
            cantidad = int(input('¿Cuantos articulos desea llevar? '))
            carrito.append((idProducto, cantidad)) #Aqui tengo que hacer la condicion de no comprar mas de 30 productos
            print('\n"Producto Agregado al Carrito"')
            print('\n¿Desea ingresar otro Producto?: ')
            op = input('Si o No: ') #Se pregunta al usuario si quiere seguir ingresando productos para que reingrese en ciclo
        return carrito
    
    def quitar_producto(self,list=[]):
        carrito = list
        orden = int(input('Ingrese el nuemero de orden del producto que desea eliminar: '))
        carrito.pop(orden) #Se saca el producto del carrito segun su orden de producto en la lista
        print('Producto Eliminado\n')

    def ver_productos(self): #Funcion para que se vean todos los productos disponibles en el super
        pro = Producto() 
        datos_pro = pro.ver_todo() #Funcion que recupera los datos de todos los productos para luego trabajar con ellos.
        print('\n------------------------------------------')
        print('          PRODUCTOS DISPONIBLES             ')
        print('--------------------------------------------')
        print(' CODIGO | PRODUCTO |    DETALLE    | PRECIO ')
        print('--------------------------------------------')
        for i in datos_pro:
            print(str(i[0]).center(8, ' ')+'|'+str(i[1]).center(10, ' ')+'|'+str(i[2]).center(15,' ')+'|'+str(i[4]).center(10, ' ')+'\n')
        print('--------------------------------------------')

    def vista_previa(self, list):
        carrito = list #Se ingresa el carrito armado a la funcion para imprimir un detalle de compra
        pro = Producto() #Se contruye la clase Producto porque se utilizaran metodos de alli
        orden = -1 #El orden se instancia en -1 para que respete el id de detalle de la base de datos
        subtotal = 0 #El subtotal es un campo calculado entre precio y cantidad
        print('\n--------------------------------------------------------')
        print('                      DETALLE DE COMPRA                   ')
        print('--------------------------------------------------------')
        print(' ORDEN | PRODUCTO |    DETALLE    | CANTIDAD | SUBTOTAL ')
        print('--------------------------------------------------------')
        for i in carrito: #Con este ciclo se mostraran todos los productos en el carrito
            orden += 1
            producto = pro.ver_producto(i[0])
            subtotal = (i[1] * producto[4])
            print(str(orden).center(7, ' ')+'|'+str(producto[1]).center(10, ' ')+'|'+producto[2].center(15,' ')+'|'+str(i[1]).center(10, ' ')+'|'+str(subtotal).rjust(10, ' ')+'\n')

    def ver_usuarios_activos(self): #Funcion para saber los clientes registrados que realizaron al menos una vez una compra
        fac = Factura()
        datos = fac.ver_todas_activas() #Recupera todas las facturas en la base de datos y luego se trabaja con ellas.

        print('\n--------------------------------------------')
        print('          FACTURAS DE CLIENTES ACTIVOS        ')
        print('----------------------------------------------')
        print(' ID  | ID PERSONA |   FECHA   |   ESTADO   |  TOTAL ')
        print('----------------------------------------------')
        for i in datos:
            print(str(i[0]).center(5, ' ')+'|'+str(i[1]).center(12, ' ')+'|'+str(i[2]).ljust(11,' ')+'|'+str(i[3]).ljust(12, ' ')+'|'+str(i[4]).ljust(8,' ')+'\n')
            print('----------------------------------------------')


    def clear(self): #Funcion para limpiar consola
        time.sleep(3)
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

