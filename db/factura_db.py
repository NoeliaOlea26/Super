from db.conexion import Conexion
from datetime import datetime

db = 'supermark.db'
def insertar_factura(idPersona):
    conexion = Conexion(db)
    fecha = (datetime.now()).date()
    conexion.consulta(f'INSERT INTO Factura VALUES(NULL,{idPersona},"{fecha}", "","")')
    conexion.commit()
    conexion.cerrar()

def eliminar_factura(codigo):
    conexion = Conexion(db)
    conexion.consulta(f'DELETE FROM Factura WHERE id={codigo}')
    conexion.commit()
    conexion.cerrar()

def editar_factura(id_persona, estado, codigo):
    conexion = Conexion(db)
    fecha = fecha = (datetime.now()).date()
    conexion.consulta(f'UPDATE Factura SET id_persona = {id_persona}, fecha ="{fecha}", estado = "{estado}" WHERE id = {codigo}')
    conexion.commit()
    conexion.cerrar()

def editar_estado_total(estado, total, idFactura):
    conexion = Conexion(db)
    conexion.consulta(f'UPDATE Factura SET estado = "{estado}", total = {total} WHERE id = {idFactura}')
    conexion.commit()
    conexion.cerrar()

def ver_factura(codigo):
    conexion = Conexion(db)
    conexion.consulta(f'SELECT * FROM Factura WHERE id={codigo}')
    datos = conexion.cursor.fetchone()
    conexion.commit()
    conexion.cerrar()
    return datos

def ver_todas(idPersona):
    conexion = Conexion(db)
    conexion.consulta(f'SELECT * FROM Factura WHERE id_persona={idPersona}')
    datos = conexion.cursor.fetchall()
    conexion.commit()
    conexion.cerrar()
    return datos

def ver_todas_activas():
    conexion = Conexion(db)
    conexion.consulta(f'SELECT * FROM Factura')
    datos = conexion.cursor.fetchall()
    conexion.commit()
    conexion.cerrar()
    return datos

def recuperar_idFactura(idPersona):
    conexion = Conexion(db)
    conexion.consulta(f'SELECT id FROM Factura WHERE id_persona={idPersona} ORDER BY id DESC')
    id = conexion.cursor.fetchone()
    conexion.commit()
    conexion.cerrar()
    return id