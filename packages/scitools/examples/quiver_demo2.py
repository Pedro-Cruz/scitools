#!/usr/bin/env python

"""
Demonstration of the quiver command in combination with other plotting
commands.
"""

from scitools.all import *

xv, yv = meshgrid(linspace(-5,5,81), linspace(-5,5,81), memoryorder='xyz')
values = sin(sqrt(xv**2 + yv**2))

setp(show=False)
pcolor(xv, yv, values, shading='interp', memoryorder='xyz')

# create a coarser grid for the gradient field:
xv, yv = meshgrid(linspace(-5,5,21), linspace(-5,5,21),
                  sparse=True, memoryorder='xyz')
values = sin(sqrt(xv**2 + yv**2))

# compute the gradient field:
uu, vv = gradient(values)

hold('on')
quiver(xv, yv, uu, vv, 'filled', 'k', axis=[-6,6,-6,6],memoryorder='xyz')
setp(show=True)
show()

#hardcopy('quiver2a.eps')
#hardcopy('quiver2a.png')


figure()
contour(xv, yv, values, 15, hold=True, show=False, memoryorder='xyz')
quiver(xv, yv, uu, vv, axis=[-6,6,-6,6], show=True, memoryorder='xyz')

#hardcopy('quiver2b.eps')
#hardcopy('quiver2b.png')

raw_input("press enter")
