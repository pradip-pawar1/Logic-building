#ifndef PARTY_H
#define PARTY_H

#include "warrior.h"
#include "mage.h"
#include <string>

class Party {
private:
    Warrior warrior;
    Mage mage;

public:
    Party(Warrior w, Mage m);

    void displayPartyStatus() const;
    void takeDamage(double damage);
    void castPartySpell(std::string spellName, double manaCost);
};

#endif