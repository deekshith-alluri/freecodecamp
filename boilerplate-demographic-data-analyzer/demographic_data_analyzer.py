import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("./adult.data.csv",delimiter=",",skip_blank_lines=True)

    #dropping duplicates and keeping the most latest one.
    # df= df.drop_duplicates(keep="last")

    df = df.replace("?",pd.NA)
    native_country= df['native-country'].ffill()
    df["native-country"] = native_country


    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    race_count.name = "Races and thier frequencies"

    # What is the average age of men?
    average_age_men = round(df.loc[df['sex']=="Male","age"].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df.loc[df['education']=="Bachelors","education"].count()/df.shape[0])*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[((df['education']=='Bachelors')|(df['education']=='Masters')|(df['education']=='Doctorate')) & (df['salary']=='>50K'),'salary'].count()
    lower_education = lower_education = df.loc[(~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K'),'salary'].count() 
    

    total_higher_edu = df.loc[(df['education']=='Bachelors')|(df['education']=='Masters')|(df['education']=='Doctorate'),'salary'].count()
    total_lower_edu = df.loc[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate']),'salary'].count()
    
    
    # percentage with salary >50K
    higher_education_rich = round((higher_education/total_higher_edu)*100,1)
    lower_education_rich = round((lower_education/total_lower_edu)*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[(df['hours-per-week']==min_work_hours) & (df['salary']==">50K"),"age"].count()

    # Total number of people who work min hours
    total_min_workers = df[df['hours-per-week'] == min_work_hours].shape[0]

    rich_percentage = (num_min_workers/total_min_workers)*100

    # What country has the highest percentage of people that earn >50K?
    country_filter_salary = df.loc[df['salary']==">50K","native-country"].value_counts()
    country_total = df["native-country"].value_counts()
    highest_earning_country = (country_filter_salary/country_total).idxmax()
    highest_earning_country_percentage =  round(max(country_filter_salary/country_total)*100,1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[(df['salary']==">50K")&(df["native-country"]=="India"),'occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
