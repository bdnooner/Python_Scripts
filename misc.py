l\\import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'~/Documents/DeVry/Courses/Fall_2019/CEIS110/JupyterModules/Module_6/fbiData.csv')

year = data["Year"]
v_crime = data["ViolentCrime"]
p_crime = data["PropertyCrime"]
murder = data["Murder"]

plt.plot(year, v_crime)
plt.plot(year, p_crime)
plt.plot(year, murder)
plt.legend(["Violent", "Property", "Murder"], loc = "best")
plt.show()
