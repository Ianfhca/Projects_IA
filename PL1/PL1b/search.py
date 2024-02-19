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

def breadthFirstSearch(problem):
    problem.expanded=[]
    problem.pqElem=util.PriorityQueue()
    problem.pqCaminos = util.PriorityQueue()
    successors=problem.getSuccessors(problem.getStartState())
    problem.expanded.append(problem.getStartState())
    for successor in successors:
        problem.pqElem.push(successor,1)
        problem.pqCaminos.push([],1)
    #nueva=[]
    while not problem.pqElem.isEmpty():
        elem=problem.pqElem.pop()
        problem.camino=problem.pqCaminos.pop()
        print(" --- Analizando ",elem," ---")
        if problem.isGoalState(elem[0]):
            print("Camino encontrado!")
            return problem.camino
        else:
            successors=problem.getSuccessors(elem[0])
            print("sucesores: ",successor)
            for successor in successors:
                if not successor[0] in problem.expanded:
                    problem.expanded.append(successor[0])
                    copia=problem.camino[:]
                    copia.append(successor[1])
                    print("Appending ",successor, " with camino:")
                    print(problem.camino)
                    problem.pqElem.push(successor,1)
                    problem.pqCaminos.push(copia,1)
                    #problem.pqElem.push(successor,problem.getCostOfActions(copia))
                    #problem.pqCaminos.push(copia,problem.getCostOfActions(copia))



