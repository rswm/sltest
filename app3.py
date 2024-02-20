import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


x= st.file_uploader("Upload data")

if x:
    df = pd.read_csv(x)
    st.write(df.head())

    fig, ax = plt.subplots()
    ax.scatter(df['species'], df['body_mass_g'])
    ax.set_xlabel('Species')
    ax.set_ylabel('Body mass')
    ax.set_title('Species vs body mass')

# Display the plot in Streamlit
    st.pyplot(fig)

    fig, ax = plt.subplots()
    ax.scatter(df['bill_length_mm'], df['bill_depth_mm'])
    ax.set_xlabel('Bill Length (mm)')
    ax.set_ylabel('Bill Depth (mm)')
    ax.set_title('Bill Length vs Bill Depth')

# Display the plot in Streamlit
    st.pyplot(fig)