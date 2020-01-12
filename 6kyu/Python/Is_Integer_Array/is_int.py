#!/usr/bin/python3

def is_int_array(arr):
    if isinstance(arr, list):
        if len(arr) == 0:
            return True
        for i in arr:
            if isinstance(i, int):
                continue
            elif isinstance(i, float):
                if i.is_integer():
                    continue
                return False
            else:
                return False
        return True
    return False

if __name__ == "__main__":
    print(is_int_array([]))
    print(is_int_array([1, 2, 3, 4]))
    print(is_int_array([-11, -12, -13, -14]))
    print(is_int_array([1.0, 2.0, 3.0]))
    print(is_int_array([1, 2, None]))
    print(is_int_array(None))
    print(is_int_array(""))
    print(is_int_array([None]))
    print(is_int_array([1.0, 2.0, 3.0001]))
    print(is_int_array(["-1"]))
