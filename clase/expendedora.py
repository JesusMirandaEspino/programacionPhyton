

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
    
    def leer_datos( self):

        self.ingresar_precio()
    
        self.ingresar_pago()

        self.verificar_cantidad()

    def verificar_cantidad(self):
        while self.precio_articulo > self.cantidad_ingresada:
            falta = self.precio_articulo - self.cantidad_ingresada
            print('Saldo insuficiente ingrese la cantidad de $', falta )
            self.cantidad_ingresada = self.verificar_numerico(input()) + self.cantidad_ingresada


    def verificar_numerico(self, valor):
        try:
            valor = float(valor)
            if type(valor) == int or type(valor) == float:
                return valor
        except ValueError:
            print('Ingrese una cantidad correcta')
            return 0

    def ingresar_precio(self):
        while self.precio_articulo <=  0:
            print( 'Ingrese el precio del producto' )
            self.precio_articulo = self.verificar_numerico(input())

    def ingresar_pago(self):
        while self.cantidad_ingresada <=  0:
            print( 'Ingrese el pago del producto' )
            self.cantidad_ingresada = self.verificar_numerico(input())


    def dar_cambio(self):
        print()

        


ejecuta_expendedora = expendedora()

ejecuta_expendedora.leer_datos()