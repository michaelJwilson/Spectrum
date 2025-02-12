import matplotlib.pylab        as plt
import matplotlib.pyplot
from   matplotlib.font_manager import FontProperties
from   matplotlib.ticker       import ScalarFormatter
from   matplotlib.ticker       import FixedFormatter
import pylab                   as pl
import numpy                   as np
import math, os
import glob, pickle

formatter = ScalarFormatter(useMathText=True)
#formatter.set_scientific(True)
#formatter.set_powerlimits((-3,3))

fig_width_pt = 246.0*2 # Get this from LaTex using \the\columnwidth
inches_per_pt = 1.0/72.27
golden_mean = (np.sqrt(5)-1.0)/2.0
fig_width  = fig_width_pt*inches_per_pt # width in inches
fig_height = fig_width*golden_mean # height in inches
fig_size = [fig_width, fig_height]
params = {'axes.labelsize':10,
          'text.fontsize':8,
          'legend.fontsize':8,
          'xtick.labelsize':8.5,
          'ytick.labelsize':5.5,
          'figure.figsize':fig_size,
          'font.family': 'serif'}

pl.rcParams.update(params)
pl.clf()
pl.figure()
fig = pl.figure()
axes = pl.Axes(fig, [.2, .2, .7, .7])
fig.add_axes(axes)
axes.yaxis.set_major_formatter(formatter)

data   = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Del2k/midK_Del2k_Cube_Jenkins_kInterval_0.01_000.dat')
pl.loglog(data[:,0], data[:,2], 'y^', label='real space')

zdata   = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Del2k/midK_Del2k_zCube_Jenkins_kInterval_0.01_000.dat')
pl.loglog(zdata[:,0], zdata[:,2], 'g^', label='redshift space')

zdata   = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Del2k/midK_Del2k_zCube_clipThreshold_1.0e+01_kInterval_0.01_000.dat')
pl.loglog(zdata[:,0], zdata[:,2], 'r^', label=r'$\delta_0 = 10.0$, redshift space')

zdata   = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Del2k/midK_Del2k_zCube_clipThreshold_5.0e+00_kInterval_0.01_000.dat')
pl.loglog(zdata[:,0], zdata[:,2], 'm^', label=r'$\delta_0 = 5.0$, redshift space')

zdata   = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Del2k/midK_Del2k_zCube_clipThreshold_2.0e+00_kInterval_0.01_000.dat')
pl.loglog(zdata[:,0], zdata[:,2], 'c^', label=r'$\delta_0 = 2.0$, redshift space')


theory = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/HODTheoryPk/Pk_hod_20.0.dat')
pl.loglog(theory[:,0], theory[:,1], 'k')

theory = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/HODTheoryPk/Pk_hod_20.0.dat')
pl.loglog(theory[:,0], 1.34*theory[:,1], 'k--', label='monopole ratio 1.34')

theory = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/HODTheoryPk/Pk_hod_20.0.dat')
pl.loglog(theory[:,0], 0.45*theory[:,1], 'k--', label='monopole ratio 0.45')

pl.xlabel(r'$k [h^{-1} Mpc]$')
pl.ylabel('P(k)')

pl.yscale('log')
pl.xscale('log')

pl.xlim(10**-2, 1.0)
pl.ylim(100, 10**5)

pl.legend(loc=3)

pl.savefig('/disk1/mjw/HOD_MockRun/Plots/Pk_Cube_clippingDraft.pdf')
