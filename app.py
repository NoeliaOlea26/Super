import os, platform, time
from db.conexion import Conexion
from clases import persona, producto
from db import persona_db
import ticket_factura

conexion = Conexion('supermark.db')
conexion.crear_db()
#carga_datos

class Menu():
    def __init__(self) -> None:
        self.__dni = 0
    
    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    print('\n<<<<<<<<<<Bienvenido a SUPERMARK>>>>>>>>>>\n')
    
    def login(self):
        print('--LOGIN--')
        print('Seleccione una opcion: ')
        print('(1) Soy Administrador')
        print('(2) Soy Cliente')
        print('(3) No soy Cliente')
        
        op = input('Opcion: ')
        if op == '1': #Ingresa como Administrador
            dni = int(input('\nIngrese DNI: ')) #Como ingreso un espacio en blanco en DNI?
            self.__dni = dni
            password = input('Ingrese contraseña: ') #Por default es 'admin'

            datos = persona_db.ver_persona(dni) #Se recupera los deatos de una persona segun su DNI
            if datos[4] == "administrador" and password == 'admin': #Se verifica que el usuario sea administrador y que la contraseña ingresada sea igual a 'admin'               
                print('Logueo Exitoso\n')
                self.clear() #Primero se limpia la consola
                self.panel_admin() #Nos redirige al panel admin
            else:
                print('Datos invalidos\n') #Como se ingresa un dato invalido entonces se regresa al login
                self.clear() #Primero limpia la consola
                self.login() #Recursividad
        
        elif op == '2': #Ingresa como Cliente
            dni = int(input('Ingrese DNI: ')) #Pide un DNI para comprobar si existe en la base de datos
            self.__dni = dni
            datos = persona_db.ver_persona(dni)

            #password = input('Ingrese contraseña: ') #Deberia guardarla en columna 5 (en mi caso no la tengo creada)

            if datos[4] == "cliente": #Si se comprueba de que el usuario existe en la base de datos entonces entra en el ciclo
               
                #if datos[5] == password: #Esto lo agregué y deberia acomodar el indentado xD, pero creo q sabes como va
                #Deberia haber un else para "contraseña incorrecta"
                
                verificacion = f'{datos[1]} {datos[2]}'#Sale cartelito con datos para confirmar el usuario
                print(f'¿Usted es {verificacion}?') #Hace una pregunta para verificar si es tal persona
                op = input('Si o No: ')
                if op.lower() == 'si':
                    print('Logueo Exitoso!')
                    self.clear()
                    print(f'Bienvenido {verificacion}\n')
                    self.panel_cli() # Re direcciona al panel cliente
                else:
                    print('Error de identidad\n')
                    self.clear()
                    self.login()
            else:
                print('\n"El DNI no corresponde a un cliente"')
                self.clear()
                self.login()

        elif op == '3': #Se accede al sistema como un usuario invitado
            self.clear()
            self.panel_invitado()   # Redirecciona al panel invitado
        
        else:
            self.clear()
            self.login()
        
    def panel_admin(self): #Panel Administrador----- Agregar imprimir todos los productos
        print('--PANEL ADMINISTRADOR--')
        print('Seleccione una opcion: ')
        print('(1) Registrar Cliente')
        print('(2) Ingresar Producto')
        print('(3) Modificar datos de un Producto')
        print('(4) Actualizar STOCK de producto')
        print('(5) Ver Usuarios que realizaron una compra')
        print('(6) Salir')
        op = input('Opcion: ')

        if op == '1':
            self.clear()
            print('--REGISTRAR NUEVO USUARIO--') #Funcion que permite ingresar un nuevo usuario a la base de datos, sea cliente o administrador
            nombre = input('Ingrese nombre: ')
            apellido = input('Ingrese apellido: ')
            dni = int(input('Ingrese DNI: '))
            condicion = input('¿Es "administrador" o "cliente"?: ')
            persona.Persona().crear_persona(nombre, apellido, dni, condicion) #Funcion de conexion a la base de datos para insertar cliente
            print('Nuevo Usuario Registrado!')
            self.clear() #Tras finalizar el registro del nuevo usuario se muestra mensaje, se limpia consola y se regresa al panel de opciones
            self.panel_admin()
        
        elif op == '2':
            self.clear()
            print('--INGRESAR PRODUCTO--') #Idem al caso de agregar usuario, se solicita datos del nuevo producto
            nombre = input('Ingrese nombre de producto: ')
            detalle = input('Ingrese detalle del producto: ')
            stock = int(input('Ingrese cantidad de Stock: '))
            precio = float(input('Ingrese precio unitario: '))
            producto.Producto().crear_producto(nombre, detalle, stock, precio)
            print('Nuevo Producto Agregado con Exito!')
            self.clear() #Se agrega el nuevo producto a la base de datos, se imprime mensaje, se limpia la consola y regresa al panel 
            self.panel_admin()
        
        elif op == '3':
            self.clear()
            print('--MODIFICAR PRODUCTO--')
            idProducto = int(input('Ingrese ID del Producto que desea modificar: '))
            nombre = input('Ingrese nombre de producto: ')
            detalle = input('Ingrese detalle del producto: ')
            stock = int(input('Ingrese cantidad de Stock: '))
            precio = float(input('Ingrese precio unitario: '))
            producto.Producto().editar_producto(nombre, detalle, stock, precio,idProducto)
            print('Producto Modificado con Exito!') #Funcion que permite modificar un producto
            self.clear()
            self.panel_admin()

        elif op == '4':
            self.clear()
            print('--ACTUALIZAR STOCK PRODUCTO--')
            print('(1) Incrementar stock de un producto')
            print('(2) Decrementar stock de un producto')
            print('(3) Salir')
            op1 = input()
            if op1 == '1': #Funcion que incrementa el stock de un producto
                idProducto = int(input('Ingrese ID del Producto: '))
                cantidad = int(input('Ingrese cuanto Stock desea ingresar: '))
                producto.Producto().incrementar_stock(idProducto, cantidad)
                print('\nActualizacion de Stock Exitosa')
                self.clear()
                self.panel_admin()
            elif op1 == '2': # Funcion que decrementa el stock de un producto
                idProducto = int(input('Ingrese ID del Producto: '))
                cantidad = int(input('Ingrese cuanto Stock desea sacar: '))
                producto.Producto().decrementar_stock(idProducto, cantidad)
                print('\nActualizacion de Stock Exitosa')
                self.clear()
                self.panel_admin()
            elif op1 == '3': #Opcion salir
                self.clear()
                self.panel_admin()
            else:
                print('\nOpcion Inválida')
                self.clear()
                self.panel_admin()

        elif op == '5': #Muestra los usuarios que compraron al menos una vez
            print('--Usuarios que Compraron--')
            ticket_factura.Ticket().ver_usuarios_activos()
            print('\n(1) Volver al Menu Anterior')
            print('(0) Salir')

            op1 = input('Opcion: ')
            if op1 == '1':
                self.clear()
                self.panel_admin()
            elif op1 == '2':
                self.clear()
                self.login()

        elif op == '6':
            print('\nGracias por usar Nuestro Servicio!')
            self.clear()
            self.login()
        
        else:
            print('\nOpcion Inválida')
            self.clear()
            self.panel_admin()
    
    def panel_cli(self): #Panel para los clientes
        print('--PANEL CLIENTE--')
        print('Seleccione una opcion: ')
        print('(1) Hacer una Compra')
        print('(2) Ver Productos')
        print('(3) Ver todas mis facturas')
        print('(4) Salir')
        op = input('Opcion: ')

        if op == '1': #Funcion para hacer compra
            self.clear()
            print('--CARRITO DE COMPRA--')
            ticket_factura.Ticket().datos_compra(self.__dni) #Funcion que permite cargar datos e imprimir ticket si se acepta la compra
            self.clear()
            self.panel_cli()
        
        elif op == '2': #Funcion para Ver los productos disponibles en el super
            self.clear()
            print('--VER PRODUCTOS--')
            ticket_factura.Ticket().ver_productos() #Funcion de conexion a la base de datos y mostrar por pantalla los productos disponibles
            print('\n(1) Volver al Menu Anterior')
            print('(0) Salir')

            op1 = input('Opcion: ')
            if op1 == '1':
                self.clear()
                self.panel_cli()
            elif op1 == '2':
                self.clear()
                self.login()
            else:
                print('La opcion ingresada es inválida')
                self.clear()
                self.panel_invitado()

        elif op == '3':
            self.clear()
            ticket_factura.Ticket().ver_facturas(self.__dni) #Funcion para ver las facturas de un cliente filtrado por DNI de usuario
            print('\n(1) Volver al Menu Anterior')
            print('(0) Salir')

            op1 = input('Opcion: ')
            if op1 == '1':
                self.clear()
                self.panel_cli()
            elif op1 == '2':
                self.clear()
                self.login()

        elif op == '4':
            print('\nGracias por usar Nuestro Servicio!')
            self.clear()
            self.login()

        else:
            print('\nOpcion Inválida')
            self.clear()
            self.panel_cli()

    def panel_invitado(self):  #Panel invitado, entra sin DNI, mismas funciones que el cliente, sin beneficio de descuento
        print('--PANEL INVITADO--')
        print('Seleccione una opcion: ')
        print('(1) Hacer una Compra')
        print('(2) Ver productos disponibles')
        print('(3) Salir')
        op = input('Opcion: ')
        
        if op == '1':
            self.clear()
            print('--CARRITO DE COMPRA--')
            ticket_factura.Ticket().datos_compra()
            self.clear()
            self.panel_invitado()

        elif op == '2':
            self.clear()
            print('--VER PRODUCTOS--')
            ticket_factura.Ticket().ver_productos()
            print('\n(1) Volver al Menu Anterior')
            print('(0) Salir')

            op1 = input('Opcion: ')
            if op1 == '1':
                self.clear()
                self.panel_invitado()
            elif op1 == '2':
                self.clear()
                self.login()
            else:
                print('La opcion ingresada es inválida')
                self.clear()
                self.panel_invitado()

        elif op == '3':
            print('Gracias por usar Nuestro Servicio!')
            self.clear()
            self.login()

        else:
            print('Opcion Inválida')
            self.clear()
            self.panel_invitado()
    
    def clear(self):
        time.sleep(1)
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')


Menu().login()