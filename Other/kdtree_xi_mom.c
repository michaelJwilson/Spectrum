int assignMemory_xi(){
  double rmax = log10(4000.);

  point_rands = (Particle *) realloc(point_rands, rand_number*sizeof(Particle));

  nlogbins    = (int)        ceil((rmax   - zerolog)/logbinsz);
  nlinbins    = (int)        ceil((maxlin - zerolin)/linbinsz);
  
  // mu^n + FKP weighted pair counts. 
  rr_0        = (double *)   calloc(nlogbins*nlinbins, sizeof(double)); 
  rr_2        = (double *)   calloc(nlogbins*nlinbins, sizeof(double));
  rr_4        = (double *)   calloc(nlogbins*nlinbins, sizeof(double));
  rr_6        = (double *)   calloc(nlogbins*nlinbins, sizeof(double));
  rr_8        = (double *)   calloc(nlogbins*nlinbins, sizeof(double));
  rr_10       = (double *)   calloc(nlogbins*nlinbins, sizeof(double));

  rr_meann    = (double *)   calloc(nlogbins*nlinbins, sizeof(double));
  rr_meanwn   = (double *)   calloc(nlogbins*nlinbins, sizeof(double)); 
  rr_meanr    = (double *)   calloc(nlogbins*nlinbins, sizeof(double));
  rr_meanmu   = (double *)   calloc(nlogbins*nlinbins, sizeof(double));
    
  xi0         = (double *)   calloc(nlogbins, sizeof(*xi0));
  xi2         = (double *)   calloc(nlogbins, sizeof(*xi2));
  xi4         = (double *)   calloc(nlogbins, sizeof(*xi4));
  xi6         = (double *)   calloc(nlogbins, sizeof(*xi6));
  xi8         = (double *)   calloc(nlogbins, sizeof(*xi8));
  xi10        = (double *)   calloc(nlogbins, sizeof(*xi10));

  logrbins    = (double *)   calloc(nlogbins, sizeof(*logrbins));
  pairsperbin = (int    *)   calloc(nlogbins, sizeof(*pairsperbin));
              
  return 0;
}

int postprocesspairs_nonodes(double* C0, double* C2, double* C4, double* C6, double* C8, double* C10, double* r, double* mu, Node* firstTree, Node* secndTree, int sameTree){
  double  mu0weighted_paircount, mu2weighted_paircount, mu4weighted_paircount, mu6weighted_paircount, mu8weighted_paircount, mu10weighted_paircount;

  // Save raw counts.
  sprintf(filepath, "%s/Qmultipoles/%s_raw.dat", outputdir, surveyType);

  output = fopen(filepath, "w");

  fprintf(output, "## Walltime: %.4lf seconds \n", getRealTime() - begin);

  fprintf(output, "## sum over pairs of weights; sum over pairs of weighted*mu2, sum over pairs of weighted mu*4 \n");

  for(j=0; j<NBINS; j++)  fprintf(output, "%.4le \t %.4le \t %.4le \n", C0[j], C2[j], C4[j]);

  fclose(output);
  
  
  for(i=0; i<nlogbins; i++){
    for(j=0; j<nlinbins; j++){
      Index = j + nlinbins*i;

      mu0weighted_paircount   =  C0[Index];
      mu2weighted_paircount   =  C2[Index];
      mu4weighted_paircount   =  C4[Index];
      mu6weighted_paircount   =  C6[Index];
      mu8weighted_paircount   =  C8[Index];
      mu10weighted_paircount  = C10[Index];

      C2[Index]  =                                                                                               3.*mu2weighted_paircount -      mu0weighted_paircount;
      C4[Index]  =                                                                35.*mu4weighted_paircount -   30.*mu2weighted_paircount +   3.*mu0weighted_paircount;
      C6[Index]  =                                 231.*mu6weighted_paircount -  315.*mu4weighted_paircount +  105.*mu2weighted_paircount -   5.*mu0weighted_paircount;
      C8[Index]  = 6435.*mu8weighted_paircount - 12012.*mu6weighted_paircount + 6930.*mu4weighted_paircount - 1260.*mu2weighted_paircount +  35.*mu0weighted_paircount;

      C2[Index] *=   5.*0.5;  // l=2, (2l+1) L_2
      C4[Index] *= 9.*0.125;  // l=4, (2l+1) L_4
      C6[Index] *=  13./16.;  // l=6, (2l+1) L_6
      C8[Index] *= 17./128.;  // l=8, (2l+1) L_8
    }
  }

  xiMonopole(C0, xi0);  // monopole calc. of *weighted* pairs.
  xiMonopole(C2, xi2);  // PREVIOUSLY gg_meanmu.
  xiMonopole(C4, xi4);
  xiMonopole(C6, xi6);
  xiMonopole(C8, xi8);  // masked RSD work.

  // Save multipoles.
  sprintf(filepath, "%s/Qmultipoles/%s.dat", outputdir, surveyType);

  output = fopen(filepath, "w");

  fprintf(output, "## Walltime: %.4lf seconds; \n", getRealTime() - begin);

  for(j=0; j<nlogbins; j++)  fprintf(output, "%.4le \t %.4le \t %.4le \t %.4le \t %.4le \t %.4le \n", logrbins[j], xi0[j], xi2[j], xi4[j], xi6[j], xi8[j]);

  fclose(output);
  
  return 0;
}

