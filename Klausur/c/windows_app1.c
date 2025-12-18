#include <windows.h>

int APIENTRY WinMain(  HINSTANCE   hInstance,
                        HINSTANCE   hPrevInstance,
                        LPSTR       lpCmdLine,
                        int         nCmdShow)

{
    MessageBoxA(NULL, "\tHello World!", "My first Windows app", MB_OK);
    return 0;
}