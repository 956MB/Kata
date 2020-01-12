#!/usr/bin/python3

def main(*args):
    if len(args) == 0:
        return args

    for arg in args:
        while len(arg) < len(sorted(args, key=len)[-1]):
            arg.append(None)
        
    out = []
    for i in range(len(args[0])):
        for arg in args:
            out.append(arg[i])
    
    return out

if __name__ == "__main__":
    print(interleave([1, 2, 3], ["c", "d", "e"]))
    print(interleave([1, 2, 3], [4, 5]))
    print(interleave([1, 2, 3], [4, 5, 6], [7, 8, 9]))
    print(interleave([]))