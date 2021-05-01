# Second pass to clean the book data. Build big dictionary to count number of reviews per book 

from collections import defaultdict
 
# Out file to write good lines to
f = open('2ndpass_reviewcounts.tsv', 'w')
f.write('Title\tCount\n')

#file_name = '1stpass_cleaned100k.tsv'
file_name = '1stpass_cleaned.tsv'

with open(file_name) as file_in:
    # Skip the header line
    next(file_in)
    good_counter = 0
    line_counter = 0
    review_count = defaultdict(int)
    # Loop through each line in the file
    for line in file_in:
        line_counter += 1
        if line_counter % 100000 == 0: print('Line counter', line_counter)
        # Split the lines on tabs
        line_data = line.split('\t')
        # Build dictionary
        review_count[line_data[0]] += 1

    #print(len(review_count.keys()))
    #print(max(review_count.items(), key=lambda a: a[1]))
    sorted_output = sorted(review_count.items(), key=lambda a: a[1], reverse=True)
    print('Finished sorting dictionary')
    #print(len(sorted_output))
    #print(sorted_output[0:5])
    
    threshold = 30
    for item in sorted_output:
        if item[1] < threshold: break 
        outline = item[0] + '\t' + str(item[1]) + '\n'
        f.write(outline)

f.close()
