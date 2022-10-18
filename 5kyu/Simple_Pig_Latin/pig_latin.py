#!/usr/bin/python3

def main(text):
    new = ""
    for w in [i for j in text.split() for i in (j, ' ')][:-1]:
        if len(w) >= 2:
            new = new + w[1:] + w[0] + "ay"
        elif len(w) == 1 and not w in ".,!? ":
            new = new + w + "ay"
        else:
            new = new + w

    return new

if __name__ == '__main__':
	print(main('This is my string'))
