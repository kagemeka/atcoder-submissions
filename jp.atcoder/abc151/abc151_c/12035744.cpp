#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, m; cin >> n >> m;
  vector<int> wa(n);
  vector<int> ac(n);
  int tot = 0;
  int penalties = 0;
  for (int i = 0; i < m; i++) {
    int p; string s; cin >> p >> s; p -= 1;
    if (s == "AC") {
      if (!ac[p]) {
        tot += 1;
        penalties += wa[p];
        ac[p] = 1;
      }
    } else {
      wa[p]++;
    }
  }

  cout << tot << " " << penalties << '\n';
  return 0;

}
