install.packages('dplyr')

df <- read.csv("/content/proportional_species_richness_NAs_removed.csv")
#library(dplyr)

head(df)

#Choosing my BD7
BD7 <- subset(df, select = c(Bees, Isopods,Grasshoppers_._Crickets,Butterflies, Bryophytes,Carabids,Ladybirds))
head(BD7)

BD11 <- df[,2:12]
df$BD11<-rowMeans(BD11)
df$BD7<-rowMeans(BD7)

head(BD11)

"""# Data Exploration: Univariate Analysis
We begin by examining the distribution of each variable separately, using descriptive statistics and graphical representations.
"""

#First, let's look at the summary statistics for each variable:
summary(BD7)

"""From these summary statistics, we can see that the proportional species richness values vary across the seven taxonomic groups, with the mean values ranging from 0.60502 for bees to 0.6140 for ladybirds. The median values for most groups are around 0.25, indicating that the data may be roughly symmetrically distributed around the median. However, the bryophytes group has a median of 0.7993, indicating that this group may have a different distribution compared to the other groups."""

install.packages('corrplot')

library(ggplot2)
library(tidyverse)
library(corrplot)

#Next, look at some graphical representations of the data
BD7 %>%
  gather(key = "taxonomic_group", value = "proportional_species_richness", -Bees) %>%
  ggplot(aes(x = proportional_species_richness, fill = taxonomic_group)) +
  geom_histogram(alpha = 0.5, position = "identity", bins = 10) +
  facet_wrap(~ taxonomic_group, ncol = 3) +
  labs(x = "Proportional Species Richness", y = "Frequency")

"""The histograms above show the distribution of the proportional species richness values for each taxonomic group. We can see that the distributions vary in shape and spread, with some groups having relatively narrow distributions (e.g., bees, isopods, and ladybirds) and others having wider distributions (e.g., grasshoppers/crickets, bryophytes, and carabids)."""



"""**Correlation Analysis**: Now, let's examine the correlations between the variables. We can use a correlation matrix to visualize the pairwise correlations between the variables:"""

library(tidyverse)
# compute correlation matrix
corr_matrix <- cor(BD7[,])

# visualize correlation matrix
corrplot::corrplot(corr_matrix, method = "color", type = "lower", tl.col = "black")

"""From the correlation matrix, we can see that there are several strong positive correlations.There are also some negative correlations present.

Overall, these correlations suggest that there are some complex relationships between the different groups of species.

In conclusion, the data presented in this report provides insights into the distribution and correlations of the proportional species richness of seven different taxonomic groups. The strong positive correlation between the proportional species richness of bees and butterflies, as well as the negative correlation between the proportional species richness of bryophites and ladybirds, are particularly noteworthy. These results could be further investigated in future studies to better understand the factors influencing the population sizes of these important taxonomic.

**Reference:**

Lefcheck, J. S. (2016). "piecewiseSEM: Piecewise structural equation modelling in R for ecology, evolution, and systematics". Methods in Ecology and Evolution, 7(5), 573-579. doi: 10.1111/2041-210X.12512

#Hypothesis Testing

Here are two hypothesis tests that we can perform using the proportional_species_richness.csv dataset:

1.   Test whether the mean proportional species richness for butterflies is significantly different from the mean proportional species richness for isopods
2.   Test whether the mean proportional species richness for butterflies is significantly different from the mean proportional species richness for isopods
"""

# Test 1: Mean proportional species richness for butterflies vs isopods
butterflies <- BD7$Butterflies
isopods <- BD7$Isopods
t.test(butterflies, isopods, alternative = "two.sided")

# Test 2: Proportional species richness for first five samples vs last five samples
first_five <- rowMeans(BD7[1:5,])
last_five <- rowMeans(BD7[10:14,])
t.test(first_five, last_five, paired = TRUE, alternative = "two.sided")

"""The t.test() function returns the p-value for each hypothesis test.

For the first hypothesis, the p-value is less than 0.05. Therefore, we reject the null hypothesis that the mean proportional species richness for butterflies is equal to the mean proportional species richness for isopods, and conclude that there is a significant difference between the two groups.

For the second hypothesis, the p-value is 0.7127, which is greater than 0.05. Therefore, the test failed to reject the null hypothesis that there is no significant difference in the proportional species richness between the first five and the last five samples

**References:**

Sokal, R. R., & Rohlf, F. J. (1995). Biometry: The principles and practice of statistics in biological research (3rd ed.). W. H. Freeman and Company.
"""



"""#Simple Linear Regression

To perform a simple linear regression to see how BD7 matches BD11, we'll use the lm() function in R as follows
"""

