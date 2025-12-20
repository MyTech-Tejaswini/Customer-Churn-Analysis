.figure(figsize=(9,4))
ax = sns.barplot(x='PaymentMethod', y='Churn_num', data=df)
plt.xticks(rotation=30)
plt.title('Churn Rate by Payment Method', fontsize=14)
plt.xlabel('Payment Method')
plt.ylabel('Churn Rate')

for p in ax.patches:
    ax.annotate(f'{p.get_height()*100:.1f}%',
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha = 'center', va = 'bottom')
    
plt.grid(axis='y', linestyle='--', alpha = 0.5)
plt.show()