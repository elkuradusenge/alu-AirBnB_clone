# AirBnB Clone - The Console

**Description of the Project**

This project is a basic clone of the AirBNB website. The first level creates a backend interface or console for managing program data (similar to shell). Console commands enable users to create, update, and destroy objects, as well as manage file storage.

**Description of the command interpreter**

The command interpreter is the same as the shell, but limited to a specific use-case of handling our project's objects.

1. Create a new object (e.g., a new user or a new place).
2. Get an object from a file, database, etc.
3. Perform operations on objects, such as counting and computing statistics.
4. Update the attributes of an object.
5. Destroy an object.

**Tasks Involved:**

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine
