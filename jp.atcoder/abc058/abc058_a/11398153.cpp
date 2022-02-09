#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b, c;
  cin >> a >> b >> c;
  string ans = b - a == c - b ? "YES" : "NO";
  cout << ans << endl;
  return 0;
}
