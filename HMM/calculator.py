from state import State
class HMM(object):
	def __init__(self, pi, tran, emm):
		self.States=[]
		self.Pi=pi
		self.Tran=tran
		self.Emm=emm
		self.Alpha=[]
	def generate( self ):
		for key,value in self.Pi.iteritems():
			state=State(key,value)
			self.States.append(state)
		for state in self.States:
			state.tran=self.Tran[state.data]
			state.emm=self.Emm[state.data]
	def forward( self, learnSample):
		for r in learnSample:
			n=len(r)
			for j in range(1 , n ):
				if ( j == 1 ):
					for state in self.States:
						alpha =  self.Pi[state.data]*self.Emm[state.data][r[j]]
						self.Alpha.append({ state.data : alpha })
						
					
				else:
					for state in self.States:
						for key,value in enumerate(self.Alpha):
							if value.has_key(state.data):
								temp=value[state.data]
								for s in self.States:
										temp +=value.get(s.data,0)*self.Tran[s.data][state.data]*self.Emm[state.data][r[j]]
										print temp
							
								value[state.data] +=temp
							#self.Alpha[r]=alpha
			
			
			self.Alpha=[]			
