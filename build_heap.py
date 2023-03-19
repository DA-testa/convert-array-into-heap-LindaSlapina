# python3
from math import floor

def s_down(data, n,i,swaps):
    x = (i << 1 ) + 1
    y = (i << 1 ) + 2
    index = i
    if y<n and data[x]<data[index]:
        index = x
    if y<n and data[y]<data[index]:
        index = y
    if index !=i:
        swaps.append((i,index))
        data[i],data[index] = data[index], data[i]
        s_down(data,n,index,swaps)        

def build_heap(data):
    swaps = []
    n=len(data)
    for i in range (n // 2 -1, -1, -1):
        s_down(data,n,i,swaps)
    return swaps


def main():
    try:
        line = input().split()
        if "I" in line:
            n= int(input())
            data = list(map(int, input().split()))
        elif "F" in line:
            nameofile = input()
            with open ("tests/" + nameofile, 'r') as filee:
                n = int(filee.readline())
                data = list(map(int, filee.readline().split()))
        else:
            raise ValueError("Invalid input, please input F or I!")
        if n != len(data):
            raise ValueError("Invalid input, lenght of data does not match!")
        swaps = build_heap(data)
        print(swp[0],swp[1])

    except ValueError:
        print("Error")

if __name__ == "__main__":
    main()
