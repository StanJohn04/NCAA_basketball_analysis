# NCAA_basketball_analysis

# Background
 The purpose of this project is to scrape ncaa basketball stats from the internet. After data is collected, run some statistical analysis and create some visualizations that explain the data.

# In Use
* All stat categories were scraped from teamranking.com

![image](https://github.com/StanJohn04/NCAA_basketball_analysis/assets/121142680/f22fd640-b000-4542-aa4e-205ba2684ac3)

  * functions used can be found in [funcs.py](https://github.com/StanJohn04/NCAA_basketball_analysis/blob/main/webscrape/funcs.py)

  * beginning analysis can be found in [analysis.ipynb](https://github.com/StanJohn04/NCAA_basketball_analysis/blob/main/analysis/analysis.ipynb)

  * Combined data frame has all stats from most recent season (2022-2023)
    
![image](https://github.com/StanJohn04/NCAA_basketball_analysis/assets/121142680/c7dbcf61-267c-485a-9cf9-cdbabc4e1edf)

  * Linear regression was run for each stat category vs win percent and r-values stored in df
![image](https://github.com/StanJohn04/NCAA_basketball_analysis/assets/121142680/dca39971-f7cd-4074-822a-822feb45041f)
![image](https://github.com/StanJohn04/NCAA_basketball_analysis/assets/121142680/31301168-6d3b-4311-88ba-a4c100006084)

Plotting of some of these relationships shows correlation between different stat categories and win percetage

![image](https://github.com/StanJohn04/NCAA_basketball_analysis/assets/121142680/34593d02-ab36-4913-bddd-890046032c56)

* Using historical data from teamrankings.com, stats of the 2023 March Madness final four teams can be compared
  
![image](https://github.com/StanJohn04/NCAA_basketball_analysis/assets/121142680/46e3a2ee-df76-431a-a24a-7f3a7511e38f)

* Using KMeans from sklearn, some clustering can be done
  
  ![image](https://github.com/StanJohn04/NCAA_basketball_analysis/assets/121142680/d2877bd3-cae6-42e6-88e8-6eac00e4b6a3)

* In the graph below, the middle cluster is faded out to allow for better contrast between the the two outside clusters

  ![image](https://github.com/StanJohn04/NCAA_basketball_analysis/assets/121142680/417c92ee-1fac-4f5e-87a3-fa5ce31579ee)

  

# HouseKeeping
  * Stats are scraped from NCAA (2022-2023 only) and TeamRankings.com (1997-2023)
    * Stats stored in csv files in Resources folder
  * Next steps:
    * Run analysis:
      * Team data
      * historical data
      * cat vs cat
  * Eventually:
    * Create a dashboard that will display stats and visualizations
    * train a machine learning algorithm that will analyze stats and attempt to predict game outcomes
      * ideally fill out a march madness bracket
