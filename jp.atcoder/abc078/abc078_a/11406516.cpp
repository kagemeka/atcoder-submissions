#include <bits/stdc++.h>
using namespace std;

int main() {
  char x, y;
  cin >> x >> y;
  char res;
  if (x > y) {
    res = '>';
  } else if (x == y) {
    res = '=';
  } else {
    res = '<';
  }
  cout << res << endl;
  return 0;
}
