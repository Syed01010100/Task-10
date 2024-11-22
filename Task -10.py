class Song:
    def __init__(self, title, artist, duration):
        # Init.  song with  title, artist, and duration
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        # return a string
        return f"{self.title} by {self.artist} ({self.duration})"


class MusicPlayer:
    def __init__(self):
        # Init the music player with an empty playlist and a current index
        self.playlist = []  # List to store songs
        self.current_index = 0  # Index of the song currently playing

    def add_song(self, title, artist, duration):
        # Add a new song to the playlist
        self.playlist.append(Song(title, artist, duration))
        print(f"Added: {self.playlist[-1]}")  # Confirm the song was added

    def view_playlist(self):
        # Display all songs in the playlist
        if not self.playlist:  # Check if the playlist is empty
            print("The playlist is empty.")
        else:
            # Loop through the playlist and print each song
            for i, song in enumerate(self.playlist, 1):
                print(f"{i}. {song}")

    def play(self):
        # Play the current song in the playlist
        if self.playlist:  # Check if there are songs to play
            print(f"Playing: {self.playlist[self.current_index]}")
        else:
            print("No songs in the playlist.")

    def next_song(self):
        # Move to the next song and play it
        if self.playlist:  # Check if there are songs in the playlist
            self.current_index = (self.current_index + 1) % len(self.playlist)  # Cycle through the playlist
            self.play()  # Play the next song


if __name__ == "__main__":
    player = MusicPlayer()

    # Adding songs to the playlist
    player.add_song("Song A", "Artist A", "3:30")
    player.add_song("Song B", "Artist B", "4:00")
    player.add_song("Song C", "Artist C", "2:45")

    # Viewing the playlist
    player.view_playlist()

    # Playing the current song
    player.play()

    # Playing the next song
    player.next_song()  # Play next song