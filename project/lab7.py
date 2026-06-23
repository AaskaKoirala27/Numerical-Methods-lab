import numpy as np

n=int(input("Enter number of regions: "))

actual=[]
pred=[]

a=-20
b1=4
b2=1.2

for i in range(n):

    print("\nRegion",i+1)

    x1=float(input("Advertising: "))
    x2=float(input("Population: "))
    y=float(input("Actual Sales: "))

    predicted=a+b1*x1+b2*x2

    actual.append(y)
    pred.append(predicted)

actual=np.array(actual)
pred=np.array(pred)

ss_res=np.sum((actual-pred)**2)

mean=np.mean(actual)

ss_tot=np.sum((actual-mean)**2)

r2=1-(ss_res/ss_tot)

error=np.sqrt(ss_res/n)

print("\nPredicted Values")

for i in range(n):
    print("Region",i+1,"=",round(pred[i],2))

print("\nR² =",round(r2,4))

print("Error Propagation =",round(error,2))

if r2>0.8:
    print("Reliable Model")

else:
    print("Model Requires Improvement")




    