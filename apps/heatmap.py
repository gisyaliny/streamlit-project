import streamlit as st
import leafmap.foliumap as leafmap


def app():

    st.title("Building")

    # A subset of the dataset retrieved from https://github.com/johannesuhl/shapefile2gif
    data = "https://open.gishub.org/data/us/boulder_buildings.zip"
    m = leafmap.Map(center=[39.9898, -105.2532], zoom=14)
    m.add_vector(data, layer_name="Buildings")
    
    m.to_streamlit(height=700)
