# Repositorio
# https://github.com/JesusMirandaEspino/programacionPhyton

import math
from turtle import right
import numpy as np
import matplotlib.pyplot as plt
from pyparsing import alphas

# Clase general para el manejo del archivo

class read_text:
    # Inicializan las variables
    def __init__(self):
        self.tomar_dato: str
        self.line_archivo = []
        self.dias = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        self.valor_dias = []
        self.meses = ['Jan', 'Feb', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
        self.list_email_order = []
        self.list_dias = []
        self.correo = dict()
        self.conteo = dict()
        self.suma_dias: int
        self.porcent_dias = []
        self.max_value: int
        



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
            self.line_archivo.append( line.split() )
        self.new_email_data()
        self.print_data_archivo()



    # Funcion para finalizar 
    def print_data_archivo(self):
        print('Que tengas un excelente dia')



    # Funcion para leer las lineas ponerlas en un diccionario y agregarlas a un arreglo (lista) 
    def new_email_data(self):
        
        for email in self.line_archivo:
            self.correo = dict()
            self.leer_partes_email(email)

            self.list_email_order.append(self.correo)
        self.count_dias()





    # Funcion para contar los dias
    def count_dias(self):
        for dia in self.list_email_order:
            self.list_dias.append(dia['Dia'])

        for dias in self.list_dias:
            self.conteo[dias] = self.conteo.get( dias, 0 ) + 1
        self.list_all_days_count()

    # Set los valores que no esten de los dias
    def list_all_days_count(self):
        for dia in  self.dias:
            if dia in self.conteo:
                self.valor_dias.append( self.conteo[dia] )
            else:
                self.valor_dias.append( 0 )
        
        self.suma_dias = sum( self.valor_dias )
        self.porcent_list_days()

    # Nuevo array o lista con valores porcentuales
    def porcent_list_days(self):
        for valor in  self.valor_dias:
            self.porcent_dias.append( math.trunc((valor / self.suma_dias) * 100)  )
        self.max_value = max(self.porcent_dias)
        self.table_data()


    # Funcion para leer las partes del email
    def leer_partes_email(self, email):
        for part in email:
            self.agregar_partes(part)


    # Funcion para agregar los elementos de cada correo en un nuevo array o lista
    def agregar_partes(self, part):
            if '@' in part:
                self.correo['Correo'] = part
            for day in self.dias:
                if day in part:
                    self.correo['Dia'] = part
            for mes in self.meses:
                if mes in part:
                    self.correo['Mes'] = part
            if ':' in part:
                self.correo['Hora'] = part
            if len(part) == 4:
                self.correo['Anio'] = part

    # Funcion para preparar los datos de la tabla
    def table_data(self):
        valores_y = self.porcent_dias
        valores_x = self.dias
        color_list =  []
        values_porcent = []
        for dias in self.porcent_dias:
            if dias == self.max_value:
                color_list.append('#2155CD')
            color_list.append('#0AA1DD')
            values_porcent.append( str(dias) + '%' )

        self.show_data(valores_x, valores_y, color_list)

    # Funcion para mostrar la tabla
    def show_data(self, x, y, color_list):  
        bar = plt.bar( x, y, width=0.5, color=color_list )
        plt.xlabel('Dias')
        plt.ylabel('Porcentaje correos')
        plt.title('Porcentaje de dias de envio de correos')

        for b in bar:
            plt.gca().text(b.get_x()+b.get_width()/2, b.get_height()+1, str(int( b.get_height()))+'%', ha='center', color='#000000', fontsize="7")
        plt.show()                

# Fin de la clase


comenzar_leer = read_text()
comenzar_leer.dato_input()

