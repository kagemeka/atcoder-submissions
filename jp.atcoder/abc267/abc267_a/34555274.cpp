#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  vector<string> a{"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"};
  string s;
  cin >> s;
  for(int i = 0; i < 5; i++) {
    if(s == a[i]) {
      cout << 5 - i << endl;
      return 0;
    }
  }
}
