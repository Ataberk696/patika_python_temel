""" Question 1:  Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5] """

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item,list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

#test 
input_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
output = flatten(input_list)
print(output)  # [1, 'a', 'cat', 2, 3, 'dog', 4, 5]




"""Question 2:  Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]] """

def reverse_list(lst):
    reversed_list = []  
    for item in reversed(lst): 
        if isinstance(item, list):  
            reversed_list.append(reverse_list(item)) 
        else: 
            reversed_list.append(item)  
    return reversed_list

#Test
input_list = [[1, 2], [3, 4], [5, 6, 7]]
output = reverse_list(input_list)
print(output)  # [[[7, 6, 5], [4, 3], [2, 1]]]
