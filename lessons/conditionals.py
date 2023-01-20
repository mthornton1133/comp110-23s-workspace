"""Checks lioght, if green, says go."""

light: str = input("what color is the light? ").lower()

if (light == "green"):
    print("Go!")
    print("Drive safe!")
else:
    if (light != "red"):
        if (light == "yellow"):
            print("slow down")
        else:
            print("Go report this")
    else:
        print("Stop!")
print("Don't look at your phone!")