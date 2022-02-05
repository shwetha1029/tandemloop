def CountFrequency(given_list):
    freq = {}
    for item in given_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    print(freq) 
given_list = [1,1,2,2,8,9,12,46,76,82,15,20,30]
CountFrequency(given_list)
