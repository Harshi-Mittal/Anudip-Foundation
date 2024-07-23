import pickle
f=open("anudip1.dat","wb")
li=[10,20,30,40,50]
pickle.dump(li,f)
f.close()
