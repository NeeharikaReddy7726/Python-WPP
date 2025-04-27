import numpy as np,math, matplotlib.pyplot as plt

l= [(2, 5), (-3, 8), (0, -7), (6, -2), (-4, -4), (3, 9), (1, -1), (7, 3), (-6, 2), (5, 0)]
arr=np.array(l)

def mag(i):
    return math.sqrt(i[0]**2 + i[1]**2)
def teta(i):
    return  np.degrees(math.atan2(i[1],i[0]))
 
r=np.apply_along_axis(mag,1,arr)
teta_degrees=np.apply_along_axis(teta,1,arr)
    
plt.polar(teta_degrees,r, marker='o')
plt.title("Polar Coordinate Plot")
plt.show()
