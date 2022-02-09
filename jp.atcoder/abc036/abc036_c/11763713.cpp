#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  vector<pair<int, int>> a(n);
  for (int i = 0; i < n; i++) {
    int v;
    cin >> v;
    a[i] = pair<int, int>(v, i);
  }
  sort(a.begin(), a.end());
  vector<int> b(n);
  int i = -1;
  int prev = -1;
  for (auto &vj: a) {
    int v = vj.first, j = vj.second;
    if (v != prev) i++;
    b[j] = i;
    prev = v;
  }
  for (int &x : b) {
    cout << x << '\n';
  }
  return 0;
}
