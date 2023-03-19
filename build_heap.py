# python3 Estella Saveljeva 221RDB176 7.gr

def build_heap(data):
    swaps = []
    n = len(data)
   
    for i in range(n//2, -1, -1):
        heap(data, i, n, swaps)
        
    return swaps

def heap(data, i, n, swaps)
    
    mindex = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left <= n and data[left] < data[mindex]:
        mindex = left
    if right <= n and data[right] < data[mindex]:
        mindex = right
    if i != mindex:
        swaps.append((i, mindex))
        data[i], data[mindex] = data[mindex], data[i]
        heap(data, i, n, swaps)
    

def main():
    
    print("[!] \tUse an input to choose files or input - F or I ?")
    textInput = input(":").upper()
    if "F" in textInput:
        print("[!] \tEnter file name or file path. For example '0'.")
        fileName = "tests/" + input(">:: \t")
        if 'a' in fileName:
            print("[Err]: \tForbidden name")
            return   
        file = open(fileName, "r")

        n = int(file.readline())
        data = list(map(int, file.readline().split()))
        assert len(data) == n
        swaps = buildHeap(data)

    elif "I" in textInput:
        print("[!] \tEnter text below.")
        n = int(input(">:: \t"))
        data = list(map(int, input(">:: \t").split()))
        assert len(data) == n
        swaps = buildHeap(data)
    else:
        print("[Err]:\tWrong input")
    pass
    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
