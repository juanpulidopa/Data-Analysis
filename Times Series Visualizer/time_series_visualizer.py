#Juan Pablo Pulido Angel

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df=pd.read_csv("fcc-forum-pageviews.csv",parse_dates=True,index_col="date")

# Clean data
#Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
df = df[(df["value"]>= df["value"].quantile(0.025)) & (df["value"]<= df["value"].quantile(0.975))]

#Create a draw_line_plot function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png". The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019. The label on the x axis should be Date and the label on the y axis should be Page Views.
def draw_line_plot():
    # Draw line plot
    fig, ax =plt.subplots(figsize=(12,6))
    ax.plot(df.index, df["value"], "r", linewidth=1)

    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

#Create a draw_bar_plot function that draws a bar chart similar to "examples/Figure_2.png". It should show average daily page views for each month grouped by year. The legend should show month labels and have a title of Months. On the chart, the label on the x axis should be Years and the label on the y axis should be Average Page Views.
#Create a draw_box_plot function that uses Seaborn to draw two adjacent box plots similar to "examples/Figure_3.png". These box plots should show how the values are distributed within a given year or month and how it compares over time. The title of the first chart should be Year-wise Box Plot (Trend) and the title of the second chart should be Month-wise Box Plot (Seasonality). Make sure the month labels on bottom start at Jan and the x and y axis are labeled correctly. The boilerplate includes commands to prepare the data.
def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df["month"]=df.index.month
    df["year"]=df.index.year
    df_bar=df.groupby(["year", "month"])["value"].mean()
    df_bar=df_bar.unstack()


    # Draw bar plot

    fig=df_bar.plot.bar(legend=True, figsize=(8,6), ylabel="Average Page Views", xlabel="Years").figure
    plt.legend(["January", "February", "March", "April", "May", "June", "July", "August","September", "October", "November", "December"])

    plt.xticks(fontsize=7)
    plt.yticks(fontsize=10)


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (16, 8))
    sns.boxplot(data = df_box, ax = ax1, x = "year", y = "value")
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")

                   
    sns.boxplot(data = df_box, ax = ax2, x = "month", y = "value",order=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

