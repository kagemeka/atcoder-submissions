#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int a, b;
  cin >> a >> b;
  int d = b - a;
  int depth = (1 + d) * d / 2 - b;
  cout << depth << '\n';
  return 0;
}
