#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  string s;
  cin >> n >> s;
  int c = 1;
  for(int i = 0; i < n - 1; i++) c += s[i] != s[i + 1];
  cout << c << '\n';
}
