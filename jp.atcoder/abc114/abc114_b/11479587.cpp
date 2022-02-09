#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string s;
  cin >> s;
  int n = s.size();
  int d = 1000;
  for (int i = 0; i < n - 2; i++) {
    int x = stoi(s.substr(i, 3));
    d = min(d, abs(753 - x));
  }
  cout << d << '\n';
  return 0;
}
