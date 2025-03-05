class Strings:
    
    def es_palindromo(self, cadena: str) -> bool:
            cadena_limpia = ''.join(c for c in cadena if c.isalnum()).lower()
            return cadena_limpia == cadena_limpia[::-1]
    
    def invertir_cadena(self, cadena):
        return cadena[::-1]
    
    def contar_vocales(self, cadena: str) -> int:
        return sum(1 for c in cadena.lower() if c in "aeiou")
    
    def contar_consonantes(self, cadena: str) -> int:
        return sum(1 for c in cadena.lower() if c.isalpha() and c not in "aeiou")
    
    def es_anagrama(self, cadena1: str, cadena2: str) -> bool:
        return sorted(c.lower() for c in cadena1 if c.isalnum()) == sorted(c.lower() for c in cadena2 if c.isalnum())
    
    def contar_palabras(self, cadena: str) -> int:
        return len(cadena.split())
    
    def palabras_mayus(self, texto):
        return texto.title()
    
    def eliminar_espacios_duplicados(self, texto):
        return ' '.join(texto.strip().split())
    
    def es_numero_entero(self, texto):
        try:
            int(texto)
            return True
        except ValueError:
            return False
    
    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""
        for caracter in texto:
            if caracter.isalpha():  
                desplazamiento_real = desplazamiento % 26  
                codigo_base = ord('A') if caracter.isupper() else ord('a')
                nuevo_codigo = codigo_base + (ord(caracter) - codigo_base + desplazamiento_real) % 26
                resultado += chr(nuevo_codigo)
            else:
                resultado += caracter  
        return resultado
    
    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        pass