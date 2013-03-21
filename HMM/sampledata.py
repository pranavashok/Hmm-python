from calculator import HMM
v = {"s": {  "t" :.7 ,  "r" : .2  }, "t" :{ "s" : 6 } }
Alpha=[]
learnSample={"abba","bab" }
model= HMM( { "s": .85, "t" : .15}, 
		{"s" : {  "t" :.7 ,  "s" : .3  },"t" : { "s" : .1 , "t" : .9} }, 
		{"s" : { "a" : .4, "b": .6}, "t" : { "a" : .5, "b": .5} } )
model.generate()
model.forward(learnSample)
#for key,value in Alpha:
#	print value
	


