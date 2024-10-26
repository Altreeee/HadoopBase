import sys
from collections import defaultdict
import heapq

def read_input(file):
    for line in file:
        yield line.strip().split('\t')

def reduce_similarities():
    similarity_dict = defaultdict(list)

   
    for line in read_input(sys.stdin):
        if len(line) != 3:
            continue
        pair, similarity, common_ref_list = line
        website1, website2 = pair.split(',')
        try:
            similarity = float(similarity)
        except ValueError:
          
            continue

       
        heapq.heappush(similarity_dict[website1], (similarity, website2, common_ref_list))
        if len(similarity_dict[website1]) > 3:
            heapq.heappop(similarity_dict[website1])

        heapq.heappush(similarity_dict[website2], (similarity, website1, common_ref_list))
        if len(similarity_dict[website2]) > 3:
            heapq.heappop(similarity_dict[website2])


    for website, similarities in similarity_dict.items():
        
        similarities = sorted(similarities, key=lambda x: (-x[0], x[1]))

        top_similar = []
        for sim in similarities:
            website2 = sim[1]
            similarity = sim[0]  
            common_ref_list = sim[2]
            top_similar.append('%s: {%s}, %.4f' % (website2, common_ref_list, similarity))
        
        
        print('%s: %s' % (website, ', '.join(top_similar)))

if __name__ == "__main__":
    reduce_similarities()
