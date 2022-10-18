#!/usr/bin/env python3
# Sort the columns of a csv-file
# https://www.codewars.com/kata/57f7f71a7b992e699400013f/train/python

def sort_csv_columns(csv_file_content):
    out, temp = [], []
    ret = [i.split(';') for i in csv_file_content.split('\n')]
    ret = [list(x) for x in sorted(zip(*ret), key=lambda v: v[0].upper())]
    for i in range(len(ret[0])):
        for x in range(len(ret)):
            temp.append(ret[x][i])
        out.append(';'.join(temp))
        temp = []
    return '\n'.join(out)

if __name__ == '__main__':
    from collections import namedtuple
    TestData = namedtuple('TestData', ['pre_sorting', 'post_sorting'])

    tests = [
        TestData(
            pre_sorting = (
                "myjinxin2015;raulbc777;smile67;Dentzil;SteffenVogel_79\n"
                "17945;10091;10088;3907;10132\n"
                "2;12;13;48;11"
            ),
            post_sorting = (
                 "Dentzil;myjinxin2015;raulbc777;smile67;SteffenVogel_79\n"
                 "3907;17945;10091;10088;10132\n"
                 "48;2;12;13;11"
            )
        ),
        TestData(
            pre_sorting = (
                "Captain America;Hulk;IronMan;Thor\n"
                "honorably;angry;arrogant;divine\n"
                "shield;greenhorn;armor;hammer\n"
                "Steven;Bruce;Tony;Thor"
            ),
            post_sorting = (
                "Captain America;Hulk;IronMan;Thor\n"
                "honorably;angry;arrogant;divine\n"
                "shield;greenhorn;armor;hammer\n"
                "Steven;Bruce;Tony;Thor"
            )
        ),
    ]

    for t in tests:
        print(sort_csv_columns(t.pre_sorting), t.post_sorting)

