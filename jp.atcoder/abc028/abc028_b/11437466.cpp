#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string cand = "ABCDEF";
  map<char, int> res;

  string s;
  cin >> s;
  for (char &c : s) {res[c]++;}
  for (int i = 0; i < 6; i++) {
    cout << res[cand[i]];
    char tail = (i == 5) ? '\n' : ' ';
    cout << tail;
  }
  return 0;
}
