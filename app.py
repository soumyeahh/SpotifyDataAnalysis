import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Title
st.title("🎧 Spotify Listening Dashboard")

# Load data
df = pd.read_csv("cleaned_spotify_data.csv")
df['date'] = pd.to_datetime(df['date'])
df['time'] = pd.to_datetime(df['time'], format="%H:%M:%S").dt.time
df['hour'] = pd.to_datetime(df['time'], format="%H:%M:%S").dt.hour
df['weekday'] = df['date'].dt.day_name()

# Sidebar filters
artist_filter = st.sidebar.multiselect("Filter by Artist", df['master_metadata_album_artist_name'].dropna().unique())

if artist_filter:
    df = df[df['master_metadata_album_artist_name'].isin(artist_filter)]

# Charts
st.subheader("Listening Over Time")
daily = df.groupby("date")["ms_played"].sum() / 60000 # in minutes
fig = px.line(daily, x=daily.index, y=daily.values,
              labels={'x': 'Date', 'y': 'Minutes Played'},
              )
fig.update_traces(line_color='orange')
st.plotly_chart(fig)

# daily = df.groupby("date")["ms_played"].sum() / 60000  
# st.line_chart(daily)

st.subheader("Top Artists")
top_artists = df.groupby("master_metadata_album_artist_name")["ms_played"].sum().sort_values(ascending=False).head(10) / 60000
fig = px.bar(
    top_artists,
    x=top_artists.index,
    y=top_artists.values,
    labels={'x': 'Artist', 'y': 'Minutes Played'},
    
)
fig.update_traces(marker_color='crimson')  # Any CSS color name or hex
st.plotly_chart(fig)


st.subheader("Listening by Hour")
hourly = df.groupby("hour")["ms_played"].sum() / 60000
fig = px.bar(
    hourly,
    x=hourly.index,
    y=hourly.values,
    labels={'x': 'Hour of Day', 'y': 'Minutes Played'},
    
)
fig.update_traces(marker_color='seagreen')
st.plotly_chart(fig)


st.subheader("Skips vs Plays")
colors = ['#1DB954', '#E91429']  # Spotify green and red
skip_counts = df['skipped'].value_counts()
labels = ['Played', 'Skipped'] if 0 in skip_counts.index else ['Skipped', 'Played']
fig = px.bar(
    x=labels,
    y=skip_counts.values,
    labels={'x': 'Action', 'y': 'Count'},
   
)
fig.update_traces(marker_color=colors)
st.plotly_chart(fig)

