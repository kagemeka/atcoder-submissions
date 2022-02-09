#include <bits/stdc++.h>
using namespace std;

long long cnt(long long n) {
  string m = to_string(n);
  int k = m.size();
  if (k == 1) return n + 1;
  long long tot = 0;
  tot += pow(10, (k - 1) / 2) * (m[0] - '1');
  tot += pow(10, k / 2) * 2 - 1 - 9 * pow(10, (k - 2) / 2) * (k & 1 ^ 1);
  while (k >= 2) {
    k -= 2;
    if (k == 0) {
      tot += m[1] >= m[0];
      break;
    } else if (k == 1) {
      tot += m[1] - '0' - (m[2] < m[0]) + 1;
      break;
    } else {
      string l = m.substr(1, k);
      n = stoi(l) - (m[k+1] < m[0]);
      m = to_string(n);
      while (m.size() < k) m = '0' + m;
      tot += (m[0] - '0') * pow(10, (k - 1) / 2);
    }
  }
  return tot;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  long long a, b;
  cin >> a >> b;

  cout << cnt(b) - cnt(a - 1) << '\n';
  return 0;
}
