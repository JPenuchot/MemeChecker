# MemeChecker

Uses ImageHash to compare images across two sets.

### Usage

```bash
python3 memechecker.py [IMAGE_BASE_1_REGEX] [IMAGE_BASE_2_REGEX] [(Optional) THRESHOLD]
```

Example :

```bash
python3 memechecker.py "/home/user/Pictures/*.jpg" "/home/user/Downloads/*.jpg" 10
```

### Dependencies

Install ImageHash using pip3 and you're done.