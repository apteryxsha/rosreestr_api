t_arr = []
with open('adr_lst.txt','r') as t_in:
    l=t_in.read().split(',')
for row in l:
        print(row)
        print()