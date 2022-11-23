from heapq import heapify, heappop, heappush

to_push  = [13, 5, 15, 3, 0]

heap = [12, 14, 8, 6]
heapify(heap)

for x in to_push:
    heappush(heap, x)
    print('{} is a minimum of {}'.format(heap[0], heap))

while heap:
    heap_copy = list(heap)
    print('{} is popped from {}'.format(heappop(heap), heap_copy))
