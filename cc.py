import pandas as pd

import numpy as np

import streamlit as st

import plotly.express as px

import seaborn as sns

import matplotlib.pyplot as plt

from PIL import Image

df_1=pd.read_csv("C:/Users/Admin/Documents/R classes notes/R programs/excel files/1.cereal.csv", index_col ="name" )

df_1.drop(["Maypo"], inplace = True)

df_1['mfr'] = df_1['mfr'].astype('category')

df_1['type'] = df_1['type'].astype('category')

df_1['shelf'] = df_1['shelf'].astype('category')


st.title('Cereal Data Analysis')
def home():
    st.header("Description")
    st.write("This dataset contains nutrition information for 74 breakfast cereals and includes 16 variables. The rating column is our target(QOI) as a rating of the cereals.")
    image = Image.open('ce.png')
    st.image(image, caption='Cereal') 
def data():
    st.header('Header of Dataframe')
    st.write(df_1.head())

def per():
    tab1, tab2, tab3, tab4  = st.tabs(['rating', 'Mfr', 'correlation', 'Nutrional information'])

    with tab1:
        st.header("Rating Value")
        fig = px.histogram(df_1, x='rating')
        st.plotly_chart(fig)
    with tab2:
        st.header("MFR vs Rating")
        fig = px.box(df_1, x='mfr', y='rating')
        st.plotly_chart(fig)
   
    with tab3:
        st.header("Correlation")
        hm = sns.heatmap(df_1.corr(), annot = True)

        hm.set(xlabel='\ncereal Nutri Details', ylabel='Cereal Nutri Details\t', title = "Correlation matrix of Cereal data\n")
        st.plotly_chart(hm)
   
    with tab4:
        st.header("Nutrional information")
        fig = px.scatter(df_1, y='rating', x='calories', color='mfr')
        st.plotly_chart(fig)
    

def uni():
    tab1, tab2 = st.tabs(['Shelf', 'Type'])

    with tab1:
        st.header("Shelf position")
        fig = px.scatter(df_1, y='rating', x='mfr', facet_col='shelf', color='shelf')
        st.plotly_chart(fig)
    with tab2:
        st.header("Type of cereaL")
        fig = px.scatter(df_1, y='rating', x='mfr', facet_col='type', color='type')
        st.plotly_chart(fig)
    
    
def rep():
    st.header("REPORT")
    st.write("*   There is a positive correlation between calories and sugars in cereal.")
    st.write("*  Most cereals do not have relatively high potassium values.")
    st.write("*   The more calories that a cereal has, the less likely it is to receive a high rating.")
    st.write("*  Manufacturers that want to bring in high ratings should create cereals that are high in fiber, protein, and potassium and avoid creating cereals with high-calorie counts or lots of sugar or fat.")
    st.write("*   Cereals with high ratings are more likely to be placed on the first or third shelf, because that is generally where the consumers’ eyes gravitate")
    
             
st.sidebar.title('Navigation')
side = st.sidebar.radio('Select what you want to display:', ['Home', 'Data Header', 'Rating Info', 'Other Info', 'Report'])
if side == 'Home':
 home()
elif side == 'Data Header':
 data()
elif side == 'Rating Info':
 per()
elif side == 'Other Info':
 uni()
elif side == 'Report':
 rep()