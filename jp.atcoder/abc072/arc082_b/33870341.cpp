#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> p(n + 1);
  for(int i = 0; i < n; i++) {
    cin >> p[i];
    p[i]--;
  }
  int s = 0;
  for(int i = 0; i < n; i++) {
    if(p[i] == i) {
      swap(p[i], p[i + 1]);
      s++;
    }
  }
  cout << s << endl;
}
