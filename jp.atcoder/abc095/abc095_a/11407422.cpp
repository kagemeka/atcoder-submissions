#include <bits/stdc++.h>
using namespace std;

int main() {
  string s;
  cin >> s;
  int cnt = 0;
  for (char c : s) {
    if (c == 'o') cnt++;
  }
  cout << 700 + 100 * cnt << endl;
  return 0;
}
