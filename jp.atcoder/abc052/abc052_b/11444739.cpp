#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  string s;
  cin >> n >> s;
  int cum = 0;
  int m = 0;
  for (char &c : s) {
    (c == 'I') ? cum++ : cum--;
    m = max(m, cum);
  }
  cout << m << '\n';
  return 0;
}
