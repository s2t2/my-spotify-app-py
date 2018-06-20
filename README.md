
# My Spotify App (Python)

An example Spotify API client application, for instructional purposes.

## Prerequisites

Create a Spotify Client application, and note its Client Id and Client Secret, and store them in environment variables called `SPOTIPY_CLIENT_ID` and `SPOTIPY_CLIENT_SECRET`.

This repo uses the "dotenv" approach, but feel free to use whatever approach works for you.

## Installation

Install package dependencies:

```sh
pip install -r requirements.txt
# or
pip3 install -r requirements.txt
# or
pipenv install -r requirements.txt
```

If using Pipenv, the following commands assume you are running them from within a `pipenv shell`.

## Usage

Run the app:

```sh
python3 list_songs.py
```
