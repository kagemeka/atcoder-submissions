#include <bits/stdc++.h>
using namespace std;


int main() {
  string w;
  cin >> w;
  std::set<char> vowels;
  for (char &c : "aeiou"s) {
    vowels.insert(c);
  }
  string t;
  for (char &c : w) {
    if (vowels.count(c)) continue;
    t += c;
  }
  cout << t << '\n';
}
