#include <bits/stdc++.h>
using namespace std;

typedef tuple<char, int, int> tcii;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, k;
  string s;
  cin >> n >> k >> s;
  vector<bool> swapped(n, false);
  for (int i = 0; i < n - 1; i++) {
    int r = k - (swapped[i] ^ 1);
    int j;
    priority_queue<tcii, vector<tcii>, greater<tcii>> q;
    for (j = i + 1; j < n; j++) {
      if (s[j] >= s[i]) continue;
      int cost = swapped[j] ^ 1;
      if (r - cost < 0) continue;
      q.push(make_tuple(s[j], cost - r, -j));
    }
    if (q.empty()) continue;
    tcii res = q.top();
    j = -get<2>(res);
    swap(s[i], s[j]);
    swapped[i] = swapped[j] = true;
    k = -get<1>(res);
  }
  cout << s << '\n';
  return 0;
}
