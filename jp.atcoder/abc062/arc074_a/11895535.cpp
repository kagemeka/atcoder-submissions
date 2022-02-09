#include <bits/stdc++.h>
using namespace std;

int solve(long long h, long long w) {
  vector<long long> res = {w * ((h + 2) / 3 - h / 3)};
  for (auto &d : {(h + 2) / 3, h / 3}) {
    vector<long long> cand;
    cand.push_back(d * w);
    cand.push_back((h - d) * (w / 2));
    cand.push_back((h - d) * ((w + 1) / 2));
    sort(cand.begin(), cand.end());
    res.push_back(cand[2] - cand[0]);
  }
  return *min_element(res.begin(), res.end());
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int h, w;
  cin >> h >> w;
  int ans = min(solve(h, w), solve(w, h));
  cout << ans << '\n';
  return 0;
}
