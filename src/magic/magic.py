class Magic:
    
    def fibonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(n - 1):
                a, b = b, a + b
            return b
    
    def secuencia_fibonacci(self, n):
        seq = [0, 1]
        for _ in range(2, n):
            seq.append(seq[-1] + seq[-2])
        return seq[:n]
    
    def es_primo(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def generar_primos(self, n):
        primos = []
        for i in range(2, n + 1):
            if self.es_primo(i):
                primos.append(i)
        return primos
    
    def es_numero_perfecto(self, n: int) -> bool:
        if n < 2:
            return False
        return sum(i for i in range(1, n) if n % i == 0) == n
    
    def triangulo_pascal(self, n: int) -> list:
        resultado = [[1]]
        for i in range(1, n):
            fila = [1]
            for j in range(1, i):
                fila.append(resultado[i-1][j-1] + resultado[i-1][j])
            fila.append(1)
            resultado.append(fila)
        return resultado[:n]
    
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado
    
    def mcd(self, a, b):
        while b:
            a, b = b, a % b
        return abs(a)
    
    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El mínimo común múltiplo de a y b
        """
        pass
    
    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.
        
        Args:
            n (int): Número para sumar sus dígitos
            
        Returns:
            int: La suma de los dígitos de n
        """
        pass
    
    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong (igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número de Armstrong, False en caso contrario
        """
        pass
    
    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).
        
        Args:
            matriz (list): Lista de listas que representa una matriz cuadrada
            
        Returns:
            bool: True si es un cuadrado mágico, False en caso contrario
        """
        pass