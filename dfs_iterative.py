def dfs(s):
    stack=[]
    stack.append(s)
    while len(stack)!=0:
        v=stack.pop()
        visited[v]=1
        for i in g[v]:
            if visited[i]==0:
                stack.append(i)
n,m=map(int,raw_input().split())
g=[]
for i in range(n+1):
    g.append([])
for _ in range(m):
    a,b=map(int,raw_input().split())
    g[a].append(b)
    g[b].append(a)
k=input()
visited=[0]*(n+1)
dfs(k)
print sum(visited)
