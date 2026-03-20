import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


def load_data():
    url = "https://raw.githubusercontent.com/freeCodeCamp/boilerplate-page-view-time-series-visualizer/master/fcc-forum-pageviews.csv"

    df = pd.read_csv(url, parse_dates=["date"], index_col="date")

    lower = df["value"].quantile(0.025)
    upper = df["value"].quantile(0.975)

    df = df[(df["value"] >= lower) & (df["value"] <= upper)]

    return df

df = load_data()


def draw_line_plot(df):
    plt.figure()
    plt.plot(df.index, df["value"])

    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")

    plt.savefig("line_plot.png")
    plt.show()

draw_line_plot(df)


import matplotlib.pyplot as plt

def draw_bar_plot(df):
    df_bar = df.copy()

    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month

    df_bar = df_bar.groupby(["year", "month"])["value"].mean().unstack()

    fig = df_bar.plot(kind="bar")

    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months")

    plt.savefig("bar_plot.png")
    plt.show()

draw_bar_plot(df)

import seaborn as sns
import matplotlib.pyplot as plt


def draw_box_plot(df):
    df_box = df.copy()

    df_box["year"] = df_box.index.year
    df_box["month"] = df_box.index.month

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    sns.boxplot(x="year", y="value", data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    sns.boxplot(x="month", y="value", data=df_box, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    plt.savefig("box_plot.png")
    plt.show()

draw_box_plot(df)
