def dfs(s):
    d[s]=x
    visited[s]=1
    for i in g[s]:
        if visited[i]==0:
            dfs(s)
