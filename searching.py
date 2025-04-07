import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if field not in {'unordered_numbers', 'ordered_numbers', 'dna_sequence'}:
        return None

    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, 'r') as json_file:
        seq = json.load(json_file)

    return seq[field] #[54, 2, 18, 5, 3, 31, 20, 65, -10, 300, 17, 5, -1, 0, 0, 102, 7, 8, 9, 9, -3, -5, 0, 1, 63, 82, -36, -5]

def linear_search(seq, num):
    '''
    v neseřazeném seznamu nalezne pozice a četnost výskytu zadaného čísla
    :param seq:  prohledávaná sekvence
    :param num: hledané číslo
    :return: slovník se dvěma klíči. První klíč positions - seznam pozic (indexů). Druhý klíč count - počet výskytů hledaného čísla
    '''
    pocet = 0
    pos = list()
    idx = 0

    while idx < len(seq): #for idx in range(0,len(seq)):
        if seq[idx] == num:
            pocet += 1
            pos.append(idx)
        idx += 1
    #slovnik = dict(zip(positions, count))

    return {
        'positions': pos,
        'count':pocet,
    }
    #nejlepsi ( O(1) ) vs. nejhorsi ( O(n) )

def pattern_search(seq, pattern):
    '''
    Najde všechny pozice výskytu vzoru v DNA sekvenci.
    :param sequence: (str) DNA sekvence
    :param pattern: (str) hledaný vzor
    :return: (set) množina pozic, kde vzor začíná
    '''
    delka = len(pattern)
    pozice = set()
    i = 0

    #for i in range(len(seq)-delka+1): #Bez +1 bys přišla o poslední možné místo, kde by vzor mohl být #minus delka, abychom neprekrocili delku sekvence
    while i <= len(seq) - delka:
        if seq[i:i+delka] == pattern:
            pozice.add(i)
            i += 1
        else:
            i += 1 ## pokračování na další pozici při neshodě
    return pozice
    # UKOL 2.6 : NEJLEPSI O(m)     NEJHORSI O(m*n)

def binary_search(seznam, searching_num):
    '''
    zda-li se ve vzestupně seřazené posloupnosti nachází libovolné požadované číslo a vrátí jeho pozici
    :param seznam: prohledávaný seznam čísel (list)
    :param searching_num: hledané číslo (int)
    :return: index, na kterém se hledané číslo v sekvenci nachází. Pokud není číslo nalezeno, funkce vrátí hodnotu None.
    '''
    left = 0
    right = len(seznam)-1 #indexace od nuly

    while left <= right:
        middle = (left + right) // 2  # Středový index

        if seznam[middle] == searching_num:
            return middle  # Pokud najdeme hledané číslo, vrátíme jeho index
        elif seznam[middle] < searching_num:
            left = middle + 1  # Pokud hledané číslo je větší, posuneme levý index
        else:
            right = middle - 1  # Pokud hledané číslo je menší, posuneme pravý index
    return None

    # UKOL 2.8 : sekvenční:NEJLEPSI O(1)   NEJHORSI O(n) (az na poslednim miste n prvku) , binární (prvek je neni v seznamu): NEJLEPSI O(1)     NEJHORSI O(log n)
    # Celkový počet porovnání je tedy počet iterací, které jsou potřebné k tomu, aby se oblast zúžila na 1 prvek. Pokud je délka seznamu n, pak počet porovnání v nejhorším případě je přibližně logaritmus z n (kde logaritmus je o základu 2, protože každé porovnání zkracuje oblast na polovinu).

def main():
    file_name = 'sequential.json' #pass
    sequential_data = read_data(file_name, field = 'unordered_numbers')
    print(sequential_data)

    sekvence = sequential_data
    hledane_cislo = 5
    vysledek = linear_search(sekvence, hledane_cislo)
    print(f"Hledané č.:{hledane_cislo} má tyto pozice: {vysledek['positions']} a nachází se v dané sekvenci čísel {vysledek['count']}krát.")

    #Načtení DNA sekvence ze souboru
    dna_data = read_data(file_name, field='dna_sequence')
    print("DNA sekvence:", dna_data)

    hledany_vzor = "ATA"
    nalezene_pozice = pattern_search(dna_data, hledany_vzor)
    print(f"Vzor '{hledany_vzor}' nalezen na pozicích: {nalezene_pozice}")

    #Nacteni serazeneho seznamu cisel
    serazeny_seznam = read_data(file_name, field='ordered_numbers')
    print(serazeny_seznam)
    hledane_num = -3
    index_pozice = binary_search(serazeny_seznam, hledane_num)
    print(f"Hledané číslo {hledane_num} se nachází na {index_pozice}. pozici dané seřazené sekvence {serazeny_seznam}")

if __name__ == '__main__':
    main()