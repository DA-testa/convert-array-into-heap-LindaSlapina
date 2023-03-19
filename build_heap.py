# python3
# Linda Slapiņa 221RDB214

def heap(data, a, i, swaps):
    gar = 2 * i + 1
    gar2 = 2 * i + 2

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
    for i in range(a// 2 -1, -1, -1):
        heap(data, a, i, swaps)
    return swaps

def main():
    text = input()
    
    if 'I' in text:
        n = int(input())
        data = list(map(int, input().split()))

    if 'F' in text:
        filee = input()
        with open("tests/" + filee, 'r') as faili:
            n = int(faili.readline())
            data = list(map(int, faili.readline().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j) 



if __name__ == "__main__":
    main()
