#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int k, x;
  cin >> k >> x;
  int r = min(1000000, x + k - 1);
  int l = max(-1000000, x - (k - 1));
  for (int i = l; i <= r; i++) {
    cout << i;
    char tail = (i == r) ? '\n' : ' ';
    cout << tail;
  }
  return 0;
}
