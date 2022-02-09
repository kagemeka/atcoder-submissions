#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;

  unordered_set<int> visited;
  int cnt = 0;
  int a;
  for (int i = 0; i < n; i++) {
    cin >> a;
    if (visited.find(a) != visited.end()) cnt++;
    visited.insert(a);
  }
  cout << cnt << '\n';
  return 0;
}
