import sys

n, m = map(int, sys.stdin.readline().split())

root = list(range(n))
height = [0] * n
size = [1] * n

def find_root(u):
  if root[u] == u: return u
  root[u] = find_root(root[u])
  return root[u]

def unite(u, v):
  ru = find_root(u)
  rv = find_root(v)
  if ru == rv: return
  if height[ru] >= height[rv]:
    root[rv] = ru
    size[ru] += size[rv]
    height[ru] = max(height[ru], height[rv] + 1)
  else:
    root[ru] = rv
    size[rv] += size[ru]

def main():
  for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    unite(x-1, y-1)

  for i in range(n): find_root(i)
  print(len(set(root)))

if __name__ == '__main__':
  main()
