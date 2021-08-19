
#1
import xlrd
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_excel("Covid19IndiaData_30032020.xlsx")
d={}
for i in data["Age"]:
    d[i]=0
for i in data["Age"]:
    d[i]=d[i]+1
#a
x=[i for i in d.keys()]
y=[float(i/1315) for i in d.values()]
plt.bar(x,y)
plt.xlabel("X = Age of infected person")
plt.ylabel("P(X)")
plt.show()

E=0
e=0
for i,j in d.items():
    E=E+i*j
    e=e+i*i*j
print("Expected age of an infected patient =",E/1315)
print("Variance =",(e-(E*E)/1315)/1315)

#b
data1=data[data["StatusCode"]=="Dead"]
l=[]
d1={}
for i in data1["Age"]:
    l.append(i)
for i in l:
    d1[i]=float(l.count(i)/len(l))
x=[i for i in d1.keys()]
y=[i for i in d1.values()]
plt.bar(x,y)
plt.xlabel("X = Age of dead patient")
plt.ylabel("P(X)")
plt.show()
E1=0
e1=0
for i,j in d1.items():
    E1=E1+i*j
    e1=e1+i*i*j
print("Expected age of a dead patient =",E1)
print("Variance =",e1-(E1*E1))
    
data2=data[data["StatusCode"]=="Recovered"]
l=[]
d2={}
for i in data2["Age"]:
    l.append(i)
for i in l:
    d2[i]=float(l.count(i)/len(l))
x=[i for i in d2.keys()]
y=[i for i in d2.values()]
plt.bar(x,y)
plt.xlabel("X = Age of recovered patient")
plt.ylabel("P(X)")
plt.show()
E2=0
e2=0
for i,j in d2.items():
    E2=E2+i*j
    e2=e2+i*i*j
print("Expected age of a recovered patient =",E2)
print("Variance =",e2-(E2*E2))

#c
data3=data[data["GenderCode0F1M"]==0]
l=[]
d3=d.copy()
for i in data3["Age"]:
    l.append(i)
for i in d3.keys():
    d3[i]=float(l.count(i)/len(l))
x=[i for i in d3.keys()]
y=[i for i in d3.values()]
plt.bar(x,y)
plt.xlabel("X = Age of infected person")
plt.ylabel("P(X|Patient is Female)")
plt.show()
E3=0
for i,j in d3.items():
    E3=E3+i*j
print("Expected age of an infected patient given that the patient is a female =",E3)

data4=data[data["GenderCode0F1M"]==1]
l=[]
d4=d.copy()
for i in data4["Age"]:
    l.append(i)
for i in d4.keys():
    d4[i]=float(l.count(i)/len(l))
x=[i for i in d4.keys()]
y=[i for i in d4.values()]
plt.bar(x,y)
plt.xlabel("X = Age of infected person")
plt.ylabel("P(X|Patient is male)")
plt.show()
E4=0
for i,j in d4.items():
    E4=E4+i*j
print("Expected age of an infected patient given that the patient is a male =",E4)

#2
import xlrd
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
data=pd.read_excel("linton_supp_tableS1_S2_8Feb2020.xlsx",skiprows=1)
data["Onset"]=data["Onset"].fillna("abc")
data=data[data["Onset"]!="abc"]
data1=data[data["ExposureType"]!="Lives-works-studies in Wuhan"]
data1["ExposureL"]=data1["ExposureL"].fillna("abc")
data1=data1[data1["ExposureL"]!="abc"]
data2=data[data["ExposureType"]=="Lives-works-studies in Wuhan"]
data2["ExposureL"]=data2["ExposureL"].fillna(pd.Timestamp('2019-12-01'))
#a
l=[]
m=[]
n=[]
for i in data1["ExposureL"]:
    l.append(i)
for i in data1["Onset"]:
    m.append(i)
for i in data2["ExposureL"]:
    l.append(i)
for i in data2["Onset"]:
    m.append(i)
for i in range(len(l)):
    x=m[i]-l[i]
    n.append(x.days)
d={}
for i in n:
    d[i]=n.count(i)
x=[i for i in d.keys()]
y=[float(i/len(n)) for i in d.values()]
plt.bar(x,y)
plt.xlabel("X = Incubation period")
plt.ylabel("P(X)")
plt.show()

E=0
e=0
for i,j in d.items():
    E=E+i*j
    e=e+i*i*j
