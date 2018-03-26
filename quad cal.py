z=float(input("Enter the coefficient of a: "))

k= float(input("Enter the coefficient of b: "))

s= float(input("Enter the coefficient of c: "))


print("Please wait a moment while we calculate your shiz..")

def quad (a,b,c):

 num1=((b*2)+ (-4*a*c))*0.5

 num2=-b

  den=2*a

  numi=num1+num2

  numo=num1-num2

  answer1=numi/den

  answer2=numo/den

  print("Values of x: ",answer1, "and", answer2)

 

quad(z,k,s)
