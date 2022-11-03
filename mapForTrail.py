from matplotlib import pyplot as plt
import plotly.graph_objects as go
import SimulationParameters
import pandas as pd
import plotly.express as px
df = px.data.gapminder()
import numpy as np

# we will need the fig object later
#fig = plt.figure






#fig.update_traces

#df = pd.read_csv('InterestingGPSCoordinates.csv')
#site_lat = df.lat
#site_lon = df.lon
#locations_name = df.text


#fig = go.Figure()


#fig.add_trace(go.Scattermapbox(
 #       lat=site_lat,
  #      lon=site_lon,
   #     mode='markers',
    #    marker=go.scattermapbox.Marker(
     #       size=8,
      #      color='rgb(242, 177, 172)',
       #     opacity=0.7
       # ),
       # hoverinfo='none'
   # ))

#fig = go.Figure(go.Scattermapbox(
 #   mode = "markers+text+lines",
  #  lon = [-19.51, -19.4, -19.56], lat = [63.53, 63.1, 63.1],
   # marker = {'size': 100, 'symbol': ["bus", "harbor", "airport"]},
    #text = ["Bus", "Harbor", "airport"],textposition = "bottom right"))

   #  mode = "markers",
   # lon = [-73.605], lat = [45.51],
    # marker = {'size': 20, 'color': ["cyan"]}
    
    ## Create path figure
    # Generate curve data
    
t = np.linspace(-1, 1, 100)
x = t + t ** 2
y = t - t ** 2
xm = np.min(x) - 1.5
xM = np.max(x) + 1.5
ym = np.min(y) - 1.5
yM = np.max(y) + 1.5
N = 50
s = np.linspace(-1, 1, N)
xx = s + s ** 2
yy = s - s ** 2



# defined search area
#fig = go.Figure(go.Scattermapbox(
   # title_text = 'London to NYC Great Circle',
 #   mode = "markers+lines",
  #  lon = [SimulationParameters.Eborderline, -19.7], lat = [SimulationParameters.Nborderline,63.61],
   # marker = {'size': 20, 'color': ["cyan"]}
    # lon2 = [SimulationParameters.Eborderline], lat2 = [SimulationParameters.Sborderline],
    # marker2 = {'size': 5, 'color': ["cyan"]},
    # lon3 = [SimulationParameters.Wborderline], lat3 = [SimulationParameters.Nborderline],
    # marker3 = {'size': 5, 'color': ["cyan"]},
    # lon4 = [SimulationParameters.Wborderline], lat4 = [SimulationParameters.Nborderline],
    # marker4 = {'size': 5, 'color': ["cyan"]}
    #))




fig = go.Figure(go.Scattermapbox(
    mode = "markers+lines",
    lon=[-19.31731 ,-19.31722 ,-19.35614,-19.35846,-19.36822,-19.39307,-19.40086,-19.43458, -19.46,-19.46638, -19.47829,-19.49375, -19.38731, -19.31731, -19.31731, -19.31731, -19.31731, -19.51731, -19.531, -19.590, -19.700, -19.750, -19.800, -19.850], 
    lat = [64.40748,64.41769,64.42856,64.42896,64.43110, 64.43137, 64.42832, 64.42063, 64.40855, 64.39119, 64.40748, 64.40300, 64.40000, 63.9232, 63.900, 63.890, 63.820, 63.740, 63.660, 63.620, 63.580, 63.565, 63.558, 63.550],
    marker = {'size': 10, 'color': ["black"]},
    line= {'width': 5, 'color': "darkgrey"}
))


#fig.add_trace(go.Scattermapbox(
   # mode = "markers",
    #lon = [-50, -60,40],
    #lat = [30, 10, -20],
    #marker = {'size': 100}))

#line_geo(lat=[64.40748,64.41769,64.42856,64.42896,64.43110], lon=[-19.31731 ,-19.31722 ,-19.35614,-19.35846,-19.36822 ])
#fig.update_geos(fitbounds="locations")

fig.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': { 'lon': SimulationParameters.Eborderline, 'lat': SimulationParameters.Nborderline},
        'zoom': 12, 'layers': [{
            'source': {
                'type': "FeatureCollection",
                'features': [{
                    'type': "Feature",
                    'geometry': {
                        'type': "MultiPolygon",
                        'coordinates': [[[
                            [-73.606352888, 45.507489991], [-73.606133883, 45.50687600],
                            [-73.605905904, 45.506773980], [-73.603533905, 45.505698946],
                            [-73.602475870, 45.506856969], [-73.600031904, 45.505696003],
                            [-73.599379992, 45.505389066], [-73.599119902, 45.505632008],
                            [-73.598896977, 45.505514039], [-73.598783894, 45.505617001],
                            [-73.591308727, 45.516246185], [-73.591380782, 45.516280145],
                            [-73.596778656, 45.518690062], [-73.602796770, 45.521348046],
                            [-73.612239983, 45.525564037], [-73.612422919, 45.525642061],
                            [-73.617229085, 45.527751983], [-73.617279234, 45.527774160],
                            [-73.617304713, 45.527741334], [-73.617492052, 45.527498362],
                            [-73.617533258, 45.527512253], [-73.618074188, 45.526759105],
                            [-73.618271651, 45.526500673], [-73.618446320, 45.526287943],
                            [-73.618968507, 45.525698560], [-73.619388002, 45.525216750],
                            [-73.619532966, 45.525064183], [-73.619686662, 45.524889290],
                            [-73.619787038, 45.524770086], [-73.619925742, 45.524584939],
                            [-73.619954486, 45.524557690], [-73.620122362, 45.524377961],
                            [-73.620201713, 45.524298907], [-73.620775593, 45.523650879]
                        ]]]
                    }
                }]
            },
            
            'type': "fill", 'below': "traces", 'color': "royalblue"}]},
    margin = {'l':0, 'r':0, 'b':0, 't':0})



fig.show()