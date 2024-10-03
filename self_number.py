kumpulan_bilangan_bukan_self = set()

for i in range(1, 5001):
    bilangan = i + sum(map(int, str(i)))
    if(bilangan < 5001):
        kumpulan_bilangan_bukan_self.add(bilangan)

# print(kumpulan_bilangan_bukan_self)

total_bilangan_bukan_self = sum(kumpulan_bilangan_bukan_self)

print(total_bilangan_bukan_self)
