#Question 1
# we lost  37 rows  in the inner join
import pandas as pd
import os


researchers = pd.read_csv('./Data/researchers.csv')
publications = pd.read_json('./Data/publications.json')
funding = pd.read_excel('./Data/funding.xlsx')


inner_df = researchers.merge(publications, on='researcher_id', how='inner'
).merge(funding, on='researcher_id', how='inner')
print("inner join:", len(inner_df))

left_df = researchers.merge(publications, on='researcher_id', how='left'
).merge(funding, on='researcher_id', how='left')
print("left join:", len(left_df))

#Qustion 2
def clean_funding(df):
    df = df.copy()
    
    df['amount_cad'] = pd.to_numeric(df['amount_cad'], errors='coerce')
    
    df['amount_cad'] = df['amount_cad'].fillna( df['amount_cad'].median())
    
    df['amount_cad'] = df['amount_cad'].clip(lower=0)
    
    return df


funding = clean_funding(funding)

print(funding.head(10))

#Question 3

researcher_top = researchers.groupby('researcher_id')['publications_count'].sum().idxmax()
print("Top Researcher :", researcher_top)


funding_high =funding.groupby('project_title')['amount_cad'].sum().idxmax()
print("Highest Funding :",funding_high)

oldest_researcher =researchers[researchers['is_active'] == True].sort_values('joined_year')['researcher_id'].head(1)
print("The Oldest :",oldest_researcher)

#Question 4
merged_file = researchers.merge(publications, on='researcher_id', how='left') \
                       .merge(funding, on='researcher_id', how='left')

os.makedirs("output")

merged_file.to_csv("output/clean_research_data.csv", index=False)


