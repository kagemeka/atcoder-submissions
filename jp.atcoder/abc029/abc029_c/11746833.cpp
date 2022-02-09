#include <bits/stdc++.h>
using namespace std;

int pow(int x, int n) {
  if (n == 0) return 1;
  if (n & 1) return x * pow(x, n - 1);
  int h = pow(x, n / 2);
  return h * h;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  vector<char> cand = {'a', 'b', 'c'};
  int n;
  cin >> n;
  queue<string> q;
  q.push("");
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < pow(3, i); j++) {
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
