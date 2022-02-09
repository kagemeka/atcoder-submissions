#include <bits/stdc++.h>
using namespace std;

int main() {
  int n = 5;
  vector<int> a(n);
  int prev = -1;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    if (a[i] == prev) {
      cout << "YES" << endl;
      return 0;
    }
    prev = a[i];
  }
  cout << "NO" << endl;
  return 0;
}
