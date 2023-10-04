#include<iostream>
using namespace std;

void monsterGen(); //declaration

int main(){
    char input;
    while (1) { //game loop!
        //your text based game goes here!
        monsterGen();
        cout << "press any key to continue..." << endl;
        cin >> input;

    }
}

void monsterGen() {
    int num = rand() % 100; //creates a number between 1-100
    if (num < 15) //15
        cout << "a witch spawned." << endl;
    else if (num < 20) //5
        cout << "a kraken appeared!" << endl;
    else if (num < 50) //30
        cout << "an alien appears!" << endl;
    else if (num < 75) //25
        cout << "a wilf dog appears!" << endl;
    else 
        cout << "final monster appeared!" << endl;
}