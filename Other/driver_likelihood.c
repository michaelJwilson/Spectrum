#define  KBIN_NO 40

#include "/home/mjw/Aux_functions/header.h"
#include "/home/mjw/Aux_functions/Aux_functions.c"

#include "header.h"
#include "FFT_log.h"
#include "header_W2.h"
#include "header_chi2.h"
#include "struct_regress.h"
// #include "struct_multipoles.h"
#include "cosmology_planck15.h"

#include "AgeOftheUniverse.c"
#include "linearGrowthRate.c"
#include "angular_limits.c"
#include "chi_zcalc.c"
#include "assign_binnedpk_memory.c"
#include "likelihood_memory.c"
#include "KaiserMultipoles.c"
#include "KaiserLorentzMultipoles.c"
#include "FFT_log.c"
#include "viperskwindow.c"
#include "viperswindow.c"
#include "vipersjwindow.c"
#include "FFTlog_vipers_clipping.c"
#include "toymodel_pk_xi.c"
#include "linear_pk.c"
#include "nonlinear_pk.c"
#include "get_pkderivedprops.c"
#include "get_allkvals.c"
#include "super_vipers.c"
#include "MultipoleCovariance_eigenvecs.c"
#include "MultipoleCovariance.c"
#include "ChiSq_input.c"
#include "calc_model.c"
#include "ChiSq_minimisation.c"
#include "onedposteriors.c"
#include "clip_icc.c"
#include "lock_files.c"
#include "AlcockPaczynski.c"
// #include "FisherForecast.c"
#include "FisherForecastFAP.c"
#include "Ruiz.c"
#include "camb_call.c"
// #include "joint_clipped_fsig8.c"
#include "priors.c"


int printf_mull(){
  if(mull == 0){
    printf("***  Generating new results (mull == %d).  ***", mull);
  }

  else{
    printf("***  Replicating skene results (mull == %d).  ***", mull);
  }

  printf("\n\n");
  
  return 0;
}
  
