#include<iostream>
using namespace std;

void monsterGen(); //declaration

int main(){
    char input;
    while (1){ //game loop!
        //your text based game goes here!
        monsterGen();
        cout << "press any key to continue..." << endl;
        cin >> input;

    }
}

void monsterGen(){
    int num = rand() % 100 + 1; //creates a number between 1-100
    if (num < 20) //20% of a witch
        cout << "a witch spawned." << endl;
    else if (num < 50) //30% chance of a skele
        cout << "a skeleton appeared!" << endl;
    else if (num < 60) //10%
        cout << "an alien appears!" << endl;
    else //40%
        cout << "nothing appeared." << endl;
}