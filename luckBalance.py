def main():
    n = 6
    k = 3
    contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]
    # print(contests[0][0])
    print(luckBalance(k, contests))

def luckBalance(k, contests):
    # Write your code here
    luck_balance = 0
    contest = sorted(contests, key=lambda x:x[0], reverse=True)
    for i in range(len(contest)):
        luck = contest[i][0]
        importance = contest[i][1]

        if importance == 1 and k > 0:
            k -= 1
            luck_balance += luck
        elif importance == 1 and k == 0:
            luck_balance -= luck
        if importance == 0:
            luck_balance += luck
    return luck_balance


if __name__=="__main__":
    main()

