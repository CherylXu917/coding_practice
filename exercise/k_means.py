import numpy as np


def k_means(arr, k):
    # Step 1: initialization: random patition the arr into k groups
    cluster = np.zeros(len(arr))
    new_cluster = np.random.choice(range(k), len(arr))

    # repeat till cluster is stablized
    iter_n = 0
    while pow((cluster - new_cluster), 2).sum() > 0 and iter_n < 100:
        iter_n += 1
        cluster = new_cluster.copy()
        # Step 2: calculate center
        centers = np.zeros((k, len(arr[0])))
        cluster_ct = np.zeros(k)
        for i, grp in enumerate(cluster):
            centers[grp] = centers[grp] + arr[i]
            cluster_ct[grp] += 1
        for i in range(k):
            centers[grp] /= cluster_ct[grp]

        # Step 3: update the cluster
        for i, n in enumerate(arr):
            new_cluster[i] = 0
            distance = ((n - centers[0]) ** 2).sum()
            for j, c in enumerate(centers[1:], 1):
                cur_distance = ((n - centers[j]) ** 2).sum()
                if cur_distance < distance:
                    new_cluster[i] = j
    return cluster


if __name__ == '__main__':
    # arr = [0, 101, 2, 103, 1, 101, 3, 104]
    arr = np.array([[0,0], [1,1], [100, 100], [101, 101]])
    print(k_means(arr, 2))





