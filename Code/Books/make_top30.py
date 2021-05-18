# Read the 3rdpass output file and creating a dataset in a format that will
# be able to be compared to the Kaggle data easily to determine which titles
# are in the top 100 ranked Amazon books by year. Then we have the reviews that
# will be used next quarter to try to determine what books make the top 100 by review

# Input file is 1 review per line. All books have at least 30 reviews
# Output file is 1 book per line and has the first30 reviews for that book (very long lines) 

import pandas as pd
import csv

# Out file to write good lines to
f = open('first30_reviews.tsv', 'w')
outline = "Title"
for i in range(1,31):
    outline += "\tDate_" + str(i) + "\t" + "Review_" + str(i)
outline += "\n"

f.write(outline)

third_pass = pd.read_csv('../../3rdpass_cleaned.tsv', sep='\t', quoting=csv.QUOTE_NONE)

first30 = third_pass.groupby('Title').tail(30)

current_title = ''
count_lines = 0
for index, row in first30.iterrows():
    count_lines += 1
    title = row[0]
    if title == current_title: # add review to the current line
        outline += "\t" + row[4] + "\t" + row[3]
    else: # write out the current line and start a new line 
        outline += "\n" 
        f.write(outline)
        outline = title + "\t" + row[4] + "\t" + row[3]
    if count_lines > 300: 
        f.close()
        print(zz)

# Read review counts and get list of good titles (this is the dict from the 2nd cleaning pass) 
good_titles_file = '2ndpass_reviewcounts_30.tsv'
good_titles = []

with open(good_titles_file) as file_in:
    # Skip the header line
    next(file_in)
    # Loop through each line in the file
    for line in file_in:
        # Split the lines on tabs
        line_data = line.split('\t')
        # Append title from good_title_file line to good_titles list 
        good_titles.append(line_data[0])

print(len(good_titles))
good_titles_set = set(good_titles) #making it a set to save time with checking if elements are in the set

# Read in the first pass cleaned tsv
file_name = '1stpass_cleaned.tsv'

with open(file_name) as file_in2:
    # Skip the header line
    next(file_in2)
    # Loop through each line in the file
    for line in file_in2:
        # Split the lines on tabs
        line_data = line.split('\t')
        if line_data[0] in good_titles_set: f.write(line)


f.close()
