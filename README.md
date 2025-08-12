# Spotify Listening Data Dashboard

An **interactive web application** built with Python, Pandas, Plotly, and Streamlit to visualize personal Spotify listening patterns. This dashboard provides insights into listening trends, top artists, platform usage, and more using custom data analysis and interactive visualizations.

## Features

* **Data Cleaning & Transformation**: Converted raw Spotify streaming history from JSON to a structured format. Extracted and separated date and time from timestamps.
* **Interactive Visualizations**:

  * Top artists and tracks
  * Listening patterns by day, time, and platform
  * Streaming duration analysis
* **Dynamic Filtering**: View data by date range, country, platform, and more.
* **Deployment**: Hosted on Streamlit Cloud with continuous integration via GitHub.

## Tech Stack

* **Python**: Pandas, NumPy, Plotly, Streamlit
* **Version Control**: Git & GitHub
* **Deployment**: Streamlit Cloud

## Getting Started

### 1. Clone the Repository

```bash
git clone git@github.com:YOUR_USERNAME/spotify-dashboard.git
cd spotify-dashboard
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Your Spotify Data

1. Download your Spotify streaming history from [Spotify Privacy Settings](https://www.spotify.com/account/privacy/).
2. Place your JSON file(s) into the `data/` folder.

### 4. Run the Dashboard

```bash
streamlit run app.py
```

## Example Visualizations

* Bar chart of top 10 most played artists
* Heatmap of listening activity by hour of day and day of week
* Trend line of listening time over months

## Project Structure

```
spotify-dashboard/
│
├── app.py                  # Main Streamlit app
├── data/                   # Folder for raw JSON data
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
└── images/                 # Example visualizations
```

## License

This project is open-source under the MIT License.
