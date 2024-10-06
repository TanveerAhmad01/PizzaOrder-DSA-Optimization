
class Queue:
    def __init__(self):
        self.front = -1
        self.back = -1
        self.queue = []
            
    def enqueue(self,item):
            self.back +=1
            if self.back < len(self.queue):
                self.queue[self.back] = item 

            else:
                newQueue = [0] *(self.back +1)
                for j in range(len(self.queue)):
                    newQueue[j] = self.queue[j]
            newQueue[self.back] = item
            self.queue = newQueue
            print("queue data is ",self.queue)
        
    def dequeue(self):
            emptystack = [0] * self.back 
            removeitem = self.queue[0]
            for i in range(self.back):
                emptystack[i] = self.queue[i + 1]  
            self.back -= 1    
            self.queue=emptystack  
            return self.queue

    def peek(self):
        print("Peek Value is : ",self.queue[self.back])

    def is_empty(self):
        if self.back == self.front:
            print("Queue is Empty")
        else:
              print("Queue is not Empty")


