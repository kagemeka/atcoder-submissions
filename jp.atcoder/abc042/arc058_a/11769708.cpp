#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, k;
  cin >> n >> k;
  unordered_set<int> d;
  for (int i = 0; i < n; i++) {
    int a;
    cin >> a;
    d.insert(a);
  }

  int i = n;
  while (true) {
    int m = i;
    bool flag = false;
    while (m) {
      if (d.find(m % 10) != d.end()) {
        flag = true;
        break;
      }
      m /= 10;
    }
    if (flag) {i++; continue;}
    cout << i << '\n';
    return 0;
  }
}
