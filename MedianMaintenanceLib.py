
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

        if self.polarity=="max": # max heap uses negative values
            val *= -1
        # Add val at end of heap
        self.keys.append(val)
        iVal = len(self.keys)-1
        iParent = int(iVal/2)

        # bubble up
        while keys[iVal] < keys[iParent] and iVal>0:
            keys[iVal], keys[iParent] = keys[iParent], keys[iVal]
            iVal = iParent
            iParent = int(iVal/2)


    def extractmax(self):
        self.extractmin(self)

    def extractmin(self):

        # swap last element into first position
        keys[0] = keys[-1]
        # delete last element
        del keys[-1]

        # bubble down



def median_maintenance(a):

    # Initialize list to hold the return list with maintained medians
    medians = len(a) * []

    # Initialize 2 empty heaps,
    # one to hold the smaller half of the processed part of the array,
    # one to hold the larger half
    maxheap = Heap("max")
    minheap = Heap("min")

    # Add one of the first two values to a to each of the heaps
    maxhead.insert(min(a[:1]))
    minhead.insert(max(a[:1]))
    # Set the corresponding medians
    medians[0] = a[0]
    medians[1] = a[0]

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
            else:
                maxheap.insert(minheap.extractmin())

            if maxheap.getsize() != minheap.getsize():
                raise(NameError, "Failed to equalize heap sizes. ")

            medians[i] = minheap.getmin()

    return medians
