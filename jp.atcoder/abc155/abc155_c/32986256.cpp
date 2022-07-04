#include <bits/stdc++.h>

using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  cin >> n;

  map<string, int> cnt;
  while (n--) {
    string s;
    cin >> s;
    cnt[s]++;
  }

  using p = pair<string, int>;
  vector<p> a(cnt.begin(), cnt.end());
  sort(a.begin(), a.end(), [](p x, p y) {
    if (x.second != y.second) {
      return x.second > y.second;
    }
    return x.first < y.first;
  });

  int t = a[0].second;
  for (auto& [s, c] : a) {
    if (c != t) break;
    cout << s << endl;
  }
}
