from copy import deepcopy
initState=[0,1,2,3,4,5,6,7,8]
goalState=[1,4,2,0,3,5,6,7,8]

q=[]
visited=[]
qList=[]
visitedList=[]
class state:
    def __init__(self,state=[],prev=None,tree=None):
        self.state=state
        self.children=[]
        self.parent=prev
        self.tree=[]
        if tree==None:
            self.tree.append(state)
        if tree is not None:
            self.tree.extend(deepcopy(tree))

    def printState(self):
        a=0
        for i in range(3):
            for j in range(3):
                print(self.state[a],end=""),
                a=a+1
            print("")
        print("")
        print("")

    def printParent(self):
        a=0
        for i in range(3):
            for j in range(3):
                print(self.parent[a],end=""),
                a=a+1
            print("")
        print("")
        print("")

    def isState(self):
        return bool(self.state==initState)

    def sameState(self,state):
        return bool(state==self.state)

    def retState(self):
        return list(self.state)

    def isPrevState(self):
        if self.parent in self.children:
            self.children.remove(self.parent)

    def moveUp(self):
        child=deepcopy(self.state)
        if child.index(0)-3>=0:
            i=child.index(0)
            temp=child[i]
            child[i]=child[i-3]
            child[i-3]=temp
            children=state(child,self.state,self.tree)
            if children.state not in self.tree and children.state not in q and children.state not in visited:
                self.children.append(children)
        else:
            del child

    def moveRight(self):
        child=deepcopy(self.state)
        if child.index(0)%3<2:
            i=child.index(0)
            temp=child[i]
            child[i]=child[i+1]
            child[i+1]=temp
            children=state(child,self.state,self.tree)
            if children.state not in self.tree and children.state not in q and children.state not in visited:
                self.children.append(children)
        else:
            del child

    def moveLeft(self):
        child=deepcopy(self.state)
        if child.index(0)%3>0:
            i=child.index(0)
            temp=child[i]
            child[i]=child[i-1]
            child[i-1]=temp
            children=state(child,self.state,self.tree)
            if children.state not in self.tree and children.state not in q and children.state not in visited:
                self.children.append(children)
        else:
            del child

    def moveDown(self):
        child=deepcopy(self.state)
        if child.index(0)+3<=8:
            i=child.index(0)
            temp=child[i]
            child[i]=child[i+3]
            child[i+3]=temp
            children=state(child,self.state,self.tree)
            if children.state not in self.tree and children.state not in q and children.state not in visited:
                self.children.append(children)
        else:
            del child

    def expandNode(self):
        self.moveLeft()
        self.moveUp()
        self.moveRight()
        self.moveDown()
        self.isPrevState()

el=state(initState)
q.append(el)
qList.append(initState)
while len(q)>0:
    if list(q[0].retState())==goalState:
        print("goal state found")
        #print(q[0])
        self=q[0]
        """while(not self.isState()):
            print(self.printParent())
            parent=self.parent
            self=()
            print("")"""
        break
    else:
        if q[0] not in visited:
            q[0].expandNode()
            visited.append(deepcopy(q[0]))
            visitedList.append((q[0].retState()))
            List=q[0].children
            del q[0]
            for i in range(len(List)):
                q.append(List[i])
                if List[i].retState not in qList and List[i] not in visitedList :
                    qList.append(List[i].retState())
            #nq=list(set(q))
            #q.clear()
            #q=nq
        else:
            del q[0]