# Perform simple linear regression for the entire dataset
model <- lm(BD11 ~ Bees + Isopods + Grasshoppers_._Crickets + Butterflies + Bryophytes + Carabids + Ladybirds, data = df)

# Print the model summary
summary(model)

"""The above summary shows the results of a linear regression model that examines the relationship between the abundance of bees (dependent variable) and several independent variables, including Isopods, Grasshoppers and Crickets, Butterflies, Bryophytes, Carabids, and Ladybirds.

The intercept value of 0.111959 indicates that the expected abundance of bees when all independent variables are zero is positive. The p-value of the intercept is less than 0.001, indicating that the intercept is statistically significant.

The coefficients for each of the independent variables indicate the expected change in the abundance of bees for a one-unit increase in the independent variable, holding all other variables constant. For example, a one-unit increase in Isopods is associated with a increase in the abundance of bees by 0.112443 units. The p-values for each of the coefficients are less than 0.001, indicating that each of the independent variables is statistically significant in explaining the variation in the abundance of bees.

The adjusted R-squared value of 0.9586 indicates that the independent variables explain approximately 95.86% of the variation in the abundance of bees. The F-statistic of 1748 and its corresponding p-value of less than 0.001 indicates that the overall model is statistically significant in explaining the variation in the abundance of bees.

Finally, the residuals standard error of 0.02197 indicates that the average difference between the observed abundance of bees and the predicted abundance of bees from the model is approximately 0.02197 units.

To perform separate linear regressions for each period in the data, we'll use the split() function in R to split the data into subsets based on the values in the period column, and then use a for loop to fit a separate linear regression model to each subset
"""

# Split the data into subsets based on period
df_by_period <- split(df, df$period)

# Loop through the subsets and fit a separate linear regression model to each
for (i in 1:length(df_by_period)) {
  period_data <- df_by_period[[i]]
  model <- lm(BD11 ~ Bees + Isopods + Grasshoppers_._Crickets + Butterflies + Bryophytes + Carabids + Ladybirds, data = period_data)
  print(paste0("Period ", i, ":"))
  print(summary(model))
  print(coef(model))
}

"""The summary output for each period's linear regression model shown above allow us to observe the variations in coefficient values and goodness of fit across different periods. From the summary of the modelling of the two different periods we can see that there is no change in statistical significance of each of the variable across the two periods and all the variable are statistically significant.This simply means that all the variables are good predictors. We'll be making make interpretation for just one of the period since there is no any significant difference across the two period.

At the first period, all of the coefficients have very small p-values (< 0.001), indicating that they are statistically significant. This means that we can reject the null hypothesis and conclude that each of these variables (Isopods, Grasshoppers & Crickets, Butterflies, Bryophytes, Carabids, and Ladybirds) has a significant linear relationship with the response variable (Bees) after controlling for the other variables in the model. The intercept also has a very small p-value, indicating that it is significantly different from zero.
The overall model has a very small p-value (< 2.2e-16), indicating that there is strong evidence that the model as a whole is a good fit for the data. The multiple R-squared and adjusted R-squared values indicate that the model explains about 43% of the variance in the response variable.

The analysis was performed using R version 4.0.3 (R Core Team, 2020).

**References**

R Core Team. (2020). R: A language and environment for statistical computing. R Foundation for Statistical Computing
"""



"""#Multiple Linear Regression"""

BD4 <- select(BD11,-Grasshoppers_._Crickets,-Butterflies,-Bryophytes,-Carabids,-Bees,-Isopods,-Ladybirds)
df$BD4 <- rowMeans(BD4)
model <- lm(BD4 ~ BD7,data=df)
summary(model)

"""Now we've build a linear regression model with the response variable `BD4`(the four taxonomic group) and the predictor variable `BD7`(the seven taxonomic group). The summary output provides information about the model fit and the estimated coefficients.

The estimated intercept is 0.419487, which represents the predicted value of `BD4` when `BD7` is zero. The estimated coefficient for `BD7` is 0.571900, which means that a one-unit increase in `BD7` is associated with an estimated 0.571900 unit increase in `BD4`. Both coefficients are statistically significant at the 0.001 level, based on their corresponding p-values.

The multiple R-squared is 0.5561, which indicates that 55.61% of the variability in `BD4` is explained by the linear relationship with `BD7`. The adjusted R-squared is almost the same as the multiple R-squared, suggesting that adding the predictor `BD7` to the model did not improve the model fit substantially.

The F-statistic is used to test the null hypothesis that all of the coefficients in the model are zero (i.e., there is no relationship between the predictor and the response). The F-statistic value is 6612, with a corresponding p-value of less than 2.2e-16, indicating strong evidence against the null hypothesis and suggesting that the model as a whole is significant.

The residuals (differences between the observed and predicted values) have a mean of zero and a standard deviation of 0.06387. The residual plot may be examined to assess the model assumptions, such as linearity, normality, constant variance, and independence of errors.
"""



