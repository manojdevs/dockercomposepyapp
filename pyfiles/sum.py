import redis
chk=1
cache=redis.StrictRedis(host='redis',port=6379,db=0)
while chk!=0:
	opt=int(raw_input("select \n1)create \n2)load \n0)Exit"))
	if(opt==1):
		id=raw_input("Enter id:")
		name=raw_input("Enter name:")
		cache.set(id,name)
	elif(opt==2):
		id=raw_input("Enter id:")
		if cache.get(id):
			print cache.get(id).decode("utf-8")
	else:
		print "invalid opt"
