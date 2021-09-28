from __future__ import annotations
from re import template
from numpy.core.numeric import True_
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import webbrowser
from threading import Timer
#port = 8050
#def open_browser():
#	webbrowser.open_new("http://localhost:{}".format(port))
app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])
server = app.server
df = pd.read_csv(r'C:\Users\mosta\Downloads\mdt_data_jan_jul_2018.csv')
#df['Location'].dropna(axis = 0 , inplace = True)

#The HeatMap
fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", hover_name="Material Description", hover_data=["ItemName", "Quantity"],
                        opacity = .5 ,color_discrete_sequence=px.colors.sequential.Rainbow ,size = df['Quantity'] , size_max=50, zoom=2, height=500)
fig.update_layout(mapbox_style='open-street-map', mapbox_center_lon=180 )
fig.update_layout(template = "plotly_dark" , margin={"r":0,"t":0,"l":0,"b":0})

#All Materials Visualization 
h =[30669, 5044, 4367, 3696 , 1315 , 1122 , 1027 , 160]
mylabels = ["Plastic", "Fishing Gear", "Paper & Lumber", "Other Items" , "Metal" , "Glass" , "Cloth" , "Rubber"]


#fig1 = go.Figure()
fig1 = make_subplots(rows=1, cols=2,  specs=[[{'type':'xy'}, {'type':'domain'}]])
fig1.add_trace(go.Bar(x = mylabels , y = h , name = 'Materials')  , 1 , 1)
fig1.update_xaxes(tickangle = 90)
fig1.add_trace(go.Pie(labels=mylabels, values=h,name = 'Material' ) , 1,2 )



fig1.update_layout(
    template = 'plotly_dark',
    title_text="All Materials Debris",
    )

#fig2
plastic_values = [9782 , 4767 , 4321 ,2907 , 2105 , 1541 , 1522 , 1289 , 686 , 553 , 400 , 286 , 277 , 159 , 74]
plastic_labels = ["Plastic or Foam Fragments" ,'Food Wrappers' ,'Cigarettes' ,'Bottle or Container','Plastic Bags','Straws' ,'Plastic Bottle' ,"Foam or Plastic Cup","Plastic Utensils","Other Plastic Jugs or Containers","Balloons" ,"Cigarette packaging",'care products','Rubber Gloves','Six-pack rings']
fig2 = make_subplots(rows=1, cols=2, specs=[[{'type':'xy'}, {'type':'domain'}]])
fig2.add_trace(go.Bar(x = plastic_labels , y = plastic_values ,name = 'Plastic' ) , 1 , 1)
fig2.update_xaxes(tickangle = 90)
fig2.add_trace(go.Pie(labels=plastic_labels, values=plastic_values , name = 'Plastic' ) , 1,2 )


fig2.update_layout(
    
    template = "plotly_dark",
    title_text="Plastic Debris")




app.layout = html.Div([
    dbc.Row(dbc.Col(html.H1("ECO BOT MISSION REPORT"),
                    width = {'size' : 6 , 'offset' : 3})),
    
    dcc.Graph(figure=fig),
    dbc.Row(dbc.Col(html.H1(""),
                    width = {'size' : 6 , 'offset' : 3})),
    dcc.Graph(figure = fig1),
    dbc.Row(dbc.Col(html.H1(""),
                    width = {'size' : 6 , 'offset' : 3})),
    dcc.Graph(figure = fig2)
])

#Timer(0 , open_browser).start();
app.run_server(debug=True)

