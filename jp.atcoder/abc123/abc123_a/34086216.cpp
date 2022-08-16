#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  vector<int> a(5);
  int k;
  for(int i = 0; i < 5; i++) cin >> a[i];
  cin >> k;
  for(int i = 0; i < 5; i++) {
    for(int j = 0; j < i; j++) {
      if(abs(a[i] - a[j]) > k) {
        cout << ":(" << endl;
        return 0;
      }
    }
  }
  cout << "Yay!" << endl;
}
