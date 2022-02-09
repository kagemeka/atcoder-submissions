#include <bits/stdc++.h>
using namespace std;

int main() {
  int k, x;
  cin >> k >> x;
  string ans = (500 * k >= x) ? "Yes" : "No";
  cout << ans << endl;
  return 0;
}
