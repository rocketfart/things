import random
import time


class Solution:
    def __init__(self):
        self.snake = [(0, 0)]
        self.board = [[' ' * 10] for _ in range(10)]

    def move(self, dir):
        while self.snake:
            x, y = self.snake.pop(0)
            time.sleep(5)
            print x, y
            xx, yy = x + dir[0], x + dir[1]
            if 0 <= xx < 10 and 0 <= yy < 10 and (xx, yy) not in self.snake:
                self.snake.append((xx, yy))
            elif (xx, yy) in self.snake:
                print 'hit snake body'
                return False
            else:
                print 'hit the wall'
                return False


# mutiple threading
import threading
from Queue import Queue

class put_dir(threading.Thread):

    def __init__(self, tname, queue):
        threading.Thread.__init__(self, name=tname)
        self.event = queue

    def run(self):
        self.event.append((1, 0))
        while True:
            dir = input()
            self.event.append(dir)

class move(threading.Thread):

    def __init__(self, tname, queue):
        self.event = queue
        threading.Thread.__init__(self, name = tname)
        self.snake = [(0, 0)]
        self.board = ['' * 10 for _ in range(10)]

    def run(self):
        dir = self.event.pop(0)

        while self.snake:
            target = (random.choice(10),random.choice(10))
            while target in self.snake:
                target = (random.choice(10),random.choice(10))
            x, y = self.snake.pop(0)
            time.sleep(2)
            print x,y
            if self.event:
                dir = self.event.pop(0)
            xx, yy = x + dir[0], y + dir[1]
            if target[0] == xx and target[1] == yy:
                self.snake = [(xx,yy)] + self.snake

            if 0 <= xx < 10 and 0 <= yy < 10 and [xx,yy] not in self.snake:
                self.snake.append((xx, yy))
            elif (xx,yy) in self.snake:
                print 'hit snake'
            else:
                print 'hit wall'

def test():
    queue = [(1,0)]
    player = put_dir(1, queue)
    action = move(2, queue)
    player.start()
    action.start()

if __name__ == '__main__':
    test()
