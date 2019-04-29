import math


def colourtohex(r, g, b):
    hex = '#' + '%X%X%X' % (r, g, b)
    print(hex)

colourtohex(255, 255, 255)

########################################################################################

RGBTOHEX = dict = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',

}

# RGB colours
r,g,b = (130, 234, 23)

# Divide all by 16
rh = r / 16
gh = g / 16
bh = b / 16

# Separating the whole number from the decimals
fracr, wholer = math.modf(rh)
fracg, wholeg = math.modf(gh)
fracb, wholeb = math.modf(bh)

rth = r // 16
rd = fracr * 16

gth = g // 16
gd = fracg * 16

bth = b // 16
bd = fracb * 16

solution = (RGBTOHEX[rth], RGBTOHEX[rd], RGBTOHEX[gth], RGBTOHEX[gd], RGBTOHEX[bth], RGBTOHEX[bd])

print('#' + ''.join(solution))

########################################################################################


def rgbtohex(r, g, b):
    colours = [130, 234, 23]
    for items in colours:
        hex = items / 16
        return hex
   

print(rgbtohex(12,156,255))



