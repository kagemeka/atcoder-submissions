#include <iostream>
#include <vector>
// #include <algorithm>


template <typename T>
int bit_length(const T &n) {
  int l = 0;
  while (1 << l <= n) l++;
  return l;
}



template <typename T>
int bit_count(T n) {
  int cnt = 0;
  while (n) {cnt += n & 1; n >>= 1;}
  return cnt;
}

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n, m;
  std::cin >> n >> m;
  std::vector<int> relation(n);
  for (int i = 0; i < n; i++) relation[i] = 1 << i;
  for (int i = 0; i < m; i++) {
    int x, y;
    std::cin >> x >> y;
    x--; y--;
    relation[x] |= 1 << y;
    relation[y] |= 1 << x;
  }
  int mx = 0;
  for (int s = 0; s < 1 << n; s++) {
    int t = s;
    for (int i = 0; i < n; i++) {
      if (~s >> i & 1) continue;
      t &= relation[i];
    }
    if (t != s) continue;
    mx = std::max(mx, bit_count(s));
  }
  std::cout << mx << '\n';

}
