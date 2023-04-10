Write Python or Java code that
• creates a MongoDB DB called "amazon"
• reads "reviews_electronics.16.json" and uploads each review as a separate document to the collection "reviews" in the DB "amazon".
• uses MongoDB's map reduce function to build a new collection "avg_scores" that averages review scores by product ("asin"). Print the first 100 entries of "avg_scores" to screen.
• uses MongoDB's map reduce function to build a new collection "weighted_avg_scores" that averages review scores by product ("asin"), weighted by the number of votes + 1 (the second number + 1). Print the first 100 entires of "weighted_avg_scores" to screen.

 

The format of "reviews_electronics.16.json" is:
• reviewerID - ID of the reviewer, e.g. A2SUAM1J3GNN3B
• asin - ID of the product, e.g. 0000013714
• reviewerName - name of the reviewer
• helpful - helpfulness rating of the review, e.g. 2/3
• reviewText - text of the review
• overall - rating of the product
• summary - summary of the review
• unixReviewTime - time of the review

 

Please submit one .py, .ipynb, or .java file.
