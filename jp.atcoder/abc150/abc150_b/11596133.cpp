#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  string s;
  cin >> n >> s;
  int cnt = 0;
  for (int i = 0; i < n - 2; i++) {
    cnt += (s.substr(i, 3) == "ABC");
  }
  cout << cnt << '\n';
  return 0;
}
