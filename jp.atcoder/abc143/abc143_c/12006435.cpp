#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  char prev = '$';
  int cnt = 0;
  for (int i = 0; i < n; i++) {
    char s; cin >> s;
    if (s == prev) continue;
    cnt++;
    prev = s;
  }
  cout << cnt << '\n';
  return 0;
}
