data = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/splineChecks/HODMocks_MockAvg_nz_chiSliced_16.0_W1_22.00_50.0.dat')
pl.plot(data[:,0], data[:,1])

data = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/nz/HODMocks_MockAvg_nz_chiSliced_16.0_W1_22.00_50.0.dat')
pl.plot(data[:,1], data[:,3])

pl.savefig('/disk1/mjw/HOD_MockRun/Plots/nzSplineCheck.pdf')
