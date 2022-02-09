#include <bits/stdc++.h>
using namespace std;

int main() {
  vector<string> day = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
  map<string, int> res;
  for (int i = 0; i < 7; i++) {
    res[day[i]] = 7 - i;
  }
  string s;
  cin >> s;
  cout << res[s] << endl;
  return 0;
}
