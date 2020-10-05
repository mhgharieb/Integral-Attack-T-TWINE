#! /usr/bin/env python

import argparse
import twine
import os
import time

def list2int(L):
    C = 0
    for i in range(len(L)):
        C = twine._append_4_bits(C, L[i])
    return C
def list2hex(L):
    return ("%x" %list2int(L)).zfill(len(L))   

def GenRandNibbleList(l):
    return map(lambda x: x & 0xf, bytearray(os.urandom(l)))


def main():
    parser = argparse.ArgumentParser(description= 'Test Vector of  T-TWINE Block Cipher')
    #parser.add_argument('-n', help= 'Active nibble')
    parser.add_argument('-z', default= 0x50, help= 'Encryption/Decryption bit size (80 or 128) bits')

    opt = parser.parse_args()
    #ActiveNibble = int(opt.n)
    if opt.z == "128":
        print "_______P________ ________________K_______________ _______T________ ______________________________Sum(C)____________________________ ____________________Persistent Balanced Bits____________________"
    else:
        print "_______P________ __________K_________ _______T________ ______________________________Sum(C)____________________________ ____________________Persistent Balanced Bits____________________"

    total = 0
    while True:
        C = 0
        P = list2hex(GenRandNibbleList(16))
        k = list2hex(GenRandNibbleList(int(opt.z)/4))
        RK = twine.generate_RK(k, len(k)*4)
        t_list = GenRandNibbleList(16)
        #t_list[5], t_list[10], t_list[11] = 0, 0, 0
        for t_list[5] in range(16):
            for t_list[10] in range(16):
                for t_list[11] in range(16):
                    t = list2hex(t_list)
                    RT = twine.generate_RT(t)
                    C ^= int(twine._encrypt11(P, RK, RT), 16)
        total |= C
        
        t_hexlist = ["%x" %i for i in t_list]
        t_hexlist[5], t_hexlist[10], t_hexlist[11] = "_", "_", "_"
        
        C_bin = bin(C)[2:].zfill(64)
        B_bin = list(bin(total)[2:].zfill(64))
        B_c = []
        for i in B_bin:
            if i == "0":
                B_c.append("0")
            else:
                B_c.append("?") 
                
        print P + " " + k + " " + "".join(t_hexlist) + " " + C_bin + " " +  "".join(B_c)
        
        
if __name__ == '__main__':
    main()    
