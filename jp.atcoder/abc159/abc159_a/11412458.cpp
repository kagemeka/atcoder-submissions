#include <bits/stdc++.h>
using namespace std;

int choose2(int const &n) {
  return n * (n - 1) / 2;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, m;
  cin >> n >> m;

  cout << choose2(n) + choose2(m) << endl;
  return 0;
}
