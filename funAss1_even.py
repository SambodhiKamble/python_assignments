def get_even_numbers(nums):
    even_numbers=[]

    for n in nums:
        if n%2==0:
            even_numbers.append(n)
        print(even_numbers)

get_even_numbers([1,2,3,4,5])