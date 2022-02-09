#include <bits/stdc++.h>
using namespace std;


int main() {
  vector<string> weather = {"Sunny", "Cloudy", "Rainy"};

  string s;
  cin >> s;
  int i = find(weather.begin(), weather.end(), s) - weather.begin();

  cout << weather[(i + 1) % 3] << endl;
  return 0;
}
