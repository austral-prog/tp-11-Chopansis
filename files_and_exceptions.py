def read_file_to_dict(nombre_archivo):
    ventas = {}

    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read().strip()
            pares = contenido.split(";")

            for par in pares:
                if par:
                    try:
                        producto, valor = par.split(":")
                        valor = float(valor)

                        if producto not in ventas:
                            ventas[producto] = []
                        ventas[producto].append(valor)
                    except ValueError:
                        print(f"Error de formato en el par: '{par}', se ignora.")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
        raise  # Importante para que los tests puedan capturarlo
    except Exception as e:
        print(f"Ocurrió un error inesperado al leer el archivo: {e}")
        return None

    return ventas


def process_dict(ventas):
    for producto, montos in ventas.items():
        total = sum(montos)
        promedio = total / len(montos)
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")


# Ejemplo de uso si se ejecuta como programa principal
if __name__ == "__main__":
    archivo = "datos_ventas.txt"
    try:
        ventas = read_file_to_dict(archivo)
        if ventas:
            process_dict(ventas)
    except FileNotFoundError:
        pass  # Ya se imprimió el mensaje dentro de la función
