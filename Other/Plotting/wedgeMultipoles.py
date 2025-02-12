pl.clf()

pl.yscale('log')
pl.xscale('log')

# Redshift space.
MockCat    = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/Observed_Multipoles_zCube_Wedge_0_Jenkins1.0_kbin_0.010_000.dat') 
MockCat    = MockCat[:,1]

for i in xrange(1, 40, 1):
    MockIn  = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/Observed_Multipoles_zCube_Wedge_'+str(i)+'_Jenkins1.0_kbin_0.010_000.dat')
    MockCat = np.vstack((MockIn[:,1], MockCat))

kvals        = MockIn[:,0]  
Mean         = np.mean(MockCat, axis=0)
Var          = np.var(MockCat,  axis=0)

pl.errorbar(kvals[1:]-0.0002, Mean[1:], np.sqrt(Var[1:])/np.sqrt(38), fmt='--', c='r', label='wedge')


# Redshift space.
MockCat    = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/Observed_Multipoles_zCube_Wedge_0_Jenkins1.0_kbin_0.010_000.dat') 
MockCat    = MockCat[:,2]

for i in xrange(1, 40, 1):
    MockIn  = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/Observed_Multipoles_zCube_Wedge_'+str(i)+'_Jenkins1.0_kbin_0.010_000.dat')
    MockCat = np.vstack((MockIn[:,2], MockCat))

kvals        = MockIn[:,0]  
Mean         = np.mean(MockCat, axis=0)
Var          = np.var(MockCat,  axis=0)

pl.errorbar(kvals[1:]-0.0002, Mean[1:], np.sqrt(Var[1:])/np.sqrt(38), fmt='--', c='r')


Data = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/Multipoles_zCube_Jenkins1.0_kbin_0.010_000.dat')
pl.loglog(Data[:,0], Data[:,1], 'k-.', label='cube')
pl.loglog(Data[:,0], Data[:,2], 'k-.')

A11Sq = 1.55

Data = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/Multipoles_zCube_Clipped_Jenkins1.0_kbin_0.010_000.dat')
pl.loglog(Data[:,0], A11Sq*Data[:,1], 'g-.', label='cube, clipped')
pl.loglog(Data[:,0], A11Sq*Data[:,2], 'g-.')


# Redshift space.
MockCat    = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/Multipoles_zCube_Wedge_0_Clipped_Jenkins1.0_kbin_0.010_000.dat') 
MockCat    = MockCat[:,1]

for i in xrange(1, 40, 1):
    MockIn  = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/Multipoles_zCube_Wedge_'+str(i)+'_Clipped_Jenkins1.0_kbin_0.010_000.dat')
    MockCat = np.vstack((MockIn[:,1], MockCat))

kvals        = MockIn[:,0]  
Mean         = np.mean(MockCat, axis=0)
Var          = np.var(MockCat,  axis=0)

pl.errorbar(kvals[1:]-0.0002, A11Sq*Mean[1:], np.sqrt(Var[1:])/np.sqrt(38), fmt='--', c='k', label='wedge, clipped')

'''
# Redshift space.
MockCat    = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/Multipoles_zCube_Wedge_0_Clipped_Jenkins1.0_kbin_0.010_000.dat') 
MockCat    = MockCat[:,2]

for i in xrange(1, 40, 1):
    MockIn  = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/Multipoles_zCube_Wedge_'+str(i)+'_Clipped_Jenkins1.0_kbin_0.010_000.dat')
    MockCat = np.vstack((MockIn[:,2], MockCat))

kvals        = MockIn[:,0]  
Mean         = np.mean(MockCat, axis=0)
Var          = np.var(MockCat,  axis=0)

pl.errorbar(kvals[1:]-0.0002, A11Sq*Mean[1:], np.sqrt(Var[1:])/np.sqrt(38), fmt='--', c='k')
'''

# MB = -20.0
linearBias = 1.495903

beta       = 0.54  

KaiserMono =  1. + (2./3.)*beta + 0.2*beta*beta
KaiserQuad = (4./3.)*beta + (4./7.)*beta*beta

HOD = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/HODTheoryPk/Pk_hod_20.0.dat')

