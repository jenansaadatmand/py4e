# Chapter 1, page 43: 
# A program to calculate interest on home loan
# The principal is the amount of funding borrowed for your home loan
# Interest is the money paid monthly for use of the loan.

principal = input('Enter principle amount borrowed for your home loan:\n')
principal = int(principal)
rate = input('Enter rate:\n')
rate = int(rate)/100
interest = principal * rate 
print(interest)


