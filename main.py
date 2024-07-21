import time

PrimesAmount = 30 #number of prime numbers to generate

start = time.perf_counter()

PrimesList = [2]
count = 1
while len(PrimesList) != PrimesAmount:
  count += 2 #after 2, all primes are odd so we can skip even numbers
  NotPrimeBoolList = [False]*len(PrimesList)
  for x in PrimesList[1:]:
    if count % x == 0:
      NotPrimeBoolList[PrimesList.index(x)] = True
  if any(NotPrimeBoolList):
    continue
  PrimesList.append(count)

end = time.perf_counter()

print(end-start)
print(PrimesList)