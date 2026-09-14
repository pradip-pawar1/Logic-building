#ifndef WARRIOR_H
#define WARRIOR_H

#include "character.h"

class Warrior : public Character {
private:
    double armor;

public:
    Warrior(std::string name, int level, double health, double armor);

    void takeDamage(double damage) override;
    void displayInfo() const;
};

#endif