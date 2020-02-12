def lbs_to_kgs(weight):
    return weight * 0.45


def kgs_to_lbs(weight):
    return  weight / 0.45


def maximum(list):
    max = list[0]
    for num in list:
        if num > max:
            max = num
    return max