orders={
    'A':50,
    'B':10,
    'C':25,
    'D':30,
    'E':25
}
sort_orders=sorted(orders.items(),key=lambda x:x[1],reverse=True)

for i in sort_orders:
     print(i[0],i[1])