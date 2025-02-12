uncorrected      = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/ConvolvedPk/IntegralConstraint_Uncorrected/midK_Pk_Sphericalsplint_padded.dat')
pl.plot(uncorrected[:,0], uncorrected[:,1], 'b^', label='Convolved, integral constraint uncorrected.')

corrected        = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/ConvolvedPk/IntegralConstraint_Corrected/midK_Pk_Sphericalsplint_padded.dat')
pl.plot(corrected[:,0], corrected[:,1], 'g^', label='Convolved, integral constraint corrected.')

Camb             = np.loadtxt('/disk1/mjw/HOD_MockRun/Data/HODTheoryPk/cambExtendedPk_hod_20.0.dat')
pl.plot(Camb[:,0], Camb[:,1], 'y', label='HOD theory')

leg = pl.legend(loc=1, ncol=1, prop = FontProperties(size = '10'))
leg.draw_frame(False)

pl.xlim([0.0, 0.1])

xx, locs = plt.xticks()
ll = ['%.3f' % a for a in xx]
plt.gca().xaxis.set_major_formatter(FixedFormatter(ll))

pl.ylabel(r'$P(k)$', fontsize = '10')
pl.xlabel(r'$k \ [h \ Mpc^{-1}]$', fontsize = '10')

pl.savefig('/disk1/mjw/HOD_MockRun/Plots/ConvolvedPk/IntegralConstraintCorrected_sphericalWf.eps')
