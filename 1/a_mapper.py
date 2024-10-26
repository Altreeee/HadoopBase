import sys

def map_referrers():
    referrer_dict = {}

    # <referrer, referee> 
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        try:
            referrer, referee = line.split()
            if referrer not in referrer_dict:
                referrer_dict[referrer] = []
            referrer_dict[referrer].append(referee)
        except ValueError:
            continue

    
    for referrer, referees in referrer_dict.items():
        referees = sorted(set(referees))  
        for i in range(len(referees)):
            for j in range(i + 1, len(referees)):
                referee1 = referees[i]
                referee2 = referees[j]
                
                print(f'{referee1},{referee2}\t{referrer}')
                print(f'{referee2},{referee1}\t{referrer}')

if __name__ == "__main__":
    map_referrers()
