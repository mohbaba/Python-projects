def sum_odd(n):
    
    
    if len(n) == 0:
        return 0
    
    else:
        pivot = n[0]
        
        if pivot % 2 == 1:
            return pivot + sum_odd(n[1:])
        else:
            
            return sum_odd(n[1:])
    
                
                
    
print(sum_odd([1,2,3,4,5,6,7,8,9]))












# def bin_search(num_list, target,low,high):
#     if low > high:
#         return None
#     mid = (low + high)//2
        
#     if num_list[mid] == target:
#         return num_list[mid]
#     elif num_list[mid] > target:
#         return bin_search( num_list, target, low,  mid - 1)
#     else:
#         return bin_search(num_list, target, mid + 1, high)
            
# print(bin_search([1,2,3,4,5,6,7],1))










# def qsort(num_list):
    
#     high = []
#     low = []
#     if len(num_list) < 2:
#         return num_list
#     else:
#         pivot = num_list[3]
#         for i in num_list[1:]:
#             if i > pivot:
#                 high.append(i)
#             else:
#                 low.append(i)
                
#         return qsort(low) + [pivot] + qsort(high) 

# print(qsort([5,3,2,4,1]))








# def item_count(num_list):
#     counter = 0
#     if not num_list:
#         return 0
#     else:
#         return 1 + item_count(num_list[1:])
    
        
# print(item_count([1,2,3,4,5,6]))



# def fact(x):
    
#     if x == 1:
#         return 1
#     else:
#        return( x * fact(x-1))
   
        
# print(fact(3))








# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1 
    
    
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             print(mid)
#             break
        
#         elif arr[mid] < target:
            
#             low = mid + 1
            
#         else:
#             high =  mid - 1
#     return None
# binary_search([1,2,3,4,5],2)





















# def small(arr):
    
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(len(arr)):
        
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index
    
    
# # small([3,4,5,1,2])
    
    
# def sorter(arr):
#     new_arr = []
#     for num in range(len(arr)):
#         smallest = small(arr)
#         new_arr.append(arr.pop(smallest))
#     print (new_arr)
    
    
# sorter([3,4,5,2,1])



















# def generateParenthesis(n):
#     result = []
    
#     def backtrack(s, left, right):
#         if len(s) == 2 * n:
#             result.append(s)
#             return 
        
#         if left < n:
#             backtrack(s + '(', left + 1, right)
            
        
#         if right < left:
#             backtrack(s + ')', left, right + 1)
        
#     backtrack('', 0, 0)
#     return result

# # Example usage
# n = 3
# parentheses = generateParenthesis(n)
# print(parentheses)