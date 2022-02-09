import 'dart:io';



int readInt() {return int.parse(stdin.readLineSync());}

class ABC001 {
  static void a() {
    int h1 = readInt(), h2 = readInt();

    print(h1-h2);
  }
}

void main() {
  ABC001.a();

}
