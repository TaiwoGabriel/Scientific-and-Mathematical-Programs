

# Print even and odd numbers in a list

int = [555, 901, 482, 1771, 121, 322, 102, 511]  # Initialize the array

num_of_even = 0     # initialize number of even
num_of_odd = 0      # initialize number of even

for i in int:       #
    if i%2 == 0:
        num_of_even +=1
    else:
        num_of_odd +=1

x = [i for i in int if i % 2 == 0]
y = [i for i in int if i % 2 == 1]
print('Even elements:', num_of_even, 'element', x)
print('Odd integers:', num_of_odd, 'elements', y)


import numpy as np
x = np.arange(1,21)
print(x)


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace( 0,10 )

for n in range(3):
    y = np.sin( x+n )
    plt.figure()
    plt.plot( x, y )
    plt.savefig('myfilename%03d.png'%(n))





