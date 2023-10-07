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

def turn_list2(num: str):
    sum_list = []
    count = 0
    num_2 = 0
    sum_list_int = []
    result = []
    for i in num:
        if i.isnumeric():
            count = 0
            int_i = int(i)
            sum_list.append(int_i)
        else:
            if count<1:
                sum_list.append(" ")
                count += 1
                continue
            else:
                continue
    for i in sum_list:
        count = 0
        if type(i) == int:
            sum_list_int.append(str(i))
        else:
            for n in sum_list_int:
                if count == 0:
                    n_result = str(n)
                    count += 1
                else:
                    n_result = str(n_result+n)
            if n_result:
                result.append(n_result)
            sum_list_int = []
    print(result)

def calc_abs_freq(num_list):
    nj_dict = {}
    for i in num_list:
        nj_i = num_list.count(i)
        nj_dict[i] = nj_i
    return(nj_dict)

def calc_rel_freq(nj_dict):
    fj_dict = {}
    N = 0
    for v in nj_dict.values():
        N += v
    for k, v in nj_dict.items():
        fj_dict[k] = round((v / N), 2)
    return fj_dict

numbers = "44 32 45 65 32 23 23 23 23 23 43 43 60 23 16"
carattere = "Età"

caratteri = turn_list(numbers)

print(caratteri)

abs_freq = calc_abs_freq(caratteri)

print(abs_freq)

rel_freq = calc_rel_freq(abs_freq)

print(rel_freq)