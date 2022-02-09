#include <bits/stdc++.h>
using namespace std;

long long cnt(long long n) {
  if (n < 0) return 0;
  string m = to_string(n);
  int k = m.size();
  if (k == 1) return n + 1;
  long long tot = 0;
  tot += pow(10, (k - 1) / 2) * (m[0] - 1);
  tot += cnt(pow(10, (k - 1) - 1));
  if (k == 2) {
    tot += (m[1] >= m[0]);
  } else {
    long long tmp = stoi(m.substr(1, k - 2)) - (m[k-1] < m[0]);
    tot += cnt(tmp);
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
