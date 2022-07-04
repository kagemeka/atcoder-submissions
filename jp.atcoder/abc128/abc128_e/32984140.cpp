#include <bits/stdc++.h>

using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  // t < s < d
  // t -= x, s -= x
  int n, q;
  cin >> n >> q;

  vector<tuple<int, int, int>> events;
  for (int i = 0; i < n; i++) {
    int s, t, x;
    cin >> s >> t >> x;
    s -= x;
    t -= x;
    events.emplace_back(t, 0, x);
    events.emplace_back(s, 1, x);
  }
  for (int i = 0; i < q; i++) {
    int d;
    cin >> d;
    events.emplace_back(d, 2, i);
  }
  sort(events.begin(), events.end());

  set<int> s;

  for (auto& [t, j, i] : events) {
    if (j == 0) {
      s.erase(i);
      continue;
    }
    if (j == 1) {
      s.insert(i);
      continue;
    }
    if (s.empty()) {
      cout << -1 << endl;
    } else {
      cout << *s.begin() << endl;
    }
  }
}
