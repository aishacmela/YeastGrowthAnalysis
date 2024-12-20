import pandas as pd
import numpy as np

#define parameters
time_points = np.linspace(0, 10, 11) #
temperatures = [25, 30, 35 ]
pH_levels = [5.0, 6.0, 7.0]
glucose_levels = [1.0, 2.0, 5.0]
replicates = 3


def logistic_growth(t, K, r, OD0):
   return K / (1 + ((K - OD0) / OD0) * np.exp(-r * t))

#generating data
data = []

for temp in temperatures:
   for pH in pH_levels:
      for glucose in glucose_levels:
         for replicate in range(1, replicates + 1):
            #Randomizes key growth parameters for each condition
            K = np.random.uniform(1.8, 2.2)
            r = np.random.uniform(0.6, 0.9)
            OD0 = 0.1
            #Calculates the yeast growth for all time points using the logistic growth model.
            growth_data = logistic_growth(time_points, K, r, OD0)
            #Adds random noise to simulate real-world experimental variability with mean = 0 amd standard diviation = 0.5
            growth_data += np.random.normal(0, 0.05, size=len(growth_data))

            #storing data
            for t, OD in zip(time_points, growth_data):
               data.append({
                  'Time (hrs)' : t,
                  'OD600' : max(0, OD),
                  'Temperature (°C)' : temp,
                  'pH' : pH,
                  'Glucose (%)' : glucose,
                   'Replicate' : replicate
               })

#convert to data frames 
yeast_growth_data = pd.DataFrame(data)

#save to CSV file
yeast_growth_data.to_csv('yeast_growth_template.csv', index=False)

#display sample data
print(yeast_growth_data.head())
