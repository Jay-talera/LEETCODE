class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        
        tickets.sort(key=lambda x: x[1])

        for u, v in tickets:
            if u in graph:
                graph[u].append(v)
            else:
                graph[u] = [v]
        
        itinerary, stack = [], [("JFK")]
        
        while stack:
            curr = stack[-1]
            
            if curr in graph and len(graph[curr]) > 0:
                stack.append(graph[curr].pop(0))
            else:
                itinerary.append(stack.pop())
        return itinerary[::-1]