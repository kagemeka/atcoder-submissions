#include <iostream>
#include <set>
#include <vector>
#include <algorithm>

int main() {
  using namespace std;
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, m;
  cin >> n >> m;
  string s;
  cin >> s;

  set<int> ok;
  for ( int i = 0; i < n + 1; i++ ) {
    if (s[i] == '0') ok.insert(i);
  }
  vector<int> res;
  int i = n;
  while (i > 0) {
    int j = *ok.lower_bound(i - m);
    if (j == i) {
      cout << -1 << '\n';
      return 0;
    }
    res.push_back(i - j);
    i = j;
  }
  for ( int i = res.size() - 1; i > 0; i--) {
    cout << res[i] << ' ';
  }
  cout << res[0] << '\n';

}
