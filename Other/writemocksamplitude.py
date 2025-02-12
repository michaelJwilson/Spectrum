import os,        sys 
import numpy   as np
import pandas  as pd
from   scipy.optimize import minimize_scalar

root   = os.environ['outputdir']
root  += "/mocks_v1.7/"

        
mocks  = 153
labels = np.array([i for i in xrange(1, mocks + 1)])

args   = sys.argv

lo_zs  = np.array([np.float(args[1]), np.float(args[2])])
hi_zs  = np.array([np.float(args[3]), np.float(args[4])])

def simple_chi2(amp, unclipped, clipped, variance):
  return np.sum((unclipped - amp*clipped)**2./variance)

for a, field in enumerate(["W1", "W4"]):
  for b, lo_z in enumerate(lo_zs):
    hi_z     = hi_zs[b]

    filename = root + "pk_derivedprops/d0_%d/%s/shotnoise_zlim_%.1lf_%.1lf.dat" % (1000, field, lo_z, hi_z)
    shot     = np.loadtxt(filename)[:,1] # high k estimate. 

    ## get unfolded.
    files    = [root + "pk/d0_%d/%s/mock_" % (1000, field) + "{0:03}".format(i+1) + "_zlim_%.1lf_%.1lf_Jf_0.dat" % (lo_z, hi_z) for i in xrange(0, mocks, 1)]
    dflist   = [pd.read_csv(fname, sep='\t', header=None, names=['k', 'P0', 'P2', 'N'])  for fname in files]

    for k in range(len(dflist)):
      dflist[k]['P0'] -= shot[k]

    noclipdf = pd.concat(dflist)
                
    indices  = dflist[0]['k'].between(0.08, 0.20) # fit at high k. 

    mean     = noclipdf.groupby(noclipdf.index).mean()
    var      = noclipdf.groupby(noclipdf.index).var()['P0'][indices].values
            
    print field, "%.1lf < z < %.1lf" % (lo_z, hi_z)
    
    ## save amplitude correction of unity for d0 = 1000.
    np.savetxt(root + "pk_derivedprops/d0_%d/%s/suppression_zlim_%.1lf_%.1lf.dat" % (1000, field, lo_z, hi_z), np.column_stack((labels, np.ones(mocks))), fmt="%d \t %.6le")
      
    for c, d0 in enumerate([10, 6, 4]):                            
      filename = root + "pk_derivedprops/d0_%d/%s/shotnoise_zlim_%.1lf_%.1lf.dat" % (d0, field, lo_z, hi_z)
      shot     = np.loadtxt(filename)[:,1] # high k estimate. 
        
      ## get unfolded. 
      files   = [root + "pk/d0_%d/%s/mock_" % (d0, field) + "{0:03}".format(i+1) + "_zlim_%.1lf_%.1lf_Jf_0.dat" % (lo_z, hi_z) for i in xrange(0, mocks, 1)]
      mflist  = [pd.read_csv(fname, sep='\t', header=None, names=['k', 'P0', 'P2', 'N'])  for fname in files]
      
      for k in range(len(mflist)):
        mflist[k]['P0'] -= shot[k]
    
      clipdf  = pd.concat(mflist)

      #mean     = clipdf.groupby(clipdf.index).mean()
      #var      = clipdf.groupby(clipdf.index).var()
                    
      results = []
           
      for i in xrange(0, mocks, 1):        
        answer = minimize_scalar(simple_chi2, bounds=(1., 100.), args=(dflist[i]['P0'][indices].values, mflist[i]['P0'][indices].values, var), method='brent')
        results.append(answer.x)
      
      np.savetxt(root + "pk_derivedprops/d0_%d/%s/suppression_zlim_%.1lf_%.1lf.dat" % (d0, field, lo_z, hi_z), np.column_stack((labels, np.array(results))), fmt="%d \t %.6le")
    
