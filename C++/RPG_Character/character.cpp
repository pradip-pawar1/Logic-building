#include "character.h"
using namespace std;

Character::Character(string name, int level, double health) {
    this->name = name;

    if (level > 0) {
        this->level = level;
    } else {
        cout << "Invalid level, default level : 1" << endl;
        this->level = 1;
    }

    if (health > 0) {
        this->health = health;
    } else {
        cout << "Invalid health, default health : 10.0" << endl;
        this->health = 10.0;
    }
}

double Character::getHealth() const { return health; }
int Character::getLevel() const { return level; }
string Character::getName() const { return name; }

void Character::setHealth(double health) {
    if (health < 0) {
        this->health = 0.0;
    } else {
        this->health = health;
    }
}

void Character::takeDamage(double damage) {
    if (damage > 0) {
        health -= damage;
        if (health < 0) health = 0.0;
        cout << name << " took " << damage << " damage. Current health: " << health << " hp." << endl;
    }
}