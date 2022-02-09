#include <bits/stdc++.h>
using namespace std;

int main() {
  vector<int> a(3);
  for (int i = 0; i < 3; i++) {
    cin >> a[i];
  }
  sort(a.begin(), a.end());
  int ans = a[2] - a[0];
  cout << ans << endl;
  return 0;
}
