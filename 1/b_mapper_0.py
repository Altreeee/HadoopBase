import sys
from collections import defaultdict

def read_input(file):
    for line in file:
        yield line.strip().split()

def map_referrers():
    referrer_dict = defaultdict(set)

    
    for line in read_input(sys.stdin):
        if not line:
            continue
        try:
            referrer, referee = line
            referrer_dict[referee].add(referrer)
        except ValueError:
            continue

    
    referrer_dict_copy = referrer_dict.copy()

   
    for referee, referrers in referrer_dict_copy.items():
        referrers = sorted(referrers)  
        for i in range(len(referrers)):
            for j in range(i + 1, len(referrers)):
                referrer1 = referrers[i]
                referrer2 = referrers[j]

                
                common_referrers = set(referrer_dict_copy[referrer1]) & set(referrer_dict_copy[referrer2])
                total_referrers = set(referrer_dict_copy[referrer1]) | set(referrer_dict_copy[referrer2])
                if total_referrers:
                    similarity = len(common_referrers) / len(total_referrers)
                    common_ref_list = ",".join(sorted(common_referrers))
                    
                    print('%s,%s\t%.4f\t%s' % (referrer1, referrer2, similarity, common_ref_list))
                    print('%s,%s\t%.4f\t%s' % (referrer2, referrer1, similarity, common_ref_list))



if __name__ == "__main__":
    map_referrers()
