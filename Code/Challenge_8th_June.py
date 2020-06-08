

# Write a FUNCTION which takes an integer input, a, and returns the sum a+aa+aaa+aaaa.

 

# So if 2 was the input, the function should return 2+22+222+2222 which is 2468.

  


# three(9) → 11106
# three(5) → 6170


a = int(input("Enter a number:")) ##%s acts as a format specifier - informs python of layout
b = int("%s" % a)  ## = (%s is the absolute value of a )
c = int("%s%s" % (a,a))
d = int("%s%s%s" % (a,a,a))
e = int("%s%s%s%s" % (a,a,a,a))


print(a+b+c+d+e)