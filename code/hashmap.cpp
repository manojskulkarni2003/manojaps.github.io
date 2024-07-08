#include <iostream>
#include <unordered_map>

int main()
{
    // Declaration
    std::unordered_map<int, int> myHashTable; // declares an empty map

    // Insertion
    int key = 1;
    int value = 100;
    myHashTable[key] = value;

    // Deletion
    myHashTable.erase(key);

    // Look up
    if (myHashTable.find(key) != myHashTable.end())
    {
        std::cout << "Key found with value: " << myHashTable[key] << std::endl;
    }
    else
    {
        std::cout << "Key not found" << std::endl;
    }

    // Check presence of a key
    if (myHashTable.count(key))
    {
        std::cout << "Key is present in the hash table" << std::endl;
    }
    else
    {
        std::cout << "Key is not present in the hash table" << std::endl;
    }

    // Number of key-value pairs in the hash table
    std::cout << "Number of key-value pairs: " << myHashTable.size() << std::endl;

    return 0;
}
