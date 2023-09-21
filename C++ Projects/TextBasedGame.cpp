#include<iostream> //library
using namespace std; //makes iostream work better

int main() { //beginning of main

    int room = 1;
    char direction;

    while(1) {
        switch(room) { //beginning of switch
        case 1:
            cout << "you're in room 1, you can go (E)ast" << endl;
            cin >> direction; //check and store user input
            if (direction == 'E') //check if they want to go east
            room = 2; //if input = E then they go to room 2
            break;
        case 2:
            cout << "you're in room 2, you can go (W)est or (S)outh" << endl;
            cin >> direction;
            if (direction == 'W')
                room = 1;
            if (direction == 'S')
                room = 3;
            break;
        case 3:
            cout << "you're in room 3, you can go (N)orth or (S)outh" << endl;
            cin >> direction;
            if (direction == 'N')
                room = 2;
            if (direction == 'S')
                room = 4;
            break;
        case 4:
            cout << "you're in room 4, you can go (E)ast or (N)orth" << endl;
            cin >> direction;
            if (direction == 'N')
                room = 3;
            if (direction == 'E')
                room = 5;
            break;
        case 5:
            cout << "you're in room 5, you can go (W)est" << endl;
            cin >> direction;
            if (direction == 'W')
                room = 4;
            break;
        } //end of switch
      } //while loop
    } //end of main