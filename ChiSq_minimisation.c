int default_params(){
  fsigma8       = 0.14;
  A11Sq         = 1.00;
  velDispersion = 2.62;
  bsigma8       = 0.82;
  epsilon_pad   = 0.00;
  alpha_pad     = 1.00;

  set_u0();

  return 0;
}


int bestfit_params(){
  fsigma8       = minChiSq_fsigma8;
  velDispersion = minChiSq_sigma;
  bsigma8       = minChiSq_bsigma8;
  alpha_pad     = minChiSq_alpha_pad;
  epsilon_pad   = minChiSq_epsilon_pad;
  
  return 0;
}


int set_chiSq_intervals(){
    fsigma8Interval       = (max_fsigma8     - min_fsigma8)/dRes;
    bsigma8Interval       = (max_bsigma8     - min_bsigma8)/dRes;
    sigmaInterval         = (max_velDisperse - min_velDisperse)/dRes;
    alpha_padInterval     = (max_alpha_pad   - min_alpha_pad)/dRes_ap;
    epsilon_padInterval   = (max_epsilon_pad - min_epsilon_pad)/dRes_ap;
    A11SqInterval         = (max_A11Sq       - min_A11Sq)/dRes;
    
    return 0;
}


int kvals_matchup(){
    double     diff;
    double min_diff;
    
    fftlog_indices = malloc(mono_order*sizeof(*fftlog_indices));
    
    for(i=0; i<mono_order; i++){  
        min_diff = pow(10., 99.);
    
        for(j=0; j<FFTlogRes; j++){  
            diff = fabs(mono_config->krvals[j][0] - kVals[i]);
            
            if(diff<min_diff){
                min_diff = diff;
            
                fftlog_indices[i]  = j;
            }
        }
    }
            
    return 0;
}


int calc_models(){
  int aa, bb, cc, dd, ee, klo;

  // input_check();
  // prep_dlnPR_dlnk();   
  
  sprintf(filepath, "%s/W1_Spectro_V7_4/models/models_W%d_%.1lf_%.1f.cat", root_dir, fieldFlag, 0.6, 0.9);

  output = fopen(filepath, "wb");
  
  for(aa=0; aa<Res; aa++){
    fsigma8 = min_fsigma8 + fsigma8Interval*aa;

    for(bb=0; bb<Res; bb++){
      bsigma8 = min_bsigma8 + bsigma8Interval*bb;

      for(cc=0; cc<Res; cc++){
	velDispersion = min_velDisperse + sigmaInterval*cc;

	for(dd=0; dd<Res_ap; dd++){
	  alpha_pad = min_alpha_pad + alpha_padInterval*dd;

	  for(ee=0; ee<Res_ap; ee++){
	    epsilon_pad = min_epsilon_pad + epsilon_padInterval*ee;

	    alpha_pad   = 1.0;
	    epsilon_pad = 0.0;

	    model_compute(aa, bb, cc, dd, ee); // updates xtheory and ytheory. 
	    
	    fwrite(xtheory[aa][bb][cc][dd][ee], sizeof(double),  order,   output);
	    // fwrite(ytheory[jj][kk][ii][ll][mm], sizeof(double),  order,   output);
	  }
	}
      }
    }
  }
  
  fclose(output);
  
  return 0;
}


