import re

class MooreMachine:
    def __init__(self):
        self.state = 'start'
        self.base = None

    def reset(self):
        self.state = 'start'
        self.base = None

    def transition(self, variable):
        variable = variable.replace('-', '')

        # Expresiones regulares para las diferentes bases
        binary_pattern = r'^[01]+$'
        octal_pattern = r'^[0-7]+$'
        hex_pattern = r'^[0-9a-fA-F]+$'

        # Validar si la variable cumple con la sintaxis de las bases
        if re.match(binary_pattern, variable):
            self.base = 'binaria'
            return True
        elif re.match(octal_pattern, variable):
            self.base = 'octal'
            return True
        elif re.match(hex_pattern, variable):
            self.base = 'hexadecimal'
            return True
        else:
            return False

    def process(self, variable):
        self.reset()
        if self.transition(variable):
            return True, self.base
        else:
            return False, None

# Funcion principal
def main():
    machine = MooreMachine()

    # Solicitar la entrada del usuario
    variable = input("Ingrese la declaracion de la variable: ")

    # Procesar la variable y determinar si es valida
    valid, base = machine.process(variable)

    if valid:
        print(f"La variable {variable} cumple con la sintaxis y es de base {base}.")
    else:
        print(f"La variable {variable} no cumple con la sintaxis.")

if __name__ == "__main__":
    main()

