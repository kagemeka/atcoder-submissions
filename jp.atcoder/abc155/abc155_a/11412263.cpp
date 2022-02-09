#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  vector<int> a(3);
  for (int i = 0; i < 3; i++) {
    cin >> a[i];
  }
  sort(a.begin(), a.end());
  string ans;
  ans = ((a[0] == a[1] && a[1] != a[2]) || (a[0] != a[1] && a[1] == a[2])) ? "Yes" : "No";
  cout << ans << endl;
  return 0;
}
