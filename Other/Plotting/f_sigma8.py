data      = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/zComovingDistance/f_sigma8.dat')

data[:,0] = np.exp(-1.*data[:,0]) - 1.

pl.plot(data[:,0], data[:,1], 'k', label=r'$D_{+}(z)$')
pl.plot(data[:,0], data[:,2], 'r', label=r'approx $D_{+}(z)$, integrate $\Omega_{M}^{\gamma}$')

pl.plot(data[:,0], data[:,3], 'y', label='f(z)')
pl.plot(data[:,0], data[:,5], 'b', label=r'$\Omega_{M}^{\gamma}$')
pl.plot(data[:,0], data[:,4], 'g', label=r'$\beta$, b = 1.496 for $M_{B} = -20.0$ sample')

pl.plot(data[:,0], data[:,6], 'c', label=r'$f \sigma_8(z)$')

pl.legend(loc=4)

pl.xlabel('z')

pl.xlim(0.0, 0.9)
pl.ylim(0.25, 1.0)

pl.savefig('/disk1/mjw/HOD_MockRun/Plots/f_sigma8.pdf')
