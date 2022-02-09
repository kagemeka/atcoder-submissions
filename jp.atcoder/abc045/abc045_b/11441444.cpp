#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string a, b, c;
  cin >> a >> b >> c;

  map<char, string> s = {{'a', a}, {'b', b}, {'c', c}};
  char nex = 'a';
  char cur;
  while (true) {
    if (s[nex].empty()) {
      printf("%c\n", toupper(nex));
      return 0;
    }
    cur = nex;
    nex = s[cur][0];
    s[cur] = s[cur].substr(1);
  }
}
