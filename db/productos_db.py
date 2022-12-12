from db.conexion import Conexion

db = 'supermark.db'

def insertar_producto(nombre, detalle, stock, precio):
    conexion = Conexion(db)
    conexion.consulta(f'INSERT INTO Productos VALUES(NULL,"{nombre}","{detalle}",{stock},{precio})')
    conexion.commit()
    conexion.cerrar()

def eliminar_producto(codigo):
    conexion = Conexion(db)
    conexion.consulta(f'DELETE FROM Productos WHERE id={codigo}')
    conexion.commit()
    conexion.cerrar()

def editar_producto(nombre, detalle, stock, precio,codigo):
    conexion = Conexion(db)
    conexion.consulta(f'UPDATE Productos SET nombre ="{nombre}", detalle = "{detalle}", stock = {stock}, precio = {precio} WHERE id = {codigo}')
    conexion.commit()
    conexion.cerrar()

def ver_producto(codigo):
    conexion = Conexion(db)
    conexion.consulta(f'SELECT * FROM Productos WHERE id={codigo}')
    datos = conexion.cursor.fetchone()
    conexion.commit()
    conexion.cerrar()
    return datos

def ver_todos():
    conexion = Conexion(db)
    conexion.consulta(f'SELECT * FROM Productos')
    datos = conexion.cursor.fetchall()
    conexion.commit()
    conexion.cerrar()
    return datos

def recuperar_precio(idProducto):
    conexion = Conexion(db)
    conexion.consulta(f'SELECT precio FROM Productos WHERE id={idProducto}')
    precio = conexion.cursor.fetchone()
    conexion.commit()
    conexion.cerrar()
    return precio

def incrementar_stock(idProducto, cantidad):
    conexion = Conexion(db)
    conexion.consulta(f'UPDATE Productos SET stock = stock + {cantidad} WHERE id={idProducto}')
    conexion.commit()
    conexion.cerrar()

def decrementar_stock(idProducto, cantidad):
    conexion = Conexion(db)
    conexion.consulta(f'UPDATE Productos SET stock = stock - {cantidad} WHERE id={idProducto}')
    conexion.commit()
    conexion.cerrar()