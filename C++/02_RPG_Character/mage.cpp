#include "mage.h"
#include <iostream>
using namespace std;

Mage::Mage(string name, int level, double health, double mana)
    : Character(name, level, health) {
    if (mana > 0) {
        this->mana = mana;
    } else {
        cout << "Mana can't be <= 0. Set to default 100.0" << endl;
        this->mana = 100.0;
    }
}

void Mage::castSpell(string spellName, double manaCost) {
    if (mana >= manaCost) {
        mana -= manaCost;
        cout << spellName << " magic worked! Remaining mana: " << mana << endl;
    } else {
        cout << "Not enough mana to cast " << spellName << "!" << endl;
    }
}

void Mage::displayInfo() const {
    cout << "Name : " << getName() << " | "
         << "Health : " << getHealth() << "hp | "
         << "Level : " << getLevel() << " | "
         << "Mana : " << mana << endl;
}