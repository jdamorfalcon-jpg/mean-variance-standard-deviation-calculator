import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Import the data from medical_examination.csv and assign it to the df variable.
print(80*"-")
url = "https://raw.githubusercontent.com/freeCodeCamp/boilerplate-medical-data-visualizer/main/medical_examination.csv"
df = pd.read_csv(url)
df.to_csv("medical_examination.csv", index=False)
print("1. medical_examination.csv loaded into dataframe")
print(80*"-")


# 2. Add an overweight column to the data. To determine if a person is overweight,
# first calculate their BMI by dividing their weight in kilograms by the square
# of their height in meters. If that value is > 25 then the person is overweight.
# Use the value 0 for NOT overweight and the value 1 for overweight.
df["BMI"] = df["weight"] / (df["height"]/100)**2
df["overweight"] = 0
df.loc[df["BMI"] > 25, "overweight"] = 1
print('2. "overweight" column added to dataframe')
print(80*"-")

#3. Normalize data by making 0 always good and 1 always bad. If the value of
# cholesterol or gluc is 1, set the value to 0. If the value is more than 1,
# set the value to 1.
df.loc[df["cholesterol"] == 1, "cholesterol"] = 0
df.loc[df["gluc"] == 1, "gluc"] = 0
df.loc[df["cholesterol"] > 1, "cholesterol"] = 1
df.loc[df["gluc"] > 1, "gluc"] = 1
print('3. "cholesterol" and "gluc"columns added are normalized')
print(80*"-")

#Draw the Categorical Plot in the draw_cat_plot function
def draw_cat_plot():
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"]
    )

    df_cat = df_cat.groupby(["cardio", "variable", "value"]).size().reset_index(name="total")

    fig = sns.catplot(
        data=df_cat,
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        kind="bar"
    )

    return fig

fig = draw_cat_plot()
plt.show()
print("Catplot done")
print(80*"-")
def draw_heat_map():
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"]) &
        (df["height"] >= df["height"].quantile(0.025)) &
        (df["height"] <= df["height"].quantile(0.975)) &
        (df["weight"] >= df["weight"].quantile(0.025)) &
        (df["weight"] <= df["weight"].quantile(0.975))
    ]

    corr = df_heat.corr()

    mask = np.triu(np.ones_like(corr, dtype=bool))

    fig, ax = plt.subplots(figsize=(10, 8))

    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5}
    )

    return fig
new_fig = draw_heat_map()
plt.show()
