# Import the Spotipy library for Spotify API access
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

# ===== ENVIRONMENT SETUP =====
# Load environment variables from the .env file
load_dotenv()


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
def get_recent_unique_history(num_tracks):
    """
    Fetch your recent listening history from Spotify.
    
    Args:
        num_tracks (int): Number of unique recent tracks to retrieve
    
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
                unique_tracks.append(track)
        limit += 1

    # Print the unique track information
    #print("Your Most Recent Spotify Tracks:\n")
    #for track in unique_tracks:
        #print(f"{track['name']} by {track['artists'][0]['name']}")

    return unique_tracks



# ===== MAIN =====
if __name__ == "__main__":

    recent_tracks = get_recent_unique_history(5)

    print(f"\n{'Your Most Recent Spotify Tracks':^135}\n")

    print(f"| {'Track Name':<30} | {'Artist':<20} | {'Album Name':<30} | {'Release Date':<12} |")
    print("-" * 135)

    for track in recent_tracks:
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        
        album_name = track['album']['name']
        release_date = track['album']['release_date']

        # # Get the artist's genres
        # artist_id = track['artists'][0]['id']
        # artist_info = sp.artist(artist_id)
        # genres = ", ".join(artist_info['genres']) if artist_info['genres'] else "N/A"

        print(f"| {track_name:<30} | {artist_name:<20} | {album_name:<30} | {release_date:<12} |")

     
    


