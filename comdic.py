#comprehesion dictionary on python programming
score = {
  "sangam" : 98,
  "Jeevan" : 87,
  "Sanjok" : 23,
  "Aadarshan" : 56
}
top_marks = {name : marks for name, marks in score.items() if marks>80}
print(top_marks)
