
#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<vector<char>> s(n), t(n);
  for(int i = 0; i < n; i++) {
    string a;
    cin >> a;
    s[i] = vector<char>(a.begin(), a.end());
  }
  for(int i = 0; i < n; i++) {
    string a;
    cin >> a;
    t[i] = vector<char>(a.begin(), a.end());
  }
  auto transpose = [&](vector<vector<char>> a) {
    int n = a.size();
    int m = a[0].size();
    vector<vector<char>> b(m, vector<char>(n));
    for(int i = 0; i < n; i++) {
      for(int j = 0; j < m; j++) { b[j][i] = a[i][j]; }
    }
    return b;
  };
  auto rot90 = [&](vector<vector<char>> a) -> vector<vector<char>> {
    reverse(a.begin(), a.end());
    return transpose(a);
  };
  auto crop_bottom = [&](vector<vector<char>> a) {
    int n = a.size();
    int m = a[0].size();
    auto ptr = a.end();
    for(int i = n - 1; i >= 0; i--) {
      for(int j = 0; j < m; j++) {
        if(a[i][j] == '#') return vector(a.begin(), ptr);
      }
      ptr--;
    }
    vector<vector<char>> pseudo;
    return pseudo;
  };
  auto crop = [&](vector<vector<char>> a) {
    for(int i = 0; i < 4; i++) {
      a = crop_bottom(a);
      a = rot90(a);
    }
    return a;
  };
  s = crop(s);
  t = crop(t);
  int h = s.size();
  int w = s[0].size();
  // cout << h << ' ' << w << endl;
  // for(int i = 0; i < h; i++) {
  //   for(int j = 0; j < w; j++) { cout << s[i][j] << " \n"[j == w - 1]; }
  // }
  auto match = [&](auto t) -> bool {
    int h2 = t.size();
    int w2 = t[0].size();
    // for(int i = 0; i < h2; i++) {
    //   for(int j = 0; j < w2; j++) { cout << t[i][j] << " \n"[j == w2 - 1]; }
    // }
    if(h2 != h || w2 != w) return false;
    for(int i = 0; i < h; i++) {
      for(int j = 0; j < w; j++) {
        if(s[i][j] != t[i][j]) return false;
      }
    }
    return true;
  };
  for(int k = 0; k < 4; k++) {
    t = rot90(t);
    if(match(t)) {
      cout << "Yes" << endl;
      return 0;
    }
  }
  cout << "No" << endl;
}
