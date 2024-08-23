import pandas as pd
import matplotlib.pyplot as plt

# Load dataset 
df = pd.read_csv('LakeCounty_Health_2397514566901885190.csv')


states = df['NAME']
obesity_percentage = df['Obesity']

# Plotting
plt.figure(figsize=(20, 15))  
plt.bar(states, obesity_percentage, color='blue')  
plt.xlabel('NAME')
plt.ylabel('Obesity')
plt.title('Obesity Percentage by State in the U.S.')
plt.xticks(rotation=90)  
plt.tight_layout()  
plt.show()
