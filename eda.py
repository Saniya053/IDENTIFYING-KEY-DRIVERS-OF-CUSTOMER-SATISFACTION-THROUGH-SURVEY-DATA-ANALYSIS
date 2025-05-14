import seaborn as sns

import matplotlib.pyplot as plt


sns.histplot(df['satisfaction_score'])

plt.show()


sns.countplot(x='product_quality', data=df)

plt.show()


sns.boxplot(x='product_quality', y='satisfaction_score', data=df)

plt.show()


sns.scatterplot(x='response_time', y='satisfaction_score', data=df)

plt.show()


sns.heatmap(df.corr(), annot=True, cmap='coolwarm')

plt.show()