print("Expected incubation period =",E/len(n))
print("Variance =",(e-(E*E)/len(n))/len(n))

#b
l1=[]
m1=[]
n1=[]
for i in data1["ExposureL"]:
    l1.append(i)
for i in data1["Onset"]:
    m1.append(i)
for i in range(len(l1)):
    x=m1[i]-l1[i]
    n1.append(x.days)
d1={}
for i in n1:
    d1[i]=n1.count(i)
x=[i for i in d1.keys()]
y=[float(i/len(n1)) for i in d1.values()]
plt.bar(x,y)
plt.xlabel("X = Incubation period of non-residents of wuhan")
plt.ylabel("P(X)")
plt.show()

E1=0
for i,j in d1.items():
    E1=E1+i*j
print("Expected incubation period of non-residents of wuhan=",E1/len(n1))
print(''' On seeing the above graphs and incubation period one
  can say that for Wuhan residents the incubation
  period was very long they dont show symptoms early 
  while those who are from outside of Wuhan showed symptoms 
  very early after infection. ''')
print('\n')

#c
data=pd.read_excel("linton_supp_tableS1_S2_8Feb2020.xlsx",skiprows=1)
data["Onset"]=data["Onset"].fillna("abc")
data=data[data["Onset"]!="abc"]
data["DateHospitalizedIsolated"]=data["DateHospitalizedIsolated"].fillna("abc")
data3=data[data["DateHospitalizedIsolated"]!="abc"]

l2=[]
m2=[]
n2=[]
for i in data3["DateHospitalizedIsolated"]:
    l2.append(i)
for i in data3["Onset"]:
    m2.append(i)
for i in range(len(l2)):
    x=l2[i]-m2[i]
    n2.append(x.days)
d2={}
for i in n2:
    d2[i]=n2.count(i)
x=[i for i in d2.keys()]
y=[float(i/len(n2)) for i in d2.values()]
plt.bar(x,y)
plt.xlabel("X = Onset to hospitalisation for surviving patients")
plt.ylabel("P(X)")
plt.show()
    
E2=0
for i,j in d2.items():
    E2=E2+i*j
print("Expected Onset to hospitalisation for surviving patients =",E2/len(n2))

data4=pd.read_excel("linton_supp_tableS1_S2_8Feb2020.xlsx","TableS2",skiprows=1)
data4["Onset"]=data4["Onset"].fillna("abc")
data4["Hospitalization/Isolation"]=data4["Hospitalization/Isolation"].fillna("abc")
data4["Death"]=data4["Death"].fillna("abc")
data4=data4[data4["Onset"]!="abc"]
data4=data4[data4["Hospitalization/Isolation"]!="abc"]
data4=data4[data4["Death"]!="abc"]
l3=[]
m3=[]
n3=[]
for i in data4["Onset"]:
    l3.append(i)
for i in data4["Hospitalization/Isolation"]:
    m3.append(i)
for i in data4["Death"]:
    n3.append(i)
p=[]
q=[]
r=[]
for i in range(len(l3)):
    x=m3[i]-l3[i]
    p.append(x.days)
for i in range(len(l3)):
    x=n3[i]-l3[i]
    q.append(x.days)
for i in range(len(l3)):
    x=n3[i]-m3[i]
    r.append(x.days)
d3={}
for i in p:
    d3[i]=p.count(i)
x=[i for i in d3.keys()]
y=[float(i/len(p)) for i in d3.values()]
plt.bar(x,y)
plt.xlabel("X = Onset to hospitalisation for dead patients")
plt.ylabel("P(X)")
plt.show()

E3=0
for i,j in d3.items():
    E3=E3+i*j
print("Expected Onset to hospitalisation for dead patients =",E3/len(p))

d4={}
for i in q:
    d4[i]=q.count(i)
x=[i for i in d4.keys()]
y=[float(i/len(q)) for i in d4.values()]
plt.bar(x,y)
plt.xlabel("X = Onset to death")
plt.ylabel("P(X)")
plt.show()

d5={}
for i in r:
    d5[i]=r.count(i)
x=[i for i in d5.keys()]
y=[float(i/len(r)) for i in d5.values()]
plt.bar(x,y)
plt.xlabel("X = Hospitalisation to death")
plt.ylabel("P(X)")
plt.show()

print('''From the graph it is evident that those who survived were hospitalised
  early between 0-5 days of infection while those who are dead were
  hospitalised in 5-10 days after infection''')



