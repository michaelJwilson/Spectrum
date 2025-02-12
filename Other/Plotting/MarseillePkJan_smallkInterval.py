# Now using a single mock estimate of Nz, but a volume limited sample at -21.00;

MockCat      = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Del2k/midK_Del2k_VIPERSparent_GaussSmoothNz_100.0_SkinDepth_5.0_VolLim_-20.15_kInterval_0.02_001.dat')
MockCat      = MockCat[:,2]

for i in xrange(2, 10, 1):
    MockIn   = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Del2k/midK_Del2k_VIPERSparent_GaussSmoothNz_100.0_SkinDepth_5.0_VolLim_-20.15_kInterval_0.02_00'+str(i)+'.dat')
    MockCat  = np.vstack((MockIn[:,2], MockCat))
    

for i in xrange(10, 27, 1):
    MockIn   = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Del2k/midK_Del2k_VIPERSparent_GaussSmoothNz_100.0_SkinDepth_5.0_VolLim_-20.15_kInterval_0.02_0' +str(i)+ '.dat')
    MockCat  = np.vstack((MockIn[:,2], MockCat))

kvals        = MockIn[:,0]  

Mean         = np.mean(MockCat, axis=0)
Var          = np.var(MockCat,  axis=0)

pl.errorbar(kvals[1:] - 0.0005, Mean[1:], np.sqrt(Var[1:])/np.sqrt(25), c='c', fmt='o',  label='Vol. lim., $M_B<-20.15$, \n single mock n(z)', markersize='1')


# Now using a mock avg. estimate of Nz, but a volume limited sample at -21.00;

MockCat      = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Del2k/midK_Del2k_VIPERSparent_GaussSmoothMockAvgNz_100.0_SkinDepth_5.0_VolLim_-20.15_kInterval_0.02_001.dat')
MockCat      = MockCat[:,2]


for i in xrange(2, 10, 1):
    MockIn   = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Del2k/midK_Del2k_VIPERSparent_GaussSmoothMockAvgNz_100.0_SkinDepth_5.0_VolLim_-20.15_kInterval_0.02_00'+str(i)+'.dat')
    MockCat  = np.vstack((MockIn[:,2], MockCat))
    

for i in xrange(10, 27, 1):
    MockIn   = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Del2k/midK_Del2k_VIPERSparent_GaussSmoothMockAvgNz_100.0_SkinDepth_5.0_VolLim_-20.15_kInterval_0.02_0' +str(i)+ '.dat')
    MockCat  = np.vstack((MockIn[:,2], MockCat))
 
kvals        = MockIn[:,0]  

Mean         = np.mean(MockCat, axis=0)
Var          = np.var(MockCat,  axis=0)

pl.errorbar(kvals[1:] + 0.0005, Mean[1:], np.sqrt(Var[1:])/np.sqrt(25), c='b', fmt='o', label='Vol. lim., $M_B<-20.15$, \n mock avg. n(z), $\sigma_{n(z)} = 100.$', markersize='1')

pl.yscale('log')
pl.xscale('log')

#theory         = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/HODTheoryPk/Pk_hod_19.5.dat')
#pl.loglog(theory[:,0], theory[:,1], label='vol. limited, $M_B< -19.5$')

theory         = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/HODTheoryPk/Pk_hod_20.15.dat')
pl.loglog(theory[:,0], theory[:,1], 'c', label='vol. limited, $M_B< -20.15$')

theory         = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/HODTheoryPk/Pk_hod_20.5.dat')
pl.loglog(theory[:,0], theory[:,1], 'g', label='vol. limited, $M_B< -20.5$')

theory         = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/HODTheoryPk/Pk_hod_21.0.dat')
pl.loglog(theory[:,0], theory[:,1], 'r', label='vol. limited, $M_B< -21.0$')

# Cube      = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/Del2k/midK_Del2k_FullCube_Jenkins1.0.dat')
# pl.loglog(Cube[:,0], Cube[:,2], 'g^', label='Mock 001')

conv           = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/ConvolvedPk/IntegralConstraint_Uncorrected/VIPERSsurvey_HODinput_VolLim_-20.15_kbinInterval_0.02.dat')
pl.loglog(conv[:,0], conv[:,2], 'c^', label='theory conv.', markersize='3')

IccCorrected   = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/ConvolvedPk/IntegralConstraint_Corrected/VIPERSsurvey_HODinput_VolLim_-20.15_kbinInterval_0.02.dat')
pl.plot(IccCorrected[1:,0], IccCorrected[1:,2], 'c^', label='Convolved + ICC corrected.', markersize='3')

pl.xlim([0.01, 0.8])
pl.ylim([5.*10**2, 3.2*10**4])

pl.ylabel(r'$P(k)$', fontsize = '10')
pl.xlabel(r'$k \ [h \ Mpc^{-1}]$', fontsize = '10')

pl.title('All parent mocks, ($0.7<z<0.9$)')

leg = pl.legend(loc=1, ncol=1, prop = FontProperties(size = '10'))
leg.draw_frame(False)

xx, locs = plt.xticks()
ll = ['%.3f' % a for a in xx]
plt.gca().xaxis.set_major_formatter(FixedFormatter(ll))

pl.savefig('/disk1/mjw/HOD_MockRun/Plots/VIPERS_Pk_smallkInterval.pdf')
