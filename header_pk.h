// Path to relevant directories. 
char         vipersHOD_dir[200];
char covariance_mocks_path[200];

// Misc. //
int    data_mock_flag;
int    thread; // Multi-thread FFTw, but 1 means multithread useful loops aswell.

int    thread_no;

// -- thread safe random number streams. --//
typedef struct drand48_data drand48_data;

drand48_data* randBuffers;
// struct drand48_data randBuffers

// r2c or c2c arrays/ 
int     fft_size;

double* overdensity;
double* smooth_overdensity;

// fftw_complex* overdensity;
// fftw_complex* smooth_overdensity;

fftw_complex* H_k;

//-- embedding volume --// 
double    lopad;
double    TotalVolume         = 0.0;
double    TotalSurveyedVolume = 0.0;

double    stefano_trans_x;  // translation parameters for Stefano's co-ordinates.
double    stefano_trans_y;
double    stefano_trans_z;

//-- Jenkins folding --//
int fold;

//-- VIPERS --//
int               max_gals;  // max. number of galaxies (lines) in any mock in covariance calc, i.e. in files in mocks directory.
int           accepted = 0;
int             Vipers_Num;

double        loChi;
double        hiChi;

double        UpperRAlimit;
double        LowerRAlimit;

double        UpperDecLimit;
double        LowerDecLimit;

int*                id   = NULL;
double*             ra   = NULL;
double*            dec   = NULL;
double*           zobs   = NULL;
double*           zcos   = NULL;
double*            M_B   = NULL;
double*          zflag   = NULL;
int*              type   = NULL;
int*          photoMask  = NULL;

double*           zpec   = NULL;  // Value added catalogue parameters.
double*          zphot   = NULL;
double*          gal_z   = NULL;
double*         sampling = NULL;
double*    fkp_galweight = NULL;
double*   clip_galweight = NULL;

// derived parameters
bool*    Acceptanceflag = NULL;
double*          rDist  = NULL;
double*          xCoor  = NULL;
double*          yCoor  = NULL;
double*          zCoor  = NULL;


// -- Randoms --//
double                   alpha; // ratio of N_rand to N_gal pretty much. 

int          rand_number   = 0;
int          accepted_rand = 0;

double       fkp_accepted_rand = 0.0;

double*      rand_ra         = NULL;
double*      rand_dec        = NULL;
double*      rand_chi        = NULL;
double*      rand_x          = NULL;  // Really need x,y,z?
double*      rand_y          = NULL;
double*      rand_z          = NULL;
double*      rand_weight     = NULL;
double*      rand_rng        = NULL;
double*      clip_randweight = NULL;
int*         rand_box        = NULL; 

double bare_rand_shot, bare_gal_shot;

// -- FKP weighting/normalisation --//
int    accepted_gals;
double       fkpPk;
double bare_fkp_norm, daccepted_gals;


//-- Embedding volume for mock. --//
int          n0, n1, n2, nx; // (z == 0), (x == 2).

double  AxisLimsArray[2][3];  // Array to hold the coordinate limits of the VIPERS survey.

double        xCellSize;            // Cell size, comoving distance, h^-1 Mpc
double        yCellSize;            // Cell size, comoving distance, h^-1 Mpc
double        zCellSize;            // Cell size, comoving distance, h^-1 Mpc 

double       CellVolume;

double        lo_zlim;              // Selection parameters. Volume limited sample between redshift 0.7 and 0.9
double        hi_zlim;
double          z_eff;
double           aexp;

int       boxlabel;
int          xlabel, ylabel, zlabel;

// -- n(z) calc. -- //
int          chibin_no;
double       chi_interval;
double       nz_smoothRadius; // smoothing length. 

double*      zbins    = NULL;
double*      chibins  = NULL;
double*      Nchi     = NULL;
double*      nbar     = NULL;
double*      nbar_2d  = NULL;
double*      comovVol = NULL;

double        cumulative_nbar[400];
double     cumulative_nbar_2d[400];
double    chi_cumulative_nbar[400];

// -- FFT units --//
double k_x, k_y, k_z;

double kSq, kmodulus, mu; // necessary for these to be global?
double kbinInterval;

double        fund_kx; // fund_kx.
double        fund_ky;
double        fund_kz;

double        xNy; // Ny_kx.
double        yNy;
double        zNy;

double*       sinc_factors;

// -- Binned modes -- //
double  logk_min;
double  logk_max;
double  logk_interval;

// -- Multipole decomposition -- //
int     hiMultipoleOrder; // 0: use monopole only, 2: use quadrupole.

// -- Clipping -- //
int     d0;
double  smooth_radius;

double* gal_clippingweights;
double* cell_metd0; // highest d0 met by cell.
double* filter_factors;

int     number_occupied = 0;
int*      rand_occupied;

int* occupied_indices;

// New basis for embedding volume.
double min_x, max_x, dx, min_y, max_y, dy, min_z, max_z, dz, F, cos_dec;

// -- Functions --
int     comovDistReshiftCalc();  // Prototyping should use voids, e.g. comovDistRedshiftCalc(void).
double  SolidAngleCalc(double decLowerBound, double decUpperBound, double raInterval);

double  invert_StefanoBasis(double centreRA, double centreDec, double* xval, double* yval, double* zval);
int     StefanoRotated(int Number, double centreDec, double xCoors[], double yCoors[], double zCoors[]);

int     load_fastread_randomCats(int rand_number);

int     prep_inverseCumulative_nbar();

int     prep_filterfactors(void);
int     Gaussian_filter(void);

int     CoordinateCalc();

int     boxCoordinates(double xCoor[], double yCoor[], double zCoor[], int rowNumber);

int     calc_clipping_weights();

int     JenkinsCoordinates();
int     JenkinsFold(double original[], int lenArray, int axis);
int     ApplyJenkins();

int     PkCalc();
int     print_nbarshot();

int     set_rand_rng(void);

// -- Pointers -- //
