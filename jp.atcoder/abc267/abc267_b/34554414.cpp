#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string s;
  cin >> s;
  if(s[0] == '1') {
    cout << "No" << endl;
    return 0;
  }
  vector<int> col{3, 2, 4, 1, 3, 5, 0, 2, 4, 6};
  vector<int> cnt(7);
  for(int i = 0; i < 10; i++) {
    if(s[i] == '0') continue;
    cnt[col[i]]++;
  }
  for(int i = 0; i < 10; i++) {
    for(int j = i + 1; j < 10; j++) {
      for(int k = j + 1; k < 10; k++) {
        if(cnt[i] > 0 && cnt[j] == 0 && cnt[k] > 0) {
          cout << "Yes" << endl;
          return 0;
        }
      }
    }
  }
  cout << "No" << endl;
}
