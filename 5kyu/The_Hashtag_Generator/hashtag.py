#!/usr/bin/python3

def main(s):
    if len(s) == 0:
        return False
        
    hashtag = "#"
    for w in s.split():
        hashtag = hashtag + w.capitalize()

    if len(hashtag) > 140:
        return False
    return hashtag

if __name__ == "__main__":
    s = """codewars is nice"""
    print(main(s))