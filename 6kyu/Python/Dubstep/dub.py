#!/usr/bin/python3

import re

def song_decoder(song):
    # print("Before:", repr(song))
    regex = re.compile(r"(WUB)")
    song = regex.sub(" ", song)
    # print("After", repr(' '.join(song.split())), "\n")
    return " ".join(song.split())


if __name__ == "__main__":
    print(song_decoder("AWUBBWUBC"))
    print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))
    print(song_decoder("WUBAWUBBWUBCWUB"))