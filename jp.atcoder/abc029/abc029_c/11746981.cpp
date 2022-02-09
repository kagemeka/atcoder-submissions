#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  vector<char> cand = {'a', 'b', 'c'};
  int n;
  cin >> n;
  queue<string> q;
  q.push("");
  for (int i = 0; i < n; i++) {
    int l = q.size();
    for (int j = 0; j < l; j++) {
      string cur = q.front(); q.pop();
      for (char &c : cand) {
        q.push(cur + c);
      }
    }
  }

  for (int i = 0; i < pow(3, n); i++) {
    cout << q.front() << '\n';
    q.pop();
  }
  return 0;
}
