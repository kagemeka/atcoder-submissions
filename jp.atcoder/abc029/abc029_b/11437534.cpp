#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string s;
  int cnt = 0;
  for (int i = 0; i < 12; i++) {
    cin >> s;
    if (s.find('r') != string::npos) {cnt++;}
  }
  cout << cnt << '\n';
  return 0;
}
