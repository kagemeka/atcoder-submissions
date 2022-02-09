#include <bits/stdc++.h>
using namespace std;

int main() {
  string n;
  cin >> n;
  int tot = 0;
  for (int i = 0; i < (int)(n.size()); i++) {
    tot += n[i] - '0';
  }
  string ans;
  int m = stoi(n);
  if (m % tot) {
    ans = "No";
  } else {
    ans = "Yes";
  }
  cout << ans << endl;
}
