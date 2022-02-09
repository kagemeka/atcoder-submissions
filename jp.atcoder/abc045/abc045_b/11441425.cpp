#include <bits/stdc++.h>
using namespace std;

int main() {
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
