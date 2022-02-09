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
  vector<long long> res(9);
  for (int i = 0; i < 9; i++) res[i] = i + 1;
  vector<long long> nex;
  while (true) {
    for (long long &n : res) {
      int d = n % 10;
      n *= 10;
      for (int i = -1; i < 2; i++) {
        int tail = d + i;
        if (tail < 0 || tail > 9) continue;
        nex.emplace_back(n + tail);
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
