import random
a=0
b=0
i=0
skaki1=[1,2,3,4,5,6,7,8]
skaki2=[1,2,3,4,5,6,7]
print("!ΓΙΑ ΣΚΑΚΙΕΡΑ 8*8!")
while (100-i)>0 :
	i +=1
	x=random.choice(skaki1)
	y=random.choice(skaki1)
	z=random.choice(skaki1)
	w=random.choice(skaki1)
	while (x==z and y==w) :
		x=random.choice(skaki1)
		y=random.choice(skaki1)
		z=random.choice(skaki1)
		w=random.choice(skaki1)
	if(x==z or y==w):
		a=a+1
	elif((z-x)==(w-y) or (z-x)==(y-w) or (x-z)==(w-y) or (x-z)==(y-w)) :
		b=b+1
	else :
		a=a
		b=b
print("Ο μαύρος αξιωματικός κέρδισε",b,"πόντους")
print("Ο λευκός πύργος κέρδισε",a,"πόντους")
print("!ΓΙΑ ΣΚΑΚΙΕΡΑ 7*8!")
i=0
a=0
b=0
while (100-i)>0 :
	i +=1
	x=random.choice(skaki2)
	y=random.choice(skaki1)
	z=random.choice(skaki2)
	w=random.choice(skaki1)
	while (x==z and y==w) :
		x=random.choice(skaki2)
		y=random.choice(skaki1)
		z=random.choice(skaki2)
		w=random.choice(skaki1)
	if(x==z or y==w):
		a=a+1
	elif((z-x)==(w-y) or (z-x)==(y-w) or (x-z)==(w-y) or (x-z)==(y-w)) :
		b=b+1
	else :
		a=a
		b=b
print("Ο μαύρος αξιωματικός κέρδισε",b,"πόντους")
print("Ο λευκός πύργος κέρδισε",a,"πόντους")
print("!ΓΙΑ ΣΚΑΚΙΕΡΑ 8*7!")
i=0
a=0
b=0
while (100-i)>0 :
	i +=1
	x=random.choice(skaki1)
	y=random.choice(skaki2)
	z=random.choice(skaki1)
	w=random.choice(skaki2)
	while (x==z and y==w) :
		x=random.choice(skaki1)
		y=random.choice(skaki2)
		z=random.choice(skaki1)
		w=random.choice(skaki2)
	if(x==z or y==w):
		a=a+1
	elif((z-x)==(w-y) or (z-x)==(y-w) or (x-z)==(w-y) or (x-z)==(y-w)) :
		b=b+1
	else :
		a=a
		b=b
print("Ο μαύρος αξιωματικός κέρδισε",b,"πόντους")
print("Ο λευκός πύργος κέρδισε",a,"πόντους")
