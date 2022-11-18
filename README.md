# gslothutils
The general utility functions frequently used in my many projects.

## Example

coming soon...



## Getting started
```bash
git submodule add https://github.com/geeksloth/gslothutils
```

## Update submodules

- Update only this submodule

Use your terminal and ```cd``` to your project's root directory, then type
```bash
cd gslothutils
```
```bash
git pull origin main
```
If you have made some changes and want to ignore all changes in submodules, reset it by
```bash
git reset --hard && git pull origin main
```

- In case you want to update all your submodules
```bash
git submodule foreach git pull origin main
```

