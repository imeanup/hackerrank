def minion_game(string):
    # your code goes here
    con = 0
    vol = 0
    n = len(s)
    for i in range(n):
        if string[i] in "AEIOU":
            vol += (n - i)
        else:
            con += (n - i)
            
    if con > vol:
        print(f"Stuart {con}")
    elif con < vol:
        print(f"Kevin {vol}")
    else:
        print("Draw")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)
