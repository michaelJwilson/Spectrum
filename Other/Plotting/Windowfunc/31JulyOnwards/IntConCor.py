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

fig_width_pt = 246.0*2 # Get this from LaTex using \the\columnwidth
inches_per_pt = 1.0/72.27
golden_mean = (np.sqrt(5)-1.0)/2.0
fig_width  = fig_width_pt*inches_per_pt # width in inches
fig_height = fig_width*golden_mean # height in inches
fig_size = [fig_width, fig_height]
params = {'axes.labelsize':10,
          'text.fontsize':6,
          'legend.fontsize':6,
          'xtick.labelsize':11.0,
          'ytick.labelsize':11.0,
          'figure.figsize':fig_size,
          'font.family': 'serif'}

pl.rcParams.update(params)
pl.clf()
pl.figure()
fig = pl.figure()
axes = pl.Axes(fig, [.2, .2, .7, .7])
fig.add_axes(axes)
axes.yaxis.set_major_formatter(formatter)

# Stefano = np.loadtxt('/disk1/mjw/HOD_MockRun/Stefano/power/ps_mocks.txt')
# pl.errorbar(Stefano[:,0], Stefano[:,1]*np.exp(-0.5*(3.*Stefano[:,0])**2.), Stefano[:,2], c='k')

data = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/Multipoles_fullCube_HOD_KlRSD_clipThreshold_2.0e-01_IntConCor_apparentMeanCorr_kbin_0.005_000.dat')
pl.loglog(data[:,0],  data[:,1], 'k^',   label=r'mono, cube', markersize=2)
pl.loglog(data[:,0],  data[:,2], 'k^',   label=r'quad, cube', markersize=2)
pl.loglog(data[:,0],  data[:,4], 'r',  label=r'input mono')

data = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/Multipoles_VipersMask_HOD_KlRSD_clipThreshold_2.0e-01_IntConCor_kbin_0.005_000.dat')
pl.loglog(data[:,0],  data[:,1], 'b',   label=r'mono, VIPERS')
pl.loglog(data[:,0],  data[:,2], 'g',   label=r'quad, VIPERS')


data = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/SpectralDistortion/mixingmatrix_convolvedPk_VipersMask_IntConCorr.dat')
pl.loglog(data[:,0],  data[:,1], 'y',   label=r'cnvld. mono, mix mat.')
pl.loglog(data[:,0],  data[:,2], 'y',   label=r'cnvld. quad, mix mat.')

pl.xlabel(r'$k [h Mpc^{-1}]$')
pl.ylabel(r'P(k) e$^{-9k^2/2}$')

pl.xlim(10.**-2., 1.0)
pl.ylim(10.**2.,  10.**5.)

pl.legend(loc=3)

pl.savefig('/disk1/mjw/HOD_MockRun/Plots/Windowfunc/31JulyOnwards/IntConCorr.pdf')

#pl.clf()

#true     = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/Multipoles_VipersMask_HOD_KlRSD_clipThreshold_2.0e-01_IntConCor_kbin_0.005_000.dat')

#apparent = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/Multipoles_VipersMask_HOD_KlRSD_clipThreshold_2.0e-01_IntConCor_apparentMean_kbin_0.005_000.dat')

#diff     = true[:,1] - apparent[:,1]

#pl.loglog(true[:,0], diff, 'k', label='difference caused by Integral constraint')

#window   = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/VipersMaskWf_Multipoles_VipersMask_HOD_KlRSD_clipThreshold_2.0e-01_IntConCor_apparentMean_kbin_0.00500.dat')
#pl.loglog(window[:,0], 2.*10.**6.*window[:,1], label='VIPERS mask monopole')

#pl.xlabel(r'$k [h Mpc^{-1}]$')
#pl.ylabel(r'true - apparent')

#pl.xlim(10.**-2., 1.0)

#pl.legend(loc=3)

#pl.savefig('/disk1/mjw/HOD_MockRun/Plots/Windowfunc/31JulyOnwards/IntConCorr_diff.pdf')

#pl.clf()

#data = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/SpectralDistortion/mixingmatrix_convolvedPk_VipersMask_IntConCorr.dat')
#pl.loglog(data[:,0],  data[:,1], 'r',   label=r'conv. mono, mixing matrix')
#pl.loglog(data[:,0],  data[:,2], 'y',   label=r'conv. quad, mixing matrix')

#pl.loglog(data[:,0],  data[:,3], 'k',   label=r'mono')
#pl.loglog(data[:,0],  data[:,4], 'k',   label=r'quad')

#pl.xlabel(r'$k [h Mpc^{-1}]$')

#pl.xlim(0., 0.2)
#pl.ylim(1000., 10.**5.)

#pl.legend(loc=1)

#pl.xscale('linear')
#pl.yscale('log')

#pl.savefig('/disk1/mjw/HOD_MockRun/Plots/Windowfunc/31JulyOnwards/convolvedPk_zeroPoint.pdf')
