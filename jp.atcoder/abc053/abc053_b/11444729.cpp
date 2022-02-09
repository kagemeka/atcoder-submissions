#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string s;
  cin >> s;
  int l, r;
  l = s.find_first_of('A');
  r = s.find_last_of('Z');
  cout << r - l + 1 << '\n';
  return 0;
}
