# life-game
assign1_GOL

# update pip ('python' may point to 2.7, make sure to use Python 3.6 or higher)
python3 -m pip install pip --upgrade

# install venv
python3 -m pip install venv

# Create a Python virtual environment
python3 -m venv gameoflife_venv

# Activate gameoflive_venv
source gameoflife_venv/bin/activate

# Install dependencies from requirements.txt (inside the venv, 'python' should point to python3)
python -m pip install -r requirements.txt

# run Conway's Game of Life
python run.py
