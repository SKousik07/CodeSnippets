def prims(n):
    visited=[0]*n
    mincost=0
    l=[]
    for i in range(n):
        l.append(list(map(lambda x: 999 if int(x)==0 else int(x),input().split())))
    visited[0]=1
    for z in range(n-1):
        m=999
        for i in range(n):
            if visited[i]==1:
                for j in range(n):
                    if visited[j]==0:
                        if l[i][j]<m:
                            m=l[i][j]
                            u=i
                            v=j
        
        visited[v]=1
        mincost+=m
        l[u][v]=999
        l[v][u]=999
        print("Edges {}-{} cost:{}".format(u,v,m))
    print("minimum cost :"+str(mincost))
        
prims(int(input()))


"""input/output
5
0 2 0 6 0
2 0 3 8 5
0 3 0 0 7
6 8 0 0 9
0 5 7 9 0
Edges 0-1 cost:2
Edges 1-2 cost:3
Edges 1-4 cost:5
Edges 0-3 cost:6
minimum cost :16
"""
