#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b, c;
  cin >> a >> b >> c;
  string ans;
  ans = (a <= c && c <= b) ? "Yes" : "No";
  cout << ans << endl;
  return 0;
}
