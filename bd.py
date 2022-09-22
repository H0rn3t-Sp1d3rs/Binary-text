import binascii
print("\033[1;32;40mEnter Your Text")
B = raw_input("=> \033[1;31;40m")

print("\n\033[1;36;40mYour Bin Code => \033[1;31;40m")
print(' '.join(format(ord(x), 'b') for x in B))
