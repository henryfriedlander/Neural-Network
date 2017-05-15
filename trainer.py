from scipy import optimize

class trainer:
	def __init__(self, network):
		self.N = network

	def wrapper(self, weights, X, y):
		self.N.setParams(params)
		cost = self.N.costFunction()
		gradient = self.N.computeGradients()
		return cost, gradient

	  def train(self, X, y):
        #Make an internal variable for the callback function:
        self.X = X
        self.y = y

        #Make empty list to store costs:
        self.J = []
        
        params0 = self.N.getParams()

        options = {'maxiter': 200, 'disp' : True}
        _res = optimize.minimize(self.wrapper, params0, jac=True, method='BFGS', \
                                 args=(X, y), options=options, callback=self.callback)

        self.N.setParams(_res.x)
        self.optimizationResults = _res