int Gaussianfield(){
    int m0, m1, m2;
    
    double Power, amplitude, phase, expectation; 
    
    for(k=0; k<n0; k++){
        for(j=0; j<n1; j++){
            for(i=0; i<n2; i++){
                m0 = k;
                m1 = j;
                m2 = i;

                if(m2>n2/2)  m2                   -= n2;
                if(m1>n1/2)  m1                   -= n1;
                if(m0>n0/2)  m0                   -= n0;
                
                k_x                                = kIntervalx*m2;
                k_y                                = kIntervaly*m1;
                k_z                                = kIntervalz*m0;
                
                Index                              = k*n1*n2 + j*n2 + i;
                
                kSq                                = pow(k_x, 2.) + pow(k_y, 2.) + pow(k_z, 2.);
                
                kmodulus                           = pow(kSq, 0.5);

                mu                                 = k_z/kmodulus;
                if(kmodulus < 0.000001)       mu   = 0.0;
                                                                                     // shot noise contribution. 
                // expectation                     = (*pt2Pk)(kmodulus)/TotalVolume; //  + (1./TotalVolume)*(*pt2shot)(1.);

                // Monopole and Quadrupole components, with z taken as the line of sight direction. 
                // expectation                     = (kaiser_multipole(kmodulus, beta, 0) + kaiser_multipole(kmodulus, beta, 2)*0.5*(3.*mu*mu -1.))*Pk_powerlaw(kmodulus, 5., 1.8)/TotalVolume;

                expectation                        = (*pt2Pk)(kmodulus)/TotalVolume;
                
                // expectation                    *= 1. + 0.5*pow(mu, 2.);
            
                // expectation                    *= pow(1. + beta*pow(mu, 2.), 2.);
                
                // fingers of God RSD.
                expectation                       /= 1. + 0.5*pow(k_z*velDispersion, 2.);

                // Power                           = -log(gsl_rng_uniform(gsl_ran_r))*expectation;
                
                // amplitude                       = sqrt(Power);
                amplitude                          = sqrt(expectation);
                                
                phase                              = 2.*pi*gsl_rng_uniform(gsl_ran_r);
                
                // Assuming Cic assignment scheme
                out[Index][0]                      = amplitude*cos(phase);
                out[Index][1]                      = amplitude*sin(phase);
                
                /*
                WindowFunc                         = 1.;

                if(k_x != 0.){
		            WindowFunc                    *= sin(pi*k_x*0.5/NyquistWaveNumber)/(pi*k_x*0.5/NyquistWaveNumber);}
                
                if(k_y != 0.){
		            WindowFunc                    *= sin(pi*k_y*0.5/NyquistWaveNumber)/(pi*k_y*0.5/NyquistWaveNumber);}
                
                if(k_z != 0.){
		            WindowFunc                    *= sin(pi*k_z*0.5/NyquistWaveNumber)/(pi*k_z*0.5/NyquistWaveNumber);}		      
	            */
	            
	            // out[Index][0]                  *= pow(WindowFunc, 2.);
	        	// out[Index][1]                  *= pow(WindowFunc, 2.);
	        }
        }
    }
    
    // Zero mean. Mean is always real for a real input fn.
    out[0][0] = 0.0;
    out[0][1] = 0.0;
    
    int negkIndex;
    
    // Hermitian condition. One hemi-sphere is independent, e.g. k_z >= 0.
    for(k=n0-1; k>=n0/2; k--){
        for(j=0; j<n1; j++){
            for(i=0; i<n2; i++){
                negkIndex          = k*n1*n2 + j*n2 + i;
                       
                Index              = 0;
                
                // zero maps to zero on reflection through the origin.
                if(i!=0)  Index   += (n2 - i);
                if(j!=0)  Index   += (n1 - j)*n2;
                          Index   += (n0 - k)*n1*n2;

                out[negkIndex][0]  =     out[Index][0];
                out[negkIndex][1]  = -1.*out[Index][1];
                
                if(negkIndex == Index)   out[Index][1] = 0.0; // purely real
            }
        }
    } 
    
    // in the k_z=0 plane one semi-circle is independent, k_y>0.         
    for(j=n1-1; j>=n1/2; j--){
        for(i=0; i<n2; i++){
            negkIndex          = j*n2 + i;
                       
            Index              = 0;
                
            // zero maps to zero on reflection through the origin.
            if(i!=0)  Index   += (n2 - i);
                      Index   += (n1 - j)*n2;

            out[negkIndex][0]  =     out[Index][0];
            out[negkIndex][1]  = -1.*out[Index][1];
            
            if(negkIndex == Index)   out[Index][1] = 0.0;
        }
    }
    
    // on the line k_z=k_y=0, one half is independent, k_x>=0.
    for(i=n2-1; i>=n2/2; i--){
        negkIndex          = i;
                       
        Index              = 0;
                
        // zero maps to zero on reflection through the origin.
        Index             += (n2 - i);

        out[negkIndex][0]  =      out[Index][0];
        out[negkIndex][1]  =  -1.*out[Index][1];
            
        if(negkIndex == Index)    out[Index][1] = 0.0;
    }

    fftw_execute(iplan);

    for(j=0; j<n0*n2*n1; j++)  densityArray[j] = in[j][0];
    
    // double GRF_var = 0.0, GRF_mean = 0.0;
    
    // apparent_mean = 0.0;
    
    // for(j=0; j<n0*n1*n2; j++){ 
    //   GRF_var        += pow(densityArray[j], 2.);
    //    GRF_mean       +=     densityArray[j];
    //}
    
    ///GRF_var            /= n0*n1*n2;
    // GRF_mean           /= n0*n1*n2;                           
    
    // printf("\n\nMean of the Gaussian realisation: %e", GRF_mean);
    // printf("\n\nVariance of Gaussian realisation: %e", GRF_var);
    
    // for(j=0; j<n0*n2*n1; j++)  apparent_mean       += densityArray[j]*Cell_AppliedWindowFn[j];
    
    // Number of non-empty cells in mask. 
    // apparent_mean    /= 123004.;
    
    // for(j=0; j<n0*n1*n2; j++)  densityArray[j]     -= apparent_mean;
    
    // printf("\n\nApparent (weighted) mean of the Gaussian realisation: %e", apparent_mean);
    
    printf("\n\nminimum delta of Gaussian realisation: %e", arrayMin(densityArray, n0*n1*n2));
    
    return 0;
}
