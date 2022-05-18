# Clase general para el manejo del archivo
from typing import Dict


class read_text:
    # Inicializan las variables
    def __init__(self):
        self.tomar_dato: str
        self.line_archivo = []
        self.dias = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        self.list_email_order = []


    # Funcion para ingresar y verificar el archivo ingresado
    def dato_input(self):

        try:

            print( 'Ingrese el nombre del archivo con su extension: ' )
            self.tomar_dato = input()

            with open(self.tomar_dato) as f:
                self.read_data_archivo(f)

        except IOError:
            print( 'Archivo inválido, hasta luego' )

    # Funcion para leer el contenido del archivo e insertarlo en las variables respectivas
    def read_data_archivo(self, f):

        for line in f:
            line = line.strip()
            if not line.startswith("From "):
                continue
            #El espacio no funciono para cortar los dos puntos se agrega la siguiente sentencia para corregirlo
            if line.startswith("From: "):
                continue
            self.line_archivo.append( line.split() )
        self.new_email_data()
        self.print_data_archivo()

    # Funcion para imprimir el resultado de leer el archivo
    def print_data_archivo(self):
        print('Que tengas un excelente dia')

    def new_email_data(self):
        
        for email in self.line_archivo:
            correo = dict()
            for part in email:
                if '@' in part:
                    correo['Correo'] = part
                for day in self.dias:
                    if day in part:
                        correo['Dia'] = part
            self.list_email_order.append(correo)

        for other in self.list_email_order:
            print(other)

        print( len(self.list_email_order))
        print( len(self.line_archivo))


# Fin de la clase


comenzar_leer = read_text()
comenzar_leer.dato_input()