int main(int argc, char** argv){
  mull                      =                           1;  // 0 for False; 1 for True (replicate mull/skene)  
  thread                    =                           1;

  z_eff                     =        atof(getenv("ZEFF"));
  
  outputdir                 =         getenv("outputdir");
  maskmultipoles_path       =        getenv("mask_Qldir");
    
  sprintf(root_dir,                              "/home/mjw/HOD_MockRun");
  sprintf(vipersHOD_dir,         "/home/mjw/HOD_MockRun/W1_Spectro_V7_2"); 
  sprintf(models_path,                                         outputdir);

  if(mull==0){
    sprintf(covariance_mocks_path,                             outputdir);
  }

  else{
    sprintf(covariance_mocks_path, "/home/mjw/HOD_MockRun/W1_Spectro_V7_2");                // W1_Spectro_V7_3
    sprintf(maskmultipoles_path,   "/home/mjw/HOD_MockRun/W1_Spectro_V7_2");
  }
  
  d0                        =    atoi(argv[1]);
  fieldFlag                 =    atoi(argv[2]);
  lo_zlim                   =    atof(argv[3]);   // previously 0.6<z<0.9, 0.7<z<1.1
  hi_zlim                   =    atof(argv[4]);
  ChiSq_kmax                =    atof(argv[5]);
  
  min_alpha_pad             =    0.9999;
  max_alpha_pad             =    1.0001;

  min_epsilon_pad           =   -0.0001;
  max_epsilon_pad           =    0.0001;
 
  min_A11Sq                 =      0.99;  // distinct from linear bias due to spectral distortion. 
  max_A11Sq                 =      1.01;

  paramNumber               =       3.0;  // # of fitted params. -> dof in X^2. 

   Res                      =        16;  // Likelihood resolution [voxel number].
  dRes                      =      16.0;  // Previously 16: 13/02/17

   Res_ap                   =         1;  // Resoltuion in AP.
  dRes_ap                   =       1.0;

  FFTlogRes                 =       768;  //  768 on skenechecked -- commit May 17 before Berkeley. 
  // FFTlogRes              =      4096;  // 4096 on master / qsmult (15/12/17).
  
  logk_min                  =      -2.0;
  logk_max                  =   0.60206;  // k = 4 hMpc^{-1}.
  
  ChiSq_kmin                =      0.02;  // Clipping: 0.6 < z < 0.8 h Mpc^-1: ChiSq_kmin = 0.11; 

  hiMultipoleOrder          =         2;  // Fit monopole (1) or mono + quad (2).
  jenkins_fold_kjoin        =       0.4;  // k at which P(k) switches from unfolded to folded.     
  modkMax                   =      1.00;  

  smooth_radius             =       2.0;

  // Regression to ~ May 2016 -> catalog number from 153 independent to 305; change file paths of mocks (covariance and chi sq input) and Q-multipoles. Change init_covariance.
  CatalogNumber             =       153;

  
  start_walltime();

  // set_oldestpriors();
  set_recordedpriors();
  // set_normalpriors();
  // set_clippingpriors();
  // set_widepriors(); 
  
  printf_branch();

  printf_mull();
  
  fftw_init_threads();

  fftw_plan_with_nthreads(omp_get_max_threads()); // Maximum number of threads to be used; use all openmp threads available. 

  set_angularlimits(0, fieldFlag);                // Cut data to mock limits.
  
  chi_zcalc();              
  
  nonlinear_pk();             
  // linear_pk();       
  
  if(mull == 0)  get_mocksshotnoise();       // <n> estimate without clipping.  high-k estimate with clipping. 
  
  prep_FFTlog_memory();                      // assign memory for arrays speeding up FFTlog calc; e.g. xi -> pre/post factors. 
  
  set_FFTlog(FFTlogRes, pow(10., -10.), pow(10., 14.), 1., velDispersion);  // assigns values to mono_config etc. 
  
  prep_VIPERS_maskMultipoles();
  
  prep_VIPERS_jmaskMultipoles();
  
  precompute_vipers_clipping_model(FFTlogRes);  // Computes P_R(k), W_0(r), ..., \tilde W_0(k), ..., and \tilde W_0(k) for the joint field.   
  
  get_allkvals(1);            // all kVals, ignoring ChiSq_kmin and ChiSq_kmax, but including folding. 
  
  allkvals_matchup();         // Match all available kVals to FFTlog modes; not just those up to ChiSq_kmax. 
  
  set_chiSq_intervals();      // set e.g. fsig8 interval = (max - min)/interval.
    
  assign_LikelihoodMemory();  // Assigns memory for xdata, ydata, xtheory, ytheory, ChiSqGrid.
  
  // get_mocksclippedamplitudes();

  // set_clippingvars();
  // set_oldclippingvars();
  
  load_CovarianceMatrix(CatalogNumber, 1);
  
  prewhitenCov();  // Pre-whiten data and covariance.
  
  // scale_Cov(CatalogNumber);
  
  Covariance_eigenVecs(CatalogNumber);
  
  delete_lockfile();
  
  prep_dlnPR_dlnk();

  kvals_matchup();  // Now match only available modes between ChiSq_kmin and ChiSq_kmax.
  
  // if(ChiSq_kmax == 0.2)
  calc_models();
  
  set_models();
  
  char   warning[200];
  double maxL_fsig8, maxL_sigv, maxL_bsig8;
  
  write_priors();
  
  for(data_mock_flag=0; data_mock_flag<2; data_mock_flag++){
    if(data_mock_flag == 0){
      sprintf(filepath, "%s/mocks_v1.7/fsig8/d0_%d/W%d/kmax_%.1lf/mocks6_%.1lf_%.1lf_%s_res_%d.dat", outputdir, d0, fieldFlag, ChiSq_kmax, lo_zlim, hi_zlim, model_flag, Res);
    }

    if(data_mock_flag == 1){
      sprintf(filepath, "%s/data_v1.7/fsig8/d0_%d/W%d/kmax_%.1lf/data6_%.1lf_%.1lf_%s_res_%d.dat", outputdir, d0, fieldFlag, ChiSq_kmax, lo_zlim, hi_zlim, model_flag, Res);
    }
    
    // output = fopen(filepath, "w");
    
    walltime("Walltime at start of chi^2 calc.");

    // for(int ab=1; ab<CatalogNumber; ab++){
    for(int ab=1; ab<20; ab++){ // mocks labelled 1 to 153 (305) 
      calc_ChiSqs(ab, 0);
      
      set_minChiSq();
      
      calc_onedposteriors(&maxL_fsig8, &maxL_bsig8, &maxL_sigv);

      prior_warnings(maxL_fsig8, maxL_bsig8, maxL_sigv, warning); 
      
      // maximum likelihood of one-dim posteriors and of entire parameter space. 
      printf("\n%.6lf \t %.6lf \t %.6lf \t %.6lf \t %.6lf \t %.6lf \t %s", maxL_fsig8, maxL_bsig8, maxL_sigv, minX2_fsig8, minX2_bsig8, minX2_sigp, warning);
      
      // fprintf(output, "%.6lf \t %.6lf \t %.6lf \t %.6lf \t %.6lf \t %.6lf \n", maxL_fsig8, maxL_sigv, maxL_bsig8, minX2_fsig8, minX2_sigp, minX2_bsig8);
      
      if(data_mock_flag == 1)  break; // Only one calculation if data.
    }
    
    // fclose(output);
  }
  
  /*
  default_params();

  // getmockmean_params(d0);
  
  // set_fittomean_params();
  
  model_compute(0, 0, 0, 0, 0, 1);
  */
  // jointfield_cnvldmodel();

  // calc_bestfit_fsig8(fieldFlag, ChiSq_kmax, z_eff);
  
  walltime("Wall time at finish");

  // MPI_Finalize();
  
  printf("\n\n");
  
  exit(EXIT_SUCCESS);
}
