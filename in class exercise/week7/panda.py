import pandas as pd 
import matplotlib.pyplot as plt

titanic = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/carData/TitanicSurvival.csv')
#pd.options.display.max_rows = 2

#age of histogram

plt.hist(titanic.age)
plt.axvline(titanic.age.mean(),color='k', linestyle='dashed', linewidth=1)
plt.title('Ages of Passengers on TItanic')
plt.ylabel('Count')
plt.xlabel('Age(in Years)')
plt.show()

