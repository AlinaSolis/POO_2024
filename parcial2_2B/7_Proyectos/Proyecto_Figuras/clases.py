import Figura

class Figura:
    def _init_(self,x,y,visible):
        self.x=x
        self.y=y
        self.visible = visible

    def visibility(self,visible):
        self.visible=visible

    def mostrar(self):
        self.visible=True

    def ocultar(self):
        self.visible=False

    def set_mostrar(self,mostrar):
        self.movmiento = False

    def move(self,mostrar):
        self.movmiento=mostrar
        
    def printed(self):
        print(f"X = {self.x}\nY = {self.y}\visible: {self.visible}")


class Rectangulo(Figura):
    def area(self):
        return self.x * self.y

    def set_x(self,x):
        self.x=x

    def set_y(self,y):
        self.y=y

    def get_ancho(self):
        return self.x

    def get_alto(self):
        return self.y
    
    def printed(self):
        print(f"X={self.x}\nY={self.y}\visible: {self.visible}")

class Circulos(Figura):
    def _init_(self,radio):
        super()._init_(radio,radio)

    def area(self):
        return 3.1416*(self.x**2)

    def get_radio(self):
        return self.x
    
    def printed(self):
        print(f"Radio = {self.x}\visible: {self.visible}")







    