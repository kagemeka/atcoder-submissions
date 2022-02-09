#include <bits/stdc++.h>
using namespace std;

unordered_set<char> atcoder = {'a', 't', 'c', 'o', 'd', 'e', 'r'};

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string s, t;
  cin >> s >> t;
  int n = s.size();

  for (int i = 0; i < n; i++) {
    if (s[i] == t[i]) continue;
    if (s[i] == '@' && atcoder.find(t[i]) != atcoder.end()) continue;
    if (t[i] == '@' && atcoder.find(s[i]) != atcoder.end()) continue;
    cout << "You will lose" << endl;
    return 0;
  }
  cout << "You can win" << endl;
  return 0;

}
