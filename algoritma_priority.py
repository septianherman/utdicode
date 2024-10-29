import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        # Menggunakan heapq untuk menjaga urutan berdasarkan prioritas
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        # Mengambil elemen dengan prioritas tertinggi (yang terendah nilainya)
        return heapq.heappop(self.elements)[1]

# Contoh penggunaan
if __name__ == "__main__":
    pq = PriorityQueue()
    
    # Menambahkan elemen dengan prioritas
    pq.put("task low", priority=5)
    pq.put("task medium", priority=3)
    pq.put("task high", priority=1)

    # Mengambil elemen berdasarkan prioritas
    while not pq.is_empty():
        print(pq.get())