import pandas as pd
df = pd.read_csv(
    'https://raw.githubusercontent.com/freeCodeCamp/boilerplate-demographic-data-analyzer/main/adult.data.csv'
)
#Questions
#How many people of each race are represented in this dataset? This should be a
#Pandas series with race names as the index labels. (race column)
print(80*"-")
print("Races represented in this dataset: ")
print(df.value_counts("race"))
print(80*"-")

#What is the average age of men?
ave_age_men = round(df[df["sex"]=="Male"]["age"].mean(),2)
print("Average age of men:", ave_age_men)
print(80*"-")

#What is the percentage of people who have a Bachelor's degree?
per_bach = round((df["education"]=="Bachelors").sum()/df.shape[0] * 100, 2)
print("Percentage of people who have a Bachelor's degree:", per_bach, "%")
print(80*"-")

#What percentage of people with advanced education (Bachelors, Masters, or Doctorate)
#make more than 50K?
A = df["education"] =="Bachelors"
B = df["education"] =="Doctorate"
C = df["education"] =="Masters"
D = df["salary"] == ">50K"
percent = round(((A | B | C) & D).sum()/(A | B | C).sum() * 100, 2)
print("Percentage of people with advanced education (Bachelors, Masters, or Doctorate)")
print("make more than 50K:", percent, "%")
print(80*"-")

#What percentage of people without advanced education make more than 50K?
new_percent = percent = round(((~A & ~B & ~C) & D).sum()/(~A & ~B & ~C).sum() * 100, 2)
print("Percentage of people without advanced education make more than 50K:", new_percent, "%")
print(80*"-")

#What is the minimum number of hours a person works per week?
min_hours = round(df["hours-per-week"].min(),2)
print("Minimum number of hours a person works per week:", min_hours, "hours")
print(80*"-")

#What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
number = ((df["hours-per-week"] == min_hours) & D).sum()
total = (df["hours-per-week"] == min_hours).sum()
print("Percentage of the people who work the minimum number of hours per week")
print("have a salary of more than 50K:", round(number/total*100,2), "%")
print(80*"-")

#What country has the highest percentage of people that earn >50K and what is that percentage?
perdf = round(df[D].value_counts("native-country")/df.value_counts("native-country")*100,2)
print("Country has the highest percentage of people that earn >50K:")
print(perdf[perdf==perdf.max()])
print(80*"-")

#Identify the most popular occupation for those who earn >50K in India."""
indiadf = df[D & (df["native-country"]=="India")]
popular  = indiadf["occupation"].value_counts().idxmax()
number_ = indiadf["occupation"].value_counts().max()
print("Most popular occupation for those who earn >50K in India:")
print(popular, "with", number_)
print(80*"-")
