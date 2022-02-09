import 'dart:io';
import 'dart:math';


String read() => stdin.readLineSync();
int readInt() => int.parse(stdin.readLineSync());
List<String> readList() => stdin.readLineSync().split(' ');
List<int> readIntList() => (stdin.readLineSync().split(' ').map((x) => int.parse(x)).toList());

class ABC001 {
  static void a() {
    int h1 = readInt(), h2 = readInt();

    print(h1-h2);
  }

  static void b() {

  }
}


class ABC002 {
  static void a() {
    var l = readIntList();
    print(max(l[0], l[1]));
  }
}

void main() {
  ABC002.a();
}
