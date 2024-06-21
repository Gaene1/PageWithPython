# import panel as pn

# pn.extension(sizing_mode="stretch_width")

# slider = pn.widgets.FloatSlider(start=0, end=10, name='Amplitude')

# def callback(new):
    # return f'Amplitude is: {new}'

# pn.Row(slider, pn.bind(callback, slider)).servable(target='simple_app')
from PySide6.QtWidgets import QApplication, QWidget

# Only needed for access to command line arguments
import sys

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = QWidget()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
sys.exit(app.exec())
