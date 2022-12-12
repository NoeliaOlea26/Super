from db.conexion import Conexion

db = 'supermark.db'
def insertar_detalle(id_factura, id_producto, cantidad, precio, subtotal):
    conexion = Conexion(db)
    conexion.consulta(f'INSERT INTO Detalles VALUES(NULL, {id_factura}, {id_producto}, {cantidad}, {precio}, {subtotal})')
    conexion.commit()
    conexion.cerrar()

def eliminar_detalle(codigo):
    conexion = Conexion(db)
    conexion.consulta(f'DELETE FROM Detalles WHERE id={codigo}')
    conexion.commit()
    conexion.cerrar()

def editar_detalle(id_factura, id_producto, cantidad, precio, codigo):
    conexion = Conexion(db)
    conexion.consulta(f'UPDATE Detalles SET id_factura = {id_factura}, id_producto = {id_producto}, cantidad = {cantidad}, precio = {precio}, WHERE id = {codigo}')
    conexion.commit()
    conexion.cerrar()

def ver_detalle(idFactura):
    conexion = Conexion(db)
    conexion.consulta(f'SELECT * FROM Detalles WHERE id_factura={idFactura}') #trae todos los detalles de una factra
    datos = conexion.cursor.fetchall()
    conexion.commit()
    conexion.cerrar()
    return datos