#include <bits/stdc++.h>
using namespace std;

int strongness(int n) {
  return (n + 11) % 13;
}

int main() {
  int a, b;
  cin >> a >> b;
  int sa = strongness(a);
  int sb = strongness(b);
  string ans;
  if (sa > sb) {
    ans = "Alice";
  } else if (sa == sb) {
    ans = "Draw";
  } else {
    ans = "Bob";
  }
  cout << ans << endl;
  return 0;
}
