# Virtual Pet Simulator (`Tamagotchi`)

You will build a console game where an object represents your pet. 
You interact with it through a menu loop, feeding it, playing with it, or resting it.

## Features to Implement
1. **Action Methods**:
    - `feed()`: Decreases hunger, slightly increases energy.

    - `play()`: Increases happiness, decreases energy, increases hunger.

    - `sleep()`: Restores energy to 100, slightly increases hunger.

2. **Stat Clamping (Validation)**:

    - Ensure stats never drop below 0 or exceed 100.

3. **Dynamic Status Output**:

    Print different ASCII faces or status messages depending on health

    - High happiness: "(^‿^)"
    - Low energy/high hunger: "(>_<)"

## Example Interaction Flow

```text
Enter Pet Name: Sparky
Choose Type (Dragon / Cat / Robot): Dragon

=== Sparky the Dragon's Dashboard ===
Mood: (^‿^) [Happy]
Hunger: 50/100 | Energy: 50/100 | Happiness: 50/100

1. Feed Sparky
2. Play with Sparky
3. Put Sparky to Sleep
4. Do Nothing
Select Choice: 2

You played fetch with Sparky!
Happiness increased (+20), but Sparky got tired (-15 Energy) and hungry (+10 Hunger).
```