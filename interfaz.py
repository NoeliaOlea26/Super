from tkinter import *
from tKinder import *
import os, platform, time
#import carga_datos as carga_datos
from db.conexion import Conexion
from clases import persona, producto, detalle, factura
from db import detalle_db, persona_db, factura_db, productos_db
#from tKinder.ventanaCom import Ventana
from tKinder.ventanaProd import Ventana
import ticket_factura

def main():
    root = Tk()
    root.wm_title("Crud Python MySQL")
    app = Ventana(root) 
    app.mainloop()

if __name__ == "__main__":
    main()
