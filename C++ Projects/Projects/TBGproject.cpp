#include <iostream>
#include <Windows.h>
#include <string>
#include <conio.h>
#include <ctime>
using namespace std;

// gens
string monsterGen();
string lootGen();

// songs
void deathSong();
void victorySong();
void welcomeSong();
void attackSong();
void damageSong();

// other functions

// variables
const int MAX_INVENTORY_SIZE = 10;

int main()
{
    string inventory[MAX_INVENTORY_SIZE]; // Create an array to store weapons
    int itemCount = 0;
    char destination;
    int roomIn;
    char initialQuestion;
    string monster;
    string chestLoot;
    bool gameGoing = true;
    int playerHealth = 100;
    int playerDamage = 25;
    int monsterHealth = 50;
    int monsterDamage = 10;

    cout << "Welcome to \"The Forgotten Prophecy\"" << endl;
    cout << "You wake up somewhere unknown. Bright green grass and orange trees surround you." << endl;
    cout << "Your memory is foggy and you can't quite remember anything about yourself, or how you got to this mysterious place." << endl;
    cout << "The only path forward is a steep set of ancient stone stairs." << endl;
    cout << "Press '0' to play..." << endl;
    cin >> roomIn;

    while (gameGoing)
    {
        char choice1;
        int choice2;

        switch (roomIn)
        {
        case 0:
            monster = monsterGen();
            cout << "You are currently in Room One" << endl;
            monsterGen();
            cout << "Press any key to attack" << endl;
            getch();
            while (monsterHealth > 0)
            {
                monsterHealth -= playerDamage;
                cout << "You attack the " << monster << " for " << playerDamage << " damage" << endl;
                if (playerHealth > 0)
                {
                    playerHealth -= monsterDamage;
                    cout << monster << " attacks you for " << monsterDamage << " damage" << endl;
                }
                else
                {
                    deathSong();
                    cout << "You are dead..." << endl;
                }

                cout << "Press any key to attack again" << endl;
                getch();
                cout << "You have slayed " << monster << endl;
                cout << "You look around the room and spot a chest!" << endl;
                cout << "Press any key to open the chest..." << endl;
                chestLoot = lootGen();
                getch();
                cout << "You have found " << chestLoot << endl;
                cout << "Press any key to continue" << endl;
                getch();
                cout << "Would you like to add " << chestLoot << " to your inventory? (Y/N)" << endl;
                cin >> choice1;
                if (choice1 == 'y' || choice1 == 'Y')
                    switch (choice2)
                    {
                    case 1:
                        if (itemCount < MAX_INVENTORY_SIZE)
                        {
                            cout << "Enter the name of the weapon to add: ";
                            cin >> inventory[itemCount];
                            itemCount++;
                            cout << "Weapon added to your inventory." << endl;
                        }
                        else
                        {
                            cout << "Your inventory is full." << endl;
                        }
                        break;
                    case 2:
                        if (itemCount > 0)
                        {
                            cout << "Enter the name of the weapon to remove: ";
                            string weaponToRemove;
                            cin >> weaponToRemove;

                            // Search for the weapon and remove it if found
                            for (int i = 0; i < itemCount; i++)
                            {
                                if (inventory[i] == weaponToRemove)
                                {
                                    // Shift remaining items to fill the gap
                                    for (int j = i; j < itemCount - 1; j++)
                                    {
                                        inventory[j] = inventory[j + 1];
                                    }
                                    itemCount--;
                                    cout << "Weapon removed from your inventory." << endl;
                                    break;
                                }
                            }
                        }
                        else
                        {
                            cout << "Your inventory is empty." << endl;
                        }
                        break;
                    case 3:
                        cout << "Your Weapons:" << endl;
                        for (int i = 0; i < itemCount; i++)
                        {
                            cout << inventory[i] << endl;
                        }
                        break;
                    case 4:
                        cout << "Exiting the inventory system." << endl;
                        return 0;
                    default:
                        cout << "Invalid choice. Please try again." << endl;
                    }
            }
        }
        cout << "You are in 'Room One', do you wish to go (E)ast towards 'Room Two'?" << endl;
        cin >> destination;
        if (destination == 'e' || destination == 'E')
            roomIn = 1; // 2
    }

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

string monsterGen()
{
    string monsterItems[] = {"Witch", "Kraken", "Alien", "Dog", "Mysterious Entity"};

    int numItems = sizeof(monsterItems) / sizeof(monsterItems[0]);

    srand(time(0));

    int randomIndex = rand() % numItems;

    return monsterItems[randomIndex];
}

string lootGen()
{
    string chestItems[] = {"Sword", "Spear", "Trident", "Bow", "Godly Bolt"};

    int numItems = sizeof(chestItems) / sizeof(chestItems[0]);

    srand(time(0));

    int randomIndex = rand() % numItems;

    return chestItems[randomIndex];
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

void damageSong()
{
}

void attackSong()
{
}