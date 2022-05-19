# Clase general para el manejo del archivo

class read_text:
    # Inicializan las variables
    def __init__(self):
        self.tomar_dato: str
        self.line_archivo = []
        self.dias = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        self.meses = ['Jan', 'Feb', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
        self.list_email_order = []
        self.list_dias = []
        self.correo = dict()
        self.conteo = dict()

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
            for part in email:
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

            self.list_email_order.append(self.correo)
        self.count_dias()

    # Funcion para contar los dias
    def count_dias(self):
        for dia in self.list_email_order:
            self.list_dias.append(dia['Dia'])

        for dias in self.list_dias:
            self.conteo[dias] = self.conteo.get( dias, 0 ) + 1
        print(self.conteo)



# Fin de la clase


comenzar_leer = read_text()
comenzar_leer.dato_input()



class read_text_refactorizada:
    # Inicializan las variables
    def __init__(self):
        self.tomar_dato: str
        self.line_archivo = []
        self.dias = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        self.meses = ['Jan', 'Feb', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
        self.list_email_order = []
        self.list_dias = []
        self.correo = dict()
        self.conteo = dict()




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
        print(self.conteo)




    # Funcion para leer las partes del array con los datos del correo
    def leer_partes_email(self, email):
        for part in email:
            self.agregar_partes(part)


    # Funcion para agregar al diccionario
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

# Fin de la clase
