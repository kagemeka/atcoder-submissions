#include <bits/stdc++.h>
using namespace std;

string s = "ACGT", t = "TGCA";
map<char, char> p;

void prepare() {
  for (int i = 0; i < 4; i++) {
    p[s[i]] = t[i];
  }
}

int main() {
  prepare();
  char b;
  cin >> b;
  cout << p[b] << endl;
  return 0;
}
