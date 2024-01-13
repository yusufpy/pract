## Statistical Analysis Report

### Introduction
This report presents a comprehensive statistical analysis of the data related to proportional species richness for different taxonomic groups. The data include information on Bees, Birds, Butterflies, Carabids, Macromoths, and Isopods. The analysis covers univariate statistics, correlation, contingency tables, likelihood-ratio tests, odds ratio, sensitivity, specificity, Youden's index, and simple linear regression.

### Data Overview
The data consist of proportional species richness values for each taxonomic group. The analysis focuses on two subsets: BD5 (Bees, Birds, Butterflies, Carabids, Macromoths) and BD11 (a broader set of taxonomic groups).

### Univariate Analysis
#### Summary Statistics
Summary statistics for BD5, including minimum, 1st quartile, median, mean, 3rd quartile, and maximum values, are presented in the table below. Additionally, a Winsorized mean is calculated to mitigate the impact of outliers.

```
                Bees           Bird       Butterflies      Carabids       Macromoths       Winsorized_Mean    
Min.   :0.03065  Min.   :0.2415  Min.   :0.3167  Min.   :0.01153  Min.   :0.08947  Min.   :0.5904
1st Qu.:0.35079  1st Qu.:0.8462  1st Qu.:0.7926  1st Qu.:0.47539  1st Qu.:0.7856   1st Qu.:0.9007
Median :0.58869  Median :0.9038  Median :0.8863  Median :0.63553  Median :0.8767   Median :0.8788
Mean   :0.60502  Mean   :0.8872  Mean   :0.8746  Mean   :0.60706  Mean   :0.8493   Mean   :0.6208
3rd Qu.:0.81663  3rd Qu.:0.9570  3rd Qu.:0.9677  3rd Qu.:0.76161  3rd Qu.:0.9415   3rd Qu.:0.8648
Max.   :3.30986  Max.   :1.1720  Max.   :1.3944  Max.   :1.19977  Max.   :1.2605   Max.   :0.5904
```

#### Winsorized Mean
The Winsorized mean values for each taxonomic group are calculated to provide a robust measure of central tendency. For example, the Winsorized mean for Macromoths is 0.5904.

### Correlation Analysis
A correlation matrix is computed for BD5, revealing the pairwise correlations between Bees, Birds, Butterflies, Carabids, and Macromoths. The matrix shows moderate to strong positive correlations between the taxonomic groups.

```
                 Bees      Bird   Butterflies   Carabids   Macromoths
Bees        1.0000000 0.3759451  0.41293480  0.25173839  0.4728640
Bird        0.3759451 1.0000000  0.34225731  0.31091907  0.5941118
Butterflies 0.4129348 0.3422573  1.00000000 -0.07224957  0.5608753
Carabids    0.2517384 0.3109191 -0.07224957  1.00000000  0.1925311
Macromoths  0.4728640 0.5941118  0.56087528  0.19253108  1.0000000
```

### Contingency Table and Likelihood-Ratio Test
A contingency table is constructed to compare the directional changes (increase or decrease) in BD11 and BD5. A likelihood-ratio test is performed, indicating a significant association between the changes in BD5 and BD11 (p-value < 0.05).

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

Reject the null hypothesis: There is a significant association between BD5 and BD11 changes.
```

### Odds Ratio, Sensitivity, Specificity, and Youden's Index
Key metrics are calculated to assess the association between BD5 and BD11 changes:

- Odds Ratio: 42.94
- Sensitivity: 0.876
- Specificity: 0.859
- Youden's Index: 0.735

These metrics provide insights into the predictive power and accuracy of the association between the two variables.

### Simple Linear Regression
A simple linear regression model is fitted to predict the Isopods variable based on the proportional species richness of Bees, Birds, Butterflies, Carabids, and Macromoths (BD5). The coefficients and statistical significance of each predictor are reported.

```
Call:
lm(formula = BD1$Isopods ~ BD5$Bees + BD5$Bird + BD5$Butterflies + 
    BD5$Carabids + BD5$Macromoths, data = BD5)

Coefficients:
                 Estimate Std. Error t value Pr(>|t|)    
(Intercept)      0.278034   0.025820  10.768  < 2e-16 ***
BD5$Bees        -0.050742   0.010322  -4.916 9.12e-07 ***
BD5$Bird         0.018511   0.032436   0.571    0.568    
BD5$Butterflies -0.001427   0.024573  -0.058    0.954    
BD5$Carabids     0.440173   0.013799  31.899  < 2e-16 ***
BD5$Macromoths   0.023820   0.027585   0.863    0.388    
```

### Model Selection via Stepwise Regression
A stepwise regression is performed to select significant predictors for the Isopods variable. The process involves eliminating non-significant predictors to optimize the model. The final model includes Bees and Carabids as predictors.

```
Call:
lm(formula = BD1$Isopods ~ Bees + Carabids, data = cbind(B

D1, BD5))

Coefficients:
             Estimate Std. Error t value Pr(>|t|)    
(Intercept)  0.307305   0.008718  35.250  < 2e-16 ***
Bees        -0.044133   0.008904  -4.957  7.4e-07 ***
Carabids     0.443689   0.012866  34.485  < 2e-16 ***
```

### Model Evaluation
The selected model is evaluated on both the training and test sets using mean squared error (MSE). The MSE on the training set is 0.0262, while on the test set, it is 0.1045. This provides insights into the model's performance and generalizability.

### Conclusion
In conclusion, this statistical analysis has provided valuable insights into the relationships between taxonomic groups, directional changes, and their impact on the Isopods variable. The identified associations and predictive models contribute to a better understanding of ecological dynamics within the studied system.
