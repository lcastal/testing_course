# Random Testing
# --------------
# Write a random tester for the Queue class.
# The random tester should repeatedly call
# the Queue methods on random input in a
# semi-random fashion. For instance, if
# you wanted to randomly decide between
# calling enqueue and dequeue, you would
# write something like this:
#
# q = Queue(500)
# if (random.random() < 0.5):
#     q.enqueue(some_random_input)
# else:
#     q.dequeue()
#
# You should call both the enqueue
# and dequeue, methods several thousand
# times each.
#
# This specific Queue class
# has bugs spread throughout the code,
# therefore you should surround calls to
# enqueue() and dequeue() with try/catch
# statements.
#
# For every input that is
# successfuly enqueued, add that input
# to a list of inputs as a tuple: (input, 0)
# where the 0 indicates success. You should
# also catch all assertion errors coming
# from the checkRep() method, and add the input
# on which the error was thrown to the list
# as a tuple (input, 1), where the 1 indicates
# failure.
#
# Similarly, for every successful dequeue and
# checkRep, you should add the tuple ('dq', 0)
# to the list. You should again catch all assertion
# errors coming from the checkRep() method, and add
# the tuple ('dq', 1) to indicate that the dequeue
# failed.
#
# The resulting list should be the return value of
# your random_test function.


import array
import random

# Although this specific Queue class has bugs spread
# throughout the code, do not modify the class.
class Queue:

    def __init__(self,size_max):
        assert size_max > 0
        self.max = size_max - 1
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max))

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self,x):
        x = x % 1000
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:
            self.tail = 0
        return True

    def dequeue(self):
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return x

    def checkRep(self):
        assert self.tail >= 0
        assert self.tail < self.max
        assert self.head >= 0
        assert self.head < self.max
        if self.tail > self.head:
            assert (self.tail-self.head) == self.size
        if self.tail < self.head:
            assert (self.head-self.tail) == (self.max-self.size)
        if self.head == self.tail:
            assert (self.size==0) or (self.size==self.max)


def random_test():
    # Write a random tester for the Queue class
    # param for testing
    n_iteration = 10
    n_element = 1000

    log = list()
    q = Queue(n_element)

    #static check
    try:
        assert q.empty()
        q.checkRep()
    except:
        log.append(("empty", 1))

    try:
        assert not q.full()
        q.checkRep()
    except:
        log.append(("empty", 1))

    #random check
    enqueue_probability = 0

    for i in range(n_iteration):
        #chose the convergency to enqueue (full list)
        if random.random() < 0.5:
            enqueue_probability = 0.8

        #chose the convergency to denqueue (empty list)
        else:
            enqueue_probability = 0.2

        for i in range(n_element*3):
            input = random.randrange(0,100)
            if random.random() < enqueue_probability:
                try:
                    q.enqueue(input)
                    q.checkRep()
                    log.append((input, 0))
                except:
                    log.append((input, 1))
            else:
                try:
                    q.dequeue()
                    q.checkRep()
                    log.append(('dq', 0))
                except:
                    log.append(('dq', 1))
    return log
