#include <iostream>
using namespace std;

int main(){

    int DarthNihilus = 0; //Atra-Manua
    int DarthVader = 0; //Djem So
    int DarthRevan = 0; //Ataru
    int DarthSidious = 0; //Juyo
    char input;
    int _input;

    //-------------------

    cout << "If you could learn any lightsaber form, what form would you use?" << endl;
    cout << "(J)uyo, (M)Atra-Manua, (A)taru, (D)jem-So" << endl;
    cin >> input;
    if (input == 'J')
        DarthSidious += 1;
    else if (input == 'A')
        DarthRevan += 1;
    else if (input == 'M')
        DarthNihilus += 1;
    else if (input == 'D')
        DarthVader += 1;
    else
        cout << "Sorry that is not an option." << endl;

    //-------------------

    cout << "If you could choose a planet in the SWU to have been born in what planet would you pick?:" << endl;
    cout << "(N)aboo, (T)atooine, (O)uterRim, (M)alachorV" << endl;
    cin >> input;
    if (input == 'N')
        DarthSidious += 1;
    else if (input == 'O')
        DarthRevan += 1;
    else if (input == 'M')
        DarthNihilus += 1;
    else if (input == 'T')
        DarthVader += 1;
    else
        cout << "Sorry that is not an option." << endl;

    //-------------------

    cout << "What is your preffered lightsaber hilt?:" << endl;
    cout << "(K)irak's hilt, (S)elf-constructed, (C)ylindrical hilt, (T)win lightsabers" << endl;
    cin >> input;
    if (input == 'T')
        DarthSidious += 1;
    else if (input == 'C')
        DarthRevan += 1;
    else if (input == 'S')
        DarthNihilus += 1;
    else if (input == 'K')
        DarthVader += 1;
    else
        cout << "Sorry that is not an option." << endl;

    //-------------------

    cout << "How would you most closely describe your personality?:" << endl;
    cout << "(S)toic, (C)autious, (M)anipulative, (F)orceful" << endl;
    cin >> input;
    if (input == 'M')
        DarthSidious += 1;
    else if (input == 'F')
        DarthRevan += 1;
    else if (input == 'C')
        DarthNihilus += 1;
    else if (input == 'S')
        DarthVader += 1;
    else
        cout << "Sorry that is not an option." << endl;

    //-------------------

    cout << "What do you look for in a Sith apprentice?:" << endl;
    cout << "(S)trength, (D)etermination, (C)omplaisance, (H)eadStrong" << endl;
    cin >> input;
    if (input == 'S')
        DarthSidious += 1;
    else if (input == 'H')
        DarthRevan += 1;
    else if (input == 'C')
        DarthNihilus += 1;
    else if (input == 'D')
        DarthVader += 1;
    else
        cout << "Sorry that is not an option." << endl;

    //-------------------

    cout << "What would be the most alluring reason that you would fall to the Dark Side?:" << endl;
    cout << "1: You would never turn, unless you were manipulated to do so." << endl; 
    cout << "2: You would never turn, unless you were tortured till your mild was splintered between death and the dark side." << endl;
    cout << "3: Your home planet has been destroyed, and in order to survive you must turn to the dark side." << endl;
    cout << "4: Your significant other is dying, you are lied to and made to beleive that joining the dark side could teach you how to stop her from dying." << endl;
    cin >> _input;
    if (_input == 1)
        DarthSidious += 1;
    else if (_input == 2)
        DarthRevan += 1;
    else if (_input == 3)
        DarthNihilus += 1;
    else if (_input == 4)
        DarthVader += 1;
    else
        cout << "Sorry that is not an option." << endl;

    //-------------------

    cout << "Which force ability would you pick?:" << endl;
    cout << "(T)elekineis, (V)alour, (D)rain, (L)ightning" << endl;
    cin >> input;
    if (input == 'L')
        DarthSidious += 1;
    else if (input == 'V')
        DarthRevan += 1;
    else if (input == 'D')
        DarthNihilus += 1;
    else if (input == 'T')
        DarthVader += 1;
    else
        cout << "Sorry that is not an option." << endl;

    //-------------------

    cout << "What gives you power?:" << endl;
    cout << "(A)dvanced Strength, (F)orce, (C)onsuming Force Energy, (N)aturally Gifted At All" << endl;
    cin >> input;
    if (input == 'N')
        DarthSidious += 1;
    else if (input == 'F')
        DarthRevan += 1;
    else if (input == 'C')
        DarthNihilus += 1;
    else if (input == 'A')
        DarthVader += 1;
    else
        cout << "Sorry that is not an option." << endl;

    //-------------------

    if (DarthSidious >= DarthVader && DarthSidious >= DarthNihilus && DarthSidious >= DarthRevan) {
        cout << "You are Darth Sidious!" << endl;
    }
    else if (DarthNihilus >= DarthVader && DarthNihilus >= DarthSidious && DarthNihilus >= DarthRevan) {
        cout << "You are Darth Nihilus!" << endl;
    }
    else if (DarthRevan >= DarthVader && DarthRevan >= DarthSidious && DarthRevan >= DarthNihilus){
        cout << "You are Darth Revan!" << endl;  
    }
    else if (DarthVader >= DarthRevan && DarthVader >= DarthSidious && DarthVader >= DarthNihilus){
        cout << "You are Darth Vader!" << endl; 
    }
    else
    cout << "Test resuls were not conclusive" << endl;

    return 0;
}