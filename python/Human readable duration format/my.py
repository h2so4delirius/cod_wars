def help_format(array : list, time : int): 
    array_t = 0
    for i in array[time + 1:]:
        if i > 0:
            array_t += 1
    if array_t == 1:
        return " and "
    elif array_t > 1:
        return ", "
    return ""
        
        


def format_duration(seconds):
    array = [0] * 5
    Y, D, H, M, S = range(5)
    res = ""
    array[Y] = seconds//(365*24*60*60)
    seconds = seconds - (array[Y] * (365*24*60*60))
    array[D] = seconds//(24*60*60)
    seconds = seconds - (array[D] * (24*60*60))
    array[H] = seconds//(60*60)
    seconds = seconds - (array[H] * (60*60))
    array[M] = seconds//60
    seconds = seconds - (array[M] * 60)
    array[S] = seconds
    if array[Y] > 0:
        if array[Y] == 1:
            res += str(array[Y]) + " year"
        else:
            res += str(array[Y]) + " years"
        res += help_format(array, Y)
    if array[D] > 0:
        if array[D] == 1:
            res += str(array[D]) + " day"
        else:
            res += str(array[D]) + " days"
        res += help_format(array, D)
    if array[H] > 0:
        if array[H] == 1:
            res += str(array[H]) + " hour"
        else:
            res += str(array[H]) + " hours"
        res += help_format(array, H)
    if array[M] > 0:
        if array[M] == 1:
            res += str(array[M]) + " minute"
        else:
            res += str(array[M]) + " minutes"
        res += help_format(array, M)
    if array[S] > 0:
        if array[S] == 1:
            res += str(array[S]) + " second"
        else:
            res += str(array[S]) + " seconds"
    if res == "":
        res += "now"
                
    return res


#"1 hour, 1 minute and 2 seconds"
print(format_duration(1))
print(format_duration(62))
print(format_duration(120))
print(format_duration(3600))
print(format_duration(3662))
print(format_duration(1000000000))