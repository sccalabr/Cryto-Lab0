import StringIO
import base64
import binascii
from operator import itemgetter
import operator
from string import ascii_lowercase, ascii_uppercase, ascii_letters
import string


def decodeHexString(string):
    return string.decode("hex")

def encodeAsciiString(string):
    return string.encode("hex")

def encodeAsciiString64(string):
    return base64.b64encode(string)

def decodeHexString64(hex):
    return base64.b64decode(hex)

def getCorrectKeyLength(string, key):
    if(len(key) > len(string)):
        key = key[0:len(string)]
    elif (len(key) < len(string)):
        while(len(key) < len(string)):
            key += key
        key = key[0:len(string)]
    return key

def xor(string, key):
    key = getCorrectKeyLength(string, key)
    zipped = zip(string, key)
    return ''.join(chr(ord(a) ^ (ord(b))) for a,b in zip(string, key))
    
def getCoincidenceScore(string): 
    map = {}
    for c in ascii_lowercase:
        map[c] = 0
    
    for c in string:
        if c in ascii_lowercase:
            map[c] = map[c] + 1
    
    ic = 0
    
    for c in ascii_lowercase:
        ic += (map[c] *(map[c] - 1))
    
    ic /= float((len(string) * (len(string) - 1)))
    
    return ic

def vigenereShift(string, key):
    key = getCorrectKeyLength(string, key)
    return "".join(chr(((ord(a) - ord(b)) % 26) + ord('A')) for a,b in zip(string,key))
    

def labB():
    file = open("Lab0.TaskII.B.txt")
    map = []

    for line in file:
        print line
        for i in range(0, 256):
            xorString = xor(decodeHexString(line.strip()), chr(i))
            xorString = str(xorString)
            map.append([i, getCoincidenceScore(xorString), xorString])

    sortedMap = sorted(map, key=itemgetter(1))
    sortedMap = reversed(sortedMap)
         
    outputB = open("outputB.txt", "r+")
    counter = 0
    for key in sortedMap: 
        print key
        outputB.write("%s   " % key[0])
        outputB.write("%s   " % key[1])
        outputB.write("%s\n=========================================\n" % key[2])
        if counter > 50:
            break
        counter += 1
     
def labC():
    pass
    
def labD():
     file = open("Lab0.TaskII.D.txt")
     map = []
     for line in file:
        print line
        for i in range(0, 1):
            decrypted = vigenereShift(line, str("TEST"))
            print decrypted
            map.append([i, getCoincidenceScore(decrypted), decrypted])
        

if __name__ == '__main__':
    secrets = ['Do or do not there is no try', 'I love Python !!!!']
    labB()
#      labC()
#     labD()
#     message = "This is my message"
#     key = "This is a key"
#     encrypt = xor(message, key)
#     print encrypt
#     print xor(encrypt, key)
#     a = asciiToHex("b")
#     print a
#      a = hexToAscii('73')
#      print a
#     b= asciiToHex64("stephen")
#     print b
#     print hex64ToAscii(b)
#     print secrets
#     print "===>", encodeAsciiString("CAT")
#     getCoincidenceScore("stephen")
