#include <iostream>
#include <Windows.h>
#include <string>
#include <ctime>
using namespace std;

const int inventorySize = 10;

int main()
{

    string inventory[inventorySize]; // Create a list to store weapons
    int itemCount = 0;
    char inventoryChoice;

    switch (inventoryChoice)
    {
    case 'Y':
        if (itemCount < inventorySize)
        {
            cout << "Enter the name of the weapon to add: ";
            cin >> inventory[itemCount];
            itemCount++;
            cout << "Weapon added to your inventory." << endl;
        }
        else
        {
            cout << "Alright then" << endl;
        }
        break;
    }
  }

