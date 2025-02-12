import matplotlib.pylab        as plt
import matplotlib.pyplot
from   matplotlib.font_manager import FontProperties
from   matplotlib.ticker       import ScalarFormatter
from   matplotlib.ticker       import FixedFormatter
import pylab                   as pl
import numpy                   as np
import math, os
#import glob, pickle

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
          'legend.fontsize':6,
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


#data = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/SpectralDistortion/TestMonopole_PowerLawSmallScaleTruncation.dat')
#pl.loglog(data[:,3], data[:,4], 'c-.', label=r'P(k)')

#pl.legend(loc=3)
#pl.xlabel(r'k $[hMpc^{-1}]$')

#pl.savefig('/disk1/mjw/HOD_MockRun/Plots/FastHank_testMono_powerLawTrunc.pdf')

#pl.clf()
#pl.loglog(data[:,0], np.abs(data[:,1]*data[:,0]**2), 'c',   label=r'FFT log')
#pl.loglog(data[:,0], np.abs(data[:,2]*data[:,0]**2), 'r-.', label=r'analytic')

#pl.xlim(0.01, 1000.0)
#pl.ylim(10.**4., 10.**8.)

#pl.legend(loc=3)
#pl.title(r'$\xi(r)$ for $\Delta^2(k) = (k/k_0)^{n+3}$exp$(-k/k_c)$')

#pl.xlabel(r'r $[h^{-1}Mpc]$')

#pl.savefig('/disk1/mjw/HOD_MockRun/Plots/FastHank_testMono_powerLawTrunc_xi.pdf')

#pl.clf()

#data = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/SpectralDistortion/TestMonopole_PowerLaw_Multipoles.dat')

#pl.loglog(data[:,5], data[:,6], label=r'$P_0$(k)')
#pl.loglog(data[:,5], data[:,7], label=r'$P_2$(k)')
#pl.loglog(data[:,5], data[:,8], label=r'$P_4$(k)')

#pl.legend(loc=3)
#pl.xlabel(r'k $[hMpc^{-1}]$')

#pl.savefig('/disk1/mjw/HOD_MockRun/Plots/FastHank_testMono_powerLawMultipoles.pdf')

#pl.clf()

#pl.semilogx(data[:,0],     data[:,1], 'c', label=r'$+\xi_0$(r)')
#pl.semilogx(data[:,0], -1.*data[:,2], '--', label=r'$-\xi_2$(r)')
#pl.semilogx(data[:,0],     data[:,3], 'k', label=r'$+\xi_4$(r)')

#pl.semilogx(data[:,0],     data[:,4], 'r--')
#pl.semilogx(data[:,0],    -data[:,5], 'g--')
#pl.semilogx(data[:,0],     data[:,6], 'r--')

#pl.ylabel(r'$\xi_i(r)/ \xi(r)$')

#pl.xlim(10.**-3, 10.**2.)
#pl.ylim(0., 1.6)

#pl.title(r'Kaiser model RSD, $\xi(r) = (r/r_0)^{1.8}$ for $r_0=5h^{-1}$Mpc')

#pl.legend(loc=4)
#pl.xlabel(r'r $[h^{-1}Mpc]$')

#pl.savefig('/disk1/mjw/HOD_MockRun/Plots/FastHank_testMono_powerLawMultipoles_xi.pdf')

#pl.clf()

#data = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/SpectralDistortion/TestMonopole_PowerLaw_pkMultipoles.dat')
#pl.loglog(data[:,0], data[:,1], label=r'$P_0$(k)')
#pl.loglog(data[:,0], data[:,2], label=r'$P_2$(k)')
#pl.loglog(data[:,0], data[:,3], label=r'$P_4$(k)')

#pl.loglog(data[:,0], data[:,4], '--', label=r'$P_0$(k), analytic ')
#pl.loglog(data[:,0], data[:,5], '--', label=r'$P_2$(k), analytic')
#pl.loglog(data[:,0], data[:,6], '--', label=r'$P_4$(k), analytic')

#pl.xlim(0.01, 10.)
#pl.ylim(1., 10.**6.)

#pl.legend(loc=3)
#pl.xlabel(r'k $[hMpc^{-1}]$')
#pl.title(r'FFTlog inverse, Kaiser model RSD, $\xi(r) = (r/r_0)^{1.8}$ for $r_0=5h^{-1}$Mpc')

#pl.savefig('/disk1/mjw/HOD_MockRun/Plots/FastHank_inverseTransform.pdf')

#pl.clf()

#beta  = 0.542
#gamma = 1.8
#r0    = 5. 

#data = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/SpectralDistortion/ClippedMonopole_Order2_xi.dat')

#xi   = (r0/data[:,0])**gamma

##pl.xlim(10.**-4, 10.**4.)
##pl.ylim(10.**-1., 2.00)

#pl.loglog(data[:,0],   np.abs(data[:,1]), 'k',    label=r'$\xi_0(r)$')
#pl.loglog(data[:,0],   np.abs(-data[:,2]), 'k--',  label=r'$-\xi_2(r)$')
#pl.loglog(data[:,0],   np.abs(data[:,3]), 'b--',  label=r'$\xi_4(r)$')
#pl.loglog(data[:,0],   np.abs(data[:,4]), 'g',  label=r'clipped $\xi_0(r)$')
#pl.loglog(data[:,0],   np.abs(data[:,5]), 'r--',  label=r'suppressed $\xi_0(r)$')

