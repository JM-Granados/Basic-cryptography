from copy import deepcopy

Alfabeto = 'abcdefghijklmnñopqrstuvwxyz'

def main(): 
    """
    Programa Principal encargada de implementar la interfaz de usuario del programa
    Entradas, y restricciones: 
    - Texto a codificarse, string 
    - Desplazamiento, int 
    Salidas: 
    - Texto Codificado 
    """
    global Alfabeto 
    Bienvenida()
    Seguir = True
    while Seguir: 
        Seguir, opcion = MenuPrincipal()
        if opcion != 's': 
            if opcion == 'a': 
                Cesar() 
            elif opcion == 'b': 
                Monoalfabetico() 
            elif opcion == 'c':
                Vigenere()
            elif opcion == 'd':
                PlayFair()
            elif opcion == "e":
                RailFence()
        
    CleanScreen()
    print("- " * 35)
    print("Gracias por usar nuestro programa")
    print("Vuelva pronto.")
    print()
    print("Intengrantes: ")
    print(" + Omar Jesús Zúñiga Campos.")
    print(" + Maria Daniela Chaves.")
    print(" + Jose Manuel Granados V.")
    print("- " * 35)
    print()
    Enter()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Subrutinas de main y globales  

def Bienvenida(): 
    """
    Subrutina la cual se encarga de presentar el programa, con una bereve introduccion de este
    Entras, y restricciones: 
    - N/A
    Salidas: 
    - Bienvenida impresa en la consola.
    """
    CleanScreen()
    print("Bienvenido al Programa de ") #https://patorjk.com/software/taag/#p=display&f=Big&t=Criptograf%C3%ADa%20y%20cifrado 
    print("   _____      _       _                         __ __                     _  __               _       ")
    print("  / ____|    (_)     | |                       / _/_/                    (_)/ _|             | |      ")
    print(" | |     _ __ _ _ __ | |_ ___   __ _ _ __ __ _| |_ _  __ _   _   _    ___ _| |_ _ __ __ _  __| | ___  ")
    print(" | |    | '__| | '_ \| __/ _ \ / _` | '__/ _` |  _| |/ _` | | | | |  / __| |  _| '__/ _` |/ _` |/ _ \ ")
    print(" | |____| |  | | |_) | || (_) | (_| | | | (_| | | | | (_| | | |_| | | (__| | | | | | (_| | (_| | (_) |")
    print("  \_____|_|  |_| .__/ \__\___/ \__, |_|  \__,_|_| |_|\__,_|  \__, |  \___|_|_| |_|  \__,_|\__,_|\___/ ")
    print("               | |              __/ |                         __/ |                                   ")
    print("               |_|             |___/                         |___/                                    ")
    print("Elaborado por Omar Jesús Zúñiga Campos, Maria Daniela Chaves, y Jose Manuel Granados V.") #Agregar Intengrantes, por si entran mas 
    print()
    Enter()
    CleanScreen()
    ResumenDelPrograma()
    Enter()

def CleanScreen(): #Uso global 
    """
    Subrutina la cual se encarga de limpiar la pantalla [consola]
    Entradas, y restricciones: 
    - N/A
    Salidas: 
    - 40 Lineas en Blanco
    """
    print("\n" * 40)

def ResumenDelPrograma(): 
    """
    Subrutina la cual se encarga de imprimir un breve resumen de la función del programa
    junto con las opciones de cifrado. 
    Entradas, y restricciones: 
    - N/A
    Salidas: 
    - Resumen, impreso en consola 
    - Opciones de cifrados, impreso en consola 
    """
    print("- " * 36)
    print("Este programa se encarga de codificar y descodificar mensajes o frases.")
    print("Utilizando cinco tipos diferentes de cifrados diferentes.") #Se puede mejorar el resumen 
    print("Cada uno con la opción de codificar o decodificar una palabra o texto. ")
    print("- " * 36)
    print()

def Enter(): #Uso global 
    """
    Subrutina la cual se encarga de agregar la opción al usuario para continuar 
    Entradas, y restricciones: 
    - N/A
    Salidas: 
    - Presiones 'Enter' para continuar
    """
    input("Presione 'Enter' para continuar: ")    

def MenuPrincipal():  
    """
    Subrutina la cual se encarga de mostrar un menú principal con las opciones de cifrado
    Este permite elegir una opción o salir del programa.
    Entradas, y restricciones: 
    - Tipo de Cifrado deseado por el usuario, str de una letra válida
    Salidas:  
    - A = Cifrado Cesar
    - B = Cifrado monoalfabético con palabra clave
    - C = Cifrado Vigenère
    - D = Cifrado PlayFair modificado
    - E = Cifrado Rail Fence
    - S = Salir del programa
    """
    CleanScreen()
    print("- " * 35)
    print("Que tipo de cifrado desea utilizar:")
    print()
    MenuPrincipalTexto()
    print("- " * 35)
    print()
    letra = input("Seleccione la opción deseada, al escribir su [letra] correspondiente: ")

    while not CheckPrincipal(letra): 
        CleanScreen()
        print("Opción seleccionada no válida. Porfavor seleccioné una opción válida: ")
        print()
        MenuPrincipalTexto()
        print()
        print("Opciones Válidas: ('a','b','c','d','e','s') ")
        letra = input('Porfavor seleccioné una opción válida: ')
    
    if letra in ('s','S'):
        letra = PrepararTextoCorto(letra)
        return (False, letra) 
    
    letra = PrepararTextoCorto(letra)
    return (True, letra)

