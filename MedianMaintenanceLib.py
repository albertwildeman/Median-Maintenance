
class Heap(object):

    def __init__(self, polarity):

        self.polarity = polarity
        self.keys = []

    def getmin(self):
        if self.polarity=="min":
            return self.keys[0]
        else:
            raise(NameError, "No getmin() method for heap with polarity 'max'.")

    def getmax(self):
        if self.polarity=="max":
            return -1 * self.keys[0]
        else:
            raise(NameError, "No getmax() method for heap with polarity 'min'.")

    def getsize(self):
        return len(self.keys)

    def insert(self, val):

        if self.polarity=="max":    # max heap uses negative values
            val *= -1
        # Add val at end of heap
        self.keys.append(val)
        iVal = len(self.keys)-1
        iParent = int((iVal-1)/2)

        # bubble up
        while self.keys[iVal] < self.keys[iParent] and iVal>0:
            self.keys[iVal], self.keys[iParent] = self.keys[iParent], self.keys[iVal]
            iVal = iParent
            iParent = int((iVal-1)/2)

        # # Check for errors
        # error_indices = [i for i in range(len(self.keys)) if self.keys[i]<self.keys[int((i-1)/2)]]
        # if len(error_indices)>0:
        #     raise(NameError, "Heap not in order.")

    def extractmax(self):
        return -1 * self.extractmin()

    def extractmin(self):

        # save current minimum to return value
        oldmin = self.keys[0]
        # swap last element into first position
        self.keys[0] = self.keys[-1]
        # save a copy as x; it'll be used a number of times
        x = self.keys[0]
        # delete last element
        del self.keys[-1]

        # bubble down
        iVal = 0
        iChild1 = 1
        iChild2 = 2
        done = False


        while iChild2 < len(self.keys) and not done:

            if x > self.keys[iChild1] or x > self.keys[iChild2]:

                # Bubble down. Pick the child to swap with to be the smaller one
                if self.keys[iChild1] < self.keys[iChild2]:
                    self.keys[iChild1], self.keys[iVal] = self.keys[iVal], self.keys[iChild1]
                    iVal = iChild1
                else:
                    self.keys[iChild2], self.keys[iVal] = self.keys[iVal], self.keys[iChild2]
                    iVal = iChild2

                # Update children
                iChild1 = iVal * 2 + 1
                iChild2 = iVal * 2 + 2
            else:   # no bubble down necessary
                done = True

        # If new position has 1 or 0 kids, do final swap if necessary and then exit the while loop.
        if not done:    # heap not fully arranged yet, but node has at most 1 child
            if iChild1 < len(self.keys):    # value has one child. Bubble down if necessary
                if x > self.keys[iChild1]:
                    # swap
                    self.keys[iChild1], self.keys[iVal] = self.keys[iVal], self.keys[iChild1]

        # # Check for errors
        # error_indices = [i for i in range(len(self.keys)) if self.keys[i]<self.keys[int((i-1)/2)]]
        # if len(error_indices)>0:
        #     raise(NameError, "Heap not in order.")

        return oldmin



def median_maintenance(a):
    # Implementation of dual heap technique for median maintenance


    # Initialize list to hold the return list with maintained medians
    medians = len(a) * [int(0)]

    # Initialize 2 empty heaps,
    # one to hold the smaller half of the processed part of the array,
    # one to hold the larger half
    maxheap = Heap("max")
    minheap = Heap("min")

    # Add one of the first two values to a to each of the heaps
    maxheap.insert(min(a[:2]))
    minheap.insert(max(a[:2]))
    # Set the corresponding medians
    medians[0] = a[0]
    medians[1] = max(a[:2])

    for i in range(2, len(a)):
        val = a[i]

        if i%2==0 : # if i is even, an even number of elements has been processed so far and the heaps have equal size

            if val < minheap.getmin():
                if val > maxheap.getmax():
                    medians[i] = val
                else:
                    medians[i] = maxheap.getmax()
                maxheap.insert(val)
            else:
                medians[i] = minheap.getmin()
                minheap.insert(val)

        else: # i is odd, an odd number of elements have been processed so far

            # Insert value in appropriate heap
            if val <= maxheap.getmax():
                maxheap.insert(val)
            else:
                minheap.insert(val)

            # Maintain balance of heap sizes
            if maxheap.getsize() > minheap.getsize():
                minheap.insert(maxheap.extractmax())
            elif maxheap.getsize() < minheap.getsize():
                maxheap.insert(minheap.extractmin())

            if maxheap.getsize() != minheap.getsize():
                raise(NameError, "Failed to equalize heap sizes. ")

            medians[i] = minheap.getmin()

    return medians
