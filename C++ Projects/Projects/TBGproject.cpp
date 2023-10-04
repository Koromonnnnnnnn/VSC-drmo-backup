#include <iostream>
using namespace std;

void monsterGen();
void lootGen();

int main(){
	char destination;
	int roomIn;
    char initialQuestion;
	bool gameGoing = true;

    cout << "You wake up somewhere unknown. Bright green grass and orange trees surround you." << endl;
    cout << "Your memory is foggy and you can't quite remember anything about yourself, or how you got to this mysterious place." << endl;
    cout << "The only path forward is a steep set of ancient stone stairs." << endl;
    cout << "Press '0' to play..." << endl;
	cin >> roomIn;

    	while (gameGoing) {
		switch (roomIn) {
        case 0:
            cout << "You are in 'Room One', do you wish to go (E)ast towards 'Room Two'?" << endl;
			cin >> destination;
			if (destination == 'e' || destination == 'E')
				roomIn = 1; //2
			break;
		case 1:
            cout << "You are in 'Room Two', do you wish to go (S)outh towards 'Room Three'? Or (W)est back to 'Room One'" << endl;
			cin >> destination;
			if (destination == 's' || destination == 'S') 
				roomIn = 2; //3
            if (destination == 'w' || destination == 'W')
                roomIn = 0; //1
			break;
		case 2:
			cout << "You are in 'Room 3', you can go (S)outh to 'Room Four' (Cave), or (N)orth back to 'Room Two'" << endl;
			cin >> destination;
			if (destination == 's' || destination == 'S') 
				roomIn = 3; //4
            if (destination == 'n' || destination == 'N')
                roomIn = 1; //2
			break;
        }
    }           
}

void monsterGen() {
    int num = rand() % 100; //creates a number between 1-100
    if (num < 15) //15
        cout << "A witch appeared!" << endl;
    else if (num < 20) //5
        cout << "A kraken appeared!" << endl;
    else if (num < 50) //30
        cout << "An alien appears!" << endl;
    else if (num < 75) //25
        cout << "A wild dog appears!" << endl;
    else 
        cout << "Nothing has spawned." << endl;
}

void lootGen() {
    int num = rand() % 100; //creates a number between 1-100
    if (num < 15) //15
        cout << "You found a gun!" << endl;
    else if (num < 20) //5
        cout << "You found a sword!" << endl;
    else if (num < 50) //30
        cout << "You found a legendary sword!" << endl;
    else if (num < 75) //25
        cout << "You found a mythical bow!" << endl;
    else 
        cout << "Nothing has spawned" << endl;
}