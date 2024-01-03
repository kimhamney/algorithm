#include <iostream>
#include <string>
using namespace std;

int main() {
	// your code goes here
	int count;
	cin >> count;
	
	char s;
	int total = 0;
	for (int i = 0; i < count; i++) {
		cin >> s;
		total += (s - '0');
	}
	
	cout << total;
	return 0;
}