#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, a, b;
  cin >> n >> a >> b;
  int res = min(n * a, b);
  cout << res << endl;
}
