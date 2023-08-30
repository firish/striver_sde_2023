# https://practice.geeksforgeeks.org/problems/heap-sort/1

class Solution:
    # Heapify function to maintain heap property.
    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Check if left child exists and is greater than root
        if left < n and arr[i] < arr[left]:
            largest = left

        # Check if right child exists and is greater than root
        if right < n and arr[largest] < arr[right]:
            largest = right

        # Change root if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap

            # Heapify the root recursively.
            self.heapify(arr, n, largest)

    # Function to build a Heap from array.
    def buildHeap(self, arr, n):
        # Index of last non-leaf node
        startIdx = n // 2 - 1

        # Reverse level order traversal, from last non-leaf node to root
        for i in range(startIdx, -1, -1):
            self.heapify(arr, n, i)

    # Function to sort an array using Heap Sort.
    def HeapSort(self, arr, n):
        # Build a max heap.
        self.buildHeap(arr, n)

        # One by one extract elements
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]   # swap
            self.heapify(arr, i, 0)  
