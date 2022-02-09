#include <bits/stdc++.h>
using namespace std;

int main() {
  string x;
  cin >> x;
  int res = 0;
  for (char c : x) res += c - '0';
  cout << res << endl;
  return 0;
}
