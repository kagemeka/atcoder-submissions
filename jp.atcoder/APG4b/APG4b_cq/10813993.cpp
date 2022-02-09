#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b;
  string op;
  cin >> a >> op >> b;

  string error = "error";

  if (op == "+") {
    cout << a + b << endl;
  } else if (op == "-") {
    cout << a - b << endl;
  } else if (op == "*") {
    cout << a * b << endl;
  } else if (op == "/") {
    if (b == 0) {
      cout << error << endl;
    } else {
      cout << a / b << endl;
    }
  } else {
    cout << error << endl;
  }
}
