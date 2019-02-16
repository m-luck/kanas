def iq_test(numbers):
    iq_list = numbers.split(" ")
    iq_evenness = {}
    odd_count = 0
    count = 1
    for iq in iq_list:
        if int(iq) % 2 == 0:
            iq_evenness["even"] = count
        else: 
            iq_evenness["odd"] = count
            odd_count += 1
        count += 1
    if odd_count == 1:
        return (iq_evenness["odd"])
    else:
        return (iq_evenness["even"])
