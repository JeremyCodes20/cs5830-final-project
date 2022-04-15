import pandas as pd

def main():
    allStars = pd.read_csv("./data/all_star.csv")

    print(len(allStars['Player'].unique()))

if __name__ == "__main__":
    main()