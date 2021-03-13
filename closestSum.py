import numpy as np

def closestSum(target, array1, array2):
    result_matrix = np.zeros((len(array1),len(array2)))

    for i in range(len(array1)):
        for j in range(len(array2)):
            result_matrix[i,j] = array1[i] + array2[j]

    result_matrix -= target
    result_matrix = np.abs(result_matrix)
    print(result_matrix)
    minimum_indices = np.where(result_matrix == np.amin(result_matrix))
    print(minimum_indices)
    print('Closest sums:')
    for i in range(len(minimum_indices[0])):
        print(array1[minimum_indices[0][i]], ' + ', array2[minimum_indices[1][i]])
