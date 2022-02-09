#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  string s;
  long long k;
  cin >> s >> k;
  for (auto &c : s) {
    if (c != '1') {
      cout << c << '\n';
      return 0;
    }
  }
}
