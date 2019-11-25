# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)

# Project 2 - Ames Housing Data Analysis

### Problem Statement

Having recently joined a property consultancy company in Ames, Iowa, I’ve been tasked with conducting a statistical analysis using the Ames Housing Dataset in order to determine which are the prominent factors that determines an Ames property's selling price. Through this analysis, I hope to gain better insights so as to make recommendations and give advices to homeowners on how to potentially increase a property's value.

---

## Executive Summary

### Contents:

- [Exploratory Data Analysis (EDA)](#EDA)
- [Data Dictionary](#Data-Dictionary)
- [Modelling Results](#Modelling-Results)
- [Interpretation of Results](#Interpretation-of-Results)
- [Business Recommendations](#Business-Recommendations)
- [Model Evaluation](#Model-Evaluation)
- [Sources](#Sources)

---

### EDA

1) **Numerical data** was cleansed and explored first. Amongst the numerical variables, 5 of them were dropped as they have at least close to, or more than, 50% null values. 2 other outliers, as advised by the [data documentation](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt), were dropped as well. Lastly, 2 additional features/variables have been engineered, both of which prove to be relevant in further statistical analysis (included in the data dictionary below).

Dropping a further 12 variables due to their extremely weak correlation with the target variable 'saleprice', I have shortened the list of numerical variables to the ones represented below in a correlation heatmap:

![Image of Cleaned Correlation Heatmap](http://localhost:8888/view/GA-coursework/Projects/Project%202/images/num_cleaned_corr.png)

2) Cleaning of the **categorical data** was tedious and non-trivial as there are many categorical variables and within them, many levels (e.g. there are close to 30 kinds of neighborhoods under the 'Neighborhood' variable). Ultimately, I chose to drop categorical variables that are correlated with each other (and would contribute to multicollinearity if included inside the model). And for the remaining, I dummied all of them but only kept those where they had a 'majority' level (e.g. in the 'Neighborhood' variable example, if Neighborhood A appeared 90% in the dataset whereas Neighborhoods B/C/D/etc account for only the other remaining 10%, I would only keep the dummy for Neighbourhood A and drop the others).

---

Finally, with further tuning of the model by dropping variables with low significance as well as variables correlated with each other, I arrive at the final list of significant variables below:

### Data Dictionary:

|Variable Name|Type|Description|
|---|---|---|
|**lot_frontage**|*continuous, float*|Linear feet of street connected to property|
|**lot_area**|*continuous, float*|Lot size in square feet|
|**overall_qual**|*continuous, float*|Rates the overall material and finish of the house|
|**mas_vnr_area**|*continuous, float*|Masonry veneer area in square feet|
|**bsmtfin_sf_1**|*continuous, float*|Basement Type 1 finished square feet|
|**full_bath**|*continuous, float*|Full bathrooms above grade|
|**totrms_abvgrd**|*continuous, float*|Total rooms above grade (does not include bathrooms)|
|**fireplaces**|*continuous, float*|Number of fireplaces|
|**garage_cars**|*continuous, float*|Size of garage in car capacity|
|**prop_age**|*continuous, float*|***Engineered Feature:*** Age of property when sold (Year when it was sold, minus year when it was built)|
|**prop_remodel_duration**|*continuous, float*|***Engineered Feature:*** Age of remodelled property when it was sold (Year when it was sold, minus year when it was remodelled)|
|**prop_remodel_dummy**|*dummy*|***Engineered Feature:*** Value = 1 if property was remodelled before, 0 otherwise|
|**land_contour_Lvl**|*dummy*|Flatness of the property: value =1 if Near Flat/Level, 0 otherwise|
|**utilities_AllPub**|*dummy*|Type of utilities available: value = 1 if all public utilities (E, G, W & S) available, 0 otherwise|
|**condition_1_Norm**|*dummy*|Proximity to various conditions: value =1 if normal, 0 otherwise|
|**roof_style_Gable**|*dummy*|Type of roof: value = 1 if gable, 0 otherwise|
|**functional_Typ**|*dummy*|Home functionality: value = 1 if typical functionality, 0 otherwise|
|**garage_qual_TA**|*dummy*|Garage quality: value = 1 if typical/average, 0 otherwise|

---

### Modelling Results

The following table are the results from running a Lasso regression model on the above variables, Lasso being chosen as it gave the highest R-squared score. Table has been sorted in descending manner via coefficient value:

|Variable Name|Coefficient|
|---|---|
|**overall_qual**|34191.069010|
|**bsmtfin_sf_1**|15148.416807|
|**totrms_abvgrd**|13407.808684|
|**lot_area**|11691.507625|
|**mas_vnr_area**|9134.859979|
|**garage_cars**|8233.437605|
|**functional_Typ**|7498.383036|
|**condition_1_Norm**|5310.069757|
|**prop_remodel_dummy**|5264.274219|
|**fireplaces**|4541.422240|
|**full_bath**|3502.246067|
|**lot_frontage**|1327.540567|
|**utilities_AllPub**|0.000000|
|**prop_age**|-4938.547390|
|**prop_remodel_duration**|-7031.363628|
|**roof_style_Gable**|-7839.014285|
|**land_contour_Lvl**|-12200.625091|
|**garage_qual_TA**|-14080.773727|

---

### Interpretation of Results:

Overall quality and finish of the house seems to matter the most in terms of determining a property's selling price - not at all surprising given that any potential buyer evaluate the house quality AS A WHOLE in their purchasing decision.

Many of the other variables that have a positive effect on sale price are typically linked to the perception of "space" - such as Lot Area, Masonry Veneer Area, Basement Square Feet - as well as "luxurious" features such as Full bathrooms, Number of Fireplaces, Size of Garage, Total Rooms Above Ground.

If a property has been remodelled before, there is a positive effect on its selling price. However, there is also a significant negative effect on selling price that outweighs the positive effect of a property remodel; for every year that the property does not get sold off after it is remodelled, there is a -7839 reduction in selling price, which exceeds the +5264 increase in selling price.

Conversely, having a typical/average quality of garage seems to hurt selling price of a property the most. Having a property situated on a flat/level ground also negatively affects property selling prices, as well as having Gable-styled roofs. Also, older, more-aged properties are likely to fetch a lower price than newer ones.

In terms of damage limitation, homeowners can also consider raising the quality of their garages to at least above-average in order to mitigate the losses in sale prices stemming from just an "average" quality of garage.

### Business Recommendations:

For existing homeowners, I would recommend them to focus on certain aspects of their house to target for renovation. This model's results show that potential homebuyers in Ames value the concept of "luxury" and "space", so homeowners looking to sell can spruce up their homes by making their homes look more luxurious and spacious, whether it be through the above-mentioned features such as adding full baths, more fireplaces, or increasing their lot area or masonry veneer area. Of course, feasibility of such enhancements is another issue. Also, the costs of making such enhancements should definitely be less than the potential gains of these enhancements (by looking at the coefficients of the variables).

That being said, if homeowners do proceed with such enhancements and major renovations ensue, it is recommended to not delay the sale of the property too long, post-renovation, as this model indicates that there is a net decrease in property selling price the longer it takes to sell the house.

### Model Evaluation:

Suffice to say, this model's isn't perfect and has a number of flaws, one of which is the absence of any 'neighborhood/district' kind of variable. It makes intuitive sense that properties at certain places of a city, perhaps near the CBD or affluent shopping districts, would fetch higher prices than properties in the outskirts of the city. Likewise, another 2 variables that would intuitively affect sale price were dropped - Building Type (type of dwelling, such as single-family detached or duplex), and House Style (style of dwelling, such as one-storey or two-storey). Perhaps the method of elimination of categorical variables can be further improved on.

Any transactional marketplace is dynamic and consists of 2 parties - the buyer (demand) and the seller (supply). This model focuses only on the supply-side of the market - types of houses, features of houses, neighbourhoods, etc. The demand side has to be explored as well in order for the model to be more holistic. For example, if a particular state or city is more open to foreign expatriates, would there be even higher property prices being traded? This ties in with sensitive sociopolitical factors as well - would the demographics of the state affect property prices as well? "Ghettoization" is a real problem facing many developed countries nowadays, and cities/states with high social inequality need to take such factors into account. In the context of the business problem, perhaps, if a particular property is located within the vicnities of a ghetto, no amount of feature enhancements can help increase its selling price (or perhaps, only to very insignificant extent that isn't worth the initial investment). Thus, any advice given to such homeowners will be rendered moot.

As such, for this model to be reproducible or transferrable in the study of other cities/states' property selling prices, there has to be many more tweaks and improvements to be made.
 
---

### Sources:

- [Original Data Dictionary](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt)
- [External Research - Matthew Perkins: *Regression & Classification with Ames Housing Data*](https://www.perkinsml.me/ames-housing)
