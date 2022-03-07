# Rebuy Case Study

This repository contains the solution (of sorts) for the case study provided by Rebuy.

The problem statement was split across two main categories: Data Analysis and Forecasting. The ask from the data analysis part was to derive some actionable insights, as well as create 4 charts that would go on the daily dashboard of a Category Manager.

Admittedly, I took quite a haphazard approach to the problem and I don't believe I have been able to derive very actionable insights from the given data. I also wasn't able to empathise enough with the role of a category manager to create those 4 charts. Ideally, I would have liked to have a conversation with them in order to understand their perspective, what they know and what they need before going ahead and creating dashboards. 

(Having said that, there are still quite a few visualisations in the notebooks that are contained within this repository.)

The modelling problem was to forecast the 'conversion rate' of each product for the dates 1st January to 7th January, 2021. I had to make an assumption here about the definition of conversion rate because I only started working on this problem on Saturday, and had to submit it by Monday, so there wasn't a window of opportunity to email Carrie to get clarification on this point. 
This was also the first time that I worked on a time series problem. (Haven't gotten the chance to do much of it in the past, at work). Since this was the first time, I tried to extensively use resources available online. The time series modelling tutorial on Kaggle was a good friend. :) ([Found here](https://www.kaggle.com/learn/time-series))

I want to thank the DS team at Rebuy for putting together this interesting case study. There was a lot of data (some of which I didn't get to dive into), and I ended up learning quite a bit!

## File Structure
- All of the analysis and visualisations can be found in the notebooks/ folder
- 'Conversion Rate Forecast.ipynb' contains the solution to the modelling challenge.
- The rest of the notebooks contain analyses and visualisations. They also contain some insights derived from the visualisations. 
- The src/ folder contains a config.py file and a helper.py file which contain helper functions that I used to modularise the code a bit, and to also clean up the notebooks.

## Analysis Approach
- I approached the analysis in a very ad-hoc way. I jumped into each of the datasets at a very high level first to get an understanding of the kind of information that is present in each of them. (This included looking at some simple statistics and plots.)
- I tried combining a few data sources together to understand how they interact, and whether any actionable insight could be pulled from there. 
- I tried to also think about the data from the business perspective (and from the perspective of a CM, but I didn't do a great job at that). 
- I pulled out numbers for some of the questions that I found interesting (best selling products, high traffic times of the year etc.)

## Modelling Approach

The approach I took here was to build a *boosted hybrid*. A simple linear regression model was be used to model the trend of the data. Then I trained an XGBoost on the residuals of the first model. 

## Some Insights
The notebooks contain many visualisations, as well as comments denoting insights. But here are a few of them. 

- Conversion Rate by Category

![Conversion Rate by Category](https://github.com/samarthum/rebuy_case_study/blob/main/images/conv_rate_by_cat.PNG "Conversion Rate by Category")

 Here we can see that Apple has the highest conversion rate amongst all the main product categories.
 
- Sales and Purchases across days of the week

![Sales vs.Day of Week](https://github.com/samarthum/rebuy_case_study/blob/main/images/sales_dayofweek.PNG)

![Purchases vs.Day of Week](https://github.com/samarthum/rebuy_case_study/blob/main/images/purchases_dayofweek.PNG)

We can observe that in both of these cases, the volume is much smaller during the weekends. 
Also, for sales, the volume is quite high on Mondays. We don't see this pattern in purchases.

