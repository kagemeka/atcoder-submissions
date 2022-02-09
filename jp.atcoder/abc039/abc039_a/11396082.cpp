#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b, c;
  cin >> a >> b >> c;
  int s = 2 * (a*b + b*c + c*a);
  cout << s << endl;
  return 0;
}
