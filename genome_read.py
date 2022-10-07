from copy import deepcopy as dc

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
codon_list = []
AA = ''
nts_in_AA = 0
orf_poss = []
orf_pos = ''
aa_list = []

def codons_into_aas(codon_list: list) -> str:
    aa_list = []
    for codon in codon_list:
        aa = [k for k, v in codon_dictionary.items() if codon in v]
        aa_list += aa[0]
    return aa_list

def form_codon_list(cut= -10, file: str) -> list:
    if cut >= 0:
        file = dc(file[0 : cut : ]) + dc(file[cut + 1 : :])
    for line in file:
        for nt in line:
            AA += nt
            nts_in_AA += 1
            if nts_in_AA == 3:
                codon_list.append(AA)
                AA = ''
                nts_in_AA = 0
    return codon_list

def extend_orf_poss(codon_list: list, side: str, cut: int):    #side can be - or + and shows which way are we reading 53 or 35
    for codon in range(len(codon_list)):
        if codon_list[codon] == 'ATG':
            if len(orf_pos) < 2:
                orf_pos += str(codon) + ' '
        elif codon_list[codon] == 'TAA' or codon_list[codon] == 'TAG' or codon_list[codon] == 'TGA':
            if len(orf_pos) > 0:
                orf_pos += str(codon) + f' {side}'
                orf_poss.append(orf_pos)
                orf_pos = ''

with open('GCF_000005845.2_ASM584v2_genomic.fna', 'r') as file_cursor:
    file = file_cursor.read()

file = file.replace('\n', '')

codon_list = form_codon_list(file)

extend_orf_poss(codon_list, '+', 0)

codon_list = form_codon_list(0, file)

extend_orf_poss(codon_list, '+', 1)

codon_list = form_codon_list(1, file)

extend_orf_poss(codon_list, '+', 2)

codon_list = form_codon_list(file)[::-1]

extend_orf_poss(codon_list, '-', 0)

codon_list = form_codon_list(0, file)[::-1]

extend_orf_poss(codon_list, '-', 1)

codon_list = form_codon_list(1, file)[::-1]

extend_orf_poss(codon_list, '-', 2)
