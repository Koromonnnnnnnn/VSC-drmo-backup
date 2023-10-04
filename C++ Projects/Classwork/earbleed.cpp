#include<iostream>
#include<Windows.h> // new library

using namespace std;

int main(){
    int num = 5;

    //call the window title function
    SetConsoleTitleA("My Awesome Game!");

    while (num > 0) {

        //call the console color function
        system("COLOR 2F");

        //call the beep function
        Beep(500, 800);

        //a new color!
        system("COLOR B4");

        //call the messagebox function
        MessageBox(nullptr, TEXT("Python Sucks!!"), TEXT("C++ Rules."), MB_OK);

        cout << "yay functions!" << endl;
        system("pause");
        num--; //decrease loop counter (so its not infinite)




    } //end of while loop

} //end of main