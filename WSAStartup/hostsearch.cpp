#include <windows.h>
#include <winsock.h>
#include <iostream>
#include <stdexcept>
using namespace std;

class use_WSA {
    WSADATA d;
    WORD ver;
public:
    use_WSA() : ver(MAKEWORD(1, 1)) {
        if ((WSAStartup(ver, &d) != 0) || (ver != d.wVersion))
            throw runtime_error("Error starting Winsock");
    }
    ~use_WSA() { WSACleanup(); }
};

int main(int argc, char** argv) {
    if (argc < 2) {
        cerr << "Usage: resolve <hostname>\n";
        return EXIT_FAILURE;
    }

    try {
        use_WSA wsa;

        hostent* h = gethostbyname(argv[1]);
        if (!h) {
            cerr << "Failed to resolve hostname.\n";
            return EXIT_FAILURE;
        }

        unsigned char* addr = reinterpret_cast<unsigned char*>(h->h_addr_list[0]);
        cout << static_cast<int>(addr[0]) << "."
                  << static_cast<int>(addr[1]) << "."
                  << static_cast<int>(addr[2]) << "."
                  << static_cast<int>(addr[3]) << "\n";
    }
    catch (const exception& exc) {
        cerr << exc.what() << "\n";
        return EXIT_FAILURE;
    }

    return 0;
}
