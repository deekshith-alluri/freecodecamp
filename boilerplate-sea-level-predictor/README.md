# Sea Level Predictor

This is the boilerplate for the Sea Level Predictor project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/sea-level-predictor

> Since this is the last peoject in this Learning, thought to give it some extra shades.
The whole project relies on the funtion shown below; It takes few parameters such as a DataFrame to work with, the column to consider for the X values and another column for the Y values to the Graph and the last one is an int type that is expected to be shown based on the particularly given DataSet

```python

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


```