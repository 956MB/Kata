#!/usr/bin/python3

from time import sleep
import sys

def main(arr, n, q):
    arr = list(arr)
    while True:
        try:
            question = str(input('Swap: '))

            if question in '':
                swap_err('err: no input given.', arr, n, q)
            elif len(question) <= 1:
                swap_err('err: only one number provided.', arr, n, q)
            elif ' ' in question:
                question = question.strip()
                if len(question) <= 1:
                    swap_err('err: only one number provided.', arr, n, q)
                else:
                    question = question.split()

            pos1 = int(question[0])
            pos2 = int(question[1])
            print(4 * "\033[K\033[A")

            swapped = swap(arr, pos1, pos2)
            arr = swapped[0]
            print(arr)
            print(f'Last swap: {swapped[1]},{swapped[2]}')
            got_match = match(arr, n, q)

            if got_match:
                print(3 * "\033[K\033[A")
                print(f'Match: {arr}')
                update_moves(0, 0, True)

        except KeyboardInterrupt:
            print('\nscript exited')
            sys.exit()

def swap(list, pos1, pos2):
    num1 = list.index(pos1)
    num2 = list.index(pos2)
    list[num1], list[num2] = list[num2], list[num1]
    update_moves(pos1, pos2, False)
    return [list, pos1, pos2]

def match(arr, n, q):
    answer= 1

    for i in range(0, len(arr)-n+1):
        section = arr[i:i+n]
        if sum(section) > q:
            answer = 0
            break

    if answer == 1:
        return True
    elif answer == 0:
        return False

def update_moves(mov1, mov2, done):
    if done:
        print(f'Moves: {moves} ({len(moves)})')
        sys.exit()
    else:
        moves.append((mov1, mov2))

def swap_err(msg, arr, n, q):
    print(msg)
    sleep(.5)
    print(3 * "\033[K\033[A")
    main(arr, n, q)

if __name__ == "__main__":
    arr, n, q = (3,5,7,1,6,8,2,4), 3, 13
    moves = []
    print(f'Start: {list(arr)}\n\n')
    main(arr, n, q)