int postprocesspairs(double* n, double* wn, double* r, double* wmu, Node* node1, Node* node2){
  double progress, mu;

  double C0[NBINS], C2[NBINS], C4[NBINS], C6[NBINS], C8[NBINS], C10[NBINS]; // mu^n weighted pair counts.
  double P0[NBINS], P2[NBINS], P4[NBINS], P6[NBINS], P8[NBINS], P10[NBINS];  
  
  for(i=0; i<nlogbins; i++){
    for(j=0; j<nlinbins; j++){
       Index      = j + nlinbins*i;
     
       mu         = wmu[Index]/wn[Index]; 

       if(n[Index] == 0.){
         mu = 0.0;
       }
       
       C0[Index]  =  wn[Index];                     
       C2[Index]  =  wn[Index]*pow(mu,  2.);
       C4[Index]  =  wn[Index]*pow(mu,  4.);
       C6[Index]  =  wn[Index]*pow(mu,  6.);
       C8[Index]  =  wn[Index]*pow(mu,  8.);
      C10[Index]  =  wn[Index]*pow(mu, 10.);
        
       P0[Index]  =                                                                               C0[Index];
       P2[Index]  =                                                           3.*C2[Index] -      C0[Index];
       P4[Index]  =                                        35.*C4[Index] -   30.*C2[Index] +   3.*C0[Index];
       P6[Index]  =                     231.*C6[Index] -  315.*C4[Index] +  105.*C2[Index] -   5.*C0[Index];
       P8[Index]  = 6435.*C8[Index] - 12012.*C6[Index] + 6930.*C4[Index] - 1260.*C2[Index] +  35.*C0[Index];
      
       P0[Index] *=       1.;  // l=0, 
       P2[Index] *=   5.*0.5;  // l=2, (2l+1) L_2
       P4[Index] *= 9.*0.125;  // l=4, (2l+1) L_4
       P6[Index] *=  13./16.;  // l=6, (2l+1) L_6
       P8[Index] *= 17./128.;  // l=8, (2l+1) L_8
    }
  }
  
  xiMonopole(P0, xi0);  // monopole calc. of *weighted* pairs.
  xiMonopole(P2, xi2);  
  xiMonopole(P4, xi4);
  xiMonopole(P6, xi6);
  xiMonopole(P8, xi8);  
  
  progress = 100.*nodeone_progresscount*nodetwo_progresscount/((double) tree_labelCount*tree_labelCount);

  // Save multipoles. 
  sprintf(filepath, "%s/Qmultipoles/%s.dat", outputdir, surveyType);

  output = fopen(filepath, "w");

  fprintf(output, "## Walltime: %.4lf seconds; Progress: %.6lf \%; number of nodes in tree: %ld; current nodes: %ld \t %ld \n", getRealTime() - begin, progress,
                                                                                                                                tree_labelCount, node1->label, node2->label);
  
  for(j=0; j<nlogbins; j++)  fprintf(output, "%.4le \t %.4le \t %.4le \t %.4le \t %.4le \t %.4le \n", logrbins[j], xi0[j], xi2[j], xi4[j], xi6[j], xi8[j]);

  fclose(output);
  
  // Save raw counts. 
  sprintf(filepath, "%s/Qmultipoles/%s_raw.dat", outputdir, surveyType);

  output = fopen(filepath, "w");

  fprintf(output, "## Walltime: %.2lf seconds; Progress: %.6lf \%; number of nodes in tree: %ld; current nodes: %ld \t %ld \n", getRealTime() - begin, progress, tree_labelCount, node1->label, node2->label);

  fprintf(output, "## number of pairs; sum over pairs of weights; sum over pairs of weighted r, sum over pairs of weighted mu. \n");
  
  for(j=0; j<NBINS; j++)  fprintf(output, "%.8le \t %.8le \t %.8le \t %.8le \n", n[j], wn[j], r[j], wmu[j]);

  // Comparison to brute force. 
  // for(j=0; j<NBINS; j++)  fprintf(output, "%.4le \t %.4le \t %.4le \t %.4le \t %.4le \n", n[j], C0[j], C2[j], C4[j], C6[j]);
  
  fclose(output);
  
  return 0;
}

int xiMonopole(double* xi, double* Monopole){
  for(i=0; i<nlogbins; i++){
    Monopole[i] = 0.0;
    logrbins[i] = pow(10., zerolog + (i + 0.5)*logbinsz);

    for(j=0; j<nlinbins; j++){
      Index        = j + nlinbins*i;

      Monopole[i] += xi[Index];
    }
  }

  return 0;
}

int randWindow_pairCount(){    
  grow_randTree();
    
  printf("\n\nCounting RR pairs.");

  // get_qsnapshot(rr_meann, rr_meanwn, rr_meanr, rr_meanmu, randTree, randTree);
  
  // bruteforce_nonodes(rr_0, rr_2, rr_4, rr_6, rr_8, rr_10, rr_meanr, rr_meanmu, point_rands, point_rands, rand_number, rand_number, 1);

  // postprocesspairs_nonodes(rr_0, rr_2, rr_4, rr_6, rr_8, rr_10, rr_meanr, rr_meanmu, randTree, randTree, 1);
  
  findSuitableNodePairs_bruteforcePairCount(rr_meann, rr_meanwn, rr_meanr, rr_meanmu, randTree, randTree, 1);

  postprocesspairs(rr_meann, rr_meanwn, rr_meanr, rr_meanmu, randTree, randTree);
  
  return 0;
}
