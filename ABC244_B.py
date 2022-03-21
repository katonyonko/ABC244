from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="244"
#問題
problem="b"

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
test_case=test_case[1:]
for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  N=int(input())
  T=input()
  x,y,d=0,0,0
  dic=[[1,0],[0,-1],[-1,0],[0,1]]
  for i in range(N):
    if T[i]=='S':
      x+=dic[d][0]
      y+=dic[d][1]
    else:
      d=(d+1)%4
  print(x,y)
  """ここから上にコードを記述"""

  print(test_case[__+1])