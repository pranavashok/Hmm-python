from state import State
class HMM(object):
	def __init__(self, pi, tran, emm):
		self.States=[]
		self.Pi=pi
		self.Tran=tran
		self.Emm=emm
		self.Alpha=[]
		self.Beta=[]
	def generate( self ):
		for key,value in self.Pi.iteritems():
			state=State(key,value)
			self.States.append(state)
		for state in self.States:
			state.tran=self.Tran[state.data]
			state.emm=self.Emm[state.data]
	def forward( self, learnSample):
		for r in learnSample:
			Alpha=[]
			Alpha2=[]
			temp=0
			for j in range(0 , len(r) ):
				if ( j == 0 ):
					for state in self.States:
						alpha =  self.Pi[state.data]*self.Emm[state.data][r[j]]
						Alpha.append({state.data : alpha })
					self.Alpha.append( {j+1 : Alpha} )
				else:
					for state in self.States:
						alpha=0
						for s in self.States:		#requires editting
							for value in Alpha:
								alpha +=value.get(s.data,0)*self.Tran[s.data][state.data]*self.Emm[state.data][r[j]]
						Alpha2.append({state.data : alpha })
					Alpha=Alpha2
					self.Alpha.append( {j+1 : Alpha} )
					Alpha2=[]	
		print self.Alpha
	
	def backward( self,learnSample):
		for r in learnSample:
			r=r[::-1]
			Beta=[]
			Beta2=[]
			temp=0
			for state in self.States:
				Beta.append( {state.data : 1 } )
			self.Beta.append( { len(r) : Beta } )
			for j in range( 0,len(r)-1 ):
				for state in self.States:
					beta=0
					for s in self.States:		#requires editting
						for value in Beta:
							beta +=value.get(s.data,0)*self.Tran[state.data][s.data]*self.Emm[s.data][r[j]]
							#print value.get(s.data,0),self.Tran[state.data][s.data],self.Emm[s.data][r[j]],beta, r[j]
					Beta2.append({state.data : beta })
				Beta=Beta2
				self.Beta.append( { len(r)-j-1 : Beta} )
				Beta2=[]
			print self.Beta

	def gamma( self, learnSample ):
