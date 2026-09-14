#include "warrior.h"
#include <iostream>
using namespace std;

Warrior::Warrior(string name, int level, double health, double armor) 
    : Character(name, level, health) {
    if (armor > 0) {
        this->armor = armor;
    } else {
        cout << "Armor health cannot be <= 0. Default armor set to 10.0hp" << endl;
        this->armor = 10.0;
    }
}

void Warrior::takeDamage(double damage) {
    double effectiveDamage = damage - armor;
    if (effectiveDamage < 0) effectiveDamage = 0;
    
    double newHealth = getHealth() - effectiveDamage;
    setHealth(newHealth);
    cout << getName() << " absorbed damage with armor! Effective damage: " << effectiveDamage 
         << ". Current health: " << getHealth() << " hp." << endl;
}

void Warrior::displayInfo() const {
    cout << "Name : " << getName() << " | "
         << "Health : " << getHealth() << "hp | "
         << "Level : " << getLevel() << " | "
         << "Armor : " << armor << "hp" << endl; 
}