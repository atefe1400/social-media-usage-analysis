import pandas as pd
import matplotlib.pyplot as plt
#Import libraries and upload CSV file
path=r"D:\python\my_code\survey_analysis\survey_data.csv"
df=pd.read_csv(path)
print(df.head())
#Reading the CSV file and initial data inspection
print(df.info())
print(df.describe(include='all'))
#Checking for missing values
print(df.isnull().sum())
#Averages and key statistics from numeric columns
print('Avrage satisfaction_level',df['satisfaction_level'].mean())
print('Avrage satisfaction_level',df['satisfaction_level'].max())
print('Avrage satisfaction_level',df['satisfaction_level'].min())
print('Avrage satisfaction_level',df['satisfaction_level'].median())
###
print('Avrage age',df['age'].mean())
print('Avrage age',df['age'].max())
print('Avrage age',df['age'].min())
print('Avrage age',df['age'].median())
###
print('Avrage daily_usage_minutes',df['daily_usage_minutes'].mean())
print('Avrage daily_usage_minutes',df['daily_usage_minutes'].max())
print('Avrage daily_usage_minutes',df['daily_usage_minutes'].min())
print('Avrage daily_usage_minutes',df['daily_usage_minutes'].median())

#Grouped Analysis
print(df.groupby('country')['satisfaction_level'].mean())
print(df.groupby('gender')['daily_usage_minutes'].mean())
print(df.groupby('education_level')['daily_usage_minutes'].mean())
df['uses_instagram'] = df['uses_instagram'].map({'Yes':1,'No':0})
print(df.groupby('country')['uses_instagram'].mean() *100)

#Bar Chart
instagram_by_country=df.groupby('country')['uses_instagram'].mean() *100
instagram_by_country.sort_values().plot(kind='barh',color='skyblue')

plt.title('instagram usage by country (%)')
plt.xlabel('usage percentage')
plt.ylabel('country')
plt.tight_layout()
plt.show()

#Pie Chart
youtube_usage = df['uses_youtube'].value_counts()
youtube_usage.plot(kind='pie',labels=['Yes','No'],autopct='%1.1f%%',colors=['lightgreen','orange'])

plt.title('YouTube Usage')
plt.ylabel('')
plt.tight_layout()
plt.show()

#scatter chart
plt.scatter(df['daily_usage_minutes'] ,df['satisfaction_level'],alpha=0.5,color='purple')
plt.title('Satisfaction vs. Daily Usage Time')
plt.xlabel('Daily Usage (Minutes)')
plt.ylabel('Satisfaction Level')
plt.tight_layout()
plt.show()