if __name__ == '__main__':
    N = int(input())
    arr=[]
    
    for x in range(N):
    comp = input().split()
    command = comp[0]
    if len(comp) > 1:
        num = int(comp[1])
    if len(comp) > 2:
        pos = int(comp[2])
        
    match command:
        case "insert":
            arr.insert(num,pos)
        case "print":
            print(arr)
        case "remove":
            arr.remove(num)
        case "append":
            arr.append(num)
        case "sort":
            arr.sort()
        case "pop":
            arr.pop()
        case "reverse":
            arr.reverse()