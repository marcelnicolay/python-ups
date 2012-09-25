.SILENT:

clean:
	echo "Cleaning up build and *.pyc files..."
	find . -name '*.pyc' -exec rm -rf {} \;

	rm -rf build

test: clean
	nosetests
