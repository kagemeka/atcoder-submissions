#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int k;
  cin >> k;
  if (k <= 9) {
    cout << k << '\n';
    return 0;
  }
  k -= 9;
  vector<string> res;
  for (int i = 1; i <= 9; i++) res.push_back(to_string(i));
  vector<string> nex;
  while (true) {
    for (string &n : res) {
      char d = n[n.size()-1];
      for (int i = -1; i < 2; i++) {
        char tail = d + i;
        if (tail < '0' || tail > '9') continue;
        nex.push_back(n + tail);
        k--;
        if (k == 0) {
          cout << nex[nex.size()-1] << '\n';
          return 0;
        }
      }
    }
    res = nex;
    nex.clear();
  }
}
