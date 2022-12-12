import db.persona_db as persona_db

class Persona:
    def __init__(self):
        self.__nombre = ""
        self.__apellido = ""
        self.__dni = 0
        self.__condicion = ""
        
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido
    
    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni
    
    @property
    def condicion(self):
        return self.__condicion

    @condicion.setter
    def condicion(self, condicion):
        self.__condicion = condicion

    def crear_persona(self, nombre, apellido, dni, condicion):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__condicion = condicion
        persona_db.insertar_persona(self.__nombre, self.__apellido, self.__dni, self.__condicion)
        
    def eliminar_persona(self, dni):
        persona_db.eliminar_persona(dni)
    
    def editar_persona(self, nombre, apellido, dni, condicion, codigo):
        persona_db.editar_persona(nombre, apellido, dni, condicion, codigo)
    
    def ver_persona(self, dni):
        return persona_db.ver_persona(dni)
    