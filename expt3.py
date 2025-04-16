
'''
Mohd Qazim Ansari
Fe-D
241P105/36
'''

import math

bs = float(input("Enter the basic salary (BS): "))

da = math.ceil(bs * 0.70)
ta = math.ceil(bs * 0.30)
hra = math.ceil(bs * 0.10)

gross_salary = bs + da + ta + hra

print(f"Basic Salary (BS):        {bs:.2f}\n")
print(f"Dearness Allowance:       {da:.2f}")
print(f"Travel Allowance:         {ta:.2f}")
print(f"House Rent Allowance:     {hra:.2f}")
print(f"Gross Salary:             {gross_salary:.2f}")
