from unicodedata import digit
from chapter3.stack.stack import Stack

def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber>0:
        rem = decNumber%base
        remstack.push(rem)
        decNumber = decNumber // base
    
    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]
    
    return newString

if __name__ == "__main__":
    decnum = int(input("Enter Decimal Number: "))
    base = int(input("Enter Base: "))
    print(baseConverter(decnum, base))
