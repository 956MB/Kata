#!/usr/bin/python3
# This works... I guess. Weird.

def main(arr):
    d = {}
    for n in arr:
        li = set(sorted(n.lower()))
        # print(li)
        if not tuple(li) in d:
            d[tuple(li)] = [1, n]
        else:
            d[tuple(li)][0] += 1
    
    # print(d)
    return sorted(d.items(), key=lambda x: x[1][0])[0][1][1]

if __name__ == "__main__":
    arr = ['Tom Marvolo Riddle', 'I am Lord Voldemort', 'Harry Potter']
    print(main(arr))
