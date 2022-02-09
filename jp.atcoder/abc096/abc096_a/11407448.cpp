#include <bits/stdc++.h>
using namespace std;

int main() {
  int m, d;
  cin >> m >> d;
  int c = (m <= d) ? m : m - 1;
  cout << c << endl;
  return 0;
}
