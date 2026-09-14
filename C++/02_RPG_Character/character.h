#ifndef CHARACTER_H
#define CHARACTER_H

#include <iostream>
#include <string>

class Character {
private:
    std::string name;
    int level;
    double health;

public:
    Character(std::string name, int level, double health);
    virtual ~Character() {}

    // Getters
    double getHealth() const;
    int getLevel() const;
    std::string getName() const;

    // Setters
    void setHealth(double health);

    // Virtual method to allow overriding in derived classes
    virtual void takeDamage(double damage);
};

#endif