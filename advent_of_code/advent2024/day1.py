l1, l2 = [], []
with open("2024_day1_input.txt") as f:
    for line in f:
        line.rstrip("\n")
        id1, id2 = line.split("   ")
        l1.append(int(id1))
        l2.append(int(id2))

diff = 0
if len(l1) == len(l2):
    for i in range(len(l1)):
        diff += abs(sorted(l1)[i] - sorted(l2)[i])

similarity = 0
l2_set = set(l2)
l2_dict = {i: l2.count(i) for i in l2_set}
for i in l1:
    if i in l2_set:
        similarity += i * l2_dict[i]

print(diff)  # 1970720 <-- correct
print(similarity)  # 17191599 <-- correct
