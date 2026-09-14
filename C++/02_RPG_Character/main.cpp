#include "party.h"
#include "warrior.h"
#include "mage.h"

int main() {
    Warrior myWarrior("Thorin", 5, 100.0, 15.0);
    Mage myMage("Gandalf", 5, 100.0, 100.0);

    Party myParty(myWarrior, myMage);

    myParty.displayPartyStatus();
    myParty.takeDamage(30.0);
    myParty.castPartySpell("Fly", 15.0);
    myParty.displayPartyStatus();

    return 0;
}