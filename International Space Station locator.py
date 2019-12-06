from urllib.request import urlopen
import json

url = "http://api.open-notify.org/iss-now.json"
jsonurl = urlopen(url)
info = json.loads(jsonurl.read())

print(info)

longitude = info['iss_position']['longitude']
latitude = info['iss_position']['latitude']

print(longitude)
print(latitude)

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

m = Basemap(projection='robin',lon_0=0,resolution='c')

m.drawcoastlines()
m.fillcontinents(color='darkgreen',lake_color='aqua')
m.drawparallels(np.arange(-90.,120.,30.))
m.drawmeridians(np.arange(0.,360.,60.))
m.drawmapboundary(fill_color='aqua')

x,y = m(longitude, latitude)
m.plot(x, y, 'ro', markersize=12)

plt.show()
