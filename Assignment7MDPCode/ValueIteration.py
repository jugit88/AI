#Artificial Intelligence: A Modern Approach

# Search AIMA
#AIMA Python file: mdp.py

"""Markov Decision Processes (Chapter 17)

First we define an MDP, and the special case of a GridMDP, in which
states are laid out in a 2-dimensional grid.  We also represent a policy
as a dictionary of {state:action} pairs, and a Utility function as a
dictionary of {state:number} pairs.  We then define the value_iteration
and policy_iteration algorithms."""

'''
Answers to questions

1. In the terminal states, there are no actions, therefore None is assigned.
2. The transition probabilities are defined in T function. The probabilities are 
    the action is successful 80% of the time, 10% of the time the action will go to
    the right and 10% to the left.
3. There are a few functions that need to be called to run value_interation, those include
    actions, T, and R.
4. (0,1):0.3984432178350045 (3,1): -1.0 (2,2): 0.7953620878466678
5. Actions are represented as movements along the x or y coordinates in both +/- directions.
    For example, from the start state (0,0), the possible actions would {(1,0),(0,1)}.
    In the general case, the set of actions would be {(1,0),(0,1),(-1,0),(0,-1)}
'''

from utils import *
import math
class MDP:
    """A Markov Decision Process, defined by an initial state, transition model,
    and reward function. We also keep track of a gamma value, for use by
    algorithms. The transition model is represented somewhat differently from
    the text.  Instead of T(s, a, s') being  probability number for each
    state/action/state triplet, we instead have T(s, a) return a list of (p, s')
    pairs.  We also keep track of the possible states, terminal states, and
    actions for each state. [page 615]"""

    def __init__(self, init, actlist, terminals, gamma=.9):
        update(self, init=init, actlist=actlist, terminals=terminals,
               gamma=gamma, states=set(), reward={})

    def R(self, state):
        "Return a numeric reward for this state."
        return self.reward[state]

    def T(state, action):
        """Transition model.  From a state and an action, return a list
        of (result-state, probability) pairs."""
        abstract

    def actions(self, state):
        """Set of actions that can be performed in this state.  By default, a
        fixed list of actions, except for terminal states. Override this
        method if you need to specialize by state."""
        if state in self.terminals:
            return [None]
        else:
            # print self.actlist
            return self.actlist

class GridMDP(MDP):
    """A two-dimensional grid MDP, as in [Figure 17.1].  All you have to do is
    specify the grid as a list of lists of rewards; use None for an obstacle
    (unreachable state).  Also, you should specify the terminal states.
    An action is an (x, y) unit vector; e.g. (1, 0) means move east."""
    def __init__(self, grid, terminals, init=(0, 0), gamma=.9):
        grid.reverse() ## because we want row 0 on bottom, not on top
        MDP.__init__(self, init, actlist=orientations,
                     terminals=terminals, gamma=gamma)
        update(self, grid=grid, rows=len(grid), cols=len(grid[0]))
        for x in range(self.cols):
            for y in range(self.rows):
                self.reward[x, y] = grid[y][x]
                if grid[y][x] is not None:
                    self.states.add((x, y))

    def T(self, state, action):
        jump = False
        if action == None:
            return [(0.0, state)]
        elif jump == True and abs(action[0]+action[1]) > 1:
               return [(0.5,self.go(state,action)),(0.5,state)]
 
        else:
            return [(0.8, self.go(state, action)),
                    (0.1, self.go(state, turn_right(action))),
                    (0.1, self.go(state, turn_left(action)))]

    def go(self, state, direction):
        "Return the state that results from going in this direction."
        state1 = vector_add(state, direction)
        return if_(state1 in self.states, state1, state)

    def to_grid(self, mapping):
        """Convert a mapping from (x, y) to v into a [[..., v, ...]] grid."""
        return list(reversed([[mapping.get((x,y), None)
                               for x in range(self.cols)]
                              for y in range(self.rows)]))

    def to_arrows(self, policy):
        chars = {(1, 0):'>', (0, 1):'^', (-1, 0):'<', (0, -1):'v', None: '.'}
        return self.to_grid(dict([(s, chars[a]) for (s, a) in policy.items()]))


def value_iteration(mdp, epsilon=0.001):
    "Solving an MDP by value iteration. [Fig. 17.4]"
    U1 = dict([(s, 0) for s in mdp.states])
    R, T, gamma = mdp.R, mdp.T, mdp.gamma
    while True:
        U = U1.copy()
        delta = 0
        for s in mdp.states:
            U1[s] = R(s) + gamma * max([sum([p * U[s1] for (p, s1) in T(s, a)])
                                        for a in mdp.actions(s)])
            delta = max(delta, abs(U1[s] - U[s]))
        if delta < epsilon * (1 - gamma) / gamma:
             return U

