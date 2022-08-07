#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, a, b;
  cin >> n >> a >> b;
  int x = 0, y = 0, z = 0;
  for(int i = 0; i < n; i++) {
    int p;
    cin >> p;
    if(p <= a) x++;
    else if(p <= b) y++;
    else z++;
  }
  cout << min(min(x, y), z) << endl;
}
