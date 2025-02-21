if __name__ == '__main__':
    N = int(input())
    arr=[]
    
    for x in range(N):
        code = input().split()
        command = code[0]
        if len(code)>1:
            num = int(code[1])
        if len(code)>2:
            pos = int(code[2])
        
        match command:
            case "insert":
                arr.insert(num, pos)
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