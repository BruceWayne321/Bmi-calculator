
name = input("Welcome to bmi calculator, what should we call you? ") 
name = name.upper()

print(">>>", name) 

weight = float(input("Please type your weight(in kg):")) 

height = float(input("Please type your height(in mtrs):")) 

def bmi_cal(w, h):
  bmi = w / h**2
  print(name, " your bmi is ", bmi) 
  if bmi < 18.5 :
    print(name, ", you are underweight, you should start eating") 
  elif bmi < 25 :
    print(name, ", you are healthy, keep it up") 
  elif bmi < 30 :
    print(name, ", you are overweight, you should start eating healthy") 
  else :
    print(name, ", you are obese, you should start working out and eat healthy") 

r = bmi_cal(weight, height) 
  
