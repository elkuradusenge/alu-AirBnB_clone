# AirBnB Clone - The Console

## Description
This project implements a command-line interpreter for managing AirBnB objects. It's the first step toward building a full web application, establishing the foundation for object management, serialization, and storage.

## Command Interpreter
### How to Start
Run the console in interactive mode:
```bash
./console.py
```

### How to Use
- Type `help` to see available commands
- Use `create <ClassName>` to create new instances
- Use `show <ClassName> <id>` to display instances
- Use `all` or `all <ClassName>` to list instances
- Use `update <ClassName> <id> <attribute> <value>` to modify instances
- Use `destroy <ClassName> <id>` to delete instances

### Examples
```
(hbnb) create User
(hbnb) show User 1234-5678
(hbnb) all
(hbnb) update User 1234-5678 email "test@test.com"
(hbnb) destroy User 1234-5678
```
