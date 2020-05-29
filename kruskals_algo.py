def kruskals(n):
    parent=[0]*n
    mincost=0
    ne=1
    l=[]
    for i in range(n):
        l.append(list(map(lambda x: 999 if int(x)==0 else int(x),input().split())))
    while(ne<n):
        m=999
        for i in range(n):
            if min(l[i])<m:
                m=min(l[i])
                u=i
                v=l[i].index(m)
        
        while(parent[u]!=0):
            u=parent[u]
        while(parent[v]!=0):
            v=parent[v]

        if(v!=u):
            ne+=1
            print("Edges {}-{} cost:{}".format(u,v,m))
            mincost+=m
            parent[v]=u

        l[u][v]=999
        l[v][u]=999
    print("minimum cost :"+str(mincost))
        
kruskals(int(input()))

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
