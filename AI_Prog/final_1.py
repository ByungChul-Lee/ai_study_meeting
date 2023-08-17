import numpy as np
import matplotlib.pyplot as plt
from urllib.request import urlretrieve

URL = 'http://go.gwu.edu/engcomp1data5?accessType=DOWNLOAD'
urlretrieve(URL, 'land_global_temperature_anomaly-1880-2016.csv')

fname = 'land_global_temperature_anomaly-1880-2016.csv'
year, temp_anomaly = np.loadtxt(fname, delimiter=',', skiprows=5, unpack=True)

yeartw = []
temptw = []
for i in range(len(year)):
    if int(year[i]) >= 1980 and int(year[i]) <= 2000 :
        yeartw.append(year[i])
        temptw.append(temp_anomaly[i])
        
ax1 = plt.subplot(2,1,1)
plt.plot(year, temp_anomaly, color='red', linestyle='solid', label='All')
plt.title("All Data")
plt.xlabel("year")
plt.ylabel("temp_anomaly")
plt.legend()

ax1 = plt.subplot(2,1,2)
plt.plot(yeartw, temptw, color='blue', linestyle='solid', label='20 year')
plt.title("1980-2000  Data")
plt.xlabel("year")
plt.ylabel("temp_anomaly")
plt.legend()

plt.tight_layout()
plt.show()

