#include <bits/stdc++.h>
using namespace std;

long long gcd(long long a, long long b) {return b ? gcd(b, a % b) : abs(a);}
long long lcm(long long a, long long b) {return abs(a / gcd(a, b) * b);}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  vector<vector<long long>> res(n, vector<long long>(2));
  for (int i = 0; i < n; i++) {
    int t, a;
    cin >> t >> a;
    res[i][0] = t;
    res[i][1] = a;
  }

  for (int i = 0; i < n - 1; i++) {
    long long a = (res[i][0] + res[i+1][0] - 1) / res[i+1][0];
    long long b = (res[i][1] + res[i+1][1] - 1) / res[i+1][1];
    long long m = max(a, b);
    res[i+1][0] *= m;
    res[i+1][1] *= m;
  }
  cout << res[n-1][0] + res[n-1][1] << '\n';
  return 0;
}
