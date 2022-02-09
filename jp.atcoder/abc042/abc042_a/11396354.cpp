#include <bits/stdc++.h>
using namespace std;

int main() {
  vector<int> c(11, 0);
  for (int i = 0; i < 3; i++) {
    int a;
    cin >> a;
    c[a]++;
  }
  string ans = (c[5] == 2 && c[7] == 1) ? "YES" : "NO";
  cout << ans << endl;
  return 0;
}
