import numpy as np
import pylab as pl

import matplotlib.pyplot as plt

from   matplotlib.colors import LogNorm

import math, sys

#nx, ny   = (100, 100)

#r        =      15.*np.linspace(0, 1, nx)
#theta    = 0.5*np.pi*np.linspace(0, 1, ny)

l        = 14.
w        = l/9.

rv, tv  = np.meshgrid(r, theta)

rsin    = rv*np.sin(tv)
rcos    = rv*np.cos(tv)

first   = np.abs(rsin)
second  = np.abs(rcos)

# w       = 0.2*first.max()
# t       =  0.05*second.max()

boolarray          = np.ones(nx*ny).reshape(nx, ny)

Indices = np.where((first < w) & (second < l))
boolarray[Indices] = 0.

Indices = np.where((second < l) & (first < w))
boolarray[Indices] = 0.

# plt.imshow(bool)

#rdependence = np.zeros(nx)

# print bool

#for i in xrange(0, nx, 1):
#    rdependence[i] = np.sum(bool[:,i])

#pl.semilogx(r, rdependence/rdependence.max(), 'k')

#pl.ylim(0.3, 1.1)
#pl.xlim(0.01, 10.)

fig, ax   = pl.subplots(subplot_kw=dict(projection='polar'))

pax = ax.pcolormesh(tv, rv, boolarray, cmap='Blues')
pax = ax.pcolormesh(np.pi*np.ones([nx, ny]) - tv, rv, boolarray, cmap='Blues')
pax = ax.pcolormesh(np.pi*np.ones([nx, ny]) + tv, rv, boolarray, cmap='Blues')
pax = ax.pcolormesh(-tv, rv, boolarray, cmap='Blues')

ax.set_theta_zero_location("N") # 'north' location for theta=0

ax.set_theta_direction(-1)      # angles increase clockwise

# ax.set_xticklabels([str(np.cos(0.0)), str(np.cos(np.pi/4.)), str(np.cos(np.pi/2.)), str(np.cos(3.*np.pi/4.)), str(np.cos(np.pi)), '', '', ''])

fig.colorbar(pax)

pl.savefig('SSPOC_polarLimits.pdf')


    
