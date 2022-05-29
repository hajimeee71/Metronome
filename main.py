# Metronome - Johnathon Kwisses (Kwistech)
# for Mac

from tkinter import *
import os

class Metronome:
    """Create Metronome app with class instance."""

    def __init__(self, root):
        """Initiate default values for class and call interface().

        Args:
            root (tkinter.Tk): Main class instance for tkinter.
        """
        self.root = root

        self.start = False
        self.bpm = 0
        self.time = 0

        self.interface()

    def interface(self):
        """Set interface for Metronome app."""
        frame = Frame()
        frame.pack()

        label_bpm = Label(frame, text="BPM:")
        label_bpm.grid(row=0, column=0)

        entry = Entry(frame, width=8, justify="center")
        entry.insert(0, "60")
        entry.grid(row=0, column=1)

 
        button_start = Button(frame, text="Start", width=10, height=2,
                              command=lambda: self.start_counter(entry))
        button_start.grid(row=2, column=0, padx=20, pady=10, sticky="W")

        button_stop = Button(frame, text="Stop", width=10, height=2,
                             command=lambda: self.stop_counter())
        button_stop.grid(row=2, column=1, padx=20, pady=10, sticky="E")

    def start_counter(self, entry):
        """Start counter if self.start is False (prevents multiple starts).

        Args:
            entry (tkinter.Entry): tkinter Entry widget for app.

        Raises:
            ValueError: if bpm field (self.bpm) on tkinter app is left blank.
        """
        if not self.start:
            try:
                self.bpm = int(entry.get())
            except ValueError:
                self.bpm = 60
            else:
                if self.bpm > 100:  # Limits BPM
                    self.bpm = 100

            self.start = True
            self.counter()

    def stop_counter(self):
        """Stop counter by setting self.start to False."""
        self.start = False

    def counter(self):
        """Control counter display and audio with calculated time delay."""
        if self.start:
            self.time = int((60 / (self.bpm) - 0.1) * 1000)
            os.system('osascript -e "beep"')
            
            # Calls this method after a certain amount of time (self.time).
            self.root.after(self.time, lambda: self.counter())

def main():
    """Call Metronome class instance with tkinter root class settings."""
    root = Tk()
    root.title("Metronome")

    Metronome(root)

    root.mainloop()

if __name__ == "__main__":
    main()
