#include <stdbool.h>

#include <gsl/gsl_sf_bessel.h>
#include <gsl/gsl_sf_erf.h>
#include <gsl/gsl_sf_gamma.h>
#include <gsl/gsl_rng.h>
#include <gsl/gsl_sf_legendre.h>
#include <gsl/gsl_linalg.h>

// Stacpolly run. 
// #define AUXfn_DIR "/home/mjw/Aux_functions/header.h"

#define   AUXfn_header "/disk1/mjw/Aux_functions/header.h"
#include  AUXfn_header

#define   AUXfn_funcs  "/disk1/mjw/Aux_functions/Aux_functions.c"
#include  AUXfn_funcs

#include "Scripts/header.h"

#include "/disk1/mjw/Aux_functions/SVD.c"

#include "Scripts/comovDistRedshiftCalc.c"

#include "Scripts/JenkinsRun.c"
#include "Scripts/GridParams.c"

#include "Scripts/assignMemory.c"

#include "Scripts/CoordinateCalc.c"
#include "Scripts/CoordinateCalcCube.c"
#include "Scripts/assignAcceptance.c"

#include "Scripts/ArtificialWf.c"

#include "Scripts/NGPCalc.c"
#include "Scripts/CloudInCell.c"
#include "Scripts/BasisChange.c"
#include "Scripts/CalcCellraDec.c"

#include "Scripts/FKPweights.c"
#include "Scripts/Windowfn_PkCorrections.c"

#include "Scripts/KaiserMultipoles.c"
// #include "Scripts/KaiserGaussMultipoles.c"
#include "Scripts/KaiserLorentzMultipoles.c"

#include "Scripts/qSortCompare.c"
#include "Scripts/FFTw_3D.c"
#include "Scripts/FFTw_3Dwf.c"
#include "Scripts/FFTw_3Dwf_pad.c"
#include "Scripts/axesWfSlices.c"

#include "Scripts/MeasureWfKernel.c"
// #include "Scripts/sphericalConvolvePk.c"
#include "Scripts/setConvolutionKernels.c"
// #include "Scripts/AnalyticTestConvolution.c"
#include "Scripts/ConvolvePkAnisoWf.c"

#include "Scripts/IntegralConstraintCorrection.c"

#include "Scripts/ComovingNumberDensityCalc.c"

#include "Scripts/AgeOftheUniverse.c"
#include "Scripts/linearGrowthRate.c"
#include "Scripts/growthfactor_derivative.c"

#include "Scripts/InvErrorfn.c"
#include "Scripts/MatrixInverse.c"

#include "Scripts/Clipped_zSpace.c"

#include "Scripts/zCubeCreate.c"
#include "Scripts/wedgeMockCreate.c"
#include "Scripts/rollCube.c"

#include "Scripts/MultipoleCovariance.c"
#include "Scripts/Multipoles_EigenVecsCovariance.c"
#include "Scripts/MultipoleCovariance_Inverse.c"
#include "Scripts/MultipolesRealisation_MultiVariateGauss.c"
#include "Scripts/Multipole_minimiseChiSq.c"
#include "Scripts/Multipole_MarginalisedPosteriors.c"
#include "Scripts/Multipole_2DPosteriors.c"

#include "Scripts/BootStrap.c"
#include "Scripts/freeMemory.c"

#include "/disk1/mjw/EisensteinHu/power.c"


