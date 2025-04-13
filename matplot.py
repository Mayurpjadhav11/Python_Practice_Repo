import matplotlib.pyplot as plt
import numpy
import seaborn as sns
import pandas as pd

age1 = [1,2,3,4,5,6,7,8,9]

age2 = [4,5,6,7,8,9,5,6,7]

df = pd.DataFrame({
    'age1': age1,
    'age2': age2
})
corr = df.corr()
sns.heatmap(corr, annot=True, cmap = 'coolwarm')
plt.show()