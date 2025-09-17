numbers=[11,18,31,7,8,232,1055]
def even_num(num):
    return num%2==0
filter_obj=filter(numbers,even_numbers)
even_numbers=list(filter_obj)
print(even_numbers)