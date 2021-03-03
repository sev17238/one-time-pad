######################################################
# Luis Delgado 17XXX
# Diego Sevilla 17238
######################################################
# test.py
######################################################
# Python3 program to....
######################################################

# imports _________________________

import string    
import random

# Functions area______________________________________________
# Genera un string random para realizar la encripción
def generar_random_string(cadena):
    #generar string de 0 a 10 caracter de longitud mayor
    longitud=len(cadena)+random.randint(0,10)
    #Generador de string random extraido de https://www.javatpoint.com/python-program-to-generate-a-random-string
    random_string = ''.join(random.choices(string.ascii_letters + string.punctuation + string.digits, k = longitud))
    return random_string

#Proceso para operar 2 string por medio de xor.
def operar_strings(param1,param2):
    #convertir string de caracteres a string de 0s y 1s
    #linea de codigo extraida de https://www.geeksforgeeks.org/python-convert-string-to-binary/
    binary_original = ''.join(format(ord(i), '08b') for i in param1) 
    binary_pad = ''.join(format(ord(i), '08b') for i in param2)
    #obtiene la longitud de las cadenas para operaciones diversas
    length_binary_original=len(binary_original)
    length_binary_pad=len(binary_pad)
    #asegura que las cadenas sean de la misma longitud
    while(length_binary_original<length_binary_pad):
        binary_original=binary_original+"0"
        length_binary_original=len(binary_original)
    binary_operated=""
    #operar los strings
    for j in range(length_binary_original):
        binary_operated=binary_operated+aplicar_xor(binary_original[j],binary_pad[j])
    return from_binary_string(binary_operated)
        

#convertir de una cadena de 0s y 1s a     
def from_binary_string(string):
    limite_inferior=0
    limite_superior=8
    string_a_devolver=""
    while (len(string)>=limite_superior):
        string_a_devolver=string_a_devolver+chr(int(string[limite_inferior:limite_superior],2))
        limite_superior+=8
        limite_inferior+=8
    return string_a_devolver
        
#función para aplicar xor a 2 cadenas de texto con 0s y 1s
def aplicar_xor(dato1,dato2):
    if (dato1=="0"):
        if(dato2=="0"):
            return("0")
        else:
            return("1")
    else:
        if(dato2=="0"):
            return("1")
        else:
            return("0")

#función para cifrar
def encriptar():
    texto=input("Ingrese el texto a encriptar: ")
    texto_random=generar_random_string(texto)
    cadena_encriptada=operar_strings(texto,texto_random)
    print("La cadena encriptada es: \""+cadena_encriptada+"\"\n")
    print("El pad es: \""+texto_random+"\"")

#función para decifrar
def desencriptar():
    texto=input("Ingrese el texto a desencriptar: ")
    texto_random=input("Ingrese el one-time-pad: ")
    cadena_encriptada=operar_strings(texto,texto_random)
    print("La cadena original es: \""+cadena_encriptada+"\"\n")

# Main______________________________________________
def main():
    desicion=0
    while(1):
        #Menu de desición del usuario
        desicion = input("Ingrese la opción que desea:\n1.Encriptar\n2.Desencriptar\n3.Salir\n")
        if (desicion=="1"):
            encriptar()
        elif (desicion=="2"):
            desencriptar()
        elif(desicion=="3"):
            break
        else:
            print("ERROR! ingreso no está en las opciones disponibles\n\n\n")




if __name__ == "__main__":
    main()



