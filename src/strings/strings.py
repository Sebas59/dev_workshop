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
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        pass
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        pass
    
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