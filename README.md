# Car-Sale-Estimator.
Car sale price estimator. 

server link- https://car-sales-estimate.herokuapp.com

Before running on your local machine make sure you run  ```pip install requirements.txt```
once installtion is done the navigate to the folder where you have downladed the files, in the same location open cmd or terminal and type ```streamlit run gui.py```
this will run the program in browser.

# About the project:
This project is all about predicting sales price of a car. The dataset used is downloaded from kaggle.
It takes parameters like:
1) price at wich you bought
2) year in which you bought
3) km driven 
4) owner
5) are a dealer or individual
6) fuel type
7) transmission type

based on these parameters it give an output of estimated sale price.

NOTE (the black background of screen shot is due to darkmode plugin for you it will be white.)

Screen shot - 1

![](Screen%20shots/sal1.png)

Screen shot - 2

![](Screen%20shots/sal2.png)

The model is deployed on heroku and the gui is made with streamlit.

# Libraries used are

1) sklearn

2) pandas

3) numpy

4) matplotlib

5) seaborn




