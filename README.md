# Classify-Anime
A random forest classifier classifies whether the anime is good or not based on 6 features. The model has been saved and passed to a Flask model then deployed as a web page using HTML.

# Detailed
For the dataset, I made use of what was available since it wasn't all that useful. I noticed that the "scores" column contained a dictionary for each entry instead of a single data entry. I dropped all other columns and created new columns with the keys of the dictionaries that were entries for the "scores" column. This enabled me to have clean data to work with. The new dataset consisted of 6 features and a label feature that classifies whether this anime is good ( label = 1 ) or bad ( label = 0 ) based on these six features. 
The features are "Story"	"Animation"	"Sound"	"Character"	"Enjoyment" and "overall" score

# Random Forest Classifier
after the data's been cleaned and visualized using Seaborn and Matplotlib, it was split and used to train a random forest classifier with tuned hyperparameters using the "hyperopt" optimization method. The model has been trained, validated, and tested. The overall accuracy turned out to be about 95%.

# Flask and HTML
After building the model, it was saved using the "pickle" library, and a Flask model was built where it took the entries of the user from an HTML webpage and used the random forest classifier to predict whether the anime was good or not good based on the different features entered.

<img width="710" alt="2023-06-23" src="https://github.com/Sapphire9-7/Classify-Anime/assets/93841475/34991943-da3b-4c1e-81c0-a92b9a5ef835">

# Output
If the prediction of the random forest classifier turned out to be 1 meaning the anime is good (based on the values entered by the user), the HTML file would pass the "this anime is good"  message on the screen, otherwise, it'll pass "This anime is not good"


