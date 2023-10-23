#include <iostream>
using namespace std;

int main(){
    int room = 1;
    char input = 'a';
    int playerHealth = 100;
    while(playerHealth >= 0 && input != 'q') {
        switch (room) {
            case 1:
            cout << "Youre in room 1, you can go (s)outh" << endl;
            cin >> input;
            if (input == 's')
                room = 1;
            break;
            case 2:
            cout << "Youre in room 2, you can go (n)orth" << endl;
            cin >> input;
            if (input == 'n')
                room = 2;
            break;
        }
    }

}