#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b;
  cin >> a >> b;
  string ans = a * b & 1 ? "Odd" : "Even";
  cout << ans << endl;
  return 0;

}
