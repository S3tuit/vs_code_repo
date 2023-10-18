from math import sqrt

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
        fj_dict[k] = round((v / N), 3)
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
        Fj_dict[k] = round(value, 3)
    return Fj_dict

# input should be numbers or abs freq.
def calc_avg(nums_copy):
    if type(nums_copy) == list:
        nums = nums_copy.copy()
        total_sum = sum(numbers)
        total_count = len(numbers)
        avg = total_sum / total_count
        return avg
    elif type(nums_copy) == dict:
        total = sum(value * frequency for value, frequency in nums_copy.items())
        length = sum(nums_copy.values())
        return total / length

# input should be abs_freq
# output is a list with the different moda
# that is if there's more than one moda
def calc_moda(nums_copy):
    nums = nums_copy.copy()
    value_list = [i for i in nums_copy.values()]
    max_value = max(value_list)
    moda = {key: value for (key, value) in nums.items() if value == max_value}
    return moda

# input should be list of numbers or cum freq.
def calc_median(nums_copy, q):
    nums = nums_copy.copy()
    if isinstance(nums, list):
        length = len(nums)
        nums.sort()
        if length % 2 == 0:
            n1 = nums[length // 2-1]
            n2 = nums[length // 2]
            median = (n1 + n2) / 2
        else:
            median = nums[length // 2]
        return median

    elif isinstance(nums, dict):
        if q == 2:
            for value, freq in nums.items():
                if freq > 0.5:
                    median = value
                    return median
        elif q == 1:
            for value, freq in nums.items():
                if freq > 0.25:
                    q1 = value
                    return q1
        elif q == 3:
            for value, freq in nums.items():
                if freq > 0.75:
                    q3 = value
                    return q3


# input should be list of numbers or cum freq.
def calc_quartili(nums_copy):
    nums = nums_copy.copy()
    length = len(nums)
    quartili = {}
    if isinstance(nums, dict):
        key_nums = list(nums.keys())
        quartili["Q0"] = key_nums[0]
        quartili["Q1"] = calc_median(nums, 1)
        quartili["Q2"] = calc_median(nums, 2)
        quartili["Q3"] = calc_median(nums, 3)
        quartili["Q4"] = key_nums[-1]
        return quartili

# input should be list abs freq.
# return coeficciente di variazione, varianza, scarto_q_medio
def calc_variabilita(nums_copy):
    nums = nums_copy.copy()
    media = calc_avg(nums)
    devianza = 0
    lenght = sum(nums.values())
    for value, freq in nums.items():
        valore = ((value - media) ** 2) * freq
        devianza += valore
    varianza = devianza / lenght
    scarto_q_medio = sqrt(varianza)  
    cv = (scarto_q_medio / media) * 100
    return cv, varianza, scarto_q_medio

# input should be list abs freq.
def calc_scost_mediana_perc(nums_copy):
    nums = nums_copy.copy()
    mediana = calc_median(nums, 1)
    summ = 0
    length = sum(nums.values())
    media = calc_avg(nums)
    for value, freq in nums.items():
        valore = abs(value - mediana)*freq
        summ += valore
    scost_mediana = summ / length
    scost_mediana_perc = (scost_mediana * 100) / media
    return scost_mediana_perc

# return indice_fisher
def calc_asimmetria(nums_copy):
    nums = nums_copy.copy()
    media = calc_avg(nums)
    summ = 0
    lenght = sum(nums.values())
    for value, freq in nums.items():
        valore = ((value - media)**3)*freq
        summ += valore
    indice_asimm = summ / lenght
    result = calc_variabilita(nums_copy)
    scarto_q_medio = result[2]
    indice_fisher = indice_asimm / (scarto_q_medio**3)
    return indice_fisher

# input should be nums or abs freq.
def give_overview_box_plot(nums_copy):
    if isinstance(nums_copy, list):
        nums_copy.sort()
        nums_abs_freq = calc_abs_freq(nums_copy)
    nums_rel_freq = calc_rel_freq(nums_abs_freq)
    nums_cum_freq = calc_cum_freq(nums_rel_freq)
    media = calc_avg(nums_abs_freq)
    moda = calc_moda(nums_abs_freq)
    quartili = calc_quartili(nums_cum_freq)
    coeff_variazione, varianza, scarto_q_medio = calc_variabilita(nums_abs_freq)
    scost_mediana_perc = calc_scost_mediana_perc(nums_abs_freq)
    index_fisher = calc_asimmetria(nums_abs_freq)
    li = quartili["Q1"] - (1.5*(quartili["Q3"]-quartili["Q1"]))
    ls = quartili["Q3"] + (1.5*(quartili["Q3"]-quartili["Q1"]))
    print("———————Frequenze———————")
    print(f"Assoluta: {nums_abs_freq}")
    print(f"\nRelativa: {nums_rel_freq}")
    print(f"\nCumulata: {nums_cum_freq}")
    print("\n———————Medie———————")
    print(f"Media: {round(media,3)}")
    print(f"Quartili: {quartili}")
    print(f"Moda: {moda}")
    print("\n———————Box Plot———————")
    print(f"Li: {round(li,3)}")
    print(f"Ls: {round(ls,3)}")
    print("\n———————Varianza———————")
    print(f"Coeff. Var.: {round(coeff_variazione, 3)}%")
    print(f"Varianza: {round(varianza, 3)}")
    print(f"Scarto Q. M.: {round(scarto_q_medio, 3)}")
    print(f"Scost. Mediana: {round(scost_mediana_perc, 3)}%")
    print("\n———————Simmetria———————")
    print(f"Indice Fisher: {round(index_fisher,3)}")


#numbers = [26, 28, 29, 29, 30, 32, 32, 33, 35, 36, 36, 37,37,37,39,39,42,42,43,47,48]
#numbers = [0,2,6,8,11,15,17,17,18,18,19,19,20,23,23,23,24,26,27,27,28]
numbers = [0.4, 0.9, 3.8, 0.4, 2.2, 1.8, 0.4, 3.8, 1.4, 1, 0.7, 4.3, 1.3, 0.1, 0.3, 0.5, 1, 4.1, 1.6, 2.7, 0.6 ]

give_overview_box_plot(numbers)