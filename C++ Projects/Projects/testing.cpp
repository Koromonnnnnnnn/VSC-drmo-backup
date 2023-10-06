#include <iostream>
#include <string>

using namespace std;

const int MAX_INVENTORY_SIZE = 10;

int main()
{
    string inventory[MAX_INVENTORY_SIZE]; // Create an array to store weapons
    int itemCount = 0;                    // Current number of items in inventory

    while (true)
    {
        cout << "Inventory Menu:" << endl;
        cout << "1. Add Weapon" << endl;
        cout << "2. Remove Weapon" << endl;
        cout << "3. List Weapons" << endl;
        cout << "4. Quit" << endl;

        int choice;
        cin >> choice;

        switch (choice)
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

    return 0;
}