def MenuPrincipalTexto():
    """
    Subrutina la cual se encarga de escribir el texto del menú principal del programa 
    Entradas, y restricciones: 
    - N/A
    Salidas: 
    - opciones del menú principal 
    """
    print("[A] Cifrado Cesar")
    print("[B] Cifrado monoalfabético con palabra clave")
    print("[C] Cifrado Vigenère")
    print("[D] Cifrado PlayFair modificado")
    print("[E] Cifrado Rail Fence")
    print("[S] 'Salir del Programa'")

def CheckPrincipal(opcion): 
    """
    Subrutina la cual se encarga de revisar que la opción elegida por el usuario sea válida
    Entradas, y Restricciones: 
    - Opción del usuario, int positivo 
    - Opción del usuario, str 'S'
    Salidas: 
    - Texto simplificado y revisado 
    """
    if type(opcion) != str: 
        return False 

    opcion = PrepararTextoCorto(opcion)
    if len(opcion) != 1 or opcion not in ('a','b','c','d','e','s'):
        return False 
    return True
    
def PrepararTextoCorto(texto): #Uso global + el texto ya ha de venir revisado 
    """
    Subrutina la cual se encarga de modificar un texto para simplificarlo 
    Entradas, y restricciones: 
    - Texto a modificar, str 
    Salidas: 
    - Texto modificado 
    """
    texto = texto.lower()
    texto = texto.strip()
    Lista = []

    texto2 = texto.split()
    for palabra in texto2: 
        txtNuevo = ''
        for letra in palabra: 
            letra = ReemplazarTildes(letra)
            txtNuevo += letra
        Lista.append(txtNuevo)
    
    return " ".join(Lista) 

def ReemplazarTildes(letra): #Uso global + el texto ya ha de venir revisado 
    """
    Subrutina la cual se encarga de reemplazar las tildes de una letra 
    Entradas, y restricciones: 
    - Letra, str 
    Salidas: 
    - letra sin tilde
    """
    if letra in ["á","é","í","ó","ú"]:
        letra = letra.replace("á", "a")
        letra = letra.replace("é", "e")
        letra = letra.replace("í", "i")
        letra = letra.replace("ó", "o")
        letra = letra.replace("ú", "u")
    return letra 
     
def CoD(texto): #Uso global + Opciones por cifrado 
    """
    Subrutina la cual se encarga de determinar si el usuario desea codificar o decodificar
    Entradas, y restricciones: 
    - N/A
    Salidas: 
    - Codificar 
    - Decodificar
    """
    CleanScreen()
    print(f"Ha seleccionado el {texto}.")
    print("¿Qué desea hacer? ")
    OpcionesCoD()
    opcion2 = input("Seleccione la opción deseada, al escribir su [letra] correspondiente: ")

    while not CheckCoD(opcion2): 
        CleanScreen()
        print("Opción Incorrecta. Por favor seleccione una opción válida")
        OpcionesCoD()
        print("Opciones Válidas: ('a','b','c') ")
        opcion2 = input('Porfavor seleccioné una opción válida: ')

    return PrepararTextoCorto(opcion2)
    
def OpcionesCoD():
    """
    Subrutina la cual escribe las opciones posibles, codificar, decodificar, salir. 
    Entradas y restricciones: 
    - N/A
    Salidas: 
    - Opciones impresas en consola
    """
    print()
    print("[A] Codificar")
    print("[B] Decodificar")
    print("[C] Seleccionar otro tipo de cifrado")
    print()

def CheckCoD(opcion2):
    """
    Subrutina la cual se encarga de chequear la entrada del usuario a la hora de decidir entre
    codificar y decodificar 
    Entradas, y restricciones: 
    - Opción, str in ['a','b']
    Salidas: 
    - True, codificar 
    - False, decodificar
    """
    if type(opcion2) != str: 
        return False 
    
    opcion2 = PrepararTextoCorto(opcion2)
    if len(opcion2) != 1 or opcion2 not in ('a','b','c'):
        return False
    return True

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#Cifrado Cesar - Finalizado 

def Cesar():
    """
    Función que se encarga de la ejecución del cifrado cesar, determina la acción que se realizara 
    Descifrar, Cifrar, salir. 
    Entradas y restricciones
    - Opción del usuario [a, b, c]
    Salidas: 
    - Código Cifrado 
    - Código Descifrado 
    - Salida para elegir un nuevo tipo de cifrado
    """
    opcion2 = CoD("Cifrado César")

    if opcion2 == 'c': 
        return 
    
    elif opcion2 =='a':
        dez, txt = CesarDatos()
        return cesarCod(dez, txt)

    elif opcion2 == 'b':
        dez, txt = CesarDatos() 
        return cesarDec(dez, txt)

def cesarCod(dez, txt): 
    """
    Subrutina encargada del proceso de codificado de un texto utilizando el cifrado Cesar 
    Entradas, y restricciones: 
    - Texto a codificarse, string 
    - Desplazamiento, int 
    Salidas: 
    - Texto Codificado
    """
    global Alfabeto
    txt2 = txt.split()
    lista = []

    for palabras in txt2: 
        txtNuevo = ''
        for letra in palabras:
            txtNuevo += Alfabeto[(Alfabeto.find(letra) + dez) % 27]
        lista.append(txtNuevo)
    
    return FinCesar(txt, dez, " ".join(lista))
             
