# python3

# Linda Slapiņa 221RDB214
from math import floor


def heap(data, a, i, swaps):
    gar = i*2+1
    gar2 = i*2+2

    rez = i
    if gar < a and data[gar] < data[rez]:
        rez = gar
    if gar2 < a and data[gar2] < data[rez]:
        rez = gar2
    if rez != i:
        swaps.append((i,rez))
        data[i], data[rez] = data[rez], data[i]
        heap(data, a, rez, swaps)    


def build_heap (data):
    swaps = []
    a = len(data)
    for i in range(a//2-1, -1, -1):
        heap(data, a, i, swaps)
    return swaps

def main():
    text = input()
    
    if "I" in text:
        n = int(input())
        data = list(map(int, input().split()))

    elif "F" in text:
        filee = input()
        with open("tests/" + filee, 'r') as faili:
            n = int(faili.readline())
            data = list(map(int, faili.readline().split()))
    else:
        print("kluuda")
        return

    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i,j in swaps:
        print(i, j) 



if __name__ == "__name__":
    main()
