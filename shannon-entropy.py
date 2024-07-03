import sys
import math

# <https://en.wikipedia.org/wiki/Entropy_(information_theory)>

def shannon_entropy(data):
    P = [float(data.count(c)) / len(data) for c in set(data)]
    return - sum([p * math.log(p, 2) for p in P])

def bitwise_shannon_entropy(data):
    P = [0, 0]
    for c in data:
        for x in range(8):
            P[1 & (ord(c) >> (7 - x))] += 1 / (len(data) * 8)

    return - sum([p * math.log(p, 2) for p in P if p])

def main():
    for p in sys.argv[1:]:
        shannon_entropy(p)
        print(f"'{p}':\t{round(shannon_entropy(p), 5)} bits/char\t{round(bitwise_shannon_entropy(p), 5)} bits/bit")

if __name__ == "__main__":
    main()
