import pandas as pd


def main():
    my_dict = {'known': [1], 'power': [1], 'new': [1], 'location': 0, 'stable': [1], 'chain_reaction': [1]}

    s = pd.DataFrame.from_dict(my_dict)

    print(s)

    # data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
    # print(pd.DataFrame.from_dict(data))


main()
