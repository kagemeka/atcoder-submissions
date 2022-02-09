#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, k, x, y;
  cin >> n >> k >> x >> y;
  int fee = (n <= k) ? x * n : x * k + y * (n - k);
  cout << fee << endl;
  return 0;
}
