# tunrs a string of things into a list of only numbers
# ex: input:"23uiw -2--..4" --> output:[23, 2, 4].
def turn_list(num):
    num_list = [i for i in num]
    reversed_num_list = list(reversed(num_list))
    list_sum = []
    final_num = []
    count = int(0)
    for n in reversed_num_list:
        if n.isdigit():
            n_int = int(n)
            count += 1
            for raised in range(count - 1):
                n_int *= 10
            list_sum.append(n_int)
        else:
            if list_sum:
                total = sum(list_sum)
                list_sum = []
                final_num.append(total)
                count = 0
    if list_sum:
        total = sum(list_sum)
        final_num.append(total)
    final_num.reverse()
    final_num.sort()
    return final_num

# retunr a dict, the keys are the caracter
# while the value are the abs freqs.
def calc_abs_freq(num_list):
    nj_dict = {}
    for i in num_list:
        nj_i = num_list.count(i)
        nj_dict[i] = nj_i
    return(nj_dict)

# retunr a dict, the keys are the caracter
# while the value are the rel freqs.
def calc_rel_freq(nj_dict):
    fj_dict = {}
    N = 0
    for v in nj_dict.values():
        N += v
    for k, v in nj_dict.items():
        fj_dict[k] = round((v / N), 2)
    return fj_dict

# input should be rel_freq
def calc_perc_freq(pn_dict_copy):
    pn_dict = pn_dict_copy.copy()
    for i in pn_dict:
        pn_dict[i] *= 100
    return pn_dict

# input should be rel_freq
def calc_cum_freq(Fj_dict_copy):
    Fj_dict = Fj_dict_copy.copy()
    value = 0
    for k, v in Fj_dict.items():
        value += v
        Fj_dict[k] = value
    return Fj_dict

# input should be list of numbers
def calc_avg(nums_copy):
    nums = nums_copy.copy()
    count = 0
    sum = 0
    for i in nums:
        count += 1
        sum += i
    result = round(sum / count, 2)
    return result

# input should be abs_freq
# output is a list with the different moda
# that is if there's more than one moda
def calc_moda(nums_copy):
    nums = nums_copy.copy()
    nums_list = []
    moda = []
    for k, v in nums.items():
        nums_list.append(k)
        nums_list.append(v)
    nums_values = nums_list[1::2]
    max_value = max(nums_values)
    indx = []
    print(nums_list)
    print(nums_values)
    for c, i in enumerate(nums_values):
        if i == max_value and c == 0:
            moda.append(nums_list[0])
        elif i == max_value and c != 0:
            moda.append(nums_list[c*2])
    return moda

numbers = "32 65 65 65 45 ---- 65bugjy32 23 32 23 43 43 23"
carattere = "Età"

caratteri = turn_list(numbers)

abs_freq = calc_abs_freq(caratteri)

rel_freq = calc_rel_freq(abs_freq)

perc_freq = calc_perc_freq(rel_freq)

cum_freq = calc_cum_freq(rel_freq)

moda = calc_moda(abs_freq)

print(abs_freq)
print(moda)