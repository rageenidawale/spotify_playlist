# 🎵 Billboard Hot 100 to Spotify Playlist  

## 📌 Overview  
This project **scrapes** the **Billboard Hot 100** chart for a user-specified date and **creates a Spotify playlist** with the top songs from that date.  

## 🚀 Features  
- 🌐 **Web Scraping** - Extracts the top 100 songs from Billboard using `BeautifulSoup`.  
- 🎧 **Spotify Integration** - Uses `Spotipy` to search for songs and create a private playlist.  
- ⏳ **Time Travel Feature** - Allows users to generate playlists from any historical date.  

## 🛠️ Technologies Used  
- **Python** 🐍  
- **BeautifulSoup** 🏗️ (for web scraping)  
- **Requests** 🌐 (to fetch Billboard data)  
- **Spotipy** 🎵 (for Spotify API integration)  

## 📂 File Structure  
```
/billboard-to-spotify
│── billboard_spotify.py
│── token.txt (Generated after first authentication)
│── README.md
```

## 📜 How to Run  
1. Clone the repository:  
   ```
   git clone https://github.com/your-username/billboard-to-spotify.git
   ```
2. Install dependencies:  
   ```
   pip install requests beautifulsoup4 spotipy
   ```
3. Set up **Spotify Developer Account**:  
   - Create an app on [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).  
   - Get **Client ID** and **Client Secret**.  
   - Set `https://example.com` as the redirect URI.  
   - Update `CLIENT_ID`, `CLIENT_SECRET`, and `SPOTIPY_REDIRECT_URI` in the script.  

4. Run the script:  
   ```
   python billboard_spotify.py
   ```
5. **Authenticate Spotify**:  
   - The script will open a URL.  
   - Grant access and paste the redirected URL into the console.  
   - The script will create a playlist in your Spotify account! 🎶  

## 🎯 Future Enhancements  
- 🔍 **Improve Song Matching** - Handle remixes and covers better.  
- 📝 **Save Playlist Links** - Store created playlist URLs in a file.  
- 🔄 **Allow Public Playlists** - Give users the option to make playlists public.  
- 🎶 **Include Album Art** - Fetch and display album covers for each song.  

