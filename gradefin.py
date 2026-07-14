def calculate_grade(name, mark):
  if mark>=90 and mark<=100:
    print(f"{name} grade is A+")
  elif mark>=80 and mark<=80:
    print(f"{name} grade is B")
  elif mark>=70 and mark<=80:
    print(f"{name} grade is C")
  else:
    print(f"{name} grade is D")
    
grades = {
  'ram' : 90,
  'hari' : 85,
  'Gita' : 71,
  'Sita' : 69,
  'Prity' : 55,
  'Sital' : 45
}

for k, v in grades.items():
  calculate_grade(k,v)