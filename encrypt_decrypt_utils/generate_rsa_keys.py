#! /usr/bin/env python3

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import ast

# generate key
privateKey = RSA.generate(1024)
publicKey = privateKey.publickey()

# crate file 
with open("private.pem", "wb") as fn:
    fn.write(privateKey.exportKey(format='PEM'))
with open("public.pem", "wb") as fn:
    fn.write(publicKey.exportKey(format='PEM'))

# encrypt and decrypt verification
with open("private.pem", "rb") as fn:
    read_privatekey = RSA.importKey(fn.read())
with open("public.pem", "rb") as fn:
    read_publickey = RSA.importKey(fn.read())


origin_msg = "hello world!"

#
encryptor = PKCS1_OAEP.new(read_publickey)
encap_msg = encryptor.encrypt(origin_msg.encode())

#
decryptor = PKCS1_OAEP.new(read_privatekey)
decrypted = decryptor.decrypt(ast.literal_eval(str(encap_msg)))
decap_msg = decrypted.decode()

print(decap_msg)
