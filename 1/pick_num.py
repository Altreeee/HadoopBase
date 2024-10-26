# -*- coding: utf-8 -*-
import re


input_file_paths = [
    '/user/s1155218605/a-output/part-00000',
    '/user/s1155218605/a-output/part-00001',
    '/user/s1155218605/a-output/part-00002',
    '/user/s1155218605/a-output/part-00003',
    '/user/s1155218605/a-output/part-00004',
    '/user/s1155218605/a-output/part-00005',
    '/user/s1155218605/a-output/part-00006',
    '/user/s1155218605/a-output/part-00007',
    '/user/s1155218605/a-output/part-00008',
    '/user/s1155218605/a-output/part-00009',
]


output_file_path = 'filtered_output.txt'


with open(output_file_path, 'w') as outfile:
    for input_file_path in input_file_paths:
        
        with open(input_file_path, 'r') as infile:
            for line in infile:
                
                match = re.match(r'(\d+):', line)
                if match:
                    first_number = match.group(1)
                    
                    if first_number[-4:] == '8605':
                        outfile.write(line)

print(f"筛选结果已写入到 {output_file_path}")
