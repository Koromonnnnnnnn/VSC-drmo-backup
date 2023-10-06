#include <iostream>
#include <Windows.h>
#include <string>
#include <conio.h>
using namespace std;

void monsterGen();
void lootGen();

void deathSong();
void victorySong();
void welcomeSong();

struct Item
{
    string name;
    int damage;
    int armor;
};

struct Monster
{
    string name;
    int health;
    int damage;
};

int main()
{
    char destination;
    int roomIn;
    char initialQuestion;
    bool gameGoing = true;
    int playerHealth = 100;
    int playerDamage = 25;

    cout << "Welcome to \"The Forgotten Prophecy\"" << endl;
    cout << "You wake up somewhere unknown. Bright green grass and orange trees surround you." << endl;
    cout << "Your memory is foggy and you can't quite remember anything about yourself, or how you got to this mysterious place." << endl;
    cout << "The only path forward is a steep set of ancient stone stairs." << endl;
    cout << "Press '0' to play..." << endl;
    cin >> roomIn;

    while (gameGoing)
    {
        switch (roomIn)
        {
        case 0:
            cout << "You are in 'Room One', do you wish to go (E)ast towards 'Room Two'?" << endl;
            cin >> destination;
            if (destination == 'e' || destination == 'E')
                roomIn = 1; // 2
            break;
        case 1:
            cout << "You are in 'Room Two', do you wish to go (S)outh towards 'Room Three'? Or (W)est back to 'Room One'" << endl;
            cin >> destination;
            if (destination == 's' || destination == 'S')
                roomIn = 2; // 3
            if (destination == 'w' || destination == 'W')
                roomIn = 0; // 1
            break;
        case 2:
            cout << "You are in 'Room Three', you can go (S)outh to 'Room Four' (Cave), or (N)orth back to 'Room Two'" << endl;
            cin >> destination;
            if (destination == 's' || destination == 'S')
                roomIn = 3; // 4
            if (destination == 'n' || destination == 'N')
                roomIn = 1; // 2
            break;
        case 3:
            cout << "You are in 'Room Four', you can go (E)ast to 'Room Five', or (N)orth back to 'Room Three'" << endl;
            cin >> destination;
            if (destination == 'e' || destination == 'E')
                roomIn = 4; // 5
            if (destination == 'n' || destination == 'N')
                roomIn = 2; // 3
            break;
        case 4:
            cout << "You are in 'Room Five', you can go (N)orth to 'Room Six', or (W)est back to 'Room Four'" << endl;
            cin >> destination;
            if (destination == 'n' || destination == 'N')
                roomIn = 5; // 6
            if (destination == 'w' || destination == 'W')
                roomIn = 3; // 3
            break;
        case 5:
            cout << "You are in 'Room Six', you can go (E)ast to 'Room Seven', or (S)outh back to 'Room Five'" << endl;
            cin >> destination;
            if (destination == 'e' || destination == 'E')
                roomIn = 6; // 7
            if (destination == 's' || destination == 'S')
                roomIn = 4; // 5
            break;
        }
    }
}

void monsterGen()
{
    int num = rand() % 100; // creates a number between 1-100
    if (num < 15)           // 15
        cout << " witch " << endl;
    else if (num < 20) // 5
        cout << " kraken " << endl;
    else if (num < 50) // 30
        cout << " alien " << endl;
    else if (num < 75) // 25
        cout << " wild dog " << endl;
    else
        cout << " mysterious entity " << endl;
}

void lootGen()
{
    int num = rand() % 100; // creates a number between 1-100
    if (num < 15)           // 15
        cout << "You found a gun!" << endl;
    else if (num < 20) // 5
        cout << "You found a sword!" << endl;
    else if (num < 50) // 30
        cout << "You found a legendary sword!" << endl;
    else if (num < 75) // 25
        cout << "You found a mythical bow!" << endl;
    else
        cout << "Nothing has spawned." << endl;
}

void deathSong()
{

    int notes[] = {392, 349, 330, 293, 261};
    int durations[] = {200, 200, 200, 400, 400};

    for (int i = 0; i < 5; i++)
    {
        Beep(notes[i], durations[i]);
        Sleep(100);
    }
}

void victorySong()
{

    int notes[] = {523, 587, 659, 698, 783, 880, 987, 1046};
    int durations[] = {500, 500, 500, 500, 500, 500, 500, 1000};

    for (int i = 0; i < 8; i++)
    {
        Beep(notes[i], durations[i]);
        Sleep(100);
    }
}