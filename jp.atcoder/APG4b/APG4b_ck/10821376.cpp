#include <bits/stdc++.h>
using namespace std;

int main() {
  string s; cin >> s;

  int res = 1;

  for (int i = 1; i < (int)(s.size()); i += 2) {
    if (s.at(i) == '+') {
      res++;
    } else {
      res--;
    }
  }
  cout << res << endl;
}
