num_p = int(input("Number of purchases: "))
s_tax = float(input("Sales tax: "))

c_name = []
c_cost = []

for i in range(num_p):
    name = input("Customer: ")
    cost = int(input("Cost: "))
    c_name.append(name)
    c_cost.append(cost)

def add_tax(cost_list, sale_tax):
    new_list = []
    for i in cost_list:
        result = sale_tax*i+i
        new_list.append(result)
    return new_list

dict = {}

final_list= add_tax(c_cost,s_tax)
for i in range(len(final_list)):
    if c_name[i] in dict:
        dict[c_name[i]] = final_list[i] + dict[c_name[i]]
    else:
        dict[c_name[i]] = final_list[i]

print(dict)


