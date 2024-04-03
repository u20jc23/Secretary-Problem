import random

#creates a list of 100 random values between 1 and 100
envelopes = [random.randint(1,100)for i in range(100)]

def strategy(envelopes):
  """
  Applies the Strategy to the secretary problem
  Input: A list of 100 values
  Output: The highest Value picked, The highest value found on the first sweep, The highest value in the list
  """
  
  highest_found = envelopes[0]
  highest_picked = 0
  
  # establishes the highest of the first 37 values
  for i in range(1,38):
    if envelopes[i] > highest_found:
      highest_found = envelopes[i]
      
  # sweeps through the rest of the list until it finds a value greater than the highest found
  for i in range(37,100):
    if envelopes[i] > highest_found:
      highest_picked = envelopes[i]
    return highest_picked, highest_found, max(envelopes)
  # if a higher value is not found this returns the last envelope
  return envelopes[-1], highest_found, max(envelopes)


def effective(value):
  """
  Tests if the strategy is effective or not
  Input: A value which determines the maximum value that can be randomly generated
  Output: The average successful attempts of the strategy as well as the average value picked
  """
  
  results = []
  accuracy = 0
  avg_value = 0
  n = 10000
  
  # records n iterations of the strategy for the given maximum value
  for i in range(n):
    envelopes2 = [random.randint(1,value) for i in range(100)]
    results.append(strategy(envelopes2))
  # returns the success rate as well as the average value picked
  for i in results:
    if i[0]>i[1]:
      accuracy += 1
    avg_value += i[0]
  return avg_value/n,(accuracy/n)*100

s = []
for i in range(10):
  s.append(effective(100))
print(s)
