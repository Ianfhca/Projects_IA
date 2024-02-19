# multiAgents.py
# --------------


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    #calcula la mejor siguiente accion posible y devuelve la siguiente accion que va a hacer pacman
    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best
        

        "Add more of your code here if you want to"

        #calcular la distancia entre fantasma y todas las bolitas

        #elegir la bolita más alejada del fantasma

        #calcular posibles nuevas soluciones

        #añadir posición actual

        #calcular el score = distanciaManhattan(posibles movimientos, bolita más alejada)

        #si distanciaManhattan(posibles movimientos, fantasma) <= 1: eliminar ese movimiento

        #devolver posicion con mayor score

        #return successorGameState.getScore()

        return legalMoves[chosenIndex]

    #evalua como de bueno es un movimiento y devuelve un score (cuando mayor, mejor es el movimiento)
    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()


        #newFood = successorGameState.getFood()
        newFood = currentGameState.getFood()

        newGhostStates = successorGameState.getGhostStates()
        #newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"

        #print("old action: ",action)
        position=list(currentGameState.getPacmanPosition())
        #print("pos: ",position)

        if action=="North":
            position[1]+=1
        elif action=="South":
            position[1]-=1
        elif action=="East":
            position[0]+=1
        elif action=="West":
            position[0]-=1
        else:
            None

        action=position

        #print("new action: ",action)

        #print("numero de agentes = ",len(currentGameState.data.agentStates))
        distToGhost=util.manhattanDistance(action,currentGameState.getGhostPosition(1))

        if distToGhost>2:
            foodPositions=[]
            for i in range(0,newFood.width):
                for j in range(0,newFood.height):
                    if newFood[i][j]==True:
                        foodPositions.append((i,j))
            #dists=[util.manhattanDistance(foodPos,action)+0.1 for foodPos in foodPositions]
            dists=[util.manhattanDistance(foodPos,action)+0.1 for foodPos in foodPositions]
            nearestDist=min(dists)
            return 1/nearestDist
            #index= dists.index(nearestDist)
            #nearestFood=foodPositions[index]
        else:
            foodPositions=[]
            for i in range(0,newFood.width):
                for j in range(0,newFood.height):
                    if newFood[i][j]==True:
                        foodPositions.append((i,j))
            #dists=[util.manhattanDistance(foodPos,action)+0.1 for foodPos in foodPositions]
            dists=[util.manhattanDistance(foodPos,action)+0.1 for foodPos in foodPositions]
            nearestDist=min(dists)
            return 0.9*util.manhattanDistance(action,currentGameState.getGhostPosition(1))+0.1*(1/nearestDist)

    

        "*    GO TO FURTHER FOOD FROM GHOST              *"

        """
        foodPositions=[]
        for i in range(0,newFood.width):
            for j in range(0,newFood.height):
                if newFood[i][j]==True:
                    foodPositions.append((i,j))
        
        dists=[util.manhattanDistance(foodPos,currentGameState.getGhostPosition(1)) for foodPos in foodPositions]

        furtherDist=min(dists)
        index= dists.index(furtherDist)
        furtherFoodFromGhost=foodPositions[index]
        print("furtherFoodFromGhost: ",furtherFoodFromGhost)
        print("Ghost:",currentGameState.getGhostPosition(1),", Pacman:",currentGameState.getPacmanPosition())
        print("Action:",action,", score: ",util.manhattanDistance(action,furtherFoodFromGhost))
        return util.manhattanDistance(action,furtherFoodFromGhost)
        """


        "   "

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
