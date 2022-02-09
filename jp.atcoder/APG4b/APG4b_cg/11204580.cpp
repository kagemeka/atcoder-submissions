#include <bits/stdc++.h>
using namespace std;

int main() {
  int n = 5;
  int cur;
  int prev = -1;
  for (int i = 0; i < n; i++) {
    cin >> cur;
    if (cur == prev) {
      cout << "YES" << endl;
      return 0;
    }
    prev = cur;
  }
  cout << "NO" << endl;
  return 0;
}