int main(int argc, char **argv){

    sprintf(root_dir,      "/disk1/mjw/HOD_MockRun");
    sprintf(vipersHOD_dir, "/disk1/mjw/VIPERS_HOD_Mocks");

    // Stacpolly run. 
    // sprintf(root_dir, "/home/mjw/HOD_MockRun");

    // MPI_Init(&argc,&argv);
    // MPI_Comm_rank(MPI_COMM_WORLD, &process_rank);
    // MPI_Comm_size(MPI_COMM_WORLD, &process_number);

    // Co-ordinate limits (Volume) defined by the random catalogue. 
    
    // lower_xlimit & upper_xlimit
    AxisLimsArray[0][0]       =        0.0;                                 // h^-1 Mpc
    AxisLimsArray[1][0]       =       1000.;                                 // h^-1 Mpc

    // lower_ylimit & upper_ylimit
    AxisLimsArray[0][1]       =        0.0;                                 // h^-1 Mpc
    AxisLimsArray[1][1]       =      1000.;                                 // h^-1 Mpc

    // lower_zlimit & upper_zlimit
    AxisLimsArray[0][2]       =        0.0;                                 // h^-1 Mpc
    AxisLimsArray[1][2]       =      1000.;                                 // h^-1 Mpc
                
    CellSize                  =        4.0;                                 // Cell size, comoving distance, h^-1 Mpc

    // Selection parameters. Mag 20.0 galaxies at redshift 0.8;
    redshiftLowLimit          =       0.795;
    redshiftHiLimit           =       0.805;
    absMagCut                 =      -20.00;

    // Apply Jenkin's scaling to beat aliasing.
    JenkinsScalefactor        =        1.0;

    // FKP P(k) of interest.
    fkpPk                     =      5000.;                                               // [P(k)] = [h^-1 Mpc]^3, Peeble's convention.

    // Binning interval for P(k).
    kbinInterval              =       0.01;
    modkMax                   =        1.2;
    muBinNumb                 =         50;

    gsl_rng_env_setup();

    gsl_ran_T                 = gsl_rng_default;
    gsl_ran_r                 = gsl_rng_alloc(gsl_ran_T);
    
    // Non-linear RSD
    beta                      =       0.493;                  // beta = 0.542
    velDispersion             =       2.53;                   // units of h^-1 Mpc rather than 300 km s^-1
    A11Sq                     =       0.567;
    
    // Priors on the model params.
    min_beta                  =      0.40;
    max_beta                  =      0.60;

    min_velDisperse           =       2.0;
    max_velDisperse           =       4.0;
 
    // upweight data. 
    min_A11Sq                 =       0.45;
    max_A11Sq                 =       0.65;

    // Resolution of the Likelihood evaluation [voxel number].
     Res                      =        30;
    dRes                      =      30.0;
    
    ChiSqEval_kmin            =      0.02;
    ChiSqEval_kmax            =       0.4; 
    
    /* linearBias.txt in dir. /HODTheoryPk/
    -22.0  2.924277
    -21.5  2.199471
    -21.0  1.824770
    -20.5  1.618792
    -20.0  1.495903
    -19.5  1.415186
    -20.75 1.707502
    -20.25 1.550205
    -20.15 1.527030
    */
    
    linearBias                =   1.495903;
    
    // Clipping variables. 
    appliedClippingThreshold  =     1000.0;    
    // linearBias             = sqrt(2.90);
    
    // zCubeCreate();
    
    // wedgeMockCreate(400., 150., 600., 150., 700., 850., 300., 850., 475., 525.);
    
    comovDistReshiftCalc();

    // JenkinsCoordinates();
    
    EvaluateGridParameters();
   
    // assign binning interval in k, and calculate number of bins required. 
    assignbinninginterval(kbinInterval);

    prepNGP();
    
    // No artificially applied window fn. 
    
    FullCube();
    // EmbeddedCube(50);
    // Gaussian(250.);
    // PencilBeamSurvey(25, 55, 25, 55);
    // Spherical(250.);
    // AnisoGauss(20., 30., 40.);
    
    Cell_AppliedWindowFn  = &Cell_SurveyLimitsMask[0];

    CalcCellraDec();

    // TotalSurveyedVolume initialised to zero in header.h
    TotalSurveyedVolume   = SumDoubleArray(Cell_AppliedWindowFn, n0*n1*n2)*CellVolume;
    
    prepFFTw(n0, n1, n2);
    
    prepFFTbinning();

    assign2DPkMemory();                
        
    // inputHODPk();
    
    pt2Pk = &splintLinearPk;
    
    inputLinearPk();

    pt2shot = &CubeShot;
    
    // Mean number density is the same when boot strapping. 
    pt2nz = &CubeMeanNumberDensity;
        
    sprintf(surveyType, "GaussCube_BootStrap_clipThreshold_%.1e_fullCube", appliedClippingThreshold, loopCount);
    /*
    Gaussianfield();
    
    prepBootStrap(n0*n1*n2, Cell_rotatedXvals, Cell_rotatedYvals, Cell_rotatedZvals, 1000.);
    
    for(loopCount=0; loopCount<100; loopCount++){
        sprintf(surveyType, "GaussCube_BootStrap_clipThreshold_%.1e_fullCube", appliedClippingThreshold, loopCount);
    
    	BootStrapGen(n0*n1*n2, Cell_rotatedXvals, Cell_rotatedYvals, Cell_rotatedZvals, 1000.);

	    // clipDensity(appliedClippingThreshold);
                
        CalcWfCorrections();
            
        cleanFFTbinning();
    
        PkCalc();
    }
    */
    // wfPkCalc();
    
    // kaiser_nonlinearSuppression_Multipoles();
    
     LikelihoodMemory();
    
     CovarianceMatrix(100,  120, 1);
    
     CovarianceEigenVecs(120, 1);
    
    // CovarianceInverse(80);
    
    // ClippingModelling();
    
    // formPkCube();

    // clipCorrfn();

    // multipolesRealisation(80);
    
    // minimiseChiSq(80);
    
    // Calc_betaPosterior();

    // Calc_sigmaPosterior();

    // Calc_betaSigmaPosterior();
    
    // ConfidenceLimits_2D();
    
    // assign2DPkMemory();

    // InvErrorfnTest();

    // Theory2Dpk();
    
    // Observed2Dpk();

    // Stacpolly run. 
    // MPI_Finalize();
    
    // sprintf(surveyType, "zPencilBeamCube_Jenkins%.1f_xtrans_%.2f_ytrans_%.2f", JenkinsScalefactor, ii*xtranslateDist, jj*ytranslateDist);
    
    // MockAvgMultipole(26);
    
    // growthfactor_derivative();
    
    printf("\n\n");

    return 0;
}
