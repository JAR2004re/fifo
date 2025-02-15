from queue import Queue

# Function to find page faults using FIFO
def pageFaults(pages, n, capacity):

    # To represent set of current pages.
    s = set()

    # To store the pages in FIFO manner
    indexes = Queue()

    # Start from initial page
    page_faults = 0
    for i in range(n):

        # Check if the set can hold more pages
        if len(s) < capacity:

            # Insert it into set if not present already which represents page fault
            if pages[i] not in s:
                s.add(pages[i])

                # Increment page fault
                page_faults += 1

                # Push the current page into the queue
                indexes.put(pages[i])

        # If the set is full then need to perform FIFO
        else:

            # Check if current page is not already present in the set
            if pages[i] not in s:

                # Pop the first page from the queue
                val = indexes.get()

                # Remove the index page from the set
                s.remove(val)

                # Insert the current page
                s.add(pages[i])

                # Push the current page into the queue
                indexes.put(pages[i])

                # Increment page faults
                page_faults += 1

    return page_faults
# Driver code  
if __name__ == '__main__': 
    pages = [1,2,3,4,1,2,5,1,2,3,4,5]  
    n = len(pages)  
    capacity = 3
    print(pageFaults(pages, n, capacity)) 

