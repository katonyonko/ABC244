from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="244"
#問題
problem="f"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/abc{0}_{1}".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  from collections import deque
  def bfs(s):
    inf=10**10
    D=[inf]*(2**N*N)
    dq=deque()
    for i in range(len(s)):
      D[s[i]]=1
      dq.append(s[i])
    while dq:
      x=dq.popleft()
      S,v=x%(2**N),x//(2**N)
      for y in E[v]:
        if D[S^(1<<y)+2**N*y]>D[x]+1:
          D[S^(1<<y)+2**N*y]=D[x]+1
          dq.append(S^(1<<y)+2**N*y)
    return D
  N,M=map(int,input().split())
  E=[set() for _ in range(N)]
  for i in range(M):
    u,v=map(int,input().split())
    u-=1; v-=1
    for j in range(2**N):
      E[u].add(v)
      E[v].add(u)
  ans=bfs([(1<<i)+2**N*i for i in range(N)])
  print(sum([min([ans[i+2**N*j] for j in range(N)]) for i in range(1,2**N)]))
  """ここから上にコードを記述"""

  print(test_case[__+1])