pl.loglog(HOD[:,0], KaiserMono*HOD[:,1], 'k')
pl.loglog(HOD[:,0], KaiserQuad*HOD[:,1], 'k')
# pl.loglog(HOD[:,0],            HOD[:,1], 'k')
'''
kaiserLorentzNorm = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/KaiserLorentzMultipoles_Pk_HOD_-20.0_beta_0.54_velDispersion_3.50.dat')
pl.loglog(kaiserLorentzNorm[:,0], kaiserLorentzNorm[:,2]/kaiserLorentzNorm[:,2], 'r', label=r'HOD, $\sigma = 3.5$')

kaiserLorentzNorm = kaiserLorentzNorm[:,2]

kaiserLorentz = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/KaiserLorentzMultipoles_Pk_HOD_-20.0_beta_0.54_velDispersion_3.00.dat')
pl.loglog(kaiserLorentz[:,0], kaiserLorentz[:,2]/kaiserLorentzNorm, 'k', label=r'HOD, $\sigma = 3.0$')
#pl.loglog(kaiserLorentz[:,0], kaiserLorentz[:,3], 'k')

kaiserLorentz = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/KaiserLorentzMultipoles_Pk_HOD_-20.0_beta_0.54_velDispersion_4.00.dat')
pl.loglog(kaiserLorentz[:,0], kaiserLorentz[:,2]/kaiserLorentzNorm, 'g', label=r'HOD, $\sigma = 4.0$')
#pl.loglog(kaiserLorentz[:,0], kaiserLorentz[:,3], 'g')

kaiserLorentz = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/KaiserLorentzMultipoles_Pk_Linear_-20.0_beta_0.54_velDispersion_3.00.dat')
pl.loglog(kaiserLorentz[:,0], kaiserLorentz[:,2]/kaiserLorentzNorm, 'k--', label=r'linear, $\sigma = 3.0$')
#pl.loglog(kaiserLorentz[:,0], kaiserLorentz[:,3], 'k--')

kaiserLorentz = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/KaiserLorentzMultipoles_Pk_Linear_-20.0_beta_0.54_velDispersion_2.75.dat')
pl.loglog(kaiserLorentz[:,0], kaiserLorentz[:,2]/kaiserLorentzNorm, 'r--', label=r'linear, $\sigma = 2.75$')
#pl.loglog(kaiserLorentz[:,0], kaiserLorentz[:,3], 'r--')

kaiserLorentz = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/KaiserLorentzMultipoles_Pk_Linear_-20.0_beta_0.54_velDispersion_2.50.dat')
pl.loglog(kaiserLorentz[:,0], kaiserLorentz[:,2]/kaiserLorentzNorm, 'g--', label=r'linear, $\sigma = 2.5$')
#pl.loglog(kaiserLorentz[:,0], kaiserLorentz[:,3], 'g--')

kaiserLorentz = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/KaiserLorentzMultipoles_Pk_Linear_-20.0_beta_0.54_velDispersion_2.00.dat')
pl.loglog(kaiserLorentz[:,0], kaiserLorentz[:,2]/kaiserLorentzNorm, 'y--', label=r'linear, $\sigma = 2.00$')
#pl.loglog(kaiserLorentz[:,0], kaiserLorentz[:,3], 'g--')


pl.clf()
kaiserLorentzNorm = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/KaiserLorentzMultipoles_Pk_HOD_-20.0_beta_0.54_velDispersion_3.50.dat')
kaiserLorentzNorm = kaiserLorentzNorm[:,2]

kaiserLorentz = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/KaiserLorentzMultipoles_Pk_HOD_-20.0_beta_0.54_velDispersion_3.00.dat')
pl.loglog(kaiserLorentz[:,0], kaiserLorentz[:,3]/kaiserLorentzNorm, 'k', label=r'HOD, $\sigma = 3.0$')

kaiserLorentz = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/KaiserLorentzMultipoles_Pk_HOD_-20.0_beta_0.54_velDispersion_3.50.dat')
pl.loglog(kaiserLorentz[:,0], kaiserLorentz[:,3]/kaiserLorentzNorm, 'r', label=r'HOD, $\sigma = 3.5$')

kaiserLorentz = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/KaiserLorentzMultipoles_Pk_HOD_-20.0_beta_0.54_velDispersion_4.00.dat')
pl.loglog(kaiserLorentz[:,0], kaiserLorentz[:,3]/kaiserLorentzNorm, 'g', label=r'HOD, $\sigma = 4.0$')

kaiserLorentz = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/KaiserLorentzMultipoles_Pk_Linear_-20.0_beta_0.54_velDispersion_3.00.dat')
pl.loglog(kaiserLorentz[:,0], kaiserLorentz[:,3]/kaiserLorentzNorm, 'k--', label=r'linear, $\sigma=3.00$')

kaiserLorentz = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/KaiserLorentzMultipoles_Pk_Linear_-20.0_beta_0.54_velDispersion_2.75.dat')
pl.loglog(kaiserLorentz[:,0], kaiserLorentz[:,3]/kaiserLorentzNorm, 'r--', label=r'linear, $\sigma=2.75$')

kaiserLorentz = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/KaiserLorentzMultipoles_Pk_Linear_-20.0_beta_0.54_velDispersion_2.50.dat')
pl.loglog(kaiserLorentz[:,0], kaiserLorentz[:,3]/kaiserLorentzNorm, 'g--', label=r'linear, $\sigma=2.50$')

kaiserLorentz = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/KaiserLorentzMultipoles_Pk_Linear_-20.0_beta_0.54_velDispersion_2.00.dat')
pl.loglog(kaiserLorentz[:,0], kaiserLorentz[:,3]/kaiserLorentzNorm, 'y--', label=r'linear, $\sigma=2.00$')
'''

