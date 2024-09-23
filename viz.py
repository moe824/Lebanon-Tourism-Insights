import streamlit as st
import pandas as pd
import plotly.express as px

# Load and prepare the data
data = pd.read_csv("Lebanon Tourism.csv")
data['Governorate'] = data['refArea'].apply(lambda x: x.split('/')[-1].replace('_Governorate', ''))

# Sidebar for visualization selection
option = st.sidebar.selectbox('Select a visualization:', 
                              ['Guest Houses and Restaurants by Governorate', 
                               'Trend of Guest Houses and Restaurants', 
                               'Existence of Cafes', 
                               'Touristic Attractions vs Guest Houses'])

if option == 'Guest Houses and Restaurants by Governorate':
    # Bar Chart
    bar_data = data.groupby('Governorate')[['Total number of guest houses', 'Total number of restaurants']].sum().reset_index()
    fig = px.bar(bar_data, x='Governorate', y=['Total number of guest houses', 'Total number of restaurants'],
                 title="Total Guest Houses and Restaurants by Governorate",
                 labels={'value': 'Total Count', 'variable': 'Type'})
    st.plotly_chart(fig)

elif option == 'Trend of Guest Houses and Restaurants':
    # Line Chart
    line_data = data.groupby('Governorate')[['Total number of guest houses', 'Total number of restaurants']].sum().reset_index()
    fig = px.line(line_data, x='Governorate', y=['Total number of guest houses', 'Total number of restaurants'],
                  title="Guest Houses and Restaurants Across Governorates",
                  labels={'value': 'Total Count', 'variable': 'Type'})
    st.plotly_chart(fig)

elif option == 'Existence of Cafes':
    # Pie Chart
    pie_data = data['Existence of cafes - exists'].value_counts().reset_index()
    pie_data.columns = ['Cafes Exist', 'Count']
    fig = px.pie(pie_data, names='Cafes Exist', values='Count', title="Existence of Cafes in Governorates")
    st.plotly_chart(fig)

elif option == 'Touristic Attractions vs Guest Houses':
    # 3D Scatter Plot
    fig = px.scatter_3d(data, x='Governorate', y='Existence of touristic attractions prone to be exploited and developed - exists', 
                        z='Total number of guest houses', color='Governorate',
                        title='3D View: Touristic Attractions Prone to be Developed vs Guest Houses')
    st.plotly_chart(fig)



st.title("Lebanon Tourism Insights")