def cesarDec(dez, txt): 
    """
    Subrutina la cual decodifica en texto con el cifrado de Cesar 
    Entradas, y restricciones: 
    - Desplazamiento, int positivo 
    - Texto, str 
    Salidas: 
    - Texto decodificado 
    """
    global Alfabeto 
    txt2 = txt.split()
    lista = []

    for palabras in txt2: 
        txtNuevo = ''
        for letra in palabras: 
            txtNuevo += Alfabeto[(Alfabeto.find(letra) - dez)]
        lista.append(txtNuevo)

    return FinCesar(txt, dez, " ".join(lista))

def CesarDatos(): 
    """
    Función la cual recibe los datos de usuario para el uso de cesarCod y cesarDec
    Entras y restricciones: 
    - Desplazamiento, int
    - Palabra o frase seleccionada, str
    Salidas: 
    - Desplazamiento revisado
    - Palabra o frase seleccionada revisada
    """
    CleanScreen()
    print("- " * 28)
    print("Cifrado César.")
    print("Por favor determine las variables para el cifrado.")
    print()
    Desplazamiento = IntDeCesarDatos()
    Texto = input("Texto o Palabra: ")
    print("- " * 28)

    while not CheckCesarDatos(Desplazamiento, Texto): 
        CleanScreen()
        print("- " * 28)
        print("Cifrado César.")
        print("Opciones seleccionadas no válidas.")
        print(" + El desplazamiento tiene que ser un entero positivo [0 a 26]")
        print(" + El texto tiene que ser un 'texto'")
        print()    
        Desplazamiento = IntDeCesarDatos()
        Texto = input("Texto o Palabra: ")

    return Desplazamiento, PrepararTextoCorto(Texto)

def CheckCesarDatos(dez, txt): 
    """
    Función la cual se encarga de revisar los datos recibidos en la función de cesar
    Entradas y restricciones: 
    - Desplazamiento, int positivo entre 1 y 26
    - Texto, str 
    Salidas: 
    - True, funciona 
    - False, no funciona
    """
    if type(txt) != str or dez < 0 or dez > 26:
        return False

    if txt == "":
        return False

    for i in txt: 
        if i.lower() not in " aábcdeéfghiíjklmnñoópqrstuúvwxyz":
            return False 

    return True

def FinCesar(txt, dez, txt2): 
    """
    Función que muestra el resultado de codificar o descodificar em modos César
    Entradas y restricciones
    txt: texto hecho por el usuario
    dez: cuantos espacio hay que desplazarze
    Salida:
    txt2: resultado final
    """
    CleanScreen()
    print("- " * 33)
    print("Cifrado César")
    print(f"Su texto: {txt}")
    print(f"Con un desplazamiento {dez}, se ve de la siguiente manera: " )
    print()
    print(txt2)
    print("- " * 33)
    print()
    Enter()

def IntDeCesarDatos(): 
    """
    Función encargada de procesar el desplazamiento en el alfabeto que el usuario
    pidió.
    Entradas y restricciones
    Desplazamiento: número entero
    Salidas:
    Desplazamiento
    """
    seguir = True
    while seguir:
        try:
            Desplazamiento = int(input("Desplazamiento del Alfabeto: ")) 
            seguir = False
            print()
        except:
            CleanScreen()
            print("- " * 28)
            print("Cifrado César.")
            print("Por favor determine las variables para el cifrado.")
            print("El desplazamiento tiene que ser un valor [0 a 26]")
            print()
    return Desplazamiento

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#Cifrado Mono alfabetico 

def Monoalfabetico():
    """
    Subrutina la cual se encarga del proceso del cifrado monoalfabetico 
    este funciona como un menú principal del cifrado monoalfabetico con palabra clave 
    Entradas, y restricciones: 
    - Opción del usuario [a, b, c]
    Salidas: 
    - Código Cifrado 
    - Código Descifrado 
    - Salida para elegir un nuevo tipo de cifrado 
    """
    opcion3 = CoD("Cifrado monoalfabético con palabra clave")

    if opcion3 == 'c': 
        return 

    elif opcion3 == 'a': 
        txt, Pclave = TextoyPclaveDatos("Cifrado monoalfabético con palabra clave.")
        return monoCod(txt, Pclave)

    elif opcion3 == 'b': 
        txt, Pclave = TextoyPclaveDatos("Cifrado monoalfabético con palabra clave.")
        return monoDec(txt, Pclave)

def monoCod(txt, Pclave): 
    """
    Subrutina la cual se encarga de codificar en Cifrado monoalfabético con palabra clave
    una palabra o frase dependiendo de la palabra clave 
    Entradas, y restricciones: 
    - Palabra Clave, str | len() == 1
    - Texto, str
    Salidas: 
    - Palabra/frase codificada
    """
    global Alfabeto
    PclaveSafe = Pclave
    Pclave = RemoverLetrasRepetidas(Pclave)
    NuevoAlfabeto = Pclave
    ListaNueva = []

    for i in Alfabeto: 
        if i not in Pclave: 
            NuevoAlfabeto += i 

    txt2 = txt.split()
    for palabra in txt2:
        txtNuevo = '' 
        for letra in palabra:
            txtNuevo += NuevoAlfabeto[Alfabeto.index(letra)] 
        ListaNueva.append(txtNuevo)
    
    return FinCifrado(txt, PclaveSafe,ListaNueva, "Cifrado monoalfabético con palabra clave")
            
