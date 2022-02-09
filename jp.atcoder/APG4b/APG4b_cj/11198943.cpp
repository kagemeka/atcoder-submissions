#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  int a[n];
  int tot = 0;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    tot += a[i];
  }
  int ave = tot / n;

  for (int i = 0; i < n; i++) {
    cout << abs(ave - a[i]) << endl;
  }
  return 0;
}
