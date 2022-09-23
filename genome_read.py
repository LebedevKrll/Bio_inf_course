from operator import index


stop_pos = 0
start_pos = 0
codon_list = []
AA = ''
nts_in_AA = 0
orf_count = 0

with open('GCF_000005845.2_ASM584v2_genomic.fna', 'r') as file:
    for line in file:
        for nt in line:
            AA += nt
            nts_in_AA += 1
            if nts_in_AA == 3:
                codon_list.append(AA)
                AA = ''
                nts_in_AA = 0

with open('GCF_000005845.2_ASM584v2_genomic.fna', 'r') as file_cursor:
    file = file_cursor.read()

file = file.replace('\n', '')

while 'ATG' in codon_list:
    if 'TAA'  in codon_list or 'TAG'  in codon_list or 'TGA' in codon_list:
        start_pos = codon_list.index('ATG')
        if 'TAA'  in codon_list:
            stop_pos = codon_list.index('TAA')
        elif 'TAG' in codon_list:
            stop_pos = codon_list.index('TAG')
        elif 'TGA' in codon_list:
            stop_pos = codon_list.index('TGA')
        else:
            break
        orf_count += 1
        del codon_list[start_pos : stop_pos + 1]
    
print(2)

cut = 0
file = file[0 : cut : ] + file[cut + 1 : :]
for line in file:
    for nt in line:
        AA += nt
        nts_in_AA += 1
        if nts_in_AA == 3:
            codon_list.append(AA)
            AA = ''
            nts_in_AA = 0
while 'TUG' in codon_list:
    if 'TAA'  in codon_list or ''  in codon_list or 'TGA' in codon_list:
        start_pos = codon_list.index('ATG')
        if 'TAA'  in codon_list:
            stop_pos = codon_list.index('TAA')
        elif 'TAG' in codon_list:
            stop_pos = codon_list.index('TAG')
        elif 'TGA' in codon_list:
            stop_pos = codon_list.index('TGA')
        else:
            break
        orf_count += 1
        del codon_list[start_pos : stop_pos + 1]

print(3)

cut = 1
file = file[0 : cut : ] + file[cut + 1 : :]
for line in file:
    for nt in line:
        AA += nt
        nts_in_AA += 1
        if nts_in_AA == 3:
            codon_list.append(AA)
            AA = ''
            nts_in_AA = 0
while 'ATG' in codon_list:
    if 'TAA'  in codon_list or 'TAG'  in codon_list or 'TGA' in codon_list:
        start_pos = codon_list.index('ATG')
        if 'TAA'  in codon_list:
            stop_pos = codon_list.index('TAA')
        elif 'TAG' in codon_list:
            stop_pos = codon_list.index('TAG')
        elif 'TGA' in codon_list:
            stop_pos = codon_list.index('TGA')
        else:
            break
        orf_count += 1
        del codon_list[start_pos : stop_pos + 1]

file = file[::-1]
for line in file:
    for nt in line:
        AA += nt
        nts_in_AA += 1
        if nts_in_AA == 3:
            codon_list.append(AA)
            AA = ''
            nts_in_AA = 0
while 'ATG' in codon_list:
    if 'TAA'  in codon_list or 'TAG'  in codon_list or 'TGA' in codon_list:
        start_pos = codon_list.index('ATG')
        if 'TAA'  in codon_list:
            stop_pos = codon_list.index('TAA')
        elif 'TAG' in codon_list:
            stop_pos = codon_list.index('TAG')
        elif 'TGA' in codon_list:
            stop_pos = codon_list.index('TGA')
        else:
            break
        orf_count += 1
        del codon_list[start_pos : stop_pos + 1]
cut = 0
file = file[0 : cut : ] + file[cut + 1 : :]
for line in file:
    for nt in line:
        AA += nt
        nts_in_AA += 1
        if nts_in_AA == 3:
            codon_list.append(AA)
            AA = ''
            nts_in_AA = 0
while 'ATG' in codon_list:
    if 'TAA'  in codon_list or 'TAG'  in codon_list or 'TGA' in codon_list:
        start_pos = codon_list.index('ATG')
        if 'TAA'  in codon_list:
            stop_pos = codon_list.index('TAA')
        elif 'TAG' in codon_list:
            stop_pos = codon_list.index('TAG')
        elif 'TGA' in codon_list:
            stop_pos = codon_list.index('TGA')
        else:
            break
        orf_count += 1
        del codon_list[start_pos : stop_pos + 1]
cut = 1
file = file[0 : cut : ] + file[cut + 1 : :]
for line in file:
    for nt in line:
        AA += nt
        nts_in_AA += 1
        if nts_in_AA == 3:
            codon_list.append(AA)
            AA = ''
            nts_in_AA = 0
print(codon_list[0:5])
while 'ATG' in codon_list:
    if 'TAA'  in codon_list or 'TAG'  in codon_list or 'TGA' in codon_list:
        start_pos = codon_list.index('ATG')
        if 'TAA'  in codon_list:
            stop_pos = codon_list.index('TAA')
        elif 'TAG' in codon_list:
            stop_pos = codon_list.index('TAG')
        elif 'TGA' in codon_list:
            stop_pos = codon_list.index('TGA')
        else:
            break
        orf_count += 1
        del codon_list[start_pos : stop_pos + 1]

print(orf_count)
