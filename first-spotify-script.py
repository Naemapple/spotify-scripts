# Import the Spotipy library for Spotify API access
import spotipy
from spotipy.oauth2 import SpotifyOAuth
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
auth_manager = SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="http://127.0.0.1:8000/callback", 
    scope = "user-read-recently-played"
)
sp = spotipy.Spotify(auth_manager=auth_manager)


# ===== FUNCTION =====
def get_recent_listening_history(num_tracks):
    """
    Fetch your recent listening history from Spotify.
    
    Args:
        num_tracks (int): Number of uniquerecent tracks to retrieve
    
    Returns:
        prints list of tracks
    """
    unique_tracks = []
    seen_tracks = set()
    limit = num_tracks

    while len(unique_tracks) < num_tracks and limit <= 50:
        # Get the current user's recently played tracks
        results = sp.current_user_recently_played(limit=limit)
    
        # Extract the track items from the API response
        recent_tracks = results["items"]

        # Loop through each track

        for i, item in enumerate(recent_tracks, 1):
            # Extract track information from the API response
            track = item["track"]

            track_id = track["id"]

            track_name = track["name"]
            artist_name = track["artists"][0]["name"]

            if track_id not in seen_tracks:
                seen_tracks.add(track_id)
                unique_tracks.append(f"{track_name} by {artist_name}")
        limit += 1

    # Print the unique track information
    print("Your Most Recent Spotify Tracks:\n")
    print("\n".join(unique_tracks))



# ===== MAIN =====
if __name__ == "__main__":

    get_recent_listening_history(5)
