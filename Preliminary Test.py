def clothing_store():
    print("n:")
    n = input()
    print("ar:")
    ar = input()
    ar = ar.split(" ")

    current_index = 1
    checked_index = 0
    count = 0
    while len(ar) != 0 and checked_index != len(ar)-1:
        if ar[checked_index] == ar[current_index]:
            ar.pop(checked_index)
            ar.pop(current_index - 1)
            current_index = 0
            count+=1
        current_index+=1
        if current_index == len(ar):
            checked_index+=1
            current_index = checked_index+1
    print(count)

def avid_hiker():
    print("n:")
    n = int(input())
    print("ar:")
    s = input()
    s = s.split(" ")
    
    state=0
    current = 0
    count = 0
    for i in range(n):
        if s[i] == 'U':
            current+=1
        elif s[i] == 'D':
            current-=1
            
        if current == -1:
            state = -1;
        elif current == 0 and state == -1:
            count+=1
            state=0
    print(count)

def switch_lamp(lamp, trip):
    check = []
    for j in range(trip):
        current = j+1
        for i in range(lamp//current):
            if current * (i+1) not in check:
                check.append(current * (i+1))
            else:
                check.remove(current * (i+1))
    print(len(check));
