# car-sale-estimator
Car sale price estimator. 

Before running on your local machine make sure you run  ```pip install requirements.txt```
once installtion is done the navigate to the folder where you have downladed the files, in the same location open cmd or terminal and type ```streamlit run gui.py```
this will run the program in browser.

About the project:
This project is all about predicting sales price of a car. The dataset used is downloaded from kaggle.
It takes parameters like:
1) price at wich you bought
2) year in which you bought
3) km driven 
4) owner
5) are a dealer or individual
6) fuel type
7) transmission type

based on this parameters it give an outup of estimated sale price.

Screen shot - 1

![](Screen%20shots/sal1.png)

Screen shot - 2

![](Screen%20shots/sal2.png)

The model is deployed on heroku.
The gui is made with streamlit.

