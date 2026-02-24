def count_routes(locations, start, finish, fuel):
    from functools import lru_cache
    n = len(locations)
    @lru_cache(None)
    def dfs(city, fuel_left):
        if fuel_left < 0:
            return 0
        count = 1 if city == finish else 0
        for nxt in range(n):
            if nxt != city:
                cost = abs(locations[city] - locations[nxt])
                count += dfs(nxt, fuel_left - cost)
        return count
    return dfs(start, fuel)