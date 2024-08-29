import random, string
from os import system

class Password():
    def __init__(self):
        self.length = 0
        self.has_uppercase = False
        self.has_lowercase = False
        self.has_numbers = False
        self.has_symbols = False
        self.password = ''
    
    def setLength(self):
        try:
            self.length = int(input("Indica la longitud de la contraseña (4 - 128 caracteres): "))
            
            if self.length < 4 or self.length > 128:
                raise Exception
            
            self.setPassParams()
            
        except ValueError:
            print('ERROR!! La longitud debe de ser un nº entero.')
            self.setLength()
        
        except Exception:
            print('ERROR!! La longitud debe de ser entre 4 y 128 caracteres.')
            self.setLength()
        
        
        
    def useUpper(self):
        self.has_uppercase = not self.has_uppercase
        self.setPassParams()

    
    
    def useLower(self):
        self.has_lowercase = not self.has_lowercase
        self.setPassParams()

    
    
    def useNumbers(self):
        self.has_numbers = not self.has_numbers
        self.setPassParams()
    
    
    
    def useSymbols(self):
        self.has_symbols = not self.has_symbols
        self.setPassParams()

    
    
    def showPassParams(self):
        mayus = '[✓]' if self.has_uppercase else '[✗]'
        minus = '[✓]' if self.has_lowercase else '[✗]'
        nums = '[✓]' if self.has_numbers else '[✗]'
        simb = '[✓]' if self.has_symbols else '[✗]'
        
        print('1. Longitud de la contraseña: %s' %self.length)
        print('2. Mayúsculas', '%s' %mayus )
        print('3. Minúsculas', '%s' %minus )
        print('4. Números', '   %s' %nums )
        print('5. Símbolos', '  %s' %simb )
    
    
    
    def genPass(self):
        pass_chars = ''
        self.password = ''
        
        if self.has_uppercase:
            pass_chars = pass_chars + string.ascii_uppercase
        
        if self.has_lowercase:
            pass_chars = pass_chars + string.ascii_lowercase
        
        if self.has_numbers:
            pass_chars = pass_chars + string.digits
            
        if self.has_symbols:
            pass_chars = pass_chars + string.punctuation
        
        
        while self.length > 0:
            self.password = self.password + random.choice(pass_chars)
            self.length -= 1
        
        self.setPassParams()
        
        
        
    def setPassParams(self):
        system('cls')
        print('----- PARÁMETROS DE LA CONTRASEÑA -----')
        self.showPassParams()
        print('---------------------------------------\n')
        
        print('  [6] Generar contraseña.')
        print('  [7] Salir.\n\n')
        
        if self.password:
            print('\n')
            print('----------------- NUEVA CONTRASEÑA -----------------\n')
            print(self.password,'\n')
            print('----------------------------------------------------\n')
        
        try:
            option = int(input('Selecciona qué quieres editar: '))
            
            if option < 1 or option > 7:
                raise Exception
        
        except ValueError:
            print('ERROR!! Introduce un nº entero.')
            self.setPassParams()
        
        except Exception:
            print('ERROR!! Selecciona una opción válida.')
            self.setPassParams()
        
        
        if option == 1:
            self.setLength()
            
        if option == 2:
            self.useUpper()
            
        if option == 3:
            self.useLower()
            
        if option == 4:
            self.useNumbers()
            
        if option == 5:
            self.useSymbols()
            
        if option == 6:
            self.genPass()
        
        if option == 7:
            print('----------------------------------------------')
            print('              CERRANDO PROGRAMA')
            print('----------------------------------------------')
            exit()

        
new_Password = Password()
new_Password.setPassParams()
