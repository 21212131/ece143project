# ECE143 Project Proposal
  Group 4 - Arik Horodniceanu, Chi Zhang, Changhao Shi
  
## Topic
Financial Career Consulting - Helping high-school students decide on career and college choices based on average graduate salaries.
We are trying to answer 3 main questions. First, Which major pays the most, and how does the results differ over time? Second, Which geographical area pays the most? Lastly, Is it more economic to go to a public school rather than private school? If time allowed we will rank schools based on Return on Investment (ROI). And build a content based school recommendation system based on student’s preferences.


## Approaches
### Question 1: 
We can sort the majors based on their corresponding start salaries. And plot the result in bar chart. As we also possess mid-career salaries. We will put those data on the same plot as well. Besides, for further analysis the distribution of mid-career salaries, we will provide a probability density distribution plot.
### Question 2: 
We can plot a USA map, each state will be single pixel of a heat map. The brighter the color is, the higher the salary would be. We will also show which region it is more profitable to go to school in.
### Question 3: 
We can make a table of salaries based on the type of school: State, Engineering, Party, Ivy League or Libral arts. Based on that, we would also make recommendations on the type of school.

## DataSet
Link : https://www.kaggle.com/wsj/college-salaries
There are 3 css files, namely degree vs salaries, region vs salaries, school vs salaries. There are 50 different majors, 5 regions, 249 US schools.

## Plan
Data cleaning and extracting.   -- 1 week 
(Arik Horodniceanu)

Data analysis and Pattern observation. -- 2 week 
(Changhao Shi)

Data visualization and content based recommendation -- 2 week
(Arik Horodniceanu,  Chi Zhang)

Preparing for the final presentation -- 1 week
(Arik Horodniceanu,  Chi Zhang, Changhao Shi)


## Challenges
### Data cleaning:
We need to clean and preprocessing the data. i.e.the data type for wages are string, we need to use integer to rank and analysis the data. Also, because some labels are too subjective, like school types, we need to integrate it into the desired categories. We added labels of tuition and location by state manually, using http://phillips-scholarship.org/new-applicants/cost-of-college-list/ and Google.

### Visualization:
In the project, we will focus on the relations between different factors, such as the salaries of different career stages, the locations of the school, the type of school and the majors of the student. Due to the large amount and various types of our factors, it will be tricky to visualize the relations in an audience-friendly way.

### Interpretation:
We need to be careful when we draw our conclusions from the dataset. There could be several problems. For example, how should we decide where it’s more worthwhile to go to college? Based on the visualizations we will decide on the appropriate methods. We may used regression models to interpret the data more analytically.
