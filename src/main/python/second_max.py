if __name__ == '__main__':
    arr = [2,3,6,6,5]
    winvalue = -100
    runner_value = -100
    for i in arr:
        print (str(i) + " " + str(winvalue) + " " + str(runner_value))
        if i > winvalue:
            runner_value = winvalue
            winvalue = i
        elif i > runner_value and i != winvalue:
            runner_value = i

print (runner_value)