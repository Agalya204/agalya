'''
write a code to calculate income tax in india.
'''
salary = float(input("Enter your salary: "))
deduction = 100000
taxable_income = salary - deduction

# Define tax slabs and rates as tuples (upper limit, rate)
tax_slabs = [
    (250000, 0.0),
    (500000, 0.05),
    (750000, 0.20),
    (1000000, 0.20),
    (1250000, 0.30),
    (1500000, 0.30),
]

tax = 0

for slab_limit, slab_rate in tax_slabs:
    if taxable_income <= 0:
        break
    if taxable_income <= slab_limit:
        tax += slab_rate * taxable_income
        break
    else:
        tax += slab_rate * (slab_limit - max(0, slab_limit - 250000))
        taxable_income -= slab_limit - 250000

print("Tax payable amount is Rs.", tax)
