#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b;
  cin >> a >> b;
  int d = abs(a - b);
  if (d & 1) {
    cout << "IMPOSSIBLE" << endl;
  } else {
    cout << min(a, b) + d / 2 << endl;
  }
  return 0;
}
