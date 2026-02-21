# Spotify Learning Project

A simple Python project to learn the basics of programming with the Spotify API.

## Setup

### 1. Install Dependencies
```bash
pip install spotipy python-dotenv
```

### 2. Get Spotify API Credentials
1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Log in or create a Spotify account
3. Create a new app to get your **Client ID** and **Client Secret**

### 3. Set Up Environment Variables
1. Copy the example env file:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and add your Spotify credentials:
   ```
   SPOTIFY_CLIENT_ID=your_client_id_here
   SPOTIFY_CLIENT_SECRET=your_client_secret_here
   ```

### 4. Run the Script
```bash
python first-spotify-script.py
```

## What It Does

The script pulls your 10 most recent Spotify listening history tracks and displays them with artist names.

## Project Structure

- `first-spotify-script.py` - Main script with comments for learning
- `.env` - Your environment variables (ignored by git)
- `.env.example` - Template for environment variables
