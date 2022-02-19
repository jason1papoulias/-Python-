import random
print("ΚΑΛΩΣΗΡΘΑΤΕ ΣΤΟ ΠΑΙΧΝΙΔΙ ΜΕ ΤΑ ΚΑΠΑΚΙΑ")
s=0
i=0
lista1=[0,1,2]
lista2=[1,2,3]
tet=[3,3]
rows,cols=(3,3)
tet=[[0]*cols]*rows
while ((100-i)>0) :
	w=0
	i +=1
	while (w<1):
		a=random.choice(lista1)
		b=random.choice(lista1)
		c=random.choice(lista2)
		if (c>tet[a][b]):
			s=s+1
			tet[a][b]=c
			if (tet[0][0]==tet[0][1] and tet[0][1]==tet[0][2]):
				w=w+1
				break
			if (tet[1][0]==tet[1][1] and tet[1][1]==tet[1][2]):
				w=w+1
				break
			if (tet[2][0]==tet[2][1] and tet[2][1]==tet[2][2]):
				w=w+1
				break
			if (tet[0][0]==tet[1][0] and tet[1][0]==tet[2][0]):
				w=w+1
				break
			if (tet[0][1]==tet[1][1] and tet[1][1]==tet[2][1]):
				w=w+1
				break
			if (tet[0][2]==tet[1][2] and tet[1][2]==tet[2][2]):
				w=w+1
				break
			if (tet[0][0]==tet[1][1] and tet[1][1]==tet[2][2]):
				w=w+1
				break
			if (tet[0][2]==tet[1][1] and tet[1][1]==tet[2][0]):
				w=w+1
				break
			if ((tet[0][0]==tet[0][1]+1 and tet[0][1]==tet[0][2]+1) or 					(tet[0][0]==tet[0][1]-1 and tet[0][1]==tet[0][2]-1)):
				w=w+1
				break
			if ((tet[1][0]==tet[1][1]+1 and tet[1][1]==tet[1][2]+1)or(tet[1]			[0]==tet[1][1]-1 and tet[1][1]==tet[1][2]-1)):
				w=w+1
				break
			if ((tet[2][0]==tet[2][1]+1 and tet[2][1]==tet[2][2]+1)or(tet[2]			[0]==tet[2][1]-1 and tet[2][1]==tet[2][2]-1)):
				w=w+1
				break
			if ((tet[0][0]==tet[1][0]+1 and tet[1][0]==tet[2][0]+1)or(tet[0]			[0]==tet[1][0]-1 and tet[1][0]==tet[2][0]-1)):
				w=w+1
				break
			if ((tet[0][1]==tet[1][1]+1 and tet[1][1]==tet[2][1]+1)or(tet[0]			[1]==tet[1][1]-1 and tet[1][1]==tet[2][1]-1)):
				w=w+1
				break
			if ((tet[0][2]==tet[1][2]+1 and tet[1][2]==tet[2][2]+1)or(tet[0]			[2]==tet[1][2]-1 and tet[1][2]==tet[2][2]-1)):
				w=w+1
				break
			if ((tet[0][0]==tet[1][1]+1 and tet[1][1]==tet[2][2]+1)or(tet[0]			[0]==tet[1][1]-1 and tet[1][1]==tet[2][2]-1)):
				w=w+1
				break
			if ((tet[0][2]==tet[1][1]+1 and tet[1][1]==tet[2][0]+1)or(tet[0]			[2]==tet[1][1]-1 and tet[1][1]==tet[2][0]-1)):
				w=w+1
				break
print("Ο μέσος όρος βημάτων για την ολοκλήρωση του παιχνιδιού σε κάθε γύρο έιναι:" , s/100)
