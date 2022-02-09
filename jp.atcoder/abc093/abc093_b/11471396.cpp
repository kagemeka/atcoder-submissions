#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int a, b, k;
  cin >> a >> b >> k;
  int c = b - a + 1;
  set<int> res;
  for (int i = 0; i < min(k, c); i++) {
    res.insert(a + i);
    res.insert(b - i);
  }
  for (const int &r : res) {cout << r << '\n';}
  return 0;
}
