PrimesAmount = 10000 #number of prime numbers to generate

PrimesList = [2]
count = 2
while len(PrimesList) != PrimesAmount:
  count += 1
  A = [False]*len(PrimesList)
  for x in PrimesList:
    if count % x == 0:
      A[PrimesList.index(x)] = True
  if any(A):
    continue
  PrimesList.append(count)

print(PrimesList)