class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        all_letters = {c for word in words for c in word}
        graph = {c: [] for c in all_letters}
        for i in range(len(words) - 1):
            letters = list(zip(words[i], words[i + 1]))

            for j, pair in enumerate(letters):
                x, y = pair
                if x != y:
                    graph[x].append(y)
                    break
                
                if j == len(letters) - 1 and words[i] > words[i + 1]:
                    return "" 
                
        
        indegree = {node: 0 for node in graph}
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1

        q = deque([node for node in graph if indegree[node] == 0])
        res = []

        while q:
            q_len = len(q)
            for _ in range(q_len):
                node = q.popleft()
                res.append(node)

                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        q.append(neighbor)

        return "" if len(res) != len(all_letters) else "".join(res)        