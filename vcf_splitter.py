import os

input_file_name = 'test.vcf'
folder_save_file = "vcf"
num_vcard = 100

all_vcard = []
temp_vcf = []

# Read and process the input VCF file
with open(input_file_name, 'rb') as file:
    content = file.read()
    decoded_content = content.decode('utf-8', errors='ignore')
    all_vcards = decoded_content.splitlines()

for line in all_vcards:
    if line.startswith("BEGIN"):
        all_vcard.append(temp_vcf)
        temp_vcf = []
    if line.startswith("N"):
        line = "N;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:;" + "----------" + line.split("N;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:;")[0]
    temp_vcf.append(line)

text_vcard = ""
vcf_name = 1
total_vcards = len(all_vcard)

# Create output files with a specified number of vCards
for idx, vcard_set in enumerate(all_vcard, start=1):
    if str(vcard_set) == "[]":
        continue
    for line in vcard_set:
        text_vcard += line + "\n"
    if idx % num_vcard == 0 or idx == total_vcards:
        print(f"Phase: {vcf_name}, Progress: {idx}/{total_vcards} ({(idx / total_vcards) * 100:.2f}%)")
        output_file_path = os.path.join(folder_save_file, f"vcf{vcf_name}.vcf")
        with open(output_file_path, "w") as output_file:
            output_file.write(text_vcard)
        vcf_name += 1
        text_vcard = ""

if text_vcard:
    print(f"Phase: {vcf_name}, Progress: {total_vcards}/{total_vcards} (100.00%)")
    output_file_path = os.path.join(folder_save_file, f"vcf{vcf_name}.vcf")
    with open(output_file_path, "w") as output_file:
        output_file.write(text_vcard)
