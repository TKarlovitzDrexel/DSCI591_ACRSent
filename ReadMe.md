Book Data
- There are two main parts of the book data
	Part 1 deals solely with the Amazon customer review datasets that
	we were able to download from Amazon's website. These tsv's contain
	data such as the book, author, star rating, date review was made, 
	and the contents of the review. 
	The goal of part 1 is to clean this dataset, perform EDA/SDA and 
	and produce a final tsv that can be used next term for sentiment
	analysis. That sentiment analysis will read the reviews and try to
	determine what star rating the book received (1-5). 

	Part 2 adds in a second dataset, Top 100 Ranked Books on Amazon by 
	Year. This dataset was found on Kaggle.com. The dataset contains
	information including the book, author, rating, rank, and year. 
	Note a book can show up twice in this dataset if it was ranked say 2
	in 2013 then 12 in 2014. In this part we utilized the dataset that 
	was produced in part 1, to create a new dataset. This new dataset 
	contains a book and the first 30 reviews that book received on 
	Amazon. We then combined that dataset with the Kaggle top ranked 
	dataset for our final product. The goal of part 2 was to produce this
	dataset and perform some EDA/SDA. The long term goal is to utilize
	this dataset next term for sentiment analysis. The sentiment analysis
	that will be performed is predicting if a book will make the top 100 
	ranked books on Amazon for that year based off the top 30 reviews. 

- The code
        For part 1, we wrote three Python standalone scripts to clean the
        original Amazon tsv: clean_books_1stpass.py, clean_books_2ndpass.py,
        and clean_books_3rdpass.py. In short, these files remove any bad rows,
        and keep only books with 30 or more reviews. EDA and SDA were performed
        in part1_book_SDA.ipynb.

        For part 2, the main work was combining the Amazon Top 100 Ranked
        books by year with our cleaned dataset that was produced in part
        1. First, we needed to create a dataset that contained the first
        30 reviews ever written for each book in our Amazon product
        reviews dataset. make_top30.py was written for this. It produced
        the file first30_reviews.tsv. We then were able to merge this file
        with the Amazon Top 100 Ranked books by year on book title in
        part2_rank_books_SDA.ipynb. EDA/SDA were performed in there as well.

Note that all of the tsv's combined for the book data are over 1GB so I was
unable to upload it to github. I can email it separately if needed.
	
Mobile Electronics
- Mobile electronic review data is from the Amazon customer review dataset from Amazon's website.
- The data consists of product reviews for various mobile electronics and accessories from 2001-2015. There are approximately 100,000 reviews within the mobile electronics dataset
- The code included here includes cleaning and pre-processing, statistical data analysis, exploratory data analysis, and visualizations that aid in the creation of a polished dataset that will be used to perform predictive modeling in future work. The main goal is to use the review dataset to make a prediction of which star rating (1-5) the reviewer will give. 
