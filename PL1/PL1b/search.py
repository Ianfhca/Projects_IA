# search.py

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    return  ['South', 'South', 'West', 'South', 'West', 'West', 'South', 'West']

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    visited = set()
    stack = util.Stack()
    stack.push((problem.getStartState(), []))

    while not stack.isEmpty():
        state, actions = stack.pop()

        if problem.isGoalState(state):
            return actions

        if state not in visited:
            visited.add(state)

        for successor, action, _ in problem.getSuccessors(state):
            if successor not in visited:
                stack.push((successor, actions + [action]))
    
    return []
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    visited = set()
    queue = util.Queue()
    queue.push((problem.getStartState(), []))

    while not queue.isEmpty():
        state, actions = queue.pop()

        if problem.isGoalState(state):
            return actions

        if state not in visited:
            visited.add(state)

        for successor, action, _ in problem.getSuccessors(state):
            if successor not in visited:
                visited.add(successor)
                queue.push((successor, actions + [action]))
    
    return []
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    visited = set()
    pQueue = util.PriorityQueue()
    pQueue.push((problem.getStartState(), [], 0), 0)

    while not pQueue.isEmpty():
        state, actions, cost = pQueue.pop()

        if problem.isGoalState(state):
            return actions
        else:
            if state not in visited:
                visited.add(state)
                for successor, action, sCost in problem.getSuccessors(state):
                    if successor not in visited:
                        pQueue.push((successor, actions + [action], cost + sCost), cost + sCost)
    return []
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"  
    visited = set()
    pQueue = util.PriorityQueue()
    pQueue.push((problem.getStartState(), [], 0), 0)
    g = 0
    h = 0
    f = 0

    while not pQueue.isEmpty():
        state, actions, cost = pQueue.pop()

        if problem.isGoalState(state):
            return actions
        else:
            if state not in visited:
                visited.add(state)
                for successor, action, sCost in problem.getSuccessors(state):
                    if successor not in visited:
                        g = cost + sCost  # Costo acumulado hasta el sucesor
                        h = heuristic(successor, problem)  # Valor heurístico para el sucesor
                        f = g + h  # Costo total estimado (g + h)
                        pQueue.push((successor, actions + [action], g), f)
            else:
                
    return []
        
    # visited = set()
    # pQueue = util.PriorityQueue()
    # pQueue.push((problem.getStartState(), [], 0), 0)

    # while not pQueue.isEmpty():
    #     state, actions, cost = pQueue.pop()

    #     if problem.isGoalState(state):
    #         return actions

    #     if state not in visited:
    #         visited.add(state)

    #         for successor, action, sCost in problem.getSuccessors(state):
    #             if successor not in visited:
    #                 g = cost + sCost  # Costo acumulado hasta el sucesor
    #                 h = heuristic(successor, problem)  # Valor heurístico para el sucesor
    #                 f = g + h  # Costo total estimado (g + h)
    #                 pQueue.push((successor, actions + [action], g), f)

    # return []

    """  
        visited = set()
    pQueue = util.PriorityQueue()
    pQueue.push((problem.getStartState(), [], 0), 0)
    goals = list()
    

    while not pQueue.isEmpty():
        state, actions, cost = pQueue.pop()
        if (problem.isGoalState(state)):
            goals.append([state, actions, cost])
            auxstate, auxactions, auxcost = pQueue.pop()
            if cost <= auxcost:
                return actions
            else:
                pQueue.push((auxstate, auxactions, auxcost), auxcost)
        else:
            if state not in visited:
                visited.add(state)
            for successor, action, sCost in problem.getSuccessors(state):
                if successor not in visited:
                    new_cost = cost + sCost + heuristic(successor, problem)
                    pQueue.update((successor, actions + [action], new_cost), new_cost)

    if len(goals) == 0:
        return []
    else:
        return goals[-1][1] 
    """
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch