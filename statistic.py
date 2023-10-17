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
    total_sum = sum(numbers)
    total_count = len(numbers)
    avg = total_sum / total_count
    return avg

# input should be abs_freq
# output is a list with the different moda
# that is if there's more than one moda
def calc_moda(nums_copy):
    nums = nums_copy.copy()
    value_list = [i for i in nums_copy.values()]
    max_value = max(value_list)
    moda = {key: value for (key, value) in nums.items() if value == max_value}
    return moda

# input should be list of numbers
def calc_median(nums_copy):
    nums = nums_copy.copy()
    length = len(nums)
    nums.sort()
    if length % 2 == 0:
        n1 = nums[length // 2-1]
        n2 = nums[length // 2]
        median = (n1 + n2) / 2
    else:
        median = nums[length // 2]
    return median

# input should be list of numbers
def calc_quartili(nums_copy):
    nums = nums_copy.copy()
    length = len(nums)
    nums.sort()
    q2 = calc_median(nums)
    if length % 2 == 0:
        nums_1 = nums[:length // 2]
        q1 = calc_median(nums_1)
        nums_3 = nums[length // 2:]
        q3 = calc_median(nums_3)
    else:
        nums_1 = nums[:(length // 2)+1]
        q1 = calc_median(nums_1)
        nums_3 = nums[length // 2:]
        q3 = calc_median(nums_3)
    quartili = {}
    quartili["Q0"] = nums[0]
    quartili["Q1"] = q1
    quartili["Q2"] = q2
    quartili["Q3"] = q3
    quartili["Q4"] = nums[-1]
    return quartili

# input should be list of numbers
# return coeficciente di variazione, varianza, scarto_q_medio
def calc_variabilita(nums_copy):
    nums = nums_copy.copy()
    media = calc_avg(nums)
    devianza = 0
    for i in nums:
        valore = (i - media)**2
        devianza += valore
    varianza = devianza / len(nums)
    scarto_q_medio = sqrt(varianza)
    cv = (scarto_q_medio / media) * 100
    return cv, varianza, scarto_q_medio

def calc_scost_mediana(nums_copy):
    nums = nums_copy.copy()
    mediana = calc_median(nums)
    sum = 0
    for i in nums:
        valore = abs(i - mediana)
        sum += i
    scost_mediana = sum / len(nums)
    return scost_mediana

# return indice_fisher
def calc_asimmetria(nums_copy):
    nums = nums_copy.copy()
    media = calc_avg(nums)
    sum = 0
    for i in nums:
        valore = (i - media)**3
        sum += valore
    indice_asimm = sum / len(nums)
    result = calc_variabilita(nums_copy)
    scarto_q_medio = result[2]
    indice_fisher = indice_asimm / (scarto_q_medio**3)
    return indice_fisher



numbers = [26, 28, 29, 29, 30, 32, 32, 33, 35, 36, 36, 37,37,37,39,39,42,42,43,47,48]
#numbers = [0,2,6,8,11,15,17,17,18,18,19,19,20,23,23,23,24,26,27,27,28]

cv, varianza, scarto_q_medio = calc_variabilita(numbers)

fisher = calc_asimmetria(numbers)

media = calc_avg(numbers)
mediana = calc_median(numbers)
abs_freq = calc_abs_freq(numbers)
moda = calc_moda(abs_freq)

quart = calc_quartili(numbers)

print("————————————————————————")
print(quart)
print()

print(f"Mediana: {mediana}\nMedia: {media}\nModa: {moda}\n")

print(f"Coeff. var.: {cv}\nVarianza: {varianza}\nScarto Q Medio: {scarto_q_medio}")
print(f"Indice di Fisher= {fisher}")
print("————————————————————————")