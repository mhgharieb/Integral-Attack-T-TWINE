#! /usr/bin/env python

import argparse
import twine



#python test_vector.py -z 80  -p "0123456789abcdef" -k "00112233445566778899" -t "fedcba9876543210"
#fbb33219433a42f2    
#python test_vector.py -z 128 -p "0123456789abcdef" -k "00112233445566778899aabbccddeeff" -t "fedcba9876543210"
#ce9e755fffeca2f8



def main():
    parser = argparse.ArgumentParser(description= 'Test Vector of  T-TWINE Block Cipher')
    parser.add_argument('-p', help= 'The plaintext to be encrypted')
#    parser.add_argument('-c', help= 'The ciphertext to be decrypted')
    parser.add_argument('-z', default= 0x50, help= 'Encryption/Decryption bit size (80 or 128) bits')
    parser.add_argument('-k', help= 'Encryption secret key')
#    parser.add_argument('-g', help= 'Automatically generate ')
    parser.add_argument('-t', help= 'Tweak')

    opt = parser.parse_args()

    if opt.k is not None:
        if opt.p is not None:
            RK = twine.generate_RK(opt.k, int(opt.z))
            RT = twine.generate_RT(opt.t)
            c = twine._encrypt(opt.p, RK, RT)
            print c
            return

if __name__ == '__main__':
    main()
