def count_positives_sum_negatives(arr):
    return [] if arr == [] else [len(list(filter(lambda arr:arr > 0, arr))), sum((filter(lambda arr:arr < 0, arr)))]
