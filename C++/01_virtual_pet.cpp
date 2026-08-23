#include <iostream>
using namespace std;


class Pet {
    private:
        string name;
        string type;
        int hunger;
        int energy;
        int happiness;

    public:
        // default constructor 
        Pet();

        // Parametrised constructor 
        Pet(string name, string type) {
            this->name = name;
            this->type = type;

            hunger = 50;
            energy = 50;
            happiness = 50;
        }

        void feed();
        void play();
        void sleep();

        void petInfo() {
            cout << "Your pet name is \"" << name 
            <<"\" from " << type << " type" << endl;
        }

        void displayStats() {
            petInfo();

            cout << "----------Stats Are----------\n" <<endl;

            cout << "Hunger level is : " << hunger << endl;
            cout << "Energy level is : " << energy << endl;
            cout << "Happiness level is : " << happiness << endl;
        }

        

};


int main() {
    Pet dragon("Sparky", "Dragon");
    dragon.displayStats();
    
    return 0;
}