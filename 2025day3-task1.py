def max_volt(filev):
    ans =0
    with open(filev, "r") as f:
        data = [line.strip() for line in f]
    print(data)
    for i in data:
        val = ""
        # i = int(k)
        max_val = max(i)

        if max_val != i[-1]:
            val += max_val
            index = i.index(max_val)
            max_val2  = max(i[index+1:])
            val += max_val2
        else:
            max_val = max(i[:-1])
            val += max_val
            index = i.index(max_val)
            max_val2  = max(i[index+1:])
            val += max_val2

        ans += int(val)
        print(val)
    return ans

filev = "data.txt"

print(max_volt(filev))
