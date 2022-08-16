#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  auto normalize = [&](string s) -> pair<int, int> {
    int l = 0;
    int r = 0;
    for(auto& c: s) {
      if(c == '(') l++;
      else {
        if(l > 0) l--;
        else r++;
      }
    }
    // cout << l << ' ' << r << endl;
    // l = (, r = )
    return {l, r};
  };
  vector<pair<int, int>> a, b;
  for(int i = 0; i < n; i++) {
    string s;
    cin >> s;
    auto x = normalize(s);
    if(x.first >= x.second) a.push_back(x);
    else b.push_back(x);
  }
  sort(a.begin(), a.end(), [](auto& i, auto& j) {
    return i.second < j.second;
  });
  sort(b.begin(), b.end(), [](auto& i, auto& j) { return i.first > j.second; });
  int x = 0;
  for(auto& [l, r]: a) {
    // cout << l << ' ' << r << endl;
    if(x < r) {
      cout << "No" << endl;
      return 0;
    }
    x -= r;
    x += l;
  }
  for(auto& [l, r]: b) {
    // cout << l << ' ' << r << endl;
    if(x < r) {
      cout << "No" << endl;
      return 0;
    }
    x -= r;
    x += l;
  }
  cout << (x == 0 ? "Yes": "No") << endl;
}
