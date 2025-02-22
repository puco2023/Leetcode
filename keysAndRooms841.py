class Solution(object):
    def canVisitAllRooms(self, rooms):
        visited=set()
        def dfs(room):
            if room in visited:
                return
            visited.add(room)
            for key in rooms[room]:
                dfs(key)
        dfs(0)
        return len(visited)==len(rooms)
