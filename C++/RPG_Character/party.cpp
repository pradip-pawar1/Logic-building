#include "party.h"
#include <iostream>
using namespace std;

Party::Party(Warrior w, Mage m) : warrior(w), mage(m) {}

void Party::displayPartyStatus() const {
    cout << "\n=== PARTY STATUS ===" << endl;
    warrior.displayInfo();
    mage.displayInfo();
    cout << "====================" << endl;
}

void Party::takeDamage(double damage) {
    cout << "\n--- Party takes " << damage << " AoE damage! ---" << endl;
    warrior.takeDamage(damage);
    mage.takeDamage(damage);
}

void Party::castPartySpell(string spellName, double manaCost) {
    mage.castSpell(spellName, manaCost);
}