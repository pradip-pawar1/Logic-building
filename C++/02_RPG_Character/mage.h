#ifndef MAGE_H
#define MAGE_H

#include "character.h"
#include <string>

class Mage : public Character {
private:
    double mana;

public:
    Mage(std::string name, int level, double health, double mana);

    void castSpell(std::string spellName, double manaCost);
    void displayInfo() const;
};

#endif