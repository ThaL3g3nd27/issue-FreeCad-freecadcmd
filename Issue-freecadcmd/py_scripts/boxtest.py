import FreeCAD as App
import Part

def create_box():
    # Create a new document
    doc = App.newDocument()

    # Create a box
    length = 1
    width = 1
    height = 1
    box = Part.makeBox(length, width, height)

    # Add the box to the document
    doc.addObject("Part::Feature", "Box").Shape = box

    # Export the box as a STEP file using Part module
    step_file = "/app/py_scripts/box.step"
    Part.export([doc], step_file)

    print(f"Box created and exported as '{step_file}'.")

if __name__ == "__main__":
    create_box()
    print("Script execution completed.")
