#include <bits/stdc++.h>
using namespace std;

int main() {
  vector<int> a(5);
  for (int i = 0; i < 5; i++) {
    cin >> a[i];
  }
  int k;
  cin >> k;
  sort(a.begin(), a.end());
  string ans = (a[4] - a[0] <= k) ? "Yay!" : ":(";
  cout << ans << endl;
  return 0;
}
