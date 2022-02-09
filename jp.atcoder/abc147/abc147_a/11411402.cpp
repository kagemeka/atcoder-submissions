#include <bits/stdc++.h>
using namespace std;

int main() {
  vector<int> a(3);
  for (int i = 0; i < 3; i++) {
    cin >> a[i];
  }
  string ans = (accumulate(a.begin(), a.end(), 0) >= 22) ? "bust" : "win";
  cout << ans << endl;
  return 0;
}
