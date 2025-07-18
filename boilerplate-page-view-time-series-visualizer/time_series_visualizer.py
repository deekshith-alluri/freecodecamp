import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(filepath_or_buffer="./fcc-forum-pageviews.csv",
                 parse_dates=True,
                 index_col=0)

# Clean data
df = df[(df.value<df.value.quantile(0.975))&(df.value>df.value.quantile(0.025))]

def draw_line_plot():
    # Draw line plot
    fig,ax = plt.subplots()
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    ax.plot(df)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot            
    df_bar=df.groupby([df.index.year,df.index.month]).mean()
    bar_width=.05
    years_list=df.index.year.unique()
    months_list=df.index.month.unique()

    fig,axes=plt.subplots()

    bar1=range(len(years_list))
    for month in zip(sorted(months_list),["January","February","March","April","May","June","July","August","September","October","November","December"]):
        dump_in=[]
        for year in sorted(years_list):
            if (year,month[0]) in df_bar.index:
                dump_in.append(df_bar.loc[year].loc[month[0]].value)
            else:
                dump_in.append(0)
        axes.bar(bar1,dump_in,bar_width,label=month[1])
        bar1=[i+bar_width for i in bar1]

    axes.legend(title="Months")
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.xticks([x+(5.5*bar_width) for x in range(len(years_list))],years_list)

    # Draw bar plot
    fig=fig

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
    fig,axes=plt.subplots(1,2, figsize=(12,5))
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set(xlabel="Year",
                ylabel="Page Views")
    sns.boxplot(data=df_box,x=df_box.year,y=df_box.value,ax=axes[0])

    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set(xlabel="Month",
                ylabel="Page Views")
    month_order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    sns.boxplot(data=df_box,x=df_box.month,y=df_box.value,ax=axes[1],order=month_order)

    # print(df_box.head())
    plt.tight_layout(pad=2.5)

    fig=fig

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
