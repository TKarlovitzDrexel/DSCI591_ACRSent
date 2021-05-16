# First pass to clean the book data. Taking out things like NaNs
 
# Out file to write good lines to
f = open('1stpass_cleaned100k.tsv', 'w')
f.write('Title\tStar_Rating\tTotal_Votes\tReview_Body\tReview_Date\n')

file_name = 'books_00_100k.tsv'
#file_name = '/Users/tessakarlovitz/Documents/DSCI591/amazon_reviews_us_Books_v1_00.tsv'

with open(file_name) as file_in:
    # Skip the header line
    next(file_in)
    good_counter = 0
    line_counter = 0
    # Loop through each line in the file
    for line in file_in:
        line_counter += 1
        if line_counter % 100000 == 0: print('Line counter', line_counter)
        # Split the lines on tabs
        line_data = line.split('\t')
        # Remove any rows that do not have 15 columns. We're not sure why some have extra data probably extra tabs
        if len(line_data) != 15: continue
        # Check if product category is not 'Books'. Remove lines that are not
        if line_data[6] != 'Books': continue
        # Remove any dates that are not correct length 
        if len(line_data[14]) != 11: continue
        # Keep only verified purchases
        if line_data[11] != 'Y': continue
        # Verify star ratings are only between 1-5
        if line_data[7] not in ['1','2','3','4','5']: continue
        # Remove rows where book title and review body are empty
        if len(line_data[5]) == 0: continue
        if len(line_data[13]) == 0: continue
        # If total_votes is empty replace with a 0
        if len(line_data[9]) == 0: line_data[9] = '0'
        good_counter += 1
        
        # Write out the good lines 
        out_line = line_data[5] + '\t' + line_data[7] + '\t' + line_data[9] + '\t' + line_data[13] + '\t' + line_data[14]
        f.write(out_line) 
    print('Good line counter', good_counter)
    f.close()
