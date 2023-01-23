# Zillow House Appraisal
 
# Project Description

Zillow is an innovative online database that people around the world use to see available properties and land for sale. Zillow provides people who visit their site with an estimate of how much a home will sell for. Data was gathered on multiple characteristics of the single family homes that were sold in 2017. The goal of this project is to use this data to make predictions/appraise homes that are currently on the market. Different features of homes were analyzed and determined to have the most influence on property value. Machine learning algorithms were applied to these features and an estimate of the property was given with the intent of allowing customers to buy and sell homes that are closest to market value.

# Project Goal
 
* Discover features that influence single family homes appraisal.
* Use features to develop a machine learning model to predict the value of single family homes.
* This information can be used to improve reliability of zillow's home estimates and increase website traffic
 
# Initial Thoughts
 
My initial hypothesis is that the square feet of a home, the number of bedrooms, and the number of bathrooms will have the greatest influence on property value.
 
# The Plan
 
* Aquire data from Sequal Server
 
* Prepare data
   * Create Engineered columns from existing data
       * tax_value
       * bedrooms
       * bathrooms
       * sqft
 
* Explore data in search of drivers of churn
   * Answer the following initial questions
      * What is a property's appraisal value?
      * What variables correlate with each other?
      * Can the number of bedrooms a property have help us know a property's appraisal value?
      * Can the number of bathrooms a property have help us know a property's appraisal value?
      * Does the area of a property help us predict tax_value?
      
* Develop a Model to accurately predict market value of homes
   * Use factors identified in explore to build predictive models of different types
   * Evaluate models on train and validate data
   * Select the best model based lowest root mean square deviation
   * Evaluate the best model on test data
 
* Draw conclusions
 
# Data Dictionary

| Feature | Definition |
|:--------|:-----------|
|tax_value(target)| this is the properties appraisal value|
|bedrooms| this is the number of bedrooms on the property|
|bathrooms| this is the number of bathrooms on the property|
|sqft| This number represents the total area of a property in square feet.|

# Steps to Reproduce
1) Clone this repo.
2) Acquire the data from sql database
3) Put the data in the file containing the cloned repo.
4) Run notebook.
 
# Takeaways and Conclusions
* "Internet service type" and "online security" were each found to be factors of "churn"
    * The influence appears strong
* Monthly charges appears to have influence on churn
    * the spread of the distribution indicates that the influence is weak
* Contract type can may influence churn based on visuals
* Having online security also affects churn as shown in our visuals
* These are enough features to create a model that can predict customer churn
 
# Recommendations
* Consider lowering price of Fiber Optic and increase customers with online_security
* Use Logistic Regression model to predict whether or not a customer is going to churn and have marketing team target these customers
* Accquire more demographic data from customers
