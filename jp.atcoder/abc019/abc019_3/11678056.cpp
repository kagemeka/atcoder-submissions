#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  unordered_set<int> res;
  for (int i = 0; i < n; i++) {
    int a;
    cin >> a;
    while (a % 2 == 0) {
      a /= 2;
    }
    res.insert(a);
  }
  cout << res.size() << '\n';
  return 0;
}
