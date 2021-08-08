def missing(arr, k):
    def calc_missing(idx):
        return arr[idx] - arr[0] - idx

    n = len(arr)
    lt, rt = 0, n - 1
    while lt < rt:
        md = (lt + rt) >> 1
        if calc_missing(md) < k:
            lt = md + 1
        else:
            rt = md
    if calc_missing(lt) < k:
        return k - calc_missing(lt) + arr[lt]
    return k - calc_missing(lt - 1) + arr[lt - 1]


if __name__ == '__main__':
    arr = [2, 3, 5, 9, 10]
    k = 1
    print(missing(arr, k))

    arr = [2, 3, 5, 9, 10, 11, 12]
    k = 4
    print(missing(arr, k))

    arr = [4, 7, 9, 10]
    k = 1
    print(missing(arr, k))

    k = 3
    print(missing(arr, k))

    arr = [1, 2, 4]
    k = 3
    print(missing(arr, k))

