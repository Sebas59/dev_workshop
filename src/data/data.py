class Data:
    
    def invertir_lista(self, lista):
        lista.reverse()
        return lista
    
    def buscar_elemento(self, lista, elemento):
        if elemento in lista:
            return lista.index(elemento)
        return -1
    
    def eliminar_duplicados(self, lista):
        if not isinstance(lista, list):
            raise TypeError("El argumento debe ser una lista.")
        elementos_vistos = set()
        lista_sin_duplicados = []
        for elemento in lista:
            clave = (type(elemento), elemento)
            if clave not in elementos_vistos:
                elementos_vistos.add(clave)
                lista_sin_duplicados.append(elemento)
        return lista_sin_duplicados
    
    def merge_ordenado(self, lista1, lista2):
        if not isinstance(lista1, list) or not isinstance(lista2, list):
            raise TypeError("Los argumentos deben ser listas.")
        combinada = []
        i, j = 0, 0
        while i < len(lista1) and j < len(lista2):
            if lista1[i] < lista2[j]:
                combinada.append(lista1[i])
                i += 1
            else:
                combinada.append(lista2[j])
                j += 1
        while i < len(lista1):
            combinada.append(lista1[i])
            i += 1
        while j < len(lista2):
            combinada.append(lista2[j])
            j += 1
        return combinada
    
    def rotar_lista(self, lista, rotaciones):
        if not isinstance(lista, list):
            raise TypeError("El primer argumento debe ser una lista.")
        if not isinstance(rotaciones, int):
            raise TypeError("El segundo argumento debe ser un entero.")
        if not lista or rotaciones == 0:
            return lista
        rotaciones_efectivas = rotaciones % len(lista)
        return lista[-rotaciones_efectivas:] + lista[:-rotaciones_efectivas]
    
    def encuentra_numero_faltante(self, lista):
        if not lista:
            return None
        n = len(lista) + 1
        suma_esperada = (n * (n + 1)) // 2
        suma_real = sum(lista)
        return suma_esperada - suma_real
    
    def es_subconjunto(self, conjunto1, conjunto2):
        if not isinstance(conjunto1, list) or not isinstance(conjunto2, list):
            raise TypeError("Los argumentos deben ser listas.")
        if not conjunto1:
            return True
        return all(elemento in conjunto2 for elemento in conjunto1)
    
    def implementar_pila(self):
        stack = [] 
        def push(elemento):
            stack.append(elemento)

        def pop():
            if is_empty():
                raise IndexError("La pila está vacía")
            return stack.pop()
        def peek():
            if is_empty():
                raise IndexError("La pila está vacía")
            return stack[-1]
        def is_empty():
            return len(stack) == 0
        return {
            "push": push,
            "pop": pop,
            "peek": peek,
            "is_empty": is_empty,
        }
    
    def implementar_cola(self):
        cola = []  
        def enqueue(elemento):
            cola.append(elemento)
        def dequeue():
            if is_empty():
                raise IndexError("La cola está vacía")
            return cola.pop(0)
        def peek():
            if is_empty():
                raise IndexError("La cola está vacía")
            return cola[0]
        def is_empty():
            return len(cola) == 0
        return {
            "enqueue": enqueue,
            "dequeue": dequeue,
            "peek": peek,
            "is_empty": is_empty,
        }
    
    def matriz_transpuesta(self, matriz):
        if not isinstance(matriz, list) or not all(isinstance(fila, list) for fila in matriz):
            raise TypeError("La entrada debe ser una lista de listas.")
        if not matriz:
            return []
        return [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]