import binascii
import time


print("\n===========================================\n")

print("\nEnter any number to see its binary form.\n")

print("\n===========================================\n")
time.sleep(0.5)


print("\nEnter Your Text : ")
time.sleep(0.5)
angga = raw_input("====> ")
time.sleep(0.5)

print("\n Your Bin Code :")
print(' '.join(format(ord(x), 'b') for x in angga))
