#!/usr/bin/python3

def main(seconds):
	mins, secs = divmod(seconds, 60)
	hours, mins = divmod(mins, 60)
	return "%d:%02d:%02d" % (hours, mins, secs)

if __name__ == '__main__':
	s = 86399
	print(main(s))
