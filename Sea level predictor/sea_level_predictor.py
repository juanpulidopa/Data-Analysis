#Juan Pablo Pulido Angel

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv("epa-sea-level.csv")
    #Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.
    x=df["Year"]
    y=df["CSIRO Adjusted Sea Level"]

    # Create scatter plot
    fig, ax= plt.subplots(figsize=(12,6))
    plt.scatter(x,y)


    # Create first line of best fit
    #Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
    reg= linregress(x,y)
    x_pred=pd.Series([i for i in range(1880,2051)])
    y_pred=reg.slope*x_pred+reg.intercept
    plt.plot(x_pred, y_pred, "r")


    # Create second line of best fit
    #Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
    df_second=df.loc[df["Year"]>=2000]
    x2=df_second["Year"]
    y2=df_second["CSIRO Adjusted Sea Level"]
    reg2= linregress(x2,y2)
    x_pred2=pd.Series([i for i in range(2000,2051)])
    y_pred2=reg2.slope*x_pred2+reg2.intercept
    plt.plot(x_pred2, y_pred2, "violet")



    # Add labels and title
    #The x label should be Year, the y label should be Sea Level (inches), and the title should be Rise in Sea Level.
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()