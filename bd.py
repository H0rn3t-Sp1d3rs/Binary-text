import binascii

print("\n\033[1;32;40mEnter Your Text : ")
angga = raw_input("=> ")

print("\n\033[1;36;40mYour Bin Code => ")
print(' '.join(format(ord(x), 'b') for x in angga))
