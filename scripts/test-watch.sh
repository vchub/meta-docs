# !/usr/local/bin/zsh

# https://stackoverflow.com/questions/34713278/fswatch-to-watch-only-a-certain-file-extension

# fswatch -e ".*" -i ".*/[^.]*\\.py$" -0 . | \
# 	xargs -0 -n 1 -I {} pytest -s ./tests

# pytest tests/draw/test_dao.py

# test with firebase emulator
# firebase emulators:exec "./scripts/test-watch.sh"

# run with firebase emulator
# firebase emulators:exec "python src/main.py"

fswatch -e ".*" -i ".*/[^.]*\\.py$" -0 . | \
	xargs -0 -n 1 -I {} python -m pytest -s .
