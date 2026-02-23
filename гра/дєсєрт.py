desserts = {
    "Ice cream":10,
    "Brownies":12,
    "Swiss roll":5,
    "Cheesecake":3,
    "Cup cake":2
}
keys = desserts.keys()
print(keys)

sorted_keys = sorted(keys)
print(sorted_keys)

sorted_desserts = {}
for key in sorted_keys:
    sorted_desserts[key] = desserts[key]

print(sorted_desserts)