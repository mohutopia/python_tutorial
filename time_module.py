import time

print(time.time()) # prints the numbers of seconds since 1/1/1970 00:00
def numbers(max):
 time1 = time.time()
 for i in range(0,max):
  print(i)
  time.sleep(0.5) # it pauses 0.5s after every iteration
 time2 = time.time()
 exectution_time = time2 - time1
 print('Execution time: ' + str(exectution_time) + 's.')

numbers(10)

print(time.localtime()) # looks confusing, so we use...
print(time.asctime()) # ah, much better!