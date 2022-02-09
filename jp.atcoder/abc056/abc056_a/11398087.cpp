#include <bits/stdc++.h>
using namespace std;

bool convert(char c) {
  return (c == 'H') ? 1 : 0;
}

int main() {
  char a, b;
  cin >> a >> b;
  char ans = convert(a) ^ convert(b) ? 'D' : 'H';
  cout << ans << endl;
  return 0;
}