coef(model)

"""Finally, we can interpret the coefficients of the model. The predictor is represented by a corresponding coefficient estimate. Here is a breakdown of the coefficients and their interpretations based on the variable names:

- `(Intercept):` This is the estimated intercept or baseline value of the dependent variable when all predictors are equal to zero.

- `BD7:` For each unit increase in the BD7 predictor, there is an estimated increase of 0.4195 in BD4


"""



"""#Open Analysis"""

new_df=subset(BD11, period == 'Y70')
summary(new_df)

new_df=subset(BD11, period == 'Y00')
summary(new_df)



"""The dataset provided contains information on the species richness of different taxa at various location, during two different periods (Y70 and Y00). This report will focus on the changes in species richness of bees and butterflies between the two periods.

Looking at the dataset, it is clear that there are differences in the proportional species richness of bees and butterflies between the two periods. In Y70, the proportional species richness of bees ranges from 0.03065 to 1.00000, while in Y00 it ranges from 0.1010 to 3.3099. Similarly, the proportional species richness of butterflies ranges from 0.3167 to 1.00000 in Y70, while in Y00 it ranges from 0.3209 to 1.3944.

These results suggest that there has been a decrease in the proportional species richness of both bees and butterflies between the two periods. This is concerning as both of these taxa are important pollinators and play a vital role in maintaining healthy ecosystems. The decline in their species richness could be attributed to a number of factors, such as habitat loss, pesticide use, and climate change.


In conclusion, the data presented in this report indicates that there has been a decrease in the proportional species richness of bees and butterflies in  between the periods of Y70 and Y00. This decline is concerning and highlights the need for further research into the causes of this decline and the implementation of conservation measures to protect these important pollinators.

**References**

Hanson, J. O. et al. Global conservation of species’ niches. Nature 580, 232–234 (2020).
"""



"""# Additional

To further investigate the change in bird species richness between the two periods, we can perform a paired t-test. The paired t-test results.

Let's say we want to compare the mean values of Bees for the two periods, Y00 and Y70.
"""

#First, we need to create two subsets of the data for each period
Y00_data <- BD11[BD11$period == "Y00",]
Y70_data<- BD11[BD11$period == "Y70",]

#Next, we can perform a t-test using the t.test() function
t.test(Y00_data$Bees, Y70_data$Bees, var.equal = TRUE)

"""From the t-test above, we can see that we have a p-value of 2.2e-16. A p-value less than 2.2e-16 means that the probability of observing such an extreme difference or more between the two groups (pre- and post-management) by chance alone is essentially zero. In other words, the results are highly statistically significant, and we can reject the null hypothesis that there is no difference between the two periods. Therefore, we can conclude that the difference in the mean proportional species richness between the two periods is likely due to the management intervention

Reference:

https://www.researchgate.net/publication/7005498_Species_richness_changes_lag_behind_climate_change

#Done

References

1). R Core Team. (2020). R: A language and environment for statistical computing. R Foundation for Statistical Computing

2). Hanson, J. O. et al. Global conservation of species’ niches. Nature 580, 232–234 (2020).

3). https://www.researchgate.net/publication/7005498_Species_richness_changes_lag_behind_climate_change
"""







#Lets read in the data
df <- read.csv('/content/proportional_species_richness_NAs_removed.csv')

head(df)

#choosing my 5 taxonomic group
BD5 <- subset(df, select = c(Bees, Bird, Butterflies, Carabids, Macromoths))
head(BD5)

BD11 <- df[,2:12]
df$BD11<-rowMeans(BD11)
df$BD5<-rowMeans(BD5)

head(BD11,3)

###Univariate Analysis
# 1). Let's build the summary statistic table
summary_table <- summary(BD5)

# Calculate 20% Winsorized mean
winsorized_mean <- function(x) {
  q_20 <- quantile(x, 0.20)
  q_80 <- quantile(x, 0.80)
  x[x < q_20] <- q_20
  x[x > q_80] <- q_80
  return(mean(x))
}

# Apply the winsorized mean to each column
winsorized_mean_values <- apply(BD5, 2, winsorized_mean)
summary_table <- cbind(summary_table, Winsorized_Mean = winsorized_mean_values)

#Lets see the output!
print(summary_table)

#2. Correlation Table
correlation_matrix <- cor(BD5)
print(correlation_matrix)

