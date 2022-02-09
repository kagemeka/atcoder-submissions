#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, x;
  cin >> n >> x;
  int d = min(n - x, x - 1);
  cout << d << endl;
  return 0;
}
