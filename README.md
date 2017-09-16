# k-means-Algorithm-Implementation---Course-Assignment
This code is developed as an assignment for the course "Data Mining"

# k-means_Implementation
1. Load the required file containing data points(to test) in the same directory, k_means_implementation.py is present.
2. Edit the line #13 in k_means_implementation.py for the required number of dimensions corresponding to data point. For instance, iris.txt contains 4D data point and is present in first 4 columns. Hence, keep the usecols values to be 0,1,2,3.
3. Change the access permissions of the file using command - k_means_implementation.py
4. To run the program, type keyword python followed by file name and number of clusters, you would like to have. For instance, if You need three clusters, run the code using python k_means_implementation.py 3
5. You can find the results for final mean of each cluster, number of iterations the program took for convergence, SSE score, final cluster assignments and the size of each clusters in the console.
6. You can read "k_means_observations.pdf" for the pros and cons of the algorithm, I observed while coding the algorithm.

# Calculating the purity of clusters for 'iris.txt' file
1. Keep the k_means_implementation.py and iris.txt in the same directory, finding_purity_of_clusters.py is present.
2. Edit the line #13 in k_means_implementation.py by keeping data file to be 'iris.txt' and usecols values to be (0,1,2,3).
3. Change the access permissions of the file using command - chmod +x finding_purity_of_clusters.py
4. Run the program using the command - python finding_purity_of_clusters.py 3
5. You can find the purity score and respective centroid values of each iterations and best purity score in the created "output.txt" file and the console.

