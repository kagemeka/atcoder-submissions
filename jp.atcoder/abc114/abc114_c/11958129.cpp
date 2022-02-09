#include <bits/stdc++.h>
using namespace std;

bool is_shichigosan(int n) {
  unordered_set<int> res;
  while (n) {
    res.insert(n % 10);
    n /= 10;
  }
  return res.size() == 3;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  vector<long long> q(1001001);
  vector<int> cand = {3, 5 ,7};
  int ma = 1001001001;
  int j = 1;
  bool flag = false;
  for (int i = 0; i < 1001001; i++) {
    for (int c : cand) {
      q[j] = q[i] * 10 + c;
      if (q[j] > ma) {flag = true; break;}
      j++;
    }
    if (flag) break;
  }
  vector<int> res;
  for (int x : q) {
    if (is_shichigosan(x)) res.push_back(x);
  }
  int n; cin >> n;
  cout << upper_bound(res.begin(), res.end(), n) - res.begin() << '\n';
  return 0;
}
