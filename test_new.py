from metaheuristics.bees import BeesAlgorithm

from cost_new import cost as cost

class test:
    def __init__(self):

        self.c=cost()


    def run(self):

        d = 20 # dimensionality of solution-space
        n = 100 # size of population, related to amount of bees, bats and fireflies
        range_min, range_max = 0.0, 100.0 # solution-space range (in all dimensions)
        T = 100 # number of iterations

        bees = BeesAlgorithm(d=d, n=n, range_min=range_min, range_max=range_max,
                            nb=50, ne=20, nrb=5, nre=10, shrink_factor=0.8, stgn_lim=5)

        objective = 'min'
        objective_fct = self.c.get_cost

        solution, latency = bees.search(objective, objective_fct, T)

        print(solution)
        bees.plot_history()
        return solution

