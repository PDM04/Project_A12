b = 66.45150601     #span
c_r  = 10.229604    #root chord
taper = 0.28        #taper ratio

def chord(y):
    chord = c_r - c_r * (1-taper) / (b/2) * y
    return chord 

print("Hello World")
