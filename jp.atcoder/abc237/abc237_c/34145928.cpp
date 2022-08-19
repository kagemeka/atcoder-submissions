#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string s;
  cin >> s;
  int d = 0;
  while(s.size() && s.back() == 'a') {
    d++;
    s.pop_back();
  }
  reverse(s.begin(), s.end());
  while(s.size() && s.back() == 'a') {
    d--;
    s.pop_back();
  }
  string t = s;
  reverse(t.begin(), t.end());
  if(d >= 0 && s == t) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }
}
