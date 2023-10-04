//9/18/2023 daily code with gus

#include <iostream>
using namespace std;
int main() {
	char destination;
	int roomIn;
	bool gameGoing = true;
	cout << "What room would you like to visit?" << endl;
	cin >> roomIn;
	

	while (gameGoing) {
		switch (roomIn) {
		case 1:
			cout << "You are in room 1, you can go (E)ast to room 2." << endl;
			cin >> destination;
			if (destination == 'E') {
				roomIn = 2;
			}
			break;
		case 2:
			cout << "You are in room 2, you can go (W)est to room 1, (N)orth to room 3, or (S)outh to room 4." << endl;
			cin >> destination;
			switch (destination) {
			case 'W':
				roomIn = 1;
				break;
			case 'N':
				roomIn = 3;
				break;
			case 'S':
				roomIn = 4;
				break;
			}
			break;
		case 3:
			cout << "You are in room 3, you can go (S)outh to room 2." << endl;
			cin >> destination;
			if (destination == 'S') {
				roomIn = 2;
			}
			break;
		case 4:
			cout << "You are in room 4, you can go (N)orth to room 2, or (E)ast to room 5." << endl;
			cin >> destination;
			switch (destination) {
			case 'N':
				roomIn = 2;
				break;
			case 'E':
				roomIn = 5;
				break;
			}
			break;
		case 5:
			cout << "You are in room 5, you can go (W)est to room 4." << endl;
			cin >> destination;
			if (destination == 'W') {
				roomIn = 4;
			}
			break;
		default:
			cout << "Sorry that's not a valid option!" << endl;
		}
	}
}



	