#3). Boxplot
boxplot(BD5$Bees, main = "Boxplot for Bees", ylab = "Proportional Species Richness")

#lets import the necessary libraries
library(dplyr)
library(tidyr)
library(MASS)

###Contingency table/comparing categorical variables
#1). Convert BD11 and BD5 to binary categorical variables indicating increase or decrease
df <- mutate(df, BD11up = ifelse(BD11 > lag(BD11, default = first(BD11)), "Increase", "Decrease"),
                    BD5up = ifelse(BD5 > lag(BD5, default = first(BD5)), "Increase", "Decrease"))

# Create a contingency table for BD11up against BD5up
contingency_table <- table(df$BD11up, df$BD5up)

# Display the contingency table
print("Contingency Table:")
print(contingency_table)

#2). Create the corresponding independent model contingency table
expected_counts <- matrix(chisq.test(contingency_table)$expected, ncol = 2, byrow = TRUE)
independent_model_table <- as.table(expected_counts)

# Display the independent model contingency table
print("Independent Model Contingency Table:")
print(independent_model_table)

# Perform the likelihood-ratio test
likelihood_ratio_test <- chisq.test(contingency_table)
print("Likelihood-Ratio Test:")
print(likelihood_ratio_test)

# Extract likelihood-ratio statistic and p-value
likelihood_ratio_statistic <- likelihood_ratio_test$statistic
p_value <- likelihood_ratio_test$p.value

# Compare proportions of increase in BD5 and BD11 at 5% confidence level
if (p_value < 0.05) {
  print("Reject the null hypothesis: There is a significant association between BD5 and BD11 changes.")
} else {
  print("Fail to reject the null hypothesis: There is no significant association between BD5 and BD11 changes.")
}

#3). lets estimate the odds-ratio, sensitivity, specificity, and Youden's index
odds_ratio <- (contingency_table[1, 1] * contingency_table[2, 2]) / (contingency_table[1, 2] * contingency_table[2, 1])
sensitivity <- contingency_table[1, 1] / sum(contingency_table[1, ])
specificity <- contingency_table[2, 2] / sum(contingency_table[2, ])
youden_index <- sensitivity + specificity - 1

# lets see the output/results
print("Odds Ratio:")
print(odds_ratio)

print("Sensitivity:")
print(sensitivity)

print("Specificity:")
print(specificity)

print("Youden's Index:")
print(youden_index)

###Simple linear regression
#lets create the variable BD1 (Isopods)
BD5 <- subset(df, select = c(Isopods))

#1). Lets perform simple Linear Regression
BD5 <- subset(df, select = c(Bees, Bird, Butterflies, Carabids, Macromoths))
BD1 <- subset(df, select = c(Isopods))
# Create a linear model
model <- lm(BD1$Isopods ~ BD5$Bees + BD5$Bird + BD5$Butterflies + BD5$Carabids + BD5$Macromoths, data = BD5)

# Lets see the summary of the model
summary(model)

#2). Lets see the slope
coefficients <- coef(model)
# Print the coefficients
print(coefficients)

# 1) Multiple Linear Regression (initial MLR)
initial_model <- lm(BD1$Isopods ~ ., data = cbind(BD1, BD5))

# Estimate the AIC for the initial MLR model
initial_AIC <- AIC(initial_model)
cat("Initial AIC:", initial_AIC, "\n")

# 2) In other for us to be able to perform feature Selection based on p-values and AIC, we will be using stepwise regression
stepwise_model <- step(initial_model)
#Print the output
summary(stepwise_model)

#3). Interaction term and compare AIC
interaction_model <- lm(BD1$Isopods ~ . + Bees:Bird, data = cbind(BD1, BD5))
interaction_AIC <- AIC(interaction_model)

# Compare AIC values
cat("AIC for initial MLR model:", initial_AIC, "\n")
cat("AIC for model with interaction term:", interaction_AIC, "\n")

# 4) Divide the dataset into training and test sets
training_set <- df %>% filter(period == "Y70")
test_set <- df %>% filter(period == "Y00")

# Fit the model on the training set
train_model <- lm(Isopods ~ BD5, data = training_set)

# Make predictions on both training and test sets
train_predictions <- predict(train_model, newdata = training_set)
test_predictions <- predict(train_model, newdata = test_set)

# Evaluate Mean Squared Error
train_mse <- mean((training_set$Isopods - train_predictions)^2)
test_mse <- mean((test_set$Isopods - test_predictions)^2)

cat("Mean Squared Error on Training Set:", train_mse, "\n")
cat("Mean Squared Error on Test Set:", test_mse, "\n")

