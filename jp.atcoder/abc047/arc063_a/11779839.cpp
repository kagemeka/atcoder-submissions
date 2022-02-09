#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string s;
  cin >> s;
  int cnt = -1;
  char prev = '$';
  for (auto &c : s) {
    cnt += c != prev;
    prev = c;
  }
  cout << cnt << '\n';
  return 0;
}