def monoDec(txt, Pclave): 
    """
    Subrutina la cual se encarga de decodificar en Cifrado monoalfabético con palabra clave
    una palabra o frase dependiendo de la palabra clave 
    Entradas, y restricciones: 
    - Palabra Clave, str | len() == 1
    - Texto, str
    Salidas: 
    - Palabra/frase decodificada    
    """
    global Alfabeto
    PclaveSafe = Pclave
    Pclave = RemoverLetrasRepetidas(Pclave)
    NuevoAlfabeto = Pclave
    ListaNueva = []

    for i in Alfabeto: 
        if i not in Pclave: 
            NuevoAlfabeto += i 
    
    txt2 = txt.split()
    for palabra in txt2:
        txtNuevo = '' 
        for letra in palabra:
            txtNuevo += Alfabeto[NuevoAlfabeto.index(letra)] 
        ListaNueva.append(txtNuevo)
    
    return FinCifrado(txt, PclaveSafe,ListaNueva,"Cifrado monoalfabético con palabra clave")

def RemoverLetrasRepetidas(palabra): #llegar ya revisado 
    """
    Subrutina la cual se encarga de remover letras repetidas en un string 
    Entradas, y restricciones: 
    - Palabra, str 
    Salidas: 
    - Palabra sin letras repetidas
    """
    Lista = []
    ListaNueva = []
    
    for i in palabra: 
        Lista.append(i)

    for letra in Lista: 
        if letra in ListaNueva: 
            pass 
        else: 
            ListaNueva.append(letra)
                    
    return "".join(ListaNueva) 

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#Funciones Generales para Vigenre y monoalfabetico

def TextoyPclaveDatos(nombre):
    """
    Subrutina la cual se encarga de recibir los datos del usuario a la hora de 
    codificar/decodificar en el cifrado monoalfabetico con palabra clave 
    Entradas, y restricciones: 
    - Palabra clave, str
    - Texto, str
    Salidas: 
    - Palabra clave modificada para el uso del sistema
    - Texto modificado para el uso del sistema
    """
    CleanScreen()
    print("- " * 28)
    print(nombre)
    print("Por favor determine las variables para el cifrado.")
    print()
    PalabraClave = input("Palabra clave: ")
    print()
    Texto = input("Texto o Palabra: ")
    print("- " * 28)

    while not CheckPclaveyTextoDatos(Texto, PalabraClave):
        CleanScreen()
        print("- " * 28)
        print(nombre)
        print('Opciones seleccionadas no válidas.')
        print("- " * 28)
        print("Solo se aceptan los caracteres: ")
        print(' aábcdeéfghiíjklmnñoópqrstuúvwxyz')
        print()
        PalabraClave = input("Palabra clave [una sola palabra]: ")
        print()
        Texto = input("Texto o Palabra: ")
    
    return PrepararTextoCorto(Texto), PrepararTextoCorto(PalabraClave)

def CheckPclaveyTextoDatos(txt, clave): 
    """
    Subrutina la cual se encarga de revisar que los datos entregados por el usuario sean 
    válidos. 
    Entradas, y restricciones: 
    - Palabra clave, str 
    - Texto o Palabra, str 
    Salidas: 
    - True, son válidos 
    - False, no es válido
    """
    if type(txt) != str or type(clave) != str: 
        return False

    if txt == "" or clave == "":
        return False

    for letra in clave: 
        if letra.lower() not in " aábcdeéfghiíjklmnñoópqrstuúvwxyz":
            return False 

    for letra in txt: 
        if letra.lower() not in " aábcdeéfghiíjklmnñoópqrstuúvwxyz":
            return False 

    clave = PrepararTextoCorto(clave)
    if len(clave.split()) != 1: 
        return False
    
    return True

def FinCifrado(txt, PclaveSafe, ListaNueva, cifrado): #Uso global
    """
    Subrutina la cual se encarga de imprimir los resultados  de descodificación y codificación de los 
    monoalfabetico y vigere
    Entradas y restricciones: 
    - texto del usuario, str
    - Palabra clave del usuario, str
    Salidas: 
    - Datos impresos en pantalla
    """
    if type(ListaNueva) == list: 
        ListaNueva = " ".join(ListaNueva)
    
    CleanScreen()
    print("- " * 33)
    print(cifrado)
    print(f"Su texto: '{txt}'")
    print(f"Con su palabra clave '{PclaveSafe}', se ve de la siguiente manera: " )
    print()
    print(ListaNueva)
    print("- " * 33)
    print()
    Enter()

#Hasta aqui se reviso la ortografia del programa. 4/24/2022
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#Cifrado Vigenere

def Vigenere(): 
    """
    Subrutina la cual se encarga de del proceso del cifrado Vigenere
    este funciona como un menu principal del cifrado Vigenere
    Entradas y restricciones: 
    - Opcion del usuario [a, b, c]
    Salidas: 
    - Codigo Cifrado 
    - Codigo Descrifado 
    - Salida para elegir un nuevo tipo de cifrado
    """
    opcion4 = CoD("Cifrado Vigenère")

    if opcion4 == 'c': 
        return 

    elif opcion4 == 'a': 
        txt, Pclave = TextoyPclaveDatos("Cifrado Vigenère")
        return VigenereCod(txt, Pclave)

    elif opcion4 == 'b': 
        txt, Pclave = TextoyPclaveDatos("Cifrado Vigenère")
        return VigenereDec(txt, Pclave)

