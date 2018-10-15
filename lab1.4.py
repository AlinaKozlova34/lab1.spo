N = int(input("Enter N\n"))
Y = N / 30
P = P1 = P2 = P3 = 0

while P != 1:
    P1 = float(input("Enter probability for Karlos\n"))
    P2 = float(input("Enter probability for Rodriges\n"))
    P3 = float(input("Enter probability for Santiago\n"))
    P = P1 + P2 + P3
    print("invalid probability sum") if P != 1.0 else 0

print("Answer ", (P1 * Y) ** 300)