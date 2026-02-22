def is_isomorphic(s, t):
    map_st = {}
    map_ts = {}

    for i in range(len(s)):
        if s[i] in map_st and map_st[s[i]] != t[i]:
            return False
        if t[i] in map_ts and map_ts[t[i]] != s[i]:
            return False

        map_st[s[i]] = t[i]
        map_ts[t[i]] = s[i]

    return True


print(is_isomorphic("egg", "add"))