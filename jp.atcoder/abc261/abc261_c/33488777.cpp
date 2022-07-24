#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  map<string, int> cnt;
  while(n--) {
    string s;
    cin >> s;
    int c = cnt[s];
    cnt[s]++;
    if(c) s += "(" + to_string(c) + ")";
    cout << s << endl;
  }
}
