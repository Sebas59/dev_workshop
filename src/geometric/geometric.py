import math

class Geometria:

    def area_rectangulo(self, base, altura):
        if base < 0 or altura < 0:
            raise ValueError("La base y la altura deben ser valores no negativos.")
        return base * altura
    
    def perimetro_rectangulo(self, base, altura):
         return 2 * (base + altura)
    
    def area_circulo(self, radio):
        if radio < 0:
            raise ValueError("El radio debe ser un valor no negativo.")
        return math.pi * (radio ** 2)
    
    def perimetro_circulo(self, radio):
        if radio < 0:
            raise ValueError("El radio debe ser un valor no negativo.")
        return 2 * math.pi * radio
    
    def area_triangulo(self, base, altura):
        if base < 0 or altura < 0:
            raise ValueError("La base y la altura deben ser valores no negativos.")
        return (base * altura) / 2
    
    def perimetro_triangulo(self, lado1, lado2, lado3):
        if lado1 < 0 or lado2 < 0 or lado3 < 0:
            raise ValueError("Los lados deben ser valores no negativos.")
        if not (lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1):
            raise ValueError("Los lados no forman un triángulo válido.")
        return lado1 + lado2 + lado3
    
    def es_triangulo_valido(self, lado1, lado2, lado3):
        if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
            return False
        return (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)
    
    def area_trapecio(self, base_mayor, base_menor, altura):
        if base_mayor < 0 or base_menor < 0 or altura < 0:
            raise ValueError("Las bases y la altura deben ser valores no negativos.")
        return (base_mayor + base_menor) * altura / 2
    
    def area_rombo(self, diagonal_mayor, diagonal_menor):
        if diagonal_mayor < 0 or diagonal_menor < 0:
            raise ValueError("Las diagonales deben ser valores no negativos.")
        return (diagonal_mayor * diagonal_menor) / 2
    
    def area_pentagono_regular(self, lado, apotema):
        if lado < 0 or apotema < 0:
            raise ValueError("El lado y el apotema deben ser valores no negativos.")
        return (5 * lado * apotema) / 2
    
    def perimetro_pentagono_regular(self, lado):
        if lado < 0:
            raise ValueError("El lado debe ser un valor no negativo.")
        return 5 * lado
    
    def area_hexagono_regular(self, lado, apotema):
        if lado < 0 or apotema < 0:
            raise ValueError("El lado y el apotema deben ser valores no negativos.")
        return (6 * lado * apotema) / 2
    
    def perimetro_hexagono_regular(self, lado):
        if lado < 0:
            raise ValueError("El lado debe ser un valor no negativo.")
        return 6 * lado
    
    def volumen_cubo(self, lado):
        """
        Calcula el volumen de un cubo.
        
        Args:
            lado (float): Longitud del lado del cubo
            
        Returns:
            float: Volumen del cubo
        """
        pass
    
    def area_superficie_cubo(self, lado):
        """
        Calcula el área de la superficie de un cubo.
        
        Args:
            lado (float): Longitud del lado del cubo
            
        Returns:
            float: Área de la superficie del cubo
        """
        pass
    
    def volumen_esfera(self, radio):
        """
        Calcula el volumen de una esfera.
        
        Args:
            radio (float): Radio de la esfera
            
        Returns:
            float: Volumen de la esfera
        """
        pass
    
    def area_superficie_esfera(self, radio):
        """
        Calcula el área de la superficie de una esfera.
        
        Args:
            radio (float): Radio de la esfera
            
        Returns:
            float: Área de la superficie de la esfera
        """
        pass
    
    def volumen_cilindro(self, radio, altura):
        """
        Calcula el volumen de un cilindro.
        
        Args:
            radio (float): Radio de la base del cilindro
            altura (float): Altura del cilindro
            
        Returns:
            float: Volumen del cilindro
        """
        pass
    
    def area_superficie_cilindro(self, radio, altura):
        """
        Calcula el área de la superficie de un cilindro.
        
        Args:
            radio (float): Radio de la base del cilindro
            altura (float): Altura del cilindro
            
        Returns:
            float: Área de la superficie del cilindro
        """
        pass
    
    def distancia_entre_puntos(self, x1, y1, x2, y2):
        """
        Calcula la distancia euclidiana entre dos puntos en un plano 2D.
        
        Args:
            x1 (float): Coordenada x del primer punto
            y1 (float): Coordenada y del primer punto
            x2 (float): Coordenada x del segundo punto
            y2 (float): Coordenada y del segundo punto
            
        Returns:
            float: Distancia entre los dos puntos
        """
        pass
    
    def punto_medio(self, x1, y1, x2, y2):
        """
        Calcula el punto medio entre dos puntos en un plano 2D.
        
        Args:
            x1 (float): Coordenada x del primer punto
            y1 (float): Coordenada y del primer punto
            x2 (float): Coordenada x del segundo punto
            y2 (float): Coordenada y del segundo punto
            
        Returns:
            tuple: Coordenadas (x, y) del punto medio
        """
        pass
    
    def pendiente_recta(self, x1, y1, x2, y2):
        """
        Calcula la pendiente de una recta que pasa por dos puntos.
        
        Args:
            x1 (float): Coordenada x del primer punto
            y1 (float): Coordenada y del primer punto
            x2 (float): Coordenada x del segundo punto
            y2 (float): Coordenada y del segundo punto
            
        Returns:
            float: Pendiente de la recta
        """
        pass
    
    def ecuacion_recta(self, x1, y1, x2, y2):
        """
        Obtiene los coeficientes de la ecuación de una recta en la forma Ax + By + C = 0.
        
        Args:
            x1 (float): Coordenada x del primer punto
            y1 (float): Coordenada y del primer punto
            x2 (float): Coordenada x del segundo punto
            y2 (float): Coordenada y del segundo punto
            
        Returns:
            tuple: Coeficientes (A, B, C) de la ecuación de la recta
        """
        pass
    
    def area_poligono_regular(self, num_lados, lado, apotema):
        """
        Calcula el área de un polígono regular.
        
        Args:
            num_lados (int): Número de lados del polígono
            lado (float): Longitud de cada lado
            apotema (float): Longitud de la apotema
            
        Returns:
            float: Área del polígono regular
        """
        pass
    
    def perimetro_poligono_regular(self, num_lados, lado):
        """
        Calcula el perímetro de un polígono regular.
        
        Args:
            num_lados (int): Número de lados del polígono
            lado (float): Longitud de cada lado
            
        Returns:
            float: Perímetro del polígono regular
        """
        pass
