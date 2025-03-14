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
        if lado < 0:
            raise ValueError("El lado debe ser un valor no negativo.")
        return lado ** 3
    
    def area_superficie_cubo(self, lado):
        if lado < 0:
            raise ValueError("El lado debe ser un valor no negativo.")
        return 6 * (lado ** 2)
    
    def volumen_esfera(self, radio):
        if radio < 0:
            raise ValueError("El radio debe ser un valor no negativo.")
        return (4/3) * math.pi * (radio ** 3)
    
    def area_superficie_esfera(self, radio):
        if radio < 0:
            raise ValueError("El radio debe ser un valor no negativo.")
        return 4 * math.pi * (radio ** 2)
    
    def volumen_cilindro(self, radio, altura):
        if radio < 0 or altura < 0:
            raise ValueError("El radio y la altura deben ser valores no negativos.")
        return math.pi * (radio ** 2) * altura
    
    def area_superficie_cilindro(self, radio, altura):
        if radio < 0 or altura < 0:
            raise ValueError("El radio y la altura deben ser valores no negativos.")
        area_lateral = 2 * math.pi * radio * altura
        area_bases = 2 * math.pi * (radio ** 2)
        return area_lateral + area_bases
    
    def distancia_entre_puntos(self, x1, y1, x2, y2):
        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return round(distancia, 2)
    
    def punto_medio(self, x1, y1, x2, y2):
        punto_x = (x1 + x2) / 2
        punto_y = (y1 + y2) / 2
        return (punto_x, punto_y)
    
    def pendiente_recta(self, x1, y1, x2, y2):
        if x2 == x1:
            raise ZeroDivisionError("La pendiente es infinita (línea vertical).")
        return (y2 - y1) / (x2 - x1)
    
    def ecuacion_recta(self, x1, y1, x2, y2):
        if x1 == x2:
            return (1, 0, -x1)
        elif y1 == y2:
            return (0, 1, -y1)
        else:
            m = (y2 - y1) / (x2 - x1)
            A = m
            B = -1
            C = y1 - m * x1
            factor = 1
            if A != 0:
                factor = 1 / A
            A, B, C = A * factor, B * factor, C * factor
            return (A, B, C)
    
    def area_poligono_regular(self, longitud_lado, n_lados, apotema):
        if apotema is None:
            apotema = longitud_lado / (2 * math.tan(math.pi / n_lados))
        
        perimetro = n_lados * longitud_lado
        area = (perimetro * apotema) / 2
        return area
    
    def perimetro_poligono_regular(self, n, l):
        return n * l
