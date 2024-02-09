#include <iostream>
#include <string>
using namespace std;

void returnSearch();

string DiverseBeats[] = {"Tusa", "Rockstar", "Tangerine"};

int main()
{
    returnSearch();                      // search for binding lights
    cout << DiverseBeats[2] << endl;     // print out 3rd slot of the array
    DiverseBeats[0] = "Save Your Tears"; // replace tusa with save your tears
    for (int j = 0; j <= 3; j++)         // print entire array
        cout << DiverseBeats[j] << " ";

    return 0;
}

void returnSearch()
{
    string DiverseBeats[] = {"Tusa", "Rockstar", "Tangerine"}, toFind = "Binding Lights", notFound = "notFound";
    for (int i = 0; i <= sizeof(DiverseBeats); i++)
    {
        if (DiverseBeats[i] == toFind)
        {
            cout << "Song is found in slot number " << i << endl;
        }
    }
    cout << notFound << endl;
}