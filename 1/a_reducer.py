import sys
from collections import defaultdict

def reduce_referrers():
    
    website_pairs_referrers = defaultdict(set)


    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        try:
            website_pair, referrer = line.split('\t')
            website1, website2 = website_pair.split(',')
            
            website_pairs_referrers[(website1, website2)].add(referrer)
        except ValueError:
            continue

    
    #website_best_match[website1] = (website2, referrers)
    website_best_match = defaultdict(lambda: (None, set()))

   
    for (website1, website2), referrers in website_pairs_referrers.items():
        common_ref_count = len(referrers)

        
        if common_ref_count > len(website_best_match[website1][1]):
            website_best_match[website1] = (website2, referrers)
        elif common_ref_count == len(website_best_match[website1][1]):
            if int(website2) < int(website_best_match[website1][0]):
                website_best_match[website1] = (website2, referrers)

        
        if common_ref_count > len(website_best_match[website2][1]):
            website_best_match[website2] = (website1, referrers)
        elif common_ref_count == len(website_best_match[website2][1]):
            if int(website1) < int(website_best_match[website2][0]):
                website_best_match[website2] = (website1, referrers)


    
    for website, (best_match, referrers) in website_best_match.items():
        if best_match is not None:
            
            referrer_list_str = ','.join(sorted(referrers, key=int))
            common_ref_count = len(referrers)
            
            print(f'{website}:{best_match}\t{{{referrer_list_str}}}, {common_ref_count}')

if __name__ == "__main__":
    reduce_referrers()
