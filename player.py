from playsound import playsound
from typing import List
from random import shuffle
from pathlib import Path

import sys
if "_enablelegacywindowsfsencoding" in dir(sys):
    sys._enablelegacywindowsfsencoding() # unicode support broken on windows; python claims it uses utf-8 wrongly

class Playlist:
    songs = []
    order = []
    current_song = None
    current_order = None

    @staticmethod
    def from_directory(directory: Path):
        return Playlist(list(directory.rglob("*.mp3")))

    def __init__(self, songs: List[Path]):
        if len(songs) == 0:
            raise ValueError()
        self.songs = songs
        self.order = list(range(len(songs)))

    def current(self):
        if self.current_song is None:
            return None
        else:
            return self.songs[self.current_song]

    def prev(self):
        if self.current_order == 0:
            self.current_order = None
            self.current_song = None
        elif self.current_order is not None:
            self.current_order -= 1
            self.current_song = self.order[self.current_order]

    def next(self):
        if self.current_order >= len(self.songs) - 1:
            self.current_order = None
            self.current_song = None
        elif self.current_order is not None:
            self.current_order += 1
            self.current_song = self.order[self.current_order]

    def first(self):
        self.current_order = 0
        self.current_song = self.order[0]

    def last(self):
        self.current_order = len(self.songs) - 1
        self.current_song = self.order[self.current_order]

    def shuffle(self):
        shuffle(self.order)
        if self.current_song is not None:
            self.current_order = self.order.index(self.current_song)

    def playlist_order(self):
        self.order = list(range(len(self.songs)))
        self.current_order = self.current_song


playlist = Playlist.from_directory(Path('./music'))

print(vars(playlist))

while True:
    current = playlist.current()
    if current is None:
        playlist.shuffle()
        playlist.first()
        current = playlist.current()

    print(str(current))
    playsound(str(current))
    playlist.next()
