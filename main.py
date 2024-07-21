import time

PrimesAmount = 500 #number of prime numbers to generate

start = time.perf_counter()

PrimesList = [2]
count = 1
NotPrime = False
while len(PrimesList) != PrimesAmount:
  count += 2 #after the prime number 2, all primes are odd so we can skip even numbers
  for x in PrimesList[1:]:#[1:] to skip first number (2)
    if count % x == 0:
      NotPrime = True
      break
  if NotPrime:
    NotPrime = False
    continue
  PrimesList.append(count)

end = time.perf_counter()
print(f"Found {len(PrimesList)} primes in {end-start} seconds")
print(PrimesList)

#generator that generates primes
def Primes():
  PrimesList = [2]
  count = 1
  yield 2
  NotPrime = False
  while True:
    count += 2
    for x in PrimesList[1:]:
      if count % x == 0:
        NotPrime = True
        break
    if NotPrime:
      NotPrime = False
      continue
    yield count
    PrimesList.append(count)