# pl.axhline(y=1.1, xmin=0, xmax=0.01, color='k')
# pl.axhline(y=0.9, xmin=0, xmax=0.01, color='k')

pl.xlim([0.01, 0.8])
pl.ylim([10**2, 10**5])
# pl.title(r'Monopole, normed by HOD, $\sigma = 3.50$')
pl.title(r'Multipoles')

pl.ylabel(r'$P(k)$', fontsize = '10')
pl.xlabel(r'$k \ [h \ Mpc^{-1}]$', fontsize = '10')

leg = pl.legend(loc=3, ncol=1, prop = FontProperties(size = '10'))
leg.draw_frame(False)

xx, locs = plt.xticks()
ll = ['%.3f' % a for a in xx]
plt.gca().xaxis.set_major_formatter(FixedFormatter(ll))

pl.savefig('/disk1/mjw/HOD_MockRun/Plots/wedgeMultipoles.pdf')

pl.clf()

linearBias = 1.495903

beta       =  0.54  
KaiserMono =  1. + (2./3.)*beta + 0.2*beta*beta
KaiserQuad = (4./3.)*beta + (4./7.)*beta*beta

HOD = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/HODTheoryPk/Pk_hod_20.0.dat')

pl.loglog(HOD[:,0], KaiserQuad/KaiserMono*np.ones(len(HOD[:,0])), 'k')

Data = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/Multipoles_zCube_Jenkins1.0_kbin_0.010_000.dat')
pl.loglog(Data[:,0], Data[:,2]/Data[:,1], 'k', label='no threshold')

ClipData = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/Multipoles_zCube_Clipped_Jenkins1.0_kbin_0.010_000.dat')
pl.loglog(ClipData[:,0], ClipData[:,2]/ClipData[:,1], 'g', label='5.0 threshold')

ClipData = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/Multipoles_zCube_Clipped_3.0_Jenkins1.0_kbin_0.010_000.dat')
pl.loglog(ClipData[:,0], ClipData[:,2]/ClipData[:,1], 'r', label='3.0 threshold')

ClipData = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/Multipoles_zCube_Clipped_2.0_Jenkins1.0_kbin_0.010_000.dat')
pl.loglog(ClipData[:,0], ClipData[:,2]/ClipData[:,1], 'c', label='2.0 threshold')

ClipData = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/Multipoles_zCube_Clipped_1.0_Jenkins1.0_kbin_0.010_000.dat')
pl.loglog(ClipData[:,0], ClipData[:,2]/ClipData[:,1], 'y', label='1.0 threshold')


kaiserLorentz = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/KaiserLorentzMultipoles_Pk_Linear_-20.0_beta_0.54_velDispersion_2.50.dat')
pl.loglog(kaiserLorentz[:,0], kaiserLorentz[:,3]/kaiserLorentz[:,2], 'k--', label=r'Kaiser-Lorentz, linear, $\sigma = 2.5$')

kaiserLorentz = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/KaiserLorentzMultipoles_Pk_Linear_-20.0_beta_0.54_velDispersion_3.00.dat')
pl.loglog(kaiserLorentz[:,0], kaiserLorentz[:,3]/kaiserLorentz[:,2], 'k--', label=r'$\sigma = 3.0$')

kaiserLorentz = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Multipoles/KaiserLorentzMultipoles_Pk_Linear_-20.0_beta_0.54_velDispersion_3.50.dat')
pl.loglog(kaiserLorentz[:,0], kaiserLorentz[:,3]/kaiserLorentz[:,2], 'k--', label=r'$\sigma = 3.5$')

pl.xlabel(r'$k \ [h \ Mpc^{-1}]$', fontsize = '10')

leg = pl.legend(loc=3, ncol=1, prop = FontProperties(size = '10'))
leg.draw_frame(False)

xx, locs = plt.xticks()
ll = ['%.3f' % a for a in xx]
plt.gca().xaxis.set_major_formatter(FixedFormatter(ll))

pl.xlim(0.005, 1.0)
pl.ylim(0.05, 2.)
pl.title('HOD z-space cube, clipped. Quadrupole to Monopole ratio.')

pl.savefig('/disk1/mjw/HOD_MockRun/Plots/zCube_Quad2Mono.pdf')
