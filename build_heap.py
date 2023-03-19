# python3 Estella Saveljeva 221RDB176 7.gr

def build_heap(data):
    swaps = []
    n = len(data)
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    
    for i in range(n):
    mindex = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left <= n-1 and data[left] < data[mindex]:
        mindex = left
    if right <= n-1 and data[right] < data[mindex]:
        mindex = right
    if i != mindex:
        data[index], data[mindex] = data[mindex], data[index]
    return swaps

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    text = input("choose 'I' for input or 'F' for file")
    
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
