import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


# Create a func that generates a best fit for the data
def generate_best_fit_line(data_in_df,col_for_x,col_for_y,target_x):
    # y=mx+c; m=slope; c=y_intercept=value when x=0
    if max(data_in_df[col_for_x].values)<target_x:
        slope,y_intercept,r_value,p_value,stdErr=linregress(data_in_df[col_for_x],data_in_df[col_for_y])
        x_vals_original_data=data_in_df[col_for_x]
        line_original_data=y_intercept+(x_vals_original_data*slope)
        x_vals_extended=pd.Series(list(range(max(x_vals_original_data)+1,target_x+1)))
        line_extended_data=y_intercept+(x_vals_extended*slope)
        x_vals_all=pd.concat([x_vals_original_data,x_vals_extended],ignore_index=True)
        line_vals_all=pd.concat([line_original_data,line_extended_data],ignore_index=True)
        return x_vals_all,line_vals_all if len(x_vals_all)==len(line_vals_all) else None
    
    if max(data_in_df[col_for_x].values)>=target_x:
        slope,y_intercept,r_value,p_value,stdErr=linregress(data_in_df[col_for_x][:pd.Index(data_in_df[col_for_x]).get_loc(target_x)],data_in_df[col_for_y][:pd.Index(data_in_df[col_for_x]).get_loc(target_x)])
        x_vals_original_data=data_in_df[col_for_x][:pd.Index(data_in_df[col_for_x]).get_loc(target_x)]
        line_original_data=y_intercept+(x_vals_original_data*slope)
        return x_vals_original_data,line_original_data if len(x_vals_original_data)==len(line_original_data) else None


def draw_plot():
    # Read data from file
    df=pd.read_csv(filepath_or_buffer="./epa-sea-level.csv",delimiter=",")
    fig,axes=plt.subplots()


    # Create scatter plot
    axes.scatter(x=df.Year,y=df["CSIRO Adjusted Sea Level"],c="blue",label="Scattered data",s=20)

    # Create first line of best fit
    x1,y1=generate_best_fit_line(df,'Year','CSIRO Adjusted Sea Level', 2050)
    axes.plot(x1,y1,'-r',lw=2,label="consider the whole data")

    # Create second line of best fit
    x1,y1=generate_best_fit_line(df[df.Year>=2000],'Year','CSIRO Adjusted Sea Level', 2050)
    axes.plot(x1,y1,'--m',lw=2,label="consider the whole data")

    # Add labels and title
    axes.set(
        xlabel="Year",
        ylabel="Sea Level (inches)",
        title="Rise in Sea Level"
        )
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()