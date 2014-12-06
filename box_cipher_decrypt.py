import numpy
import math

'''Read text from the file'''
def read_text_from_file(filename):
    f = open(filename,'r')
    text = f.readlines()
    text = "".join(text)
    return text.strip()

'''Transform text into array'''
def text_to_list(text):
    l = list(text)
    return l

'''Print array into regular string'''
def print_list(l):
    print(''.join(l))

'''Get int value of a letter'''
def let_int(letter):
    return ord(letter)

class Box_Cipher:
    plain = ''
    
    def __init__(self, pl):
        self.plain = pl
        
    def encrypt(self, row, col):
        p_len = len(self.plain)
        p_len = math.ceil( 1.0 * p_len / (row * col))
        a = numpy.chararray(shape=(row,p_len * col))
        #setup empty matrix
        for i in range(0,len(a)):
            for j in range(0,len(a[i])):
                a[i,j] = ""
        #fill in
        r = 0
        c = 0
        count = 0
        for l in self.plain:
            #print(str(r) + str(c))
            #print(a)
            a[r,c] = l
            c += 1
            count += 1
            if c % (col) == 0:
                r += 1
                if count % ((row * col)) != 0:
                    c = c - (col)
            if count % ((row * col)) == 0:
                r = 0
            #print(a)
        str = ''
        r = 0
        c = 0
        for i in range(0,row * col * int(p_len)):
            str += a[r,c]
            #print(str)
            r += 1
            if (i+1) % row == 0:
                r = 0
                c += 1
        return str