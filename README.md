# VCF Splitter

## Overview

This Python script is designed to split a VCF (vCard) file into multiple smaller files, each containing a specified number of vCards. The script reads the input VCF file, processes its content, and creates separate output files with a limited number of vCards in each.

## Usage

1. **Input File:**
   - Provide the VCF file you want to split by setting the `input_file_name` variable.
  
2. **Output Folder:**
   - Specify the folder where the split VCF files will be saved by setting the `folder_save_file` variable.

3. **Number of vCards per File:**
   - Adjust the `num_vcard` variable to set the desired number of vCards in each output file.

4. **Running the Script:**
   - Execute the script in a Python environment.

```bash
python vcf_splitter.py
