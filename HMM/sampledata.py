from calculator import HMM
v = {"s": {  "t" :.7 ,  "r" : .2  }, "t" :{ "s" : 6 } }
Alpha=[]
learnSample = [['a', 'b', 'b', 'a'], ['b', 'a', 'b']]

model= HMM({ "s": .85, "t" : .15}, 
		{("s", "t") :.7 ,  ("s", "s") : .3 , ("t", "s"): .1 , ("t", "t") : .9}, 
		{("s", "a"): .4, ("s", "b"): .6, ("t", "a"): .5, ("t", "b"): .5})
model.generate()
model.forward(learnSample)
model.backward(learnSample)
model.forwardbackward(learnSample)