import streamlit as st
import leafmap.foliumap as leafmap


def app():

    st.title("Heatmap")

    m = leafmap.Map()
    m.add_basemap("Esri.WorldTopoMap")
    # m.add_heatmap_demo()
    m.add_scatter_plot_demo()
    
    m.to_streamlit(height=700)
