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

def codons_into_aas(codon_list: list) -> str:
    aa_list = []
    for codon in codon_list:
        aa = [k for k, v in codon_dictionary.items() if codon in v]
        if aa[0] == 'stop':
            break
        aa_list += aa[0]
    return aa_list