##pl.xlim(1., 200.)
##pl.ylim(0.0001, 120.)

#pl.xlabel(r'r [h$^{-1}$Mpc]')
#pl.ylabel(r'$\xi$(r)')

##pl.loglog(data[:,0], -data[:,2], 'g', label=r'$-\xi_2(r)$')
##pl.loglog(data[:,0],  data[:,3], 'r', label=r'$\xi_4(r)$')
## pl.loglog(data[:,0],  data[:,4], 'b', label=r'clipped $\xi_0(r)$')
## pl.loglog(data[:,0],  data[:,5], 'y--', label=r'suppressed $\xi_0(r)$')

##pl.loglog(data[:,0], (1. + (2./3.)*beta + 0.2*beta*beta)*np.ones(len(data[:,0])), 'k--', label=r'analytic $\xi_0(r)$')
##pl.loglog(data[:,0], -((4./3.)*beta + (4./7.)*beta*beta)*(-gamma/(3.-gamma))*np.ones(len(data[:,0])), 'g--', label=r'analytic -$\xi_2(r)$')
##pl.loglog(data[:,0], (8./35.)*beta*beta*gamma*(2.+gamma)*((-5. + gamma)*(-3. +gamma))**-1.*np.ones(len(data[:,0])), 'r--', label=r'analytic $\xi_4(r)$')

##pl.xlabel(r'r[h$^{-1}$Mpc]')
##pl.title(r'Clipped $\xi(r)$, Kaiser RSD, $\xi(r) = (r/r_0)^{1.8}$ for $r_0=5h^{-1}$Mpc')
##pl.legend(loc=3)

#pl.savefig('/disk1/mjw/HOD_MockRun/Plots/FastHank_clippedMono.pdf')

#pl.clf()

##data = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/SpectralDistortion/UnclippedMonopole_Order2_pk.dat')
##pl.loglog(data[:,0], data[:,1], 'k',   label=r'$P_0(k)$')
##pl.loglog(data[:,0], data[:,2], 'r', label=r'analytic')

#data = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/SpectralDistortion/ClippedMonopole_Order2_pk.dat')
#pl.loglog(data[:,0], data[:,1], 'k',   label=r'$P_0(k)$')
#pl.loglog(data[:,0], data[:,2], 'r--',   label=r'analytic')

#pl.xlabel(r'k [hMpc$^{-1}$]')
#pl.title('Monopole')

## pl.xlim(0.01, 1.)
#pl.legend(loc=3)

#pl.savefig('/disk1/mjw/HOD_MockRun/Plots/FastHank_clippedMono_pk.pdf')

#pl.clf()

#data = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/SpectralDistortion/hi_k_hod_powerlaw.dat')
#pl.loglog(data[:,0], data[:,1])
##pl.loglog(data[:,0], data[:,2])

##pl.xlim(60., 80.)
##pl.ylim(1., 10.)

#pl.savefig('/disk1/mjw/HOD_MockRun/Plots/FastHank_hi_k_hod_powerlaw.pdf')

pl.clf()

data = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/SpectralDistortion/fftlog_pk_truncpowerlaw_4096_1.00e-10_1.00e+14.dat')

pl.loglog(data[:,0], data[:,1], 'g',     label='mono, FFT log')
pl.loglog(data[:,0], data[:,2], 'y',     label='quad, FFT log')
pl.loglog(data[:,0], data[:,3], 'y',     label='hex, FFT log')
pl.loglog(data[:,0], data[:,4], 'k',   label='clip mono, FFT log')
pl.loglog(data[:,0], data[:,5], 'k',   label='clip quad, FFT log')

data = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/SpectralDistortion/2D_corrfn_multipoles_5.00.dat')
pl.loglog(data[:,0], np.abs(data[:,1]), 'k--',   label='mono, 3D FFT')
pl.loglog(data[:,0], np.abs(data[:,2]), 'r--',   label='quad, 3D FFT')
#pl.loglog(data[:,0], np.abs(data[:,3]), 'k--',   label=' hex, 3D FFT')

data = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/SpectralDistortion/2D_corrfn_Suppressedmultipoles_5.00.dat')
pl.loglog(data[:,0], np.abs(data[:,1]), 'c',   label='supp., 3D FFT', markersize=2)
pl.loglog(data[:,0], np.abs(data[:,2]), 'm',   label='supp., 3D FFT', markersize=2)

data = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/SpectralDistortion/2D_corrfn_Clippedmultipoles_5.00.dat')
pl.loglog(data[:,0], np.abs(data[:,1]), 'k^',   label='clipped, 3D FFT', markersize=2)
pl.loglog(data[:,0], np.abs(data[:,2]), 'k^',   label='clipped, 3D FFT', markersize=2)
#pl.loglog(data[:,0], np.abs(data[:,3]), 'k^',   label='clipped, 3D FFT', markersize=2)

pl.ylabel(r'$| \xi_n(r) |$')
pl.xlabel(r'r')

pl.legend(loc=1, ncol=2)

pl.xlim(10.**1., 300.)
pl.ylim(10.**-5., 10.**0.)

# pl.xlim(10., 50.)
# pl.ylim(10.**-2., 10.**-1.)

# pl.xscale('linear')
# pl.yscale('linear')

pl.savefig('/disk1/mjw/HOD_MockRun/Plots/pk_powerlaw_trunc.pdf')
