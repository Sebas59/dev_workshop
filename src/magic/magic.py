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
        return abs(a * b) // self.mcd(a, b) if a and b else 0
    
    def suma_digitos(self, n):
        return sum(int(d) for d in str(abs(n)))
    
    def es_numero_armstrong(self, n: int) -> bool:
        num_str = str(n)
        num_digitos = len(num_str)
        return sum(int(d) ** num_digitos for d in num_str) == n
    
    def es_cuadrado_magico(self, matriz: list) -> bool:
        if not matriz or not matriz[0]:
            return False
        n = len(matriz)
        suma_magica = sum(matriz[0])
        
        for fila in matriz:
            if sum(fila) != suma_magica:
                return False
        
        for j in range(n):
            if sum(matriz[i][j] for i in range(n)) != suma_magica:
                return False

        if sum(matriz[i][i] for i in range(n)) != suma_magica:
            return False
        if sum(matriz[i][n - i - 1] for i in range(n)) != suma_magica:
            return False
        
        return True