#include <bits/stdc++.h>
using namespace std;

map<char, char> p = {{'A', 'T'}, {'T', 'A'}, {'C', 'G'}, {'G', 'C'}};

int main() {
  char b;
  cin >> b;
  cout << p[b] << endl;
  return 0;

}