int calc_ChiSqs(int mockNumber){    
    int ll, mm, nn;

    minChiSq = pow(10., 12.);
    
    if(data_mock_flag == 0)  load_mock(mockNumber);  // Needs amplitude corrected. 
    else                     load_data();

    // set_meanmultipoles();
    // scale_Cov(130);
    
    for(j=0; j<order; j++){
       ydata[j] = 0.0;  // new zero mean, unit variance, decorrelated variables.
      dkdata[j] = 0.0;
      
      gsl_matrix_get_col(col, evec, j);
        
      for(k=0; k<order; k++){
	ydata[j] += gsl_vector_get(col, k)*gsl_matrix_get(sigma_norm, k, k)*xdata[k];
       dkdata[j] += gsl_vector_get(col, k)*gsl_matrix_get(sigma_norm, k, k)*kdata[k];	// normalisation problem? 
      }
    }

    printf("\n\nDecorrelated data (normalisation?): ");

    for(j=0; j<order; j++)  printf("\n%+.4le \t %+.4le \t %+.4le", dkdata[j], ydata[j], sqrt(gsl_vector_get(eval, j)));
    
    printf("\n\nChi sq. calc:");
    
    for(jj=0; jj<Res; jj++){    
      fsigma8 = min_fsigma8 + fsigma8Interval*jj;

      for(kk=0; kk<Res; kk++){
        bsigma8 = min_bsigma8 + bsigma8Interval*kk;

        for(ii=0; ii<Res; ii++){
          velDispersion = min_velDisperse + sigmaInterval*ii;
                
          for(ll=0;ll<Res_ap; ll++){
            alpha_pad = min_alpha_pad + alpha_padInterval*ll;
                
            for(mm=0; mm<Res_ap; mm++){
              epsilon_pad = min_epsilon_pad + epsilon_padInterval*mm;
                    
	      alpha_pad   = 1.0;
	      epsilon_pad = 0.0; 

              ChiSqGrid[jj][kk][ii][ll][mm] = 0.0;

	      for(nn=0; nn<order; nn++){
	        ChiSqGrid[jj][kk][ii][ll][mm] += pow(ydata[nn] - ytheory[jj][kk][ii][ll][mm][nn], 2.)/gsl_vector_get(eval, nn);
		// ChiSqGrid[jj][kk][ii][ll][mm] += pow(xdata[nn] - xtheory[jj][kk][ii][ll][mm][nn], 2.)*pow(gsl_matrix_get(sigma_norm, nn, nn), 2.);
	      }

	      // printf("\n%.2lf \t %.2lf \t %.2lf \t %.2lf", fsigma8, velDispersion, bsigma8,  ChiSqGrid[jj][kk][ii][ll][mm]);
	      
              if(ChiSqGrid[jj][kk][ii][ll][mm] < minChiSq){
                minChiSq = ChiSqGrid[jj][kk][ii][ll][mm];
                    
                minChiSq_fsigma8     = fsigma8;
                minChiSq_A11Sq       = A11Sq;
                minChiSq_sigma       = velDispersion;
                minChiSq_bsigma8     = bsigma8;
                minChiSq_alpha_pad   = alpha_pad;
                minChiSq_epsilon_pad = epsilon_pad;

		printf("\n%.2lf \t %.2lf \t %.2lf \t %.2lf", fsigma8, velDispersion, bsigma8,  minChiSq);
	      }
	    }
          }
        }
      }
    }
    
    return  0;
}


int read_models(){
  int ll, mm;

  sprintf(filepath, "%s/W1_Spectro_V7_4/models/models_W%d_%.1lf_%.1f.cat", root_dir, fieldFlag, 0.6, 0.9);

  inputfile = fopen(filepath, "rb");
  
  for(jj=0; jj<Res; jj++){
    fsigma8 = min_fsigma8 + fsigma8Interval*jj;

    for(kk=0; kk<Res; kk++){
      bsigma8 = min_bsigma8 + bsigma8Interval*kk;

      for(ii=0; ii<Res; ii++){
	velDispersion = min_velDisperse + sigmaInterval*ii;

	for(ll=0;ll<Res_ap; ll++){
	  alpha_pad = min_alpha_pad + alpha_padInterval*ll;

	  for(mm=0; mm<Res_ap; mm++){
	    epsilon_pad = min_epsilon_pad + epsilon_padInterval*mm;

	    alpha_pad   = 1.0;
	    epsilon_pad = 0.0;

	    fread(xtheory[jj][kk][ii][ll][mm], sizeof(double),  order,   inputfile);
	  }
	}
      }
    }
  }
  
  fclose(inputfile);
  
  return 0;
}


int test_chiSq(){
  // default_params();
  bestfit_params();
    
  model_compute(0, 0, 0, 0, 0);

  sprintf(filepath, "%s/W1_Spectro_V7_4/model.dat", root_dir);
  
  output = fopen(filepath, "w");

  for(j=0; j<mono_order; j++)  fprintf(output, "%.4le \t %.4le \t %.4le \t %.4le \t %.4le \n", kVals[j], xdata[j], xdata[j + mono_order], xtheory[0][0][0][0][0][j], xtheory[0][0][0][0][0][j + mono_order]);
  
  fclose(output);
  
  return 0;
}