def breadthFirstSearch22(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    problem.expanded = [problem.getStartState()]
    problem.pqElem = util.PriorityQueue()
    problem.pqCaminos = util.PriorityQueue()
    successors=problem.getSuccessors(problem.getStartState())
    for successor in successors:
        problem.pqElem.push(successor,1)
    problem.pqCaminos.push([],1)

    while not problem.pqElem.isEmpty():
        elem=problem.pqElem.pop()
        print("Analizando ",elem)
        state=elem[0]
        
        
        actions = problem.pqCaminos.pop()

        if problem.isGoalState(state):
            return actions

        if state not in problem.expanded:
            problem.expanded.append(state)

        #print("problem.getSuccessors(state) :",problem.getSuccessors(state))
            print("state: ",state)
            
        successors=problem.getSuccessors(state)

        #for successor, action, _ in problem.getSuccessors(state):
        for successor in successors:
            if successor not in problem.expanded:
                print("Expandiendo ",successor)
                problem.expanded.append(successor[0])
                #queue.push((successor, actions + [action]))
                problem.pqElem.push(successor,1)
                copia=actions[:]
                copia.append(successor[1])
                print("Camino: ",copia)
                problem.pqCaminos.push(copia,1)
    
    return []

def breadthFirstSearchCOPIA(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    problem.expanded = []
    problem.pqElem = util.Queue()
    problem.pqCaminos = util.Queue()
    problem.pqElem.push(problem.getStartState())
    problem.pqCaminos.push([])

    while not problem.pqElem.isEmpty():
        state=problem.pqElem.pop()
        
        
        actions = problem.pqCaminos.pop()

        if problem.isGoalState(state):
            return actions

        if state not in problem.expanded:
            problem.expanded.append(state)

        #print("problem.getSuccessors(state) :",problem.getSuccessors(state))
            print("state: ",state)
            
        successors=problem.getSuccessors(state)

        #for successor, action, _ in problem.getSuccessors(state):
        for successor in successors:
            if successor not in problem.expanded:
                print("Expandiendo ",successor)
                problem.expanded.append(successor[0])
                #queue.push((successor, actions + [action]))
                problem.pqElem.push(successor[0])
                copia=actions[:]
                copia.append(successor[1])
                print("Camino: ",copia)
                problem.pqCaminos.push(copia)
    
    return []

    

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    visited = set()
    pQueue = util.PriorityQueue()
    pQueue.push((problem.getStartState(), []), problem.getCostOfActions([]))

    while not pQueue.isEmpty():
        state, actions = pQueue.pop()

        if problem.isGoalState(state):
            return actions

        if state not in visited:
            visited.add(state)

        for successor, action, cost in problem.getSuccessors(state):
            if successor not in visited or problem.getCostOfActions(actions) < cost:
                visited.add(successor)
                pQueue.update((successor, list(actions + [action])), problem.getCostOfActions(actions) + cost)
                #print(successor, problem.getCostOfActions(actions) + cost)

    return []
    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    #print("-> ",problem.getSuccessors(problem.getStartState()))
    #for i in range(0,len(problem.getSuccessors(problem.getStartState()))):
        #print("---> ",problem.getSuccessors(problem.getSuccessors(problem.getStartState())[i][0]))

    problem.pqElem=util.PriorityQueue()
    problem.pqCaminos=util.PriorityQueue()
    #pqElem=util.Queue()
    #pqCaminos=util.Queue()

    #visitados=[]
    #visitados.append(problem.getStartState())

    sucesores=problem.getSuccessors(problem.getStartState())
    problem.expandidos=[problem.getStartState()]

    for i in range(0,len(sucesores)):
        #visitados.append(sucesores[i][0])
        g=sucesores[i][2]
        h=heuristic(sucesores[i][0],problem)
        coste=g+h
        problem.pqElem.push(sucesores[i][:],coste)
        problem.pqCaminos.push([sucesores[i][1]],coste)
        #pqElem.push(sucesores[i][:])
        #pqCaminos.push([sucesores[i][1]])
    iter=0
    print("stack inicial: ",sucesores[:][:])
    
    while(not problem.pqElem.isEmpty()):
        #print("expandidos: ",problem.expandidos)
        iter=iter+1
        problem.nextElem=problem.pqElem.pop()     
        problem.camino=problem.pqCaminos.pop()
        #print(problem.camino)
        #print("elem: ",nextElem)
        if problem.isGoalState(problem.nextElem[0]):
            #print("Solucion encontrada: ",problem.camino)
            return problem.camino
        #sucesores=problem.getSuccessors(nextElem[0])
        if not problem.nextElem[0] in problem.expandidos: 
            sucesores=problem.getSuccessors(problem.nextElem[0])
            problem.expandidos.append(problem.nextElem[0])

            for i in range(0,len(sucesores)):
            #if not sucesores[i][0] in visitados:
                #visitados.append(sucesores[i][0])
                #g=util.manhattanDistance(sucesores[i][0],problem.getStartState())
                g=problem.nextElem[2]+sucesores[i][2]
                h=heuristic(sucesores[i][0],problem)
                coste=g+h
                copiaCamino=[]
                copiaCamino=problem.camino[:]
                copiaCamino.append(sucesores[i][1])
                s=[]
                for f in range(0,len(sucesores)):
                    s.append(list(sucesores[f][:]))
                #print("s : ",s)
                s[i][2]+=problem.nextElem[2]
                sucesores=tuple(s)
                #print("coste ",sucesores[i][0]," = ",sucesores[i][2])
                problem.pqElem.push(sucesores[i][:],coste)
                problem.pqCaminos.push(copiaCamino,coste)
                #pqElem.push(sucesores[i][:])
                #pqCaminos.push(copiaCamino)
    print("saliendo del bucle.")
    return []

def aStarSearchCOPIA(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    #print("-> ",problem.getSuccessors(problem.getStartState()))
    #for i in range(0,len(problem.getSuccessors(problem.getStartState()))):
        #print("---> ",problem.getSuccessors(problem.getSuccessors(problem.getStartState())[i][0]))

    problem.pqElem=util.PriorityQueue()
    problem.pqCaminos=util.PriorityQueue()
    #pqElem=util.Queue()
    #pqCaminos=util.Queue()

    #visitados=[]
    #visitados.append(problem.getStartState())

    sucesores=problem.getSuccessors(problem.getStartState())
    problem.expandidos=[problem.getStartState()]

    for i in range(0,len(sucesores)):
        #visitados.append(sucesores[i][0])
        g=sucesores[i][2]
        h=heuristic(sucesores[i][0],problem)
        coste=g+h
        problem.pqElem.push(sucesores[i][:],coste)
        problem.pqCaminos.push([sucesores[i][1]],coste)
        #pqElem.push(sucesores[i][:])
        #pqCaminos.push([sucesores[i][1]])
    iter=0
    print("stack inicial: ",sucesores[:][:])
    
    while(not problem.pqElem.isEmpty()):
        #print("expandidos: ",problem.expandidos)
        iter=iter+1
        problem.nextElem=problem.pqElem.pop()     
        problem.camino=problem.pqCaminos.pop()
        #print(problem.camino)
        #print("elem: ",nextElem)
        if problem.isGoalState(problem.nextElem[0]):
            #print("Solucion encontrada: ",problem.camino)
            return problem.camino
        #sucesores=problem.getSuccessors(nextElem[0])
        if not problem.nextElem[0] in problem.expandidos: 
            sucesores=problem.getSuccessors(problem.nextElem[0])
            problem.expandidos.append(problem.nextElem[0])

            for i in range(0,len(sucesores)):
            #if not sucesores[i][0] in visitados:
                #visitados.append(sucesores[i][0])
                #g=util.manhattanDistance(sucesores[i][0],problem.getStartState())
                g=problem.nextElem[2]+sucesores[i][2]
                h=heuristic(sucesores[i][0],problem)
                coste=g+h
                copiaCamino=[]
                copiaCamino=problem.camino[:]
                copiaCamino.append(sucesores[i][1])
                s=[]
                for f in range(0,len(sucesores)):
                    s.append(list(sucesores[f][:]))
                #print("s : ",s)
                s[i][2]+=problem.nextElem[2]
                sucesores=tuple(s)
                #print("coste ",sucesores[i][0]," = ",sucesores[i][2])
                problem.pqElem.push(sucesores[i][:],coste)
                problem.pqCaminos.push(copiaCamino,coste)
                #pqElem.push(sucesores[i][:])
                #pqCaminos.push(copiaCamino)
    print("saliendo del bucle.")
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
