seating_chart = [
    ["Sarah", "CLaire", "Ben", "Taylor", "Eva"],
    ["Frankie", "George", "Lindsey", "Izzy", "Jack"],
    ["Katherine", "Lauren", "Mary", "Nathan", "Olive"],
    ["Chad", "April", "Matt", "Thomas", "Penny"]
]

#print(seating_chart[2][1])

for i, row in enumerate(seating_chart):
  for j, student_name in enumerate(row):
    print(f"fila {i+1}, asiento {j+1}, estudiante {student_name}")
