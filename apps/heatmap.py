import streamlit as st
import leafmap.foliumap as leafmap


def app():

    st.title("Heatmap")

    m = leafmap.split_map(
    left_layer="NLCD 2001 CONUS Land Cover",
    right_layer="NLCD 2016 CONUS Land Cover",
    left_label="2001",
    right_label="2016",
    label_position="bottom",
    center=[36.1, -114.9],
    zoom=10,
    )
    
    m.to_streamlit(height=700)
