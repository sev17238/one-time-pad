######################################################
# Luis Delgado 17XXX
# Diego Sevilla 17238
######################################################
# test.py
######################################################
# Python3 program to....
######################################################

# tools ___________________________
# https://onlinestringtools.com/convert-string-to-ascii
# https://www.traductorbinario.com/

# imports _________________________
import random

# Functions area______________________________________________
def random_binary_string(l=8): 
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
    '''
    Function to convert from string to binary

    Params:
     - message: a string containing any message
    '''
    binaryMessage = ''.join(format(ord(i), '08b') for i in message) 
    return binaryMessage

#convertir de una cadena de 0s y 1s a     
def binary_to_string(string):
    '''
    Function to convert from binary to string

    Params:
     - string: a binary string containing 1's and 0's
    '''
    limite_inferior=0
    limite_superior=8
    string_a_devolver=""
    while (len(string)>=limite_superior):
        string_a_devolver=string_a_devolver+chr(int(string[limite_inferior:limite_superior],2))
        limite_superior+=8
        limite_inferior+=8
    return string_a_devolver

def xor_operation(string1,string2):
    '''
    Function that executes xor binary operation on two given strings.

    Params:
     - string1: the message
     - string2: the key
     - return - ciphertext
    '''
    resultString = ''
    if(len(string1) == len(string2)):
        for s in range(0,len(string1)):
            if(string1[s] == '0' and string2[s] == '0'):
                resultString += '0'
            elif(string1[s] == '0' and string2[s] == '1'):
                resultString += '1'
            elif(string1[s] == '1' and string2[s] == '0'):
                resultString += '1'
            elif(string1[s] == '1' and string2[s] == '1'):
                resultString += '0'
    else:
        print('input strings doesnt have the same number of bytes')

    return resultString

def encrypt_message(file='message.txt'):

    f = open("message.txt", "r", encoding="utf-8")
    message = f.read()
    binaryMessage = string_to_binary(message)
    randomStringForXor = random_binary_string(len(binaryMessage)) #hi = 10101010 10101010
    randomTailString = random_binary_string(8)

    encryptedMessageB = xor_operation(binaryMessage,randomStringForXor)
    encryptedMessageB += randomTailString
    encryptedMessage = binary_to_string(encryptedMessageB)
    enMFile = open("encrypted_message.txt", "w", encoding="utf-8")
    enMFile.write(encryptedMessage)

    theKeyB = randomStringForXor + randomTailString
    theKey = binary_to_string(theKeyB)
    keyFile = open("the_key.txt", "w", encoding="utf-8")
    keyFile.write(theKey)

    return message, encryptedMessage, theKey

def decrypt_message(encryptedMessageFile='encrypted_message.txt',theKeyFile='the_key.txt'):
    enF = open(encryptedMessageFile, "r", encoding="utf-8")
    encryptedMessage = enF.read()
    theKF = open(theKeyFile, "r", encoding="utf-8")
    theKey = theKF.read()
    enMessageB = string_to_binary(encryptedMessage)
    keyB = string_to_binary(theKey)

    resultB = xor_operation(enMessageB,keyB)
    result = binary_to_string(resultB)
    deMFile = open("decrypted_message.txt", "w", encoding="utf-8")
    deMFile.write(result)

    return result

def decrypt_encrypt_straight_forward():
    #default input file: message.txt 
    #output files: encrypted_message.txt and the_key.txt
    en,k = encrypt_message() 
    # output file: decrypted_message.txt 
    print('original: '+decrypt_message()) 

# Main______________________________________________
def main():
    desition = ''
    while(desition != '3'):
        desition = input("Choose an option:\n1.Encrypt\n2.Decrypt\n3.Exit\n")
        if (desition == '1'):
            message_file = input("Enter the .txt file with your message (message.txt): ")
            message,encryptedMessage,theKey = encrypt_message(message_file)
            print('Message in the file: '+message)
            print('Encrypted Message: "'+encryptedMessage+'"')
            print('The key: "'+theKey+'"\n')
        elif (desition == '2'):
            encryptedMessage = input("Enter the encrypted_message.txt file: ")
            theKey = input("Enter the_key.txt file: ")
            decrypt_message(encryptedMessage,theKey)

            f = open('decrypted_message.txt',"r", encoding="utf-8")
            decrytedMessage = f.read()
            print('\nDecrypted Message: "'+decrytedMessage+'"\n')
        else:
            print("\nSee you soon! \n")


if __name__ == "__main__":
    main()




