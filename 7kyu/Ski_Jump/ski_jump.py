#!/usr/bin/python3

def main(mountain):
	speed = len(mountain) * 1.5
	jump = (len(mountain) * speed * 9) / 10
	rounded = "%.2f" % round(jump, 2)

	if jump <= 10:
		return "%s metres: He's crap!" % (rounded)
	elif 10 <= jump <= 25:
		return "%s metres: He's ok!" % (rounded)
	elif 25 <= jump <= 50:
		return "%s metres: He's flying!" % (rounded)
	elif jump >= 50:
		return "%s metres: Gold!!" % (rounded)

if __name__ == '__main__':
	m = ["*", "**", "***", "****", "*****", "******", "*******", "********"]
	result = main(m)
	print(result)

# Mountain height: 1
# Speed: 1.5            # 1 * 1.5
# Jump length: 1.35     # (1 * 1.5 * 9) / 10

# Output format: "1.35 metres: He's flying!"
