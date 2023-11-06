#include <iostream>  //library
using namespace std; // makes iostream work better

string inventory[10];
bool gameGoing = true;

int main()
{ // beginning of main
    for (int i = 0; i < 10; i++)
        inventory[i] = " ";
    
    int room = 1;
    char direction;

    while (gameGoing)
    {
        cout << "your inventory:" << endl;
        for (int i = 0; i < 10; i++)
            cout << inventory[i] << " ";
        cout << endl;

        switch (room)
        { // beginning of switch
        case 1:
            cout << "you're in room 1, you can go (E)ast" << endl;
            if (inventory[0] != "Key")
            cout << "You see a (K)ey on the floor." << endl;
            cin >> direction; // check and store user input
            if (direction == 'E')
                room = 2;
            if (direction == 'K')
                inventory[0] = "Key";
            // check if they want to go east //if input = E then they go to room 2
            break;
        case 2:
            cout << "you're in room 2, you can go (W)est or (S)outh" << endl;
            cin >> direction;
            if (direction == 'W')
                room = 1;
            if (direction == 'S')
                if (inventory[0] == "Key"){
                    cout << "you unlock the door with the key!" << endl;
                    inventory[0] = " ";
                    room = 3;
                }
            else
                cout << "the door is locked" << endl;
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
        } // end of switch
    }     // while loop
} // end of main