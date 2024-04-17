from datetime import date

s = input().strip()
start = s[:2]
end = s[2:]
if "01" <= start <= "12" and "01" <= end <= "12":
    print("AMBIGUOUS")
elif "01" <= start <= "12":
    print("MMYY")
elif "01" <= end <= "12":
    print("YYMM")
else:
    print("NA")