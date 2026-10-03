import streamlit as st
import pandas as pd

st.title("My Music Project 🎵")
st.write("Hello! If you can see this, Streamlit is working.")

# a tiny table made by hand, just to test pandas
songs = pd.DataFrame({
    "song": ["Song A", "Song B", "Song C"],
    "plays": [12, 30, 7],
})
st.write(songs)
st.bar_chart(songs, x="song", y="plays")
