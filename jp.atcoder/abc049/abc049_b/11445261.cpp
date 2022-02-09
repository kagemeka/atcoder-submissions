#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int h, w;
  cin >> h >> w;
  string s;
  for (int i = 0; i < h; i++) {
    cin >> s;
    for (int i = 0; i < 2; i++) {cout << s << '\n';}
  }
  return 0;
}
