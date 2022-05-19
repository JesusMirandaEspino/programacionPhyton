# Repositorio
# https://github.com/JesusMirandaEspino/programacionPhyton

# Clase general para el manejo del archivo
class read_text:
    # Inicializan las variables
    def __init__(self):
        self.correo: str
        self.dia_semana: str
        self.dia_num: int
        self.mes: str
        self.anio: int
        self.hora: str
        self.archivo_extension: str = 'txt'
        self.tomar_dato: str
        self.data_archivo = ['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', 5, '09:14:16', 2008]

    # Funcion para ingresar y verificar el archivo ingresado
    def dato_input(self):
        print( 'Ingrese el nombre del archivo con su extension: ' )
        self.tomar_dato = input()

        if self.tomar_dato == 'Historial.txt':
            self.read_data_archivo()
        else:
            print( 'Archivo inválido, hasta luego' )

    # Funcion para leer el contenido del archivo e insertarlo en las variables respectivas
    def read_data_archivo(self):
        for data in self.data_archivo:
            if data == 'stephen.marquard@uct.ac.za':
                self.correo = data
            elif data == 'Sat':
                self.dia_semana = data
            elif data == 'Jan':
                self.mes = data
            elif data == 5:
                self.dia_num = data
            elif data == '09:14:16':
                self.hora = data
            elif data == 2008:
                self.anio = data

        self.print_data_archivo()

    # Funcion para imprimir el resultado de leer el archivo
    def print_data_archivo(self):
        print( 'El correo es: ', self.correo )
        print( 'El día en que se mandó fue: ', self.dia_semana )
        print( 'El número de día fue: ', self.dia_num )
        print( 'El mes en que se mandó fue: ', self.mes )
        print( 'El año en que se mandó fue: ', self.anio )
        print( 'La hora a la que se mandó fue: ', self.hora )

        print('Que tengas un excelente dia')

# Fin de la clase


comenzar_leer = read_text()
comenzar_leer.dato_input()