def VigenereCod(txt, Pclave): 
    """ 
    Subrutina la cual se encarga de el cifrado de un texto utilizando el cifrado vigenere 
    Entradas y restricciones: 
    - texto deseado a modificar, str 
    - palabra clave, str 
    Salidas: 
    - Texto codificado
    """
    global Alfabeto 
    ValorNuevo = ValorDeNuevoTexto(txt, Pclave, Alfabeto, "codificar")
    ListaNueva = []

    for palabras in ValorNuevo:
        ListaNueva.append("".join(palabras))

    Dato =  " ".join(ListaNueva)

    FinCifrado(txt, Pclave, ListaNueva, "Cifrado Vigenère")

def VigenereDec(txt, Pclave):
    """
    Subrutina la cual se encarga de decoficar el texto dado por el ususario, junto con su palabra clave 
    Entradas y restricciones: 
    - texto deseado a modificar, str 
    - palabra clave, str 
    Salidas: 
    - Texto codificado
    """
    global Alfabeto
    ValorNuevo = ValorDeNuevoTexto(txt, Pclave, Alfabeto, "decodificar")
    ListaNueva = []

    for palabras in ValorNuevo:
        ListaNueva.append("".join(palabras))

    FinCifrado(txt, Pclave, ListaNueva, "Cifrado Vigenère")

def ValorDeNuevoTexto(txt, clave, alfabeto, llave):
    """
    Subrutina la cual se encarga de asignarle a un texto la suma de los valores del texto + la palabra clave 
    Esto dandonos los valores del texto codificar o decodificado
    Entradas y restricciones 
    - Texto a querer modificar, str 
    - Palabra Clave, str 
    Salidas 
    - Valores del nuevo texto/palabra 
    """
    txt = PrepararTextoCorto(txt)
    txt2 = txt.split()
    ValorNuevo = []
    ListaFinal = []
    clave = clave.replace(" ", "")
    PosClave = -1 

    for palabras in txt2: 
        ValorNuevo.clear() 
        for letra in palabras: 
            PosClave += 1
            if PosClave >= len(clave):
                PosClave = 0

            valor1 = alfabeto.find(letra)
            valor2 = alfabeto.find(clave[PosClave])

            valorTotal = DecisionDeSuma(valor1, valor2, llave)
            
            ValorNuevo.append(alfabeto[valorTotal])
            
        ListaFinal.append(ValorNuevo)
        ListaFinal = deepcopy(ListaFinal)
 
    return ListaFinal

def DecisionDeSuma(valor1, valor2, llave): 
    """
    Subrutina la cual se encarga de definir si sumar(codificar) o restar(decodificar)
    Entradas, y retricciones: 
    - Valor1, int 
    - Valor2, int 
    Salidas: 
    - Sumar de valores junto con % 27 
    - Resta de valores
    """
    if llave == "codificar": 
        return (valor1 + valor2) % 27 
    else: 
        return valor1 - valor2

def FinVigere(txt, clave, resultado):
    """
    Subrutina la cual se encarga de imprimir los resultados  de descodificación y codificación de VigereCod 
    y VigereDec
    Entradas y restricciones: 
    - texto del usuario, str
    - Palabra clave del usuario, str
    Salidas: 
    - Datos impresos en pantalla
    """
    
    CleanScreen()
    print("- " * 33)
    print("Cifrado Vigenère")
    print(f"Su texto: '{txt}'")
    print(f"Con su palabra clave {clave}, se ve de la siguiente manera: " )
    print()
    print(resultado)
    print("- " * 33)
    print()
    Enter()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#Cifrado PlayFair modificado 

def PlayFair():
    """
   Subrutina la cual se encarga de recibir las opcion seleccionada por usuario y realizar su determinada tarea 
    Entradas y restricciones: 
    - Entradas y restricciones:
    opción4: el usuario elige que desea hacer una vez elegido el modo, solo puede ser una letra (a, b, c)
    Salidas: 
    - Devolverse (c)
    """
    opcion4 = CoD("Cifrado PlayFair modificado")

    if opcion4 == 'c': 
        return 

    elif opcion4 == 'a': 
        txt, Pclave = DatosPlayFair("Cifrado PlayFair modificado")
        return playFairCod(txt, Pclave)

    elif opcion4 == 'b': 
        txt, Pclave = DatosPlayFair("Cifrado PlayFair modificado")
        return playFairDec(txt, Pclave)

