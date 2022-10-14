
from copy import deepcopy as dc

def codons_into_aas(codon_list: list) -> str:
    codon_dictionary = { 
    "A": ["GCA","GCC","GCG","GCT"], 
    "C": ["TGC","TGT"], 
    "D": ["GAC", "GAT"],
    "E": ["GAA","GAG"],
    "F": ["TTC","TTT"],
    "G": ["GGA","GGC","GGG","GGT"],
    "H": ["CAC","CAT"],
    "I": ["ATA","ATC","ATT"],
    "K": ["AAA","AAG"],
    "L": ["CTA","CTC","CTG","CTT","TTA","TTG"],
    "M": ["ATG"],
    "N": ["AAC","AAT"],
    "P": ["CCA","CCC","CCG","CCT"],
    "Q": ["CAA","CAG"],
    "R": ["AGA","AGG","CGA","CGC","CGG","CGT"],
    "S": ["AGC","AGT","TCA","TCC","TCG","TCT"],
    "T": ["ACA","ACC","ACG","ACT"],
    "V": ["GTA","GTC","GTG","GTT"],
    "W": ["TGG"],
    "Y": ["TAC","TAT"],
    "stop": ["TAG", "TAA", "TGA"]
    }
    aa_list_func = []
    for codon in codon_list:
        aa = [k for k, v in codon_dictionary.items() if codon in v]
        aa_list_func += aa[0]
    return aa_list_func

def form_codon_list(file_func: str, side: str,  cut: int) -> list:

    nts_in_AA = 0
    AA = ''
    codon_list = []

    if side == '-':
        file_func = file_func[::-1]

    if int(cut) - 1 >= 0:
        file_func = dc(file_func[0 : cut : ]) + dc(file_func[cut + 1 : :])

    for line in file_func:
        for nt in line:
            AA += nt
            nts_in_AA += 1
            if nts_in_AA == 3:
                codon_list.append(AA)
                AA = ''
                nts_in_AA = 0

    return codon_list

def extend_orf_poss(codon_list: list, side: str, cut: int):    #side can be - or + and shows which way are we reading 53 or 35
    
    orf_pos = []

    for codon in range(len(codon_list)):
        if codon_list[codon] == 'ATG':
            if len(orf_pos) < 1:
                orf_pos.append(codon)
        elif codon_list[codon] == 'TAA' or codon_list[codon] == 'TAG' or codon_list[codon] == 'TGA':
            if len(orf_pos) > 0:
                orf_pos.append(codon)
                orf_pos.append(side)
                orf_pos.append(cut)
                orf_poss.append(orf_pos)
                orf_pos = []

with open('GCF_000005845.2_ASM584v2_genomic.fna', 'r') as file_cursor:
    file = file_cursor.read()

file = file.replace('\n', '')

orf_poss = []

extend_orf_poss(form_codon_list(file, '+', 0), '+', 0)

extend_orf_poss(form_codon_list(file, '+', 1), '+', 1)

extend_orf_poss(form_codon_list(file, '+', 2), '+', 2)

extend_orf_poss(form_codon_list(file, '-', 0), '-', 0)

extend_orf_poss(form_codon_list(file, '-', 1), '-', 1)

extend_orf_poss(form_codon_list(file, '-', 2), '-', 2)

aa_list = []

for i in range(len(orf_poss)):
    if orf_poss[i][2] == '+':
        coord_opening = 3 * orf_poss[i][0]
        coord_closing = 3 * (orf_poss[i][1] + 1)
        if orf_poss[i][3] == 1:
            coord_opening += 1
            coord_closing += 1
        elif orf_poss[i][3] == 2:
            coord_opening += 2
            coord_closing += 2
        aa_list.append(codons_into_aas(form_codon_list(file[coord_opening : coord_closing + 1], '+', 0)))
    else:
        coord_opening = len(file) - 3 * orf_poss[i][0] - 1
        coord_closing = len(file) - 3 * (orf_poss[i][1] + 1) - 1
        if orf_poss[i][3] == 1:
            coord_opening -= 1
            coord_closing -= 1
        elif orf_poss[i][3] == 2:
            coord_opening -= 2
            coord_closing -= 2
        aa_list.append(codons_into_aas(form_codon_list(file[coord_opening : coord_closing - 1 : -1], '+', 0)))

print([] in aa_list)