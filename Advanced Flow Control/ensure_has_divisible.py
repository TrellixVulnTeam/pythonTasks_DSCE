items = [2, 25, 9]
divisor = 12

for item in items:
    if item % divisor == 0:
        found = item
        break
else:
    items.append(divisor)
    found = divisor

print("{items} contains {found} which is a multiple of {divisor}"
      .format(**locals()))
