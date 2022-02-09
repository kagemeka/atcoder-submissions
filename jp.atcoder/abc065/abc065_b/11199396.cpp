#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> a(n);
  vector<bool> pressed(n);
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }
  int now = 1;
  for (int i = 0; i < n; i++) {
    if (now == 2) {
      cout << i << endl;
      return 0;
    }
    pressed[now-1] = true;
    now = a[now-1];

    if (pressed[now-1]) {
      cout << -1 << endl;
      return 0;
    }
  }
}
