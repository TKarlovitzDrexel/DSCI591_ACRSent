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
first30_grouped = first30.groupby('Title')

count_lines = 0
for title, group in first30_grouped:
    outline = title
    for index, row in group.iterrows():
        outline += "\t" + row['Review_Date'] + "\t" + row['Review_Body']
    count_lines += 1
    outline += "\n"
    f.write(outline)
    if count_lines % 100 == 0: 
        print(count_lines)


f.close()
