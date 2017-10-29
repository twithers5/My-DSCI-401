# This is a test driver for our functions defined in basic_functions.py

# Import the module and name as bs
import basic_functions as bs

# Test the add_2 function defined in bs
print(bs.add_2(3,5))
print(bs.add_2(4,6))
print(bs.add_2(7,8))

# Test the my_range function.
print(bs.my_range(1,50))
print(bs.my_range(1,50,3))
print(bs.my_range(1,50,by=4))
print(bs.my_range(1,11,by=3))

# Test the triangle-printing function 
bs.print_triangle(3)
#print(\n\n)
bs.print_triangle(5)
#print(\n\n)
bs.print_triangle(5, full=True)

# Test
print(bs.histogram(['a','x',2,'x',3,2]))


path = 'data/sample_text.txt'
print(bs.word_counts(path, case_sensitive = False))

print(bs.my_max([4,2,6,1,7,9,0,6,4]))

print(bs.variable_number_of_inputs(2,3))
print(bs.variable_number_of_inputs(2,3,4,5,6, "Something","Else"))

# Test the fzip function
print(bs.fzip(lambda x,y:x+y,[1,2,3],[4,5,6]))
print(bs.fzip(max,[1,2,3],[4,5,6],[7,8,9]))

# Test the sum_range function.
print(bs.sum_range(1,10))
print(bs.sum_range(1,100))

# Test the rrev function
print(bs.rrev([1,2,3,4,5]))

# Test the fib function
print(bs.fib(1,1,6))
print(bs.fib(1,1,7))
print(bs.fib(1,1,8))

# Test the mfib function
print(bs.mfib(1,1,100))

# Test the cp function.
print(bs.cp([1,2],[3,4]))
print(bs.cp([1,2],[3,4],[5,6,7]))

# Test the kcomb function
print(bs.kcomb([1,2,3,4],2))
print(bs.kcomb([1,2,3,4,5,6],3))

# Print combinations as tuples
print(map(lambda x: tuple(x), bs.kcomb([1,2,3,4,5,6],3)))

# Test the pipe function
f1 = lambda x: x + 3
f2 = lambda x: x * x
f3 = lambda x: x / 2.3
f4 = lambda x: x ** 0.5

# Construct a new function that pipes the above in sequence
my_pipe = bs.pipe(f1,f2,f3,f4)

# Apply my_pipe to the numbers [1,2,3 ... 20]
print(map(my_pipe, range(1,21)))









