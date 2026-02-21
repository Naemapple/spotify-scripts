# Import the Spotipy library for Spotify API access
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

# ===== ENVIRONMENT SETUP =====
# Load environment variables from the .env file
load_dotenv()

# Get Spotify API credentials from environment variables
# To set these up:
# 1. Go to https://developer.spotify.com/dashboard
# 2. Log in or create a Spotify account
# 3. Create a new app to get your Client ID and Client Secret
# 4. Create a .env file in this directory with:
#    SPOTIFY_CLIENT_ID=your_id_here
#    SPOTIFY_CLIENT_SECRET=your_secret_here

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")


# ===== AUTHENTICATION =====
# Create a Spotify API client using your credentials
# SpotifyClientCredentials handles the authentication automatically
auth_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)
sp = spotipy.Spotify(auth_manager=auth_manager)


# ===== FUNCTION =====
def get_recent_listening_history(limit=10):
    """
    Fetch your recent listening history from Spotify.
    
    Args:
        limit (int): Number of recent tracks to retrieve (default: 10, max: 50)
    
    Returns:
        list: A list of track information dictionaries
    """
    # Get the current user's recently played tracks
    results = sp.current_user_recently_played(limit=limit)
    
    # Extract the track items from the API response
    tracks = results["items"]
    
    return tracks


# ===== MAIN =====
if __name__ == "__main__":
    # Get and display the 10 most recent tracks
    recent_tracks = get_recent_listening_history(limit=10)
    
    # Loop through each track and print the information
    print("Your 10 Most Recent Spotify Tracks:\n")
    for i, item in enumerate(recent_tracks, 1):
        # Extract track information from the API response
        track = item["track"]
        track_name = track["name"]
        artist_name = track["artists"][0]["name"]
        
        # Print the track information in a readable format
        print(f"{i}. {track_name} by {artist_name}")
