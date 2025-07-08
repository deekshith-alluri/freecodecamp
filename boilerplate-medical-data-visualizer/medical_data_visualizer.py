import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("./medical_examination.csv",
                 delimiter=",",
                 skip_blank_lines=True,
                )
# 2
bmi = df['weight']/((df['height']/100)**2)
df['overweight'] = (bmi>25).astype(int)

# 3
df["cholesterol"] = df["cholesterol"].apply(lambda x: 0 if x<=1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x<=1 else 1)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df,
                     id_vars=["cardio"],
                     value_vars=["cholesterol","gluc","smoke","alco","active","overweight"]
                     )


    # 6
    df_cat = df_cat.groupby(["cardio","variable"]).value_counts().reset_index(name="total")
    
    

    # 7
    plotting = sns.catplot(data=df_cat,
                       x=df_cat.variable,
                       y=df_cat.total,
                       col=df_cat.cardio,
                       kind="bar",
                       hue=df_cat.value
                       )


    # 8
    fig = plotting.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df.ap_lo<=df.ap_hi)&
                 (df.height>=df.height.quantile(0.025))&
                 (df.height<=df.height.quantile(0.975))&
                 (df.weight>=df.weight.quantile(0.025))&
                 (df.weight<=df.weight.quantile(.975))
                 ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr,dtype=bool))

    # 14
    fig, ax = plt.subplots()

    # 15
    sns.heatmap(data=corr,
                annot=True,
                fmt='.1f',
                mask=mask,
                square=False,
                center=0,
                vmax=0.30,
                linewidth=5,
                annot_kws={'fontsize':6},
                cbar_kws={'shrink':.7}
                )


    # 16
    fig.savefig('heatmap.png')
    return fig
