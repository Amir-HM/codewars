strng = 'foo'
def string_incrementer(strng):
    numbers = ["1","2","3","4","5","6","7","8","9"]
    number = ""
    strng = list(strng)
    for i in range(len(strng)):
        ch = strng[i]
        print (ch)
        if ch in numbers:
            print (ch)
            number += ch
        if ch == "0" and strng[i-1] in numbers:
            number += ch

    for x in number:
        strng.remove(x)

    number = int(number) + 1
    strng.append(str(number))
    strng = ''.join(strng)
    return strng


string_incrementer(strng)
