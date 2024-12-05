N1  = int(input())
N2  = int(input())

if N1 > 100 or N2 > 100 and N1 < 10 or N2 < 10:
    print("error")
    exit()

def desc_base_10(n):
        desc = n // 10
        unid = n % 10
        return [desc,unid]
    
n1_desc = desc_base_10(N1)
n2_desc = desc_base_10(N2)

for i in n1_desc:
    for j in n2_desc:
        if i == j:
            print("True")
            exit()

print("False")
exit()