import pageviewapi.period
import pandas as pd

global num_players
global curr_player

def main():
    global num_players
    global curr_player

    df = pd.DataFrame(pd.read_csv("./basketball_scraper/basketball_stats.csv")["Name"].unique())
    df.rename(columns={0: "Name"}, inplace=True)
    num_players = len(df.Name)
    curr_player = 0

    df['avgvisitslast30days'] = [l(name) for name in df.Name]

    df.to_csv("./wikipedia_stats.csv", index=False)

def l(name):
    global num_players
    global curr_player
    curr_player += 1
    try:
        count = pageviewapi.period.avg_last('en.wikipedia', name, last=30)
        print("{}: {} ({}/{})".format(name, count, curr_player, num_players))
        return count
    except Exception:
        print("[ERROR]: Couldn't resolve Wikipedia entry for {}".format(name))
        return -1
    

if __name__ == '__main__':
    main()