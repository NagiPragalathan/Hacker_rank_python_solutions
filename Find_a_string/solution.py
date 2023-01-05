def count_substring(string, sub_string):
    last_index = 0
    count = 0
    for i in range(len(string)):
        if(sub_string[0] == string[i]):
            last_index = i
            temp = last_index
            occer = False
            for i in sub_string:
                try:
                    if(i == string[temp]):
                        occer = True
                    else:
                        occer = False
                        break
                    temp = temp + 1
                except:
                    occer = False
                    break
            if(occer):
                count = count + 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)