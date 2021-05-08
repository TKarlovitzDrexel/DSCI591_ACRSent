# Third pass to clean the book data. Create output file 3rd pass cleaned 
# Contains all the "good" titles found in the 2nd pass and creates the output
# file to have all the same data as is in the 1st pass cleaned dataset. 

 
# Out file to write good lines to
f = open('3rdpass_cleaned.tsv', 'w')
f.write('Title\tStar_Rating\tTotal_Votes\tReview_Body\tReview_Date\n')

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
