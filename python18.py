#Write a Python program to convert RGB color to HSV color.
def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
    v = mx*100
    return h, s, v

print(rgb_to_hsv(255, 255, 255))
print(rgb_to_hsv(0, 215, 0))

#Write a Python program to implement Euclidean Algorithm to compute the greatest common divisor (gcd)
from math import *

def euclid_algo(x, y, verbose=True):
	if x < y: # We want x >= y
		return euclid_algo(y, x, verbose)
	print()
	while y != 0:
		if verbose: print('%s = %s * %s + %s' % (x, floor(x/y), y, x % y))
		(x, y) = (y, x % y)
	
	if verbose: print('gcd is %s' % x) 
	return x


euclid_algo(150, 304)
euclid_algo(1000, 10)
euclid_algo(150, 9)
