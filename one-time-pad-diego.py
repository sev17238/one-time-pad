######################################################
# Luis Delgado 17
# Diego Sevilla 17238
######################################################
# test.py
######################################################
# Python3 program to....
######################################################


# imports _________________________
import random


# Definitions _________________________
oneTimePad = 'cool'


# Functions area______________________________________________
def randon_binary_string(l=8): 
    '''
    Function to create the random binary string 

    Params:
     - l: length of random generated string
    '''
    key1 = "" 
    for i in range(l): 
        temp = str(random.randint(0, 1)) 
        key1 += temp 
    return(key1) 

def string_to_binary(message):
    binaryMessage = ''.join(format(ord(i), '08b') for i in message) 
    #binaryMessage = ''.join(format(i, '08b') for i in bytearray(message, encoding ='utf-8')) 
    return binaryMessage


def xor_operation(string1,string2):
    '''
    Function that executes xor binary operation on two given strings.

    Params:
     - string1: the message
     - string2: the key
     - return - ciphertext
    '''

    resultString = ''
    for s in range(0,len(string1)):
        if(string1[s] == '0' and string2[s] == '0'):
            resultString += '0'
        elif(string1[s] == '0' and string2[s] == '1'):
            resultString += '1'
        elif(string1[s] == '1' and string2[s] == '0'):
            resultString += '1'
        elif(string1[s] == '1' and string2[s] == '1'):
            resultString += '0'

    return resultString



# Main______________________________________________
def main():
    try:
        number = 1
        print(number)

        f = open("message.txt", "r")
        message = f.read()
        print(message.split(',')) 

        print(string_to_binary('Hi'))
        print(randon_binary_string())
        print(xor_operation('0101','1010'))

    except ValueError:
        print("Check the input parameters. Try again...")

    # print(x.get_string(fields=["Estado"])[0])
    # print(x)



if __name__ == "__main__":
    main()


#python afn_to_afd.py afn-tran-table.csv
