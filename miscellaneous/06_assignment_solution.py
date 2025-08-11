
#### Q1.

# num = int(input("Enter a number to cal. the cube till the number: "))

# cube_list = list(map(lambda x: x**3, range(1, num+1)))
# print(cube_list)


#### Q2.

# strings = ['alexander','joe','tiffany','ana','max','george']

# string_list = list(filter(lambda x: len(x)>4, strings))
# print(string_list)


#### Q3.

# from functools import reduce
# num = int(input("Enter a number to cal. its factorial: "))

# factorial = reduce(lambda x,y: x*y, range(1,num+1))
# print(factorial)


#### Q4.

# alist = [1,2,3,4,5,6,7,8,9,10]

# str_list = list(map(lambda x: str(x), alist))
# print(str_list)


#### Q5.

# numbers = [12, 35, 7, 64, 22, 17]

# num_list = list(filter(lambda x: x>20, numbers))
# print(num_list)


#### Q6.

# blist = [1,2,3,4,5,6,7,8,9,10]

# sq_dict = {i:i*i for i in blist if i%2==0}
# print(sq_dict)


#### Q7.

# c_list = [1,2,3,4,5]
# d_list = [1,2,3,4,5]

# mul_list = list(map(lambda x,y: x*y,c_list, d_list))
# print(mul_list)


#### Q8.

# li = ['Hello', 12, True, '92', ' ', 'Morning', 45, '@', 3, False, 40]

# from functools import reduce
# result_list = reduce(lambda x,y: x+y, filter(lambda x: type(x)==int, li))
# print(result_list)


#### Q9.

# given_list = [2,3,4,5,6,7,8,9,10,11]

# def prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             break
#     else:
#         return True
    
# primes = list(filter(prime, given_list))
# print(primes)

