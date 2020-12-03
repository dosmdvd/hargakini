import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly as pt




csv_file_total = ("master.csv")
df= pd.read_csv(csv_file_total)

st.title("Weekly Total Spending")

#Sidebar
st.sidebar.title("About")
st.sidebar.markdown("The dashboard is a visualization of data from Price Intelligence database." )


#Create the selection box
selected_metrics = st.selectbox(
    label="Pick your category", options=['Air Conditioner','Bedroom Furniture','Cooktops','Freezer','Home Furniture','Living Furniture','Laptops','Phones','Refrigerator','Smart Televisions'])
st.write("You selected: ", selected_metrics)

# Plotting,Change it to lines mode or lines+markers where it fits
fig = go.Figure()
if selected_metrics == 'Air Conditioner':
	fig.add_trace(go.Scatter(x=df.Date, y=df.air_con,
                    mode='markers',
                    name='Air Conditioner'))
if selected_metrics == 'Bedroom Furniture':
	fig.add_trace(go.Scatter(x=df.Date, y=df.bedroom,
	                    mode='markers', name='Bedroom'))
if selected_metrics == 'Cooktops':
	fig.add_trace(go.Scatter(x=df.Date, y=df.cooktops,
	                    mode='markers', name='Cooktops'))
if selected_metrics == 'Freezer':
	fig.add_trace(go.Scatter(x=df.Date, y=df.freezer,
	                    mode='markers',
	                    name='Freezer'))
if selected_metrics == 'Home Furniture':
	fig.add_trace(go.Scatter(x=df.Date, y=df.home,
	                    mode='markers', name='Home Furniture'))
if selected_metrics == 'Living Furniture':
	fig.add_trace(go.Scatter(x=df.Date, y=df.living,
	                    mode='markers', name='Living'))
if selected_metrics == 'Laptops':
    fig.add_trace(go.Scatter(x=df.Date, y=df.laptops,
                         mode='markers',
                         name='Laptops'))
if selected_metrics == 'Phones':
	fig.add_trace(go.Scatter(x=df.Date, y=df.phones,
	                    mode='markers', name='Phones'))
if selected_metrics == 'Refrigerator':
	fig.add_trace(go.Scatter(x=df.Date, y=df.refrigerator,
	                    mode='markers', name='Refrigerator'))
if selected_metrics == 'Smart Televisions':
	fig.add_trace(go.Scatter(x=df.Date, y=df.tv,
	                    mode='markers', name='Cooktops'))
st.plotly_chart(fig, use_container_width=True)

st.markdown("Note: Hover over the scatter plot to see the figure.")
