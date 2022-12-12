from db.conexion import Conexion

db = 'supermark.db'
def insertar_persona(nombre, apellido, dni, condicion):
    conexion = Conexion(db)
    conexion.consulta(f'INSERT INTO Persona VALUES(NULL,"{nombre}","{apellido}",{dni},"{condicion}")')
    conexion.commit()
    conexion.cerrar()

def eliminar_persona(dni):
    conexion = Conexion(db)
    conexion.consulta(f'DELETE FROM Persona WHERE dni={dni}')
    conexion.commit()
    conexion.cerrar()

def editar_persona(nombre, apellido, dni, condicion, codigo):
    conexion = Conexion(db)
    conexion.consulta(f'UPDATE Persona SET nombre = "{nombre}", apellido = "{apellido}", dni = {dni}, condicion = "{condicion}" WHERE id = {codigo}')
    conexion.commit()
    conexion.cerrar()

def ver_persona(dni):
    conexion = Conexion(db) #Como evitar que tenga que poner el nombre de la bd
    try:
        conexion.consulta(f'SELECT * FROM Persona WHERE dni={dni}')
        datos = conexion.cursor.fetchone()
        conexion.commit()
        conexion.cerrar()
        return datos
    except IndexError:
        return 'Fuera de rango'