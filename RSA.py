import random
from PIL import Image
from Stegan import Encode, Decode
import math
letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",",",".","!","?"," "]
number = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
def cipher(num,e):
    for i in range(len(num)):
        X.append((int(num[i])**e)%n)
def decipher(num,d):
    for i in range(len(num)):
        Y.append((int(num[i])**d)%n)
def gcd(a, b):
    while b != 0:
        (a, b)=(b, a % b)
    return a
def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    return amount
def Decrypt():
    global i,j,Y
    Y=[]
    encoded_image_file = "enc_2.png"
    img2 = Image.open(encoded_image_file)
    print(img2, img2.mode)
    hidden_text = Decode(img2)
    print(hidden_text)
    decipher(hidden_text,d)
    numD=[]
    for i in range(len(Y)):
        for j in range(len(number)):
            if(Y[i]==int(number[j])):
                numD.append(letter[j])
    for i in numD:
        print(i,end="")
    print("\n")
def Encrypt():
# encrypts a plaintext message using the current key
    global plaintext, numC, j, X
    X=[]
    plaintext = (input("Enter Plaintext :"))
    plaintext = (plaintext.lower())
    numC = []
    for i in range(len(plaintext)):
        for j in range(len(letter)):
            if(plaintext[i]==letter[j]):
                numC.append(number[j])
    cipher(numC,e)
    print("Ciphertext:", X)
    print("Number of Ciphertext blocks:", len(X))
    original_image_file = "2.png"
    img = Image.open(original_image_file)
    print(img, img.mode)
    encoded_image_file = "enc_" + original_image_file
    img_encoded = Encode(img, plaintext, X)
    if img_encoded:
        img_encoded.save(encoded_image_file)
        print("{} saved!".format(encoded_image_file))

n = 2537
e = 13
d = 937

print("To redefine n,e, or d, type 'n','e',... etc.")
print("To encrypt a message with the current key, type 'Encrypt'")
print("To decrypt a message with the current key, type 'Decrypt'")
print("Type quit to exit")
print('\n')
print('\n')
mm = str()
mm = str()
while mm != 'quit':
    mm = input("Enter Command: ")
    if mm.lower() == 'encrypt':
        Encrypt()
    elif mm.lower() == 'decrypt':
        Decrypt()
    elif mm.lower() == 'n':
        try:
            print('current n = ', n)
            n1 = int(input(" Enter a value for n:"))
            if	n1<2 :
                print('Invalid input')
            else :
                n=n1
                print('n set to :',n)
        except ValueError:
            print('please enter a number')
    elif mm.lower() == 'help':
        print("To redefine n,e, or d, type 'n','e',... etc.")
        print("To encrypt a message with the current key, type 'Encrypt'")
        print("To decrypt a message with the current key, type 'Decrypt'")
        print("Type quit to exit")
        print('\n')
        print('\n')
    elif mm.lower() == 'e':
        try:
            print('current e = ', e)
            e1 = int(input(" Enter a value for e :"))
            if	e1<= 2 or gcd(phi(n),e1)!=1:
                print('Invalid input')
            else :
                e=e1
                print('e set to :', e)
        except ValueError:
            print('please enter a number')
    elif mm.lower() == 'd':
        try:
            print('current d = ', d)
            d1 = int(input(" Enter a value for d :"))
            if d1 <= 0 and (e*d1)%phi(n)!=1:
                print('Invalid input')
            else:
                d=d1
                print('d set to :',d)
        except ValueError:
            print('please enter a number')
    else:
        if mm != 'quit':
            ii = random.randint(0, 6)
            statements = ["This cannot be done", "Read the directions again", "Didnt say the magic word", "This input is UNACCEPTABLE!!","Was that even a word???", "Please follow thedirections","Just type 'help' if you are really that lost"]
            print(statements[ii])
