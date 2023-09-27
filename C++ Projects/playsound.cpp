#include<Windows.h>

int main(){

    PlaySound(TEXT("song.mp3"), NULL, SND_FILENAME);
    
    return 0;
}