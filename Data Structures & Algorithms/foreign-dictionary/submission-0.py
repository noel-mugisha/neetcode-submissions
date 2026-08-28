class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words) == 1:
            return words[0]
        
        graph = {c: [] for word in words for c in word}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(len(w1)):
                if j == len(w2):
                    return ""
                
                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    break

        stack = []
        visited, path = set(), set()

        def dfs(node):
            if node in path:
                return True
            if node in visited:
                return False

            visited.add(node)
            path.add(node)

            for neighbor in graph[node]:
                if dfs(neighbor):
                    return True

            stack.append(node)
            path.remove(node)

            return False

        for node in graph:
            if node not in visited:
                if dfs(node):
                    return ""

        return "".join(stack[::-1])







