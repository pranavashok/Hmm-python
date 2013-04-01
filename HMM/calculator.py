from state import State
class HMM(object):
	def __init__(self, pi, tran, emm):
		self.States = []
		self.Pi = pi
		self.Tran = tran
		self.Emm = emm
		self.Alpha = {}
		self.Beta = {}
		self.Gamma = {}
		self.Prob = {}
	def generate(self):
		for key, value in self.Pi.iteritems():
			self.States.append(key)
	def forward(self, learnSample):
		for r in learnSample:
			for j in xrange(0, len(r)):
				if j == 0:
					for state in self.States:
						self.Alpha[(" ".join(r), j+1, state)] = self.Pi[state]*self.Emm[(state, r[j])]
				else:
					for s1 in self.States:
						alpha = 0
						for s2 in self.States:
							alpha += self.Alpha[(" ".join(r), j, s2)]*self.Tran[(s2, s1)]*self.Emm[(s1, r[j])]
						self.Alpha[(" ".join(r), j+1, s1)] = alpha
	
	def backward(self, learnSample):
		for r in learnSample:
			rdash = r[:]
			rdash.reverse()

			for state in self.States:
				self.Beta[(" ".join(r), len(r), state)] = 1

			for j in xrange(0, len(r)-1):
				for s1 in self.States:
					beta = 0
					for s2 in self.States:
							beta += self.Beta[(" ".join(r), len(r)-j, s2)]*self.Tran[(s1, s2)]*self.Emm[(s2, rdash[j])]
					self.Beta[(" ".join(r), len(r)-j-1, s1)] = beta
	
	def sampleProb(self, learnSample):
		for r in learnSample:
			for s in state:
				self.Prob[r] += self.Alpha[(r, len(r), s)]

	def forwardbackward(self, learnSample):
		self.sampleProb(learnSample)
		for r in learnSample:
			for j in xrange(0, len(r)-1):
				for s1 in self.States:
					for s2 in self.States:
						self.Gamma[(r, j, s1, s2)] = self.Alpha[(r, j, s1)]*self.Tran[(s1, s2)]*self.Emm[(s2, r[j+1])]*self.Beta[(r, j, s2)]/self.Prob[r]

		print self.Gamma