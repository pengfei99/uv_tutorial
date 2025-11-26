import numpy as np
import pandas as pd

def main():
    print("Hello from my-app!")
    gen_df()

def gen_df():
    data = np.array([['', 'Col1', 'Col2'],
                     ['Row1', 1, 2],
                     ['Row2', 3, 4]])

    print(pd.DataFrame(data=data[1:, 1:],
                       index=data[1:, 0],
                       columns=data[0, 1:]))


if __name__ == "__main__":
    main()
