#lex_auth_012693795044450304151

def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    for item in reqd_gems:
        if item in gems_list:
            index = gems_list.index(item)
            price = price_list[index]
            bill_amount = bill_amount + ( price * reqd_quantity[reqd_gems.index(item)] )
        else:
            bill_amount = - 1;
            return bill_amount
    if bill_amount >= 30000:
        bill_amount = bill_amount - (5*bill_amount)/100
    return bill_amount

#List of gems available in the store
gems_list=['Amber', 'Aquamarine', 'Opal', 'Topaz']

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list =[4316, 1342, 8734, 6421]

#List of gems required by the customer
reqd_gems=['Amber', 'Topaz']
#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[1, 4]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)