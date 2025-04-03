#!/usr/bin/env python
"""
Victoria Mullin
Script to filter the low coverage haplocalls (ANGSD) to ensure either the major or minor allele has been called
Outputs a gz haplo file. This script also alters the header in the filtered file to include the sample name

Order of input: Reference BIM file, haplo file, output_name(.gz), problems_file_name, sample_name
"""

import sys
import gzip

def main(input1, input2, output_name, problem_out, sample_name):
    dictionary_position = {}
    dictionary_major = {}
    dictionary_minor = {}
    output = gzip.open(output_name, 'w')
    problem = open(problem_out, 'w')
    output.write("chr""\t""pos""\t""major""\t"+sample_name+"\n")
    good_lines = 0
    bad_lines = 0
    other_lines = 0
    total_lines = 0
    major_lines = 0
    minor_lines = 0

    # file1 will be the BIM file from the SNP list
    with open(input1, "r") as file1:
        for line in file1:
            line = line.rstrip()
            column2 = line.split("\t")
            chromo_pos = column2[1]
            minor = column2[4]
            major = column2[5]
            dot = "_"
            bim_minor = chromo_pos + dot + minor
            bim_major = chromo_pos + dot + major

            dictionary_position[chromo_pos] = chromo_pos
            dictionary_major[bim_major] = bim_major
            dictionary_minor[bim_minor] = bim_minor

    # file1 will be the haplo file from ANGSD - individual
    with gzip.open(input2 , "r") as file2:
        for line in file2:
            if not line.startswith('chr'):
                line = line.rstrip()
                column = line.split("\t")
                chromosome = column[0]
                position = column[1]
                result = column[3]
                dot = "_"
                chr_pos = chromosome + dot + position
                haploresult = chromosome + dot + position + dot + result

                if chr_pos in dictionary_position:
                    # print("I'm in the dictionary chr_pos")
		            # print(chromo_pos)
                    total_lines += 1
                    if haploresult in dictionary_major:
                        good_lines += 1
                        output.write(line + '\n')
                        #print("Im in the major")
                        #print(bim_line)
                        major_lines += 1
                    elif haploresult in dictionary_minor:
                        good_lines += 1
                        output.write(line + '\n')
                        #print("I'm in the minor")
                        minor_lines += 1
                    else:
                        problem.write(line + '\n')
                        bad_lines += 1
                else:
                    other_lines += 1
                    print(line + '\n')
                    problem.write(line + '\n')

    print(
    'All finished. There were {:,} total positions - {:,} of lines with no issues and {:,} lacking the major or minor and {:,} not in the reference BIM file. {:,} Major & {:,} Minor'.format(total_lines,good_lines, bad_lines, other_lines, major_lines, minor_
lines))
main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
