# Author: Jacob Noethiger jln5438@psu.edu
# Collaborator:Travis Navarro trn5106@psu.edu
# Collaborator:Minsoo Joo mbj5335@psu.edu
# Collaborator:Shravani Samala sjs7049@psu.edu
# Section:2
# Breakout:4
def getLetterGrade(grade):
  letter="F"
  if(grade>=93.0):
    print("Your letter grade for CMPSC 131 is A.")
    letter="A"
  elif(grade>=90.0 and grade<93):
    print("Your letter grade for CMPSC 131 is A-.\n");
    letter="A-"
  elif(grade>=87):
    print("Your letter grade for CMPSC 131 is B+.\n");
    letter="B+"
  elif(grade>=83):
    print("Your letter grade for CMPSC 131 is B.\n");
    letter="B"
  elif(grade>=80):
    print("Your letter grade for CMPSC 131 is B-.\n");
    letter="B-"
  elif(grade>=77):
    print("Your letter grade for CMPSC 131 is C+.\n");
    letter="C+"
  elif(grade>=70):
    print("Your letter grade for CMPSC 131 is C.\n");
    letter="C"
  elif(grade>=60):
    print("Your letter grade for CMPSC 131 is D.\n");
    letter="D"
  else:
    print("Your letter grade for CMPSC 131 is F.\n");
    letter="F"
  return letter

def run():
  grade=float(input("Enter your CMPSC 131 grade: "))
  getLetterGrade(grade)

if __name__=="__main__":
  run()

  