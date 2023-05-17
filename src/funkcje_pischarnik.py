import numpy as np
from skimage import io
def dx(max,min):
    return max-min

def x_c(min, dx, C):
    return min+ dx*(C/255)


def normalise(liczba, max, min):
    return min + liczba*(max-min)

def reverse_normalise(liczba, max, min):
    return (liczba - min)/(max-min)

def x_c_reverse(min, dx, x_c):
    return np.round((x_c-min)*255/dx)

def chaos_function(a, iter_num, x_c):
    for i in range(iter_num):
        x_c = a*x_c*(1-x_c)
    return x_c


def iterations(kanal, iter_num, a, dx):
    s = kanal.shape[0]
    kanal_n = np.copy(kanal)
    for i in range(s):
        
        temp = chaos_function(a, iter_num, kanal_n[i-1]) + kanal[i] #   +kanal[i-1]
        kanal_n[i] = temp if temp<dx else temp-dx
              
    return kanal_n


def reverse_iterations(kanal, iter_num, a , dx, mini):
    s = kanal.shape[0]
    kanal_n = np.copy(kanal)
    for i in range(s-1, -1, -1):
        
        temp = kanal[i] - chaos_function(a, iter_num, kanal_n[i-1])
        
        kanal_n[i] = temp if temp>mini else temp+dx #tutaj chyba i-1 ale jak cos to dac i
        
        
    return kanal_n

def encrypt(path):
        img = io.imread(path)

        x, y, z = img.shape
        img = img.reshape(x*y, z)

        red = img[...,0]

        maks = 0.975
        mini = 0.095062
        iter_j = 3
        iter_i = 10
        a = 3.9

        red_c = x_c(mini, dx(maks, mini), red)



        red_norm = np.copy(red_c)
        for i in range(iter_j):

            red_norm = normalise(red_norm, maks, mini)
            red_norm = iterations(red_norm, iter_i, a, maks)
        return red_norm.reshape(x, y, 1)






