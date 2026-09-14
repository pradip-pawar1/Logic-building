# 🛡️ C++ RPG Party System

Welcome! This is a mini C++ project that simulates a classic RPG battle system. It's designed to demonstrate core Object-Oriented Programming (OOP) concepts like inheritance, encapsulation, and method overriding, all neatly organized into a professional multi-file architecture.

Instead of cramming everything into one massive file, the code is split into clean, manageable modules—just like a real-world software project.

## 📂 Project Structure

Every class has a **Header file (`.h`)** for its blueprint and a **Source file (`.cpp`)** for its actual logic:

* **`character.h` & `character.cpp`**
The base class. It handles universal stats like Name, Level, and Health.
* **`warrior.h` & `warrior.cpp`**
A tough fighter derived from `Character`. Features a custom armor system that absorbs incoming damage.
* **`mage.h` & `mage.cpp`**
A spellcaster derived from `Character`. Uses a mana pool to cast magical spells.
* **`party.h` & `party.cpp`**
The manager. It groups our heroes together, displays their collective status, and handles Area of Effect (AoE) damage.
* **`main.cpp`**
The entry point of the game where we create our characters, form the party, and run the simulation!

## 🛠️ How to Compile

Because the project spans multiple files, you need to tell the compiler to grab all the `.cpp` source files and bundle them together.

Open your terminal, navigate to the folder containing these files, and run this single command:

```bash
g++ main.cpp character.cpp warrior.cpp mage.cpp party.cpp -o game

```

*(Note: You don't compile `.h` files directly; the `.cpp` files will pull them in automatically!)*

## 🚀 How to Run

Once compiled, you will see a new executable file in your folder. Run it using the command for your operating system:

**For Mac and Linux:**

```bash
./game

```

**For Windows (PowerShell or Command Prompt):**

```bash
.\game.exe

```

Have fun exploring the code, and feel free to add new heroes (like a `Rogue` or `Cleric`) to test your skills!

---