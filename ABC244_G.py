import io
import sys

_INPUT = """\
6
6 6
6 3
2 5
4 2
1 3
6 5
3 2
110001
3 3
3 1
3 2
1 2
000
"""
sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  ans=[]
  def EulerTour(G, s):
    tmp=[0]*len(G)
    depth=[-1]*len(G)
    depth[s]=0
    done = [0]*len(G)
    Q = [~s, s] # 根をスタックに追加
    parent=[-1]*len(G)
    ET = []
    left,right=[-1]*len(G),[-1]*len(G)
    while Q:
      i = Q.pop()
      if i >= 0: # 行きがけの処理
        ans.append(i)
        tmp[i]^=1
        done[i] = 1
        ET.append(i)
        for a in G[i][::-1]:
          if done[a]: continue
          depth[a]=depth[i]+1
          parent[a]=i
          Q.append(~a) # 帰りがけの処理をスタックに追加
          Q.append(a) # 行きがけの処理をスタックに追加
      else: # 帰りがけの処理
        ans.append(parent[-i-1])
        tmp[parent[-i-1]]^=1
        if tmp[-i-1]!=int(S[-i-1]):
          if parent[-i-1]!=-1:
            ans.append(-i-1)
            ans.append(parent[-i-1])
            tmp[-i-1]^=1
            tmp[parent[-i-1]]^=1
          else:
            ans.pop()
            tmp[parent[-i-1]]^=1
        ET.append(i)
    ans.pop()

  class UnionFind():
    def __init__(self, n):
      self.n = n
      self.parents = [-1] * n
    def find(self, x):
      if self.parents[x] < 0:
        return x
      else:
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def union(self, x, y):
      x = self.find(x)
      y = self.find(y)
      if x == y:
        return
      if self.parents[x] > self.parents[y]:
        x, y = y, x
      self.parents[x] += self.parents[y]
      self.parents[y] = x
    def size(self, x):
      return -self.parents[self.find(x)]
    def same(self, x, y):
      return self.find(x) == self.find(y)
    def members(self, x):
      root = self.find(x)
      return [i for i in range(self.n) if self.find(i) == root]
    def roots(self):
      return [i for i, x in enumerate(self.parents) if x < 0]
    def group_count(self):
      return len(self.roots())
    def all_group_members(self):
      return {r: self.members(r) for r in self.roots()}
    def __str__(self):
      return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

  N,M=map(int,input().split())
  uf=UnionFind(N)
  G=[[] for _ in range(N)]
  for _ in range(M):
    u,v=map(lambda x: int(x)-1, input().split())
    if uf.find(u)!=uf.find(v):
      uf.union(u,v)
      G[u].append(v)
      G[v].append(u)
  S=input()
  EulerTour(G,0)
  print(len(ans))
  print(*[ans[i]+1 for i in range(len(ans))])