def playFairCod(txt, clave): 
    """
    Subrutina que se encarga de encriptar el mensaje en modo Play Fair.
    Entradas y restricciones:
    -txt: palabra o frase que se desea modificar, str.
    -clave: palabra clave, str.
    Salidas:
    texto codificado
    """
    global Alfabeto
    claveSafe = clave
    clave = RemoverLetrasRepetidas(clave)
    txtSafe = txt

    #Crea alfabeto Nuevo junto con su matriz 
    AlfabetoNuevo = clave + "".join([x for x in Alfabeto if x not in clave])
    Matriz = [AlfabetoNuevo[:5],AlfabetoNuevo[5:10] ,AlfabetoNuevo[10:15] , AlfabetoNuevo[15:20] , AlfabetoNuevo[20:25] , AlfabetoNuevo[25:] + "123"]

    #Revisa que si una letra se repite en una palabra esta se le agrega un 1 por repeticion - Completo -No para Dec
    txtLista = []
    for i in range(len(txt) - 1):
        txtLista.append(txt[i])
        if txt[i] == txt[i + 1]:
            txtLista.append("1")
    txtLista.append(txt[-1])
    txt = "".join(txtLista)

    #Revisa que si un palabra es impar se le agrega un 1 al final - Completo -No para Dec
    txtLista = txt.split()
    Postemporal = 0 
    txtListaComplete = deepcopy(txtLista)
    for palabra in txtLista:
        if len(palabra) % 2 == 1:
            txtListaComplete.pop(Postemporal)
            txtListaComplete.insert(Postemporal, palabra + "1")
        Postemporal += 1
    
    txtFiltrado = txtListaComplete
    print(txtListaComplete)

    #Crea los pares apartir de la lista - Completa
    pares = [] #Pares para todo el sistema
    par = [] #Par temporal 
    parPalabra = [] #Par por palabra 
    #print(txtFiltrado)
    for palabra in txtFiltrado: 
        for letra in palabra:
            par.append(letra)
            if len(par) == 2: 
                parPalabra.append("".join(par))
                #parPalabra = deepcopy(parPalabra)
                par.clear()

        pares.append(parPalabra)
        pares = deepcopy(pares)
        #print(pares)
        parPalabra.clear()


    #Crea la lista final del sistema "resultado"
    ListaFinal = []
    ResultadoFinal = ""
    for palabras in pares:#fila, columna
        for i in palabras:
            #ListaCod = [] 
            #print(i)
            #[a ,b]
            Posicion0 = definirFilayColumna(Matriz, i[0]) #L[0] es x y L[1] es y #Posicion de A
            Posicion1 = definirFilayColumna(Matriz, i[1]) #Posicion de B 
            
            if Posicion0[1] == Posicion1[1]: #caso #3
                NuevaFila0 = (Posicion0[0] + 1) % 6
                NuevaFila1 = (Posicion1[0] + 1) % 6

                NuevoValor0 = Matriz[NuevaFila0][Posicion0[1]]
                NuevoValor1 = Matriz[NuevaFila1][Posicion1[1]]
                ListaFinal.append(NuevoValor0 + NuevoValor1)
            
            elif Posicion0[0] == Posicion1[0]: #caso #2
                NuevaColumna0 = (Posicion0[1] + 1) % 5
                NuevaColumna1 = (Posicion1[1] + 1) % 5 

                NuevoValor0 = Matriz[Posicion0[0]][NuevaColumna0]
                NuevoValor1 = Matriz[Posicion1[0]][NuevaColumna1]
                #print(NuevoValor0 + NuevoValor1)
                ListaFinal.append(NuevoValor0 + NuevoValor1 )
            
            else: #caso #1
                NuevoValor0 = Matriz[Posicion0[0]][Posicion1[1]]
                NuevoValor1 = Matriz[Posicion1[0]][Posicion0[1]]

                ListaFinal.append(NuevoValor0 + NuevoValor1 )

        ResultadoFinal += "".join(ListaFinal) + " "
        ListaFinal.clear()

    
    return FinCifrado(txtSafe, claveSafe, ResultadoFinal, "Cifrado PlayFair modificado")
     
def definirFilayColumna(matriz, valor): 
    """
    Subrutina que define la posición de las letras de cada par según el alfabeto nuevo
    Entradas y restricciones:
    matriz: alfabeto nuevo
    valor: letra
    Salida:
    posicion de letras en cada par
    """
    for i in range(len(matriz)): 
        if valor in matriz[i]: 
            posicion =  i, matriz[i].index(valor)

    return posicion

def ErrorDeTextoFair(nombre): 
    """
    Función para ver si el mensaje hecho por el usuario es válido.
    Entrada:
    nombre: texto del usuario
    Salida:
    Continua con la operación si el mensaje es válido, si no le dice
    el error al usuario y vuelve a pedir la entrada.
    """
    CleanScreen()
    print("- " * 28)
    print(nombre)
    print("Por favor determine las variables para el cifrado.")
    print("Recuerde que las palabras deben de tener un valor par.")
    print()
    PalabraClave = input("Palabra clave: ")
    print()
    Texto = input("Texto o Palabra: ")
    print("- " * 28)

    while not CheckPclaveyTextoDatos(Texto, PalabraClave):
        CleanScreen()
        print("- " * 28)
        print(nombre)
        print('Opciones seleccionadas no válidas.')
        print("- " * 28)
        print("Solo se aceptan los caracteres: ")
        print(' aábcdeéfghiíjklmnñoópqrstuúvwxyz')
        print("Recuerde que las palabras deben de tener un valor par")
        print()
        PalabraClave = input("Palabra clave [una sola palabra]: ")
        print()
        Texto = input("Texto o Palabra: ")
    
    txt = PrepararTextoCorto(Texto)
    PClave = PrepararTextoCorto(PalabraClave)
    return txt, PClave 

