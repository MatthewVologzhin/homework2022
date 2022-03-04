import itertools as it

class NEW_password(BaseException):
    def __init__(self,string):
        None
        

with open('input.txt','r') as INPUT:
    string = INPUT.readline()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

array_aa = []
array_abc = []
for i in range(len(alphabet)-2):
    array_abc.append(alphabet[i:i+3])
for i in range(len(alphabet)):
    array_aa.append(2*alphabet[i])
print(array_abc)
print(array_aa)

while True:
    if 'i' in string or 'j' in string or 'l' in string:
        raise NEW_password
    None
