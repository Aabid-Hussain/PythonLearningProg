
sent = "We " \
       "promptly judged antique ivory buckles for the prize"
sentlower = sent.lower()
for i in "abcdefghijklmnopqrstuvwxyz":
    if i in sentlower:
        continue

    else:
        print("not pangram")
        break
else:
    print("Pangram")