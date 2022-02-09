#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string s;
  cin >> s;
  while (!s.empty()) {
    if (s.substr(s.size()-5, 5) == "erase") {
      s = s.substr(0, s.size() - 5);
    } else if (s.substr(s.size()-5, 5) == "dream") {
      s = s.substr(0, s.size() - 5);
    } else if (s.substr(s.size()-6, 6) == "eraser") {
      s = s.substr(0, s.size() - 6);
    } else if (s.substr(s.size()-7, 7) == "dreamer") {
      s = s.substr(0, s.size() - 7);
    } else {
      cout << "NO" << '\n';
      return 0;
    }
  }
  cout << "YES" << '\n';
  return 0;
}
