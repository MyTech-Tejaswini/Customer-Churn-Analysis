import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv(r"C:/Users/tejas/OneDrive/Desktop/Customer-Churn-Analysis/data/Telco-Customer-Churn.csv")

# Check data
print(df.head())
print(df.shape)

# Quick Validation(Churn %)
print(df['Churn'].value_counts())
print(df['Churn'].value_counts(normalize=True) * 100)

df['Churn_num'] = df['Churn'].map({'Yes':1, 'No':0})

## How many customers churn vs stay
# churn count plot

# plt.figure(figsize=(6,4))
# sns.countplot(x='Churn', data=df)
# plt.title('Customer Churn Distribution')
# plt.xlabel('Churn Status')
# plt.ylabel('Number of Customers')
# plt.grid(axis='y', linestyle='--', alpha = 0.5)
# plt.savefig("plots/churn_by_distribution.png", bbox_inches='tight')
# plt.show()

## Churn by Contract type

# plt.figure(figsize=(7,4))
# ax = sns.barplot(x='Contract', y='Churn_num', data=df)
# plt.title('Churn Rate by Contract Type', fontsize = 14)
# plt.ylabel('Churn Rate')
# plt.xlabel('Contract Type')

# # Add percentage labels
# for p in ax.patches:
#     ax.annotate(f'{p.get_height()*100:.1f}%',
#                 (p.get_x() + p.get_width() / 2., p.get_height()),
#                 ha = 'center', va = 'bottom')

# plt.grid(axis='y', linestyle='--', alpha = 0.5)
# plt.savefig("plots/churn_by_contract.png", bbox_inches='tight')
# plt.show()

## Churn By Payment Method

# plt.figure(figsize=(8,5))
# ax = sns.barplot(x='PaymentMethod', y='Churn_num', data=df)
# plt.xticks(rotation=45, ha='right')
# plt.title('Churn Rate by Payment Method', fontsize=14)
# plt.xlabel('Payment Method')
# plt.ylabel('Churn Rate')

# for p in ax.patches:
#     ax.annotate(f'{p.get_height()*100:.1f}%',
#                 (p.get_x() + p.get_width() / 2., p.get_height()),
#                 ha = 'center', va = 'bottom')
    
# plt.grid(axis='y', linestyle='--', alpha = 0.5)
# plt.tight_layout()
# plt.savefig("plots/churn_by_payment.png", bbox_inches='tight')
# plt.show()

# # Churn Rate by Tenure Group

# def tenure_group(tenure):
#     if tenure <= 12:
#         return '0-12 months'
#     elif tenure <= 24:
#         return '13-24 months'
#     elif tenure <= 48:
#         return '25-48 months'
#     else:
#         return '49+ months'
    
# df['tenure_group'] = df['tenure'].apply(tenure_group)

# tenure_df = (
#     df.groupby('tenure_group')['Churn_num']
#         .mean()
#         .reset_index()
# )
# plt.figure(figsize=(8,5))
# plt.bar(tenure_df['tenure_group'], tenure_df['Churn_num'])
# plt.title('Churn Rate by Tenure Group')
# plt.xlabel('Tenure Group')
# plt.ylabel('Churn Rate')
# plt.xticks(rotation = 0)
# plt.tight_layout()
# plt.grid(axis='y', linestyle='--', alpha = 0.5)
# plt.savefig("plots/churn_by_tenure.png", bbox_inches='tight')
# plt.show()