def playFairDec(txt, clave):
    """
    Subrutina para desencriptar un mensaje escrito en código PlayFair modificado
    Entradas y restricciones:
    -txt: mensaje a desencriptar, str.
    -clave: palabra clave
    Salida:
    mensaje desencriptado.
    """
    global Alfabeto

    ListaCheckPar = txt.split()
    seguir = True

    while seguir:
        for palabras in ListaCheckPar: 
            if len(palabras) % 2 == 1:             
                txt, clave = ErrorDeTextoFair("Cifrado PlayFair modificado")
                seguir = True
            else: 
                seguir = False
        ListaCheckPar = txt.split()
    
    claveSafe = clave
    clave = RemoverLetrasRepetidas(clave)
    txtSafe = txt

    #Crea alfabeto Nuevo junto con su matriz 
    AlfabetoNuevo = clave + "".join([x for x in Alfabeto if x not in clave])
    Matriz = [AlfabetoNuevo[:5],AlfabetoNuevo[5:10] ,AlfabetoNuevo[10:15] , AlfabetoNuevo[15:20] , AlfabetoNuevo[20:25] , AlfabetoNuevo[25:] + "123"] 
            
    #Hacer pares
    txtFiltrado = txt.split()
    paresDec = [] #Pares para todo el sistema
    parDec = [] #Par temporal 
    parPalabraDec = [] #Par por palabra 
    for palabra in txtFiltrado: 
        for letra in palabra:
            parDec.append(letra)
            if len(parDec) == 2: 
                parPalabraDec.append("".join(parDec))
                #parPalabra = deepcopy(parPalabra)
                parDec.clear()

        paresDec.append(parPalabraDec)
        paresDec = deepcopy(paresDec)
        #print(pares)
        parPalabraDec.clear()

    #Decodificar 
    ListaFinal = []
    ResultadoFinal = ""
    for palabras in paresDec:#fila, columna
        for i in palabras:
            #ListaCod = [] 
            #print(i)
            #[a ,b]
            Posicion0 = definirFilayColumna(Matriz, i[0]) #L[0] es x y L[1] es y #Posicion de A
            Posicion1 = definirFilayColumna(Matriz, i[1]) #Posicion de B 
            
            if Posicion0[1] == Posicion1[1]: #caso #3
                NuevaFila0 = (Posicion0[0] - 1) 
                NuevaFila1 = (Posicion1[0] - 1) 

                NuevoValor0 = Matriz[NuevaFila0][Posicion0[1]]
                NuevoValor1 = Matriz[NuevaFila1][Posicion1[1]]
                ListaFinal.append(NuevoValor0 + NuevoValor1)
            
            elif Posicion0[0] == Posicion1[0]: #caso #2
                NuevaColumna0 = (Posicion0[1] - 1) 
                NuevaColumna1 = (Posicion1[1] - 1)  

                NuevoValor0 = Matriz[Posicion0[0]][NuevaColumna0]
                NuevoValor1 = Matriz[Posicion1[0]][NuevaColumna1]
                #print(NuevoValor0 + NuevoValor1)
                ListaFinal.append(NuevoValor0 + NuevoValor1 )
            
            else: #caso #1
                NuevoValor0 = Matriz[Posicion0[0]][Posicion1[1]]
                NuevoValor1 = Matriz[Posicion1[0]][Posicion0[1]]

                ListaFinal.append(NuevoValor0 + NuevoValor1 )

        ResultadoFinal += "".join(ListaFinal) + " "
        ListaFinal.clear()

    #Eliminar numeros del final
    ResultadoFinal = ResultadoFinal.replace("1", "")

    return FinCifrado(txtSafe, claveSafe, ResultadoFinal, "Cifrado PlayFair modificado")

def DatosPlayFair(nombre): 
    """
    Función para introducir la palabra clave y el texto a decodificar
    Entradas:
    -texto: frase que el usuario desea que sea descifrado, no acepta signos de
    puntuación ni números que sean 1, 2, 3.
    -clave: palabra clave para hacer alfabeto
    -nombre: Título del Cifrado PlayFair modificado
    Salidas:
    Clave y texto simplificados
    """
    CleanScreen()
    print("- " * 28)
    print(nombre)
    print("Por favor determine las variables para el cifrado.")
    print()
    PalabraClave = input("Palabra clave: ")
    print()
    Texto = input("Texto o Palabra: ")
    print("- " * 28)

    while not CheckDatosPlayFair(Texto, PalabraClave):
        CleanScreen()
        print("- " * 28)
        print(nombre)
        print('Opciones seleccionadas no válidas.')
        print("- " * 28)
        print("Solo se aceptan los caracteres: ")
        print(' aábcdeéfghiíjklmnñoópqrstuúvwxyz')
        print("Junto con los numeros [1,2,3] para el texto a decodificar.")
        print()
        PalabraClave = input("Palabra clave [una sola palabra]: ")
        print()
        Texto = input("Texto o Palabra: ")
    
    return PrepararTextoCorto(Texto), PrepararTextoCorto(PalabraClave) 

