#include <iostream>
using namespace std;

int main(){

    int age;

    cout << "Enter your age:" << endl;
    cin >> age;

    if (age < 13)
        cout << "You're too young to play this game, go away!" << endl;

    else if (age < 18)
        cout << "please get parent permission to play this game." << endl;

    else
        cout << "Welcome to the game!" << endl;

    return 0;
}