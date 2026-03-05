import matplotlib.pyplot as plt
import kagglehub
path = kagglehub.dataset_download("farnooshsoltani/wather-englich")
days = ['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri']
temps = [22, 25, 21, 23, 27, 24, 20]
plt.figure(figsize=(8, 5))
plt.plot(days, temps, marker='*', markersize=15, linestyle='-', color='darkred', linewidth=3)
plt.title('Weekly Temperature Variation') 
plt.xlabel('Days of the Week')          
plt.ylabel('Temperature (°C)')           
print("Path to dataset files:", path) 
plt.grid(True)
plt.show()