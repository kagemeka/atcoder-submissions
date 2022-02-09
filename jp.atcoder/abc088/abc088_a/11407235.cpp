#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, a;
  cin >> n >> a;
  n %= 500;
  string ans = (n <= a) ? "Yes" : "No";
  cout << ans << endl;
  return 0;
}
