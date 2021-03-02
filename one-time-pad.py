######################################################
# Luis Delgado 17
# Diego Sevilla 17238
######################################################
# test.py
######################################################
# Python3 program to....
######################################################

# tools ___________________________
# https://onlinestringtools.com/convert-string-to-ascii

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

def string_to_ascii(test_list):
    #test_list = ['gfg', 'is', 'best'] 
    
    # printing original list  
    print("The original list : " + str(test_list)) 

    # Convert String list to ascii values using loop + ord() 
    res = [] 
    for ele in test_list: 
        res.extend(ord(num) for num in ele) 
    return res

def ssss(string):
    result = list(bytes(b'test'))
    return result

def binary_to_decimal(binary): 
    # Using int function to convert to string    
    string = int(binary, 2) 
    return string 
      
def BynaryToDecimal(b = '10001111100101110010111010111110011'):
    # Driver's code 
    # initializing binary data 
    bin_data = b
    print("The binary value is:", bin_data) 
    str_data =' '
    
    # slicing the input and converting it  
    # in decimal and then converting it in string 
    for i in range(0, len(bin_data), 7): 
        
        # slicing the bin_data from index range [0, 6] 
        # and storing it in temp_data 
        temp_data = bin_data[i:i + 7] 
        
        # passing temp_data in BinarytoDecimal() function 
        # to get decimal value of corresponding temp_data 
        decimal_data = binary_to_decimal(temp_data) 
        
        # Deccoding the decimal value returned by  
        # BinarytoDecimal() function, using chr()  
        # function which return the string corresponding  
        # character for given ASCII value, and store it  
        # in str_data 
        str_data = str_data + chr(decimal_data)  

    return str_data


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

        print(randon_binary_string())
        print(xor_operation('0101','1010'))

        print(string_to_ascii(['hello',' ','world']))

        print(string_to_binary(' Geeks'))
        print(BynaryToDecimal(string_to_binary(' Geeks')))



    except ValueError:
        print("Check the input parameters. Try again...")

    # print(x.get_string(fields=["Estado"])[0])
    # print(x)



if __name__ == "__main__":
    main()


#python afn_to_afd.py afn-tran-table.csv
