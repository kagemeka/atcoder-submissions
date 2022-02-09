#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  vector<pair<int, int>> p(n);
  for (int i = 0; i < n; i++) {
    int a; cin >> a;
    p[i] = make_pair(a, i + 1);
  }
  sort(p.begin(), p.end());
  for (int i = 0; i < n; i++) {
    char tail = (i == n - 1) ? '\n' : ' ';
    cout << p[i].second << tail;
  }
  return 0;
}
