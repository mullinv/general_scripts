# general_scripts
Place for my general scripts for public release, these have been written for specific workflows within our research group.
Please note that they may need to be altered to suit your data.


SNP_ANGSD_LowCov_SanityCheck.py 

A script to ensure that the haploid allele call that has been called by ANGSD (-doHaploCall) is one of two known alleles (provided by a BIM file).
The output includes a filtered .haplo.gz file and a file containing the removed positions.

Note its written in python2 

python script.py refeernce_bim haplofile output_name problem_out_file sample_name
