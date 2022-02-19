import random
a=0
b=0
i=0
skaki=[1,2,3,4,5,6,7,8]
while (100-i)>0 :
	i +=1
	print("Γύρος ΝΟ.",i)
	x=random.choice(skaki)
	y=random.choice(skaki)
	z=random.choice(skaki)
	w=random.choice(skaki)
	k=random.choice(skaki)
	m=random.choice(skaki)
	while ((x==z and y==w) or (x==k and y==m) or (z==k and w==m)) :
		x=random.choice(skaki)
		y=random.choice(skaki)
		z=random.choice(skaki)
		w=random.choice(skaki)
		k=random.choice(skaki)
		m=random.choice(skaki)
	if (x==k or y==m) :
		a=a+1
		print("Νίκησε ο λευκός πύργος την μαύρη βασίλισσα")
	if((k-x)==(m-y) or (k-x)==(y-m) or (x-k)==(m-y) or (x-k)==(y-m)) :
		a=a+1
		print("Νίκησε ο λευκός αξιωματικός την μαύρη βασίλισσα")
	if (k==x or m==y):
		b=b+1
		print("Νίκησε η μαύρη βασίλισσα τον λευκό πύργο")
	if (k==z or m==w):
		b=b+1
		print("Νίκησε η μαύρη βασίλισσα τον λευκό αξιωματικό")
	if ((k-x)==(m-y) or (k-x)==(y-m) or (x-k)==(m-y) or (x-k)==(y-m)) :
		b=b+1
		print("Νίκησε η μαύρη βασίλισσα τον λευκό πύργο")
	if ((k-z)==(m-w) or (k-z)==(w-m) or (z-k)==(m-w) or (z-k)==(w-m)):
		b=b+1
		print("Νίκησε η μαύρη βασίλισσα τον λευκό αξιωματικό")
print("Ο μαύρος παίκτης κέρδισε ",b," πόντους")
print("Ο λευκός παίκτης κέρδισε ",a," πόντους")
