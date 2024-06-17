# CS5530Assign1MB
In Assignment 1 part 1, I was given a relatively small dataset that relates
grip strength in women and medically defined fraility.
The task is to design a workflow to import, process, and analyze the dataset.
The importing and preprocessing should be automated. Sorting and visualization
should be as automated as possible. If these are done properly, the workflow
should yield reproducible results.
The first step was to create a Data.csv file. I copied over the table to OpenOfficeCalc.
That took a little formatting, then I saved the table as a CSV file. This also took
bit of formatting. Thusly, Data1a.CSV was created.
Then I loaded up Visual Studios and created a new python application.
Installed the necessary libraries (I had to install Python 3.12 via Microsoft Store first).
Once the console was ready, I added a folder Data, and transferred the Data1a.CSV to the folder.
The Visual Studio environment was not working once I set up some code and tried to execute.
This led me to use Google Colab to run the initial small dataset analysis.
Colab ran real well. The virualized Pyhton environment ran the test codes well.

![Screenshot 2024-06-16 122147](https://github.com/BuffaloManwich/CS5530Assign1MB/assets/145368105/a4ea9bf8-211c-48c5-abed-b3449d7b19de)

![Screenshot 2024-06-16 122159](https://github.com/BuffaloManwich/CS5530Assign1MB/assets/145368105/06b03115-8fa2-46b5-9a0c-0136eeb80251)

![Screenshot 2024-06-16 122208](https://github.com/BuffaloManwich/CS5530Assign1MB/assets/145368105/991ded48-ac07-447b-9134-05c8e4e3195b)

![Screenshot 2024-06-16 122219](https://github.com/BuffaloManwich/CS5530Assign1MB/assets/145368105/776a4e2c-05ec-4697-8354-e3ac7de5c8c8)

![Screenshot 2024-06-16 122242](https://github.com/BuffaloManwich/CS5530Assign1MB/assets/145368105/135c3943-ab68-489d-9f65-c76776e6b2d1)

I am going to attempt to run the Part 2 analysis on VSCode.
VS Code worked very well in Python! The necessary pip instalations were scikit-learn, plotly, seaborn, matplotlib, scipy, and pandas.

![Screenshot 2024-06-16 200724](https://github.com/BuffaloManwich/CS5530Assign1MB/assets/145368105/d764f867-51ba-4710-9384-201142a51b96)

As you can see, initializing the main.py file generated many .png and a few .html files.
The processes are functionalized in the different .py files. I started the data processing by removing empty values.
Next, I change the catergories with only two options into 0 and 1 (This is ended up a waste of time). That left a cleaned_data.csv
without Nulls and only 2 string-type catergories (parental level of education and race/ethnicity), several binary categories, and our 3 scores types.
Next, I split the the dataset into three, one for each score type. This leaves me with a clean dataset for Math, Writing, and Reading.
The data_analysis.py splits the cleaned_data.csv into cleaned_math.csv (writing, reading also) and generates a p-value and saves the values to a .txt document. Then it produces a heatmap for all three cleaned subtypes. After the heatmap, it generates a t-SNE graph for each.
The heatmap yields some interesting relationship results. The t-SNE is probably setup wrong because I can't make heads or tails of those results.

So far, my code has preprocessed the data, saving as different datasets along the way, it has generated a p-value, a heatmap, and t-SNE for each score type. These are handy ways to decide what correlations to focus on for further analysis.
The final processes are the different visualizations. My program generates three types of graphs for each data subset, a bar graph relating race and lunch program (a substitute for economic status) score, a line graph that relates parent's education and test prep to scores, and an interactive scatter graph that relates gender and ethnicity to scores using a color gradient for occurrence count.

Human analysis: Assuming this dataset is accurate in nature, the relationship between race, economic standing, parental education level, and indivdual student preparation is complex. The heatmap showed a positive correlation between race but that gets a bit complicated to decipher in practicality. The next obvious factor is test prep. In nearly every category, the prepared students did much better, though there is some overlap on the fringes. Economics and parental eduction are obviously influential factors that could be flushed out via another graph or two.
I attempted to generate a scatter graph that used a different axis layout to perform another visualization but couldn't get it setup right. A lot of additional information could be gathered from this dataset and I look forward to using new graphs and analytical techniques in the future. 