def CheckDatosPlayFair(txt, clave):  
    """
    Función que revisa si la clave y el texto son válidos para la codificación
    Entradas y restricciones:
    -txt: texto a desencriptar
    -clave: palabra clave
    Ninguno puede estar vacío o incluir símbolos
    Clave no puede tener números, txt solo puede tener 1, 2, 3
    Ambos deben ser strings, n
    Salidas:
    Dice si txt y clave son válidos
    """
    if type(txt) != str or type(clave) != str: 
        return False

    if txt == "" or clave == "":
        return False

    for letra in clave: 
        if letra.lower() not in " aábcdeéfghiíjklmnñoópqrstuúvwxyz":
            return False 

    for letra in txt: 
        if letra.lower() not in " aábcdeéfghiíjklmnñoópqrstuúvwxyz123":
            return False 

    clave = PrepararTextoCorto(clave)
    if len(clave.split()) != 1: 
        return False
    
    return True

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#Cifrado Rail Fence - Falta documentacion Total

def RailFence():
    """
    Elige que hacer en el modo Rail Fence, (codificar, descodificar, regresar)
    No hay entradas
    Salidas:
    Si el usuario elige c, este regrasa.
    """
    opcion4 = CoD("Cifrado Rail Fence")

    if opcion4 == 'c': 
        return 

    elif opcion4 == 'a': 
        txt = RailFenceOpciones("Cifrado Rail Fence")
        RailFenceCod(txt)

    elif opcion4 == 'b': 
        txt = RailFenceOpciones("Cifrado Rail Fence")
        RailFenceDec(txt)

def RailFenceOpciones(txt): #Cambiar lo del multiplo de 4 
    """
    Función para poner el texto y revisar si es válido
    Entradas y restricciones:
    -Texto = palabra o palabras a codificar o decodificar
    Salida:
    Texto sin espacios al principio o el final
    """
    CleanScreen()
    print("- " * 28)
    print(txt)
    print("Por favor determine las variables para el cifrado.")
    print()
    Texto = input("Texto o Palabra: ")
    print("- " * 28)

    while not CheckRailFence(Texto):
        CleanScreen()
        print("- " * 28)
        print(txt)
        print('Opciones seleccionadas no válidas.')
        print("- " * 28)
        print("Solo se aceptan los caracteres: ")
        print(' aábcdeéfghiíjklmnñoópqrstuúvwxyz-')
        print()
        Texto = input("Texto o Palabra: ")
    
    return Texto.strip() 

def CheckRailFence(txt):
    """
    Función que revisa que txt sea válido
    Entradas y restricciones
    -txt: debe ser un string, solo acepta letras del alfabeto español  
    Salida:
    Dice si txt es válido
    """
    if type(txt) != str: 
        return False

    if txt == "":
        return False

    for letra in txt: 
        if letra.lower() not in " aábcdeéfghiíjklmnñoópqrstuúvwxyz-":
            return False 
    
    return True

def RailFenceCod(txt):
    """
    Función para codificar un texto en modo Rail Fence
    Entradas:
    -txt: es un string
    Salida:
    txt codificado
    """
    txtSafe = txt
    #Preparar texto
    while len(txt) % 4 != 0: 
        txt += " "
    
    txt = txt.replace(" ", "-")

    #Los separa en las filas 
    Fila1 = txt[::4]  
    Fila2 = txt[1::2]
    Fila3 = txt[2::4]

    Resultado = Fila1 + Fila2 + Fila3
    print(Resultado)

    contador = 0
    ResultadoTotal = ""
    for letra in Resultado: 
        if contador == 0: 
            ResultadoTotal += " "
        ResultadoTotal += letra 
        contador = (contador + 1) % 5 

    ResultadoTotal = ResultadoTotal.strip()

    return FinRailFence(txtSafe, ResultadoTotal)

def RailFenceDec(txt):
    """
    Función para decodificar mensaje escrito en modo Rail Fence
    Entradas y restriccones
    txt:
    Salidas:
    """
    txtSafe = txt
    txt = txt.replace(" ", "")

    seguir = True
    while seguir:
        if len(txt) % 4 != 0:             
            txt = RailFenceOpciones("Cifrado PlayFair modificado")
            txt = txt.replace(" ", "")
            seguir = True
        else: 
            seguir = False

    ValorMedio = len(txt) // 2 
    ValorExterior = (len(txt) - ValorMedio) // 2
    ValorMedio = ValorMedio + ValorExterior

    Fila1 = txt[:ValorExterior]  
    Fila2 = txt[ValorExterior : ValorMedio]
    Fila3 = txt[ValorMedio:]

    ResultadoTotal = ""

    for i in range(ValorExterior):

        ResultadoTotal += Fila1[0]
        Fila1 = Fila1[1:]

        ResultadoTotal += Fila2[0]
        Fila2 = Fila2[1:]
        
        ResultadoTotal += Fila3[0]
        Fila3 = Fila3[1:]
        
        ResultadoTotal += Fila2[0]
        Fila2 = Fila2[1:]
    
    resultado = ResultadoTotal.replace("-", " ")
    resultado = resultado.strip()

    return FinRailFence(txtSafe, resultado)
          
def FinRailFence(txt, resultado):
    """
    Función que muestra el resultado del modo Rail Fence
    Entrada:
    resultado y txt
    Salida:
    Imprime el resultado
    """
    CleanScreen()
    print("- " * 33)
    print("Cifrado Rail Fence")
    print(f"Su texto: '{txt}'")
    print(f"Se ve de la siguiente manera: " )
    print()
    print(resultado)
    print("- " * 33)
    print()
    Enter()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

main()
