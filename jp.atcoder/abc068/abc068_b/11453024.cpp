#include <bits/stdc++.h>
using namespace std;

int pow2(int x, int n) {
  if (n == 0) return 1;
  if (n == 1) return x;
  int res = 1;
  for (int i = 0; i < 31; i++) {
    if (n >> i & 1) res *= pow(x, pow(2, i));
  }
  return res;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  cout << pow2(2, floor(log2(n))) << '\n';
  return 0;
}
