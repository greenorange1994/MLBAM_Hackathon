import pandas as pd
def find_away():
    st = pd.read_csv("us_streams.csv")
    at = pd.read_csv("attendance.csv")
    at["day"] = pd.Series()
    st["AWAY_TEAM"] = pd.Series()

    for i in range(len(at)):
        a = at["START_TIME"][i].split(' ')
        at["day"][i] = a[0]

    for j in range(len(st)):
        s = st["GAME_DATE"][j].split(' ')
        for m in range(len(at)):
            if at["HOME_TEAM"][m] == st["HOME_TEAM"][j] and at["day"][m] == s[0]:
                    st["AWAY_TEAM"][j] = at["AWAY_TEAM"][m]
    print (st["AWAY_TEAM"])
    return st

def main():
    data = find_away()
    data.to_csv("new_streams.csv", index = False)

if __name__ == "__main__": main()
