

from matplotlib.pyplot import switch_backend


class expendedora:
    def __init__(self):
        self.m10:                int  = 50
        self.m5:                 int  = 100
        self.m2:                 int  = 250
        self.m1:                 int  = 500
        self.m50:                int  = 1000
        self.count:              int = 1
        self.precio_articulo:    float = -1
        self.cantidad_ingresada: float = -1
        self.cambio:             float
        self.cambio_restante:    float
        self.count_m50:          int = 0
        self.count_m5:           int = 0 
        self.count_m10:          int = 0
        self.count_m2:           int = 0
        self.count_m1:           int = 0
        self.init_maquina: bool = True
        self.menu: str


    #Inicio de las funciones internas
    def init_expendedora( self):

        while self.init_maquina:
            print('Que deseas hacer: ')
            print('1.- Comprar')
            print('2.- Salir')
            self.menu = input()

            if self.menu != '1':
                self.init_maquina = False
            else:
                self.precio_articulo = 0
                self.cantidad_ingresada = 0
                self.cambio = 0
                self.cambio_restante = 0
                self.count_m50 = 0
                self.count_m10 = 0
                self.count_m5 = 0
                self.count_m2 = 0
                self.count_m1 = 0
                self.ingresar_precio()
            
                self.ingresar_pago()

                self.verificar_cantidad()



        print('Ten un Buen dia')

    # funcion para verificar el pago vs el precio
    def verificar_cantidad(self):
        while self.precio_articulo > self.cantidad_ingresada:
            falta = self.precio_articulo - self.cantidad_ingresada
            print('Saldo insuficiente ingrese la cantidad de $', falta )
            self.cantidad_ingresada = self.verificar_numerico(input()) + self.cantidad_ingresada

        total_maquina = (self.m10 * 10 ) + (self.m5 * 5) + (self.m2 * 2) + self.m1 + (self.m50 * 50)
        if total_maquina >  self.cantidad_ingresada:
            self.dar_cambio()
        else:
            print('No se puede procesar el pedido')
            print('Se devuelve la cantidad de: $', self.cantidad_ingresada)
            self.init_maquina = False

    # Funcion para verificar que el tipo de dato ingresado sea correcto
    def verificar_numerico(self, valor):
        try:
            valor = float(valor)
            if type(valor) == int or type(valor) == float:
                return valor
        except ValueError:
            print('Ingrese una cantidad correcta')
            return 0


    # Funcion para ingresar el precio del producto
    def ingresar_precio(self):
        while self.precio_articulo <=  0:
            print( 'Ingrese el precio del producto' )
            self.precio_articulo = self.verificar_numerico(input())

        
    # Funcion para ingresar el pago
    def ingresar_pago(self):
        while self.cantidad_ingresada <=  0:
            print( 'Ingrese el pago del producto' )
            self.cantidad_ingresada = self.verificar_numerico(input())


    # Funcion para procesar el cambio
    def dar_cambio(self):
        self.cambio = self.cantidad_ingresada - self.precio_articulo
        print( 'Se tiene que dar cambio de: $',  self.cambio )
        self.validar_tipo_cambio()

        
    # Funcion para dar el cambio
    def validar_tipo_cambio(self):
        self.cambio_restante = self.cambio
        while self.cambio_restante > 0:
            if self.cambio_restante >= 50 and self.m50 > 0:
                self.cambio_restante = self.factor_cambio( self.cambio_restante, 50 )
                self.count_m50 += 1
                self.m50 -= 1
            elif self.cambio_restante >= 10 and self.m10 > 0:
                self.cambio_restante = self.factor_cambio( self.cambio_restante, 10 )
                self.count_m10 += 1
                self.m10 -= 1
            elif self.cambio_restante >= 5 and self.m5 > 0:
                self.cambio_restante = self.factor_cambio( self.cambio_restante, 5 )
                self.count_m5 += 1
                self.m5 -= 1
            elif self.cambio_restante >= 2 and self.m2 > 0:
                self.cambio_restante = self.factor_cambio( self.cambio_restante, 2 )
                self.count_m2 += 1
                self.m2 -= 1
            elif self.cambio_restante >= 1 and self.m1 > 0:
                self.cambio_restante = self.factor_cambio( self.cambio_restante, 1 )
                self.count_m1 += 1
                self.m1 -= 1
            else: 
                print('Ocurrio un error con la maquina...')
                self.cambio_restante = 0

        print('50: ', self.count_m50, '  Son: ', self.count_m50 * 50 )
        print('10: ', self.count_m10, '  Son: ', self.count_m10 * 10)
        print('5: ', self.count_m5, '.  Es: ', self.count_m5 * 5)
        print('2: ', self.count_m2, '.  Es: ', self.count_m2 * 2)
        print('1: ', self.count_m1, '.  Son: ', self.count_m1)


    def factor_cambio(self, cantidad: float, factor: float):
            return  cantidad - factor



ejecuta_expendedora = expendedora()

ejecuta_expendedora.init_expendedora()