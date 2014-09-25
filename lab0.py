import binascii
import base64
import string
import StringIO
import operator
from string import ascii_lowercase


 
def asciiToHex(string):
    return binascii.hexlify(string)

def hexToAscii(hex):
    return binascii.unhexlify(hex)

def asciiToHex64(string):
    return base64.b64encode(string)

def hex64ToAscii(hex):
    return base64.b64decode(hex)

def xorSameLength(string, key):
    if(len(key) == len(string)):
        return asciiToHex(string) ^ asciiToHex(key)
    elif(len(key) > len(string)):
        key = key[0:len(string)]
        return asciiToHex(string) ^ asciiToHex(key)
    else:
        while(len(key) < len(string)):
            key += key
        key = key[0:len(string)]
        return asciiToHex(string) ^ asciiToHex(key)
    
def xor(string, key):
    return float(asciiToHex(string)) ^ int(key)
    
    
def getCoincidenceScore(string): 
    string = string.lower()
    map = {}
    for c in ascii_lowercase:
        map[c] = 0
    
    for c in string:
        c = c
        map[c] = map[c] + 1
    
    ic = 0
    
    for c in ascii_lowercase:
        ic += (map[c] *(map[c] - 1))
    
    ic /= float((len(string) * (len(string) - 1)))
    
    return ic
    


if __name__ == '__main__':
    secrets = ['Do or do not there is no try', 'I love Python !!!!']
    file = open("Lab0.TaskII.B.txt")
    map = {}
    for line in file:
        for i in range(0, 256):
            print i
            print line
            xorString = xor(line, i)
            print xorString
            xorString = str(xorString)
            print xorString, '===='
            print hexToAscii(xorString)
            map["xorString"] = [i, getCoincidenceScore(xorString)]
       
    sortedMap = sorted(map.iteritems(), key=operator.itemgetter(1))
       
    outputB = open("outputB.txt", "r+")
      
    for key in sortedMap: 
        outputB.write(key, "   ", sortedMap[key][0], "   ", sortedMap[key][1])
#     a = asciiToHex("s")
#     a = hexToAscii('3')
#     print a
#     b= asciiToHex64("stephen")
#     print b
#     print hex64ToAscii(b)
#     print secrets
    print xor("ab", "a")
#     getCoincidenceScore("stephen")
