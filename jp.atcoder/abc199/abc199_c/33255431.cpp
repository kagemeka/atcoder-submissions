#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  string s;
  int q;
  cin >> n >> s >> q;
  int flip = 0;
  while(q--) {
    int t, a, b;
    cin >> t >> a >> b;
    a--;
    b--;
    if(flip) {
      a += n;
      b += n;
      a %= 2 * n;
      b %= 2 * n;
    }
    if(t == 1) {
      swap(s[a], s[b]);
    } else {
      flip ^= 1;
    }
  }
  if(flip) {
    for(int i = 0; i < n; i++) swap(s[i], s[i + n]);
  }
  cout << s << endl;
}
