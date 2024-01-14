## Statistical Analysis Report

### Introduction
This report presents a comprehensive statistical analysis of the data related to proportional species richness for different taxonomic groups. The data include information on Bees, Birds, Butterflies, Carabids, Macromoths, and Isopods. The analysis covers univariate statistics, correlation, contingency tables, likelihood-ratio tests, odds ratio, sensitivity, specificity, Youden's index, and simple linear regression.

### Data Overview
The data consist of proportional species richness values for each taxonomic group. The analysis focuses on two subsets: BD5 (Bees, Birds, Butterflies, Carabids, Macromoths) and BD11 (a broader set of taxonomic groups).

### Univariate Analysis
We will begin with comprehensive analysis of proportional species richness for five taxonomic group in the BD5 group, namely Bees, Birds, Butterflies, Carabids, and Macromoths. The analysis includes `summary` statistics commonly obtained using the summary() command in R, as well as an additional statistic – the 20% Winsorized mean.

### Summary Statistic
```
                Bees           Bird       Butterflies      Carabids       Macromoths       Winsorized_Mean    
Min.   :0.03065  Min.   :0.2415  Min.   :0.3167  Min.   :0.01153  Min.   :0.08947  Min.   :0.5904
1st Qu.:0.35079  1st Qu.:0.8462  1st Qu.:0.7926  1st Qu.:0.47539  1st Qu.:0.7856   1st Qu.:0.9007
Median :0.58869  Median :0.9038  Median :0.8863  Median :0.63553  Median :0.8767   Median :0.8788
Mean   :0.60502  Mean   :0.8872  Mean   :0.8746  Mean   :0.60706  Mean   :0.8493   Mean   :0.6208
3rd Qu.:0.81663  3rd Qu.:0.9570  3rd Qu.:0.9677  3rd Qu.:0.76161  3rd Qu.:0.9415   3rd Qu.:0.8648
Max.   :3.30986  Max.   :1.1720  Max.   :1.3944  Max.   :1.19977  Max.   :1.2605   Max.   :0.5904
```

The summary statistic table above shows a comprehensive overview of the proportional species richness for the BD5 group. The inclusion of Winsorized means enhances the robustness of the central tendency measures, providing a more reliable insight into the distribution of each variable. Here are the key take away from the table

- Central Tendency: The mean values generally indicate the central tendency of each variable, with Birds having the highest mean (0.8872) and Bees the lowest (0.60502).
- Variability: The range between the minimum and maximum values illustrates the variability in each variable, with Bees displaying the widest range (3.30986 - 0.03065).
- Winsorized Mean: The Winsorized mean provides a robust alternative to the regular mean, less influenced by extreme values. In some cases, it differs noticeably from the regular mean, suggesting the presence of outliers.

### Correlation Analysis
Correlation analysis presents the correlation analysis of proportional species richness for the BD5 group variables, namely Bees, Birds, Butterflies, Carabids, and Macromoths. The correlation matrix below illustrates the relationships between each pair of variables.

```
                 Bees      Bird   Butterflies   Carabids   Macromoths
Bees        1.0000000 0.3759451  0.41293480  0.25173839  0.4728640
Bird        0.3759451 1.0000000  0.34225731  0.31091907  0.5941118
Butterflies 0.4129348 0.3422573  1.00000000 -0.07224957  0.5608753
Carabids    0.2517384 0.3109191 -0.07224957  1.00000000  0.1925311
Macromoths  0.4728640 0.5941118  0.56087528  0.19253108  1.0000000
```

Here are the key take away from the correlation table:
- Bees and Birds: The correlation coefficient of 0.3759451 suggests a moderate positive correlation between Bees and Birds. This indicates that as the proportional species richness of Bees increases, there is a tendency for Birds to also increase.

- Birds and Macromoths: The correlation coefficient of 0.5941118 indicates a strong positive correlation between Birds and Macromoths. It suggests that as the proportional species richness of Birds increases, Macromoths also tend to increase.

- Butterflies and Carabids: The correlation coefficient of -0.07224957 indicates a weak negative correlation between Butterflies and Carabids. This suggests that there is little to no linear relationship between the two variables.

This correlation analysis provides insights into the relationships between different variables in the BD5 group. Understanding these correlations is crucial for identifying potential patterns in species richness and can aid in ecological interpretations.

### Hypothesis Test
Here are two hypothesis tests that we can perform with the give data:
i). Test whether the mean proportional species richness for butterflies is significantly different from the
mean proportional species richness for isopods
ii). Test the independence between two categorical variables, the "dominantLandClass" and "ecologicalStatus"

Test1:
```
Welch Two Sample t-test

data:  butterflies and isopods
t = 91.859, df = 9050.9, p-value < 2.2e-16
alternative hypothesis: true difference in means is not equal to 0
95 percent confidence interval:
 0.3176938 0.3315483
sample estimates:
mean of x mean of y 
0.8745706 0.5499496
```
The p-value for the Welch Two Sample t-test comparing the means of butterflies and isopods is less than 2.2 \times 10^{-16}2.2×10 
−16
 , indicating strong evidence against the null hypothesis. The alternative hypothesis suggests that the true difference in means is not equal to 0. The 95% confidence interval for the difference in means is (0.3176938, 0.3315483). The sample estimates show that the mean of butterflies (0.8745706) is significantly higher than the mean of isopods (0.5499496).

Test2:
```
[1] 0.4738761
[1] "There is not enough evidence to reject the null hypothesis of independence."
```

The p-value for the Chi-squared test is 0.4738761 which means there is not enough evidence to reject the null hypothesis of independence. This suggests that the variables being tested are not significantly associated based on the observed data.

overall, these hypothesis tests provide insights into the relationships and differences between variables in the dataset

### Contingency table/comparing categorical variables
We constructed a contingency table to compare the directional changes (increase or decrease) in BD11 and BD5. A likelihood-ratio test is also performed, indicating a significant association between the changes in BD5 and BD11

```
Contingency Table:
          
           Decrease Increase
  Decrease     2382      337
  Increase      362     2199

Independent Model Contingency Table:
         A        B
A 1413.056 1330.944
B 1305.944 1230.056

Likelihood-Ratio Test:
	Pearson's Chi-squared test with Yates' continuity correction
	data:  contingency_table
	X-squared = 2849, df = 1, p-value < 2.2e-16
```
The likelihood-ratio statistic is calculated using Pearson's Chi-squared test with Yates' continuity correction. The test results in a chi-squared value of 2849, with 1 degree of freedom and a p-value less than 2.2 \times 10^{-16}2.2×10 
−16 which indicate a significant association between BD5 and BD11 changes hence we will reject the null hypothesis.

### Odds Ratio, Sensitivity, Specificity, and Youden’s Index:
Key metrics are calculated to assess the association between BD5 and BD11 changes:

- Odds Ratio: The calculated odds ratio is 42.93669, indicating a substantial association between BD5 and BD11 changes. 
- Sensitivity: The sensitivity is 0.8760574, representing the ability of the test to correctly identify increases in both BD5 and BD11. 
- Specificity: The specificity is 0.858649, indicating the ability to correctly identify decreases in both BD5 and BD11. 
- Youden’s Index: The calculated Youden's Index is 0.7347063, suggesting a strong overall performance of the test in distinguishing between BD5 and BD11 changes.

With this comprehensive analysis, which include the likelihood-ratio test and various measures such as odds ratio and sensitivity, It can be concluded that changes in BD5 are not independent of changes in BD11. The results emphasize the interconnected nature of these biodiversity measures over the specified periods.

### Simple Linear Regression
