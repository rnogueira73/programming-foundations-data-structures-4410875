from collections import deque

def numero_binario(n):
  if n <= 0:
        return
  
  binary_queue = deque()
  binary_queue.append(1)

  for i in range(n):
      binary = binary_queue.popleft()
      print(binary)
      binary_queue.append(binary * 10)
      binary_queue.append(binary * 10 + 1)

n = int(input ("numero:"))
numero_binario(n)