def best_policy(mdp, U):
    """Given an MDP and a utility function U, determine the best policy,
    as a mapping from state to action. (Equation 17.4)"""
    pi = {}
    for s in mdp.states:
        pi[s] = argmax(mdp.actions(s), lambda a:expected_utility(a, s, U, mdp))
    return pi

def expected_utility(a, s, U, mdp):
    "The expected utility of doing a in state s, according to the MDP and U."
    return sum([p * U[s1] for (p, s1) in mdp.T(s, a)])


def policy_iteration(mdp):
    "Solve an MDP by policy iteration [Fig. 17.7]"
    U = dict([(s, 0) for s in mdp.states])
    pi = dict([(s, random.choice(mdp.actions(s))) for s in mdp.states])
    while True:
        U = policy_evaluation(pi, U, mdp)
        unchanged = True
        for s in mdp.states:
            a = argmax(mdp.actions(s), lambda a: expected_utility(a,s,U,mdp))
            if a != pi[s]:
                pi[s] = a
                unchanged = False
        if unchanged:
            return pi 

def policy_evaluation(pi, U, mdp, k=20):
    """Return an updated utility mapping U from each state in the MDP to its
    utility, using an approximation (modified policy iteration)."""
    R, T, gamma = mdp.R, mdp.T, mdp.gamma
    for i in range(k):
        for s in mdp.states:
            U[s] = R(s) + gamma * sum([p * U[s1] for (p, s1) in T(s, pi[s])])
    return U

r = 0
myMDP = GridMDP([[r, r, r, r, -1, r, -1, -1, r, 50],
[None, None, -1, -1, r, -.5, None, r, None, r],
[r, r, r, r, r, -.5, None, r, r, r],
[None, 2, None, None, None, -.5, r, 2, None, 0],
[None, r, r, r, r, None, -1, -.5, -1, r],
[r, -.5, None, r, r, None, r, r, None, r],
[r, -.5, None, r, -1, None, r, -1, None, None],
[r, r, r, r, r, r, r, r, r, r]],terminals=[(9,7)])

U = value_iteration(myMDP, .001)
V = policy_iteration(myMDP)
# print U
# print V
contents = ''
for i in xrange(0,10):
    for j in xrange(0,8):
        if (i,j) in U:
            t = (i,j)
            t1 = str(t)
            U_1 = str(U[(i,j)])
            contents += '{0}: {1} '.format(t1,U_1)
        elif (i,j) not in U:
            t = (i,j)
            t1 = str(t)
            contents += '{0}: None '.format(t1)
        if j == 7:
            contents += '\n'
# print contents
contents1 = ''
for i in xrange(0,10):
    for j in xrange(0,8):
        if (i,j) in U:
            t = (i,j)
            t1 = str(t)
            if V[(i,j)] == (0,1):
                V_1 = '^'
            elif V[(i,j)] == (1,0):
                V_1 = '>'
            elif V[(i,j)] == (-1,0):
                V_1 = '<'
            elif V[(i,j)] == (0,-1):
                V_1 = 'v'
            elif V[(i,j)] == (0,2):
                V_1 = '^^'
            elif V[(i,j)] == (2,0):
                V_1 = '>>'
            elif V[(i,j)] == (-2,0):
                V_1 = '<<'
            elif V[(i,j)] == (0,-2):
                V_1 = 'vv'
            else:
                V_1 = 'None'
            contents1 += '{0}: {1} '.format(t1,V_1)
        elif (i,j) not in U:
            t = (i,j)
            t1 = str(t)
            contents += '{0}: None '.format(t1)
        if j == 7:
            contents += '\n'
print contents1

'''


#AI: A Modern Approach by Stuart Russell and Peter Norvig	Modified: Jul 18, 2005

The data matrix you will need for the assignment:

[0, 0, 0, 0, -1, 0, -1, -1, 0, 50],
[None, None, -1, -1, 0, -.5, None, 0, None, 0],
[0, 0, 0, 0, 0, -.5, None, 0, 0, 0],
[None, 2, None, None, 0, -.5, 0, 2, None, 0],
[0, 0, None, 0, 0, None, -1, -.5, -1, 0],
[0, -.5, None, 0, 0, None, 0, 0, None, 0],
[0, -.5, None, 0, -1, None, 0, -1, None, None],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

'''