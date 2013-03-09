Unit 5.3: File formats
======================

Introduction
------------

This exercise imagines a library for describing systems of chemical reactions. A python module with a model for a system of reactions is provided. You should imagine that the library also contains code for doing something useful with the system: perhaps simulating the mass-action kinetics, or a stochastic simulation using the Gillespie algorithm.

The model assumes a reaction system has an enumerable, finite number of species. Each reaction has a set of products, and a set of reactants, with forward and reverse rate constants.

An example system might be:

Species: A,B,C,D,E
                                                                  
A+B <-> C with forward rate constant 0.1 mol^-1 s^-1 and reverse rate constant 0.3 s^-1
C   <-> D+E with forward rate constant 0.3 s^-1 and reverse rate constant 0.2 mol^-1 s^-1

Your objective will be to provide *parsers* and *serialisers* for this model for a number of different file formats. In doing so, you will explore issues around choice and capabilities of different ways of serialising data.
 
The skeleton code in the provided reaction module has been set up to convert between file formats:
	python -m reactions --in system1.csv --out system1.xml 
	
The formats to be used will be guessed from the file extensions. Empty methods have been created to read and write each of the file types we will be working with: you will be asked to fill in each of these as we progress. 

Prerequisites
-------------

You are assumed to know:
1. Basic python
2. Basic unit testing in python with pyunit.
3. Attendance at introductory talk (see file in this repository)
4. Basic GIT.

You should fork this repo on GitHub into your own account, check out the *trainee_answers* branch, and make your changes to complete the exercises. You can look at suggested answers by the author in the *author_answers* branch.

1: CSV
------
###1.0: Read about CSV 

Wiki pages: http://en.wikipedia.org/wiki/Comma-separated_values
http://en.wikipedia.org/wiki/Delimiter-separated_values
http://www.creativyst.com/Doc/Articles/CSV/CSV01.htm

###1.1: Write a fixture

You should invent a way that seems plausible to you of storing a reaction system in a comma-separated variable file. Create a test system using your format by hand, describing the example system above, and save it in reactions/test/fixtures/system1.csv.

###1.2: Write a parser

Using python CSV, write a parser that reads .csv files. You should put your code in reactions/formats/format_csv.py in the appropriate empty functions.
A test has been written in reactions/test/test_csv.py 
You should be able to run this test with:
	> py.test
Modify your code until this test passes. Feel free to modify the test if it is not appropriate to your test case. You may want to add more tests.

###1.3: Write a serialiser

Using python CSV, write code that writes .csv files. Appropriate tests have been written, which you can invoke with
	> py.test

	You will probably find that you don't expect the output file to be exactly the same as your input example.
	You should add your output example to fixtures/system1out.csv
	Your code should be placed in reactions/csv.py in the appropriate empty functions.
###1.4: Check support for large files
The provided skeleton python program has built in functionality to create a random large reaction system. Run this with:
	> python -m reactions --bigfile 100 --out reactions/test/fixtures/bigsystem.csv
and bigsystem.csv should appear in your fixtures folder, and contain a big CSV system. When this works, the full set of tests invoked with
	> py.test 
should pass.

###1.5: Extra credit: add support for comments
Add support for comments at the end of a line, or on a separate line, with your choice of comment character.
You should add an extra test.

2: XML
------

###2.1: Fixture and parser

Invent an XML file format for reaction systems, save it in the fixtures folder as system1.xml, and write a parser in reactions/formats/format_xml.py. Use the python module elementtree to implement your parser. Tests have been written for you in test_xml.py.

###2.2: Serialiser using Mako

Write mako code to create your XML file format. The provided tests will check it comes out exactly the same as your fixture. Code to invoke Mako has already been put in reactions/formats/format_xml.py, and the mako template in reactions/xml.mko

###2.3: Extra credit: Using lxml

Write mako code to create your XML file format using lxml, by building up your DOM. The scaffold code has been written to enable this option using --nomako
       
###2.4: Extra credit: To your neighbour's format using XSLT

Read about XSLT at http://www.w3schools.com/xsl/xsl_intro.asp 
Obtain a copy of system1.xml from your neighbour (they should be able to email it to you).
Write an XSL transform to produce your neighbour's XML format from your own. Invoke your transform using xsltproc.
If you're working alone on this project, then you should look at the authors' answers (in the *author_answers* branch on this repo) and write a transform to produce that output.

###2.5: Extra credit: To Latex using Mako

Write a mako template to produce a pretty rendering in Latex of your reaction system.
 
###2.6: Extra credit: XML Schema

Write an XML Schema for your file format, put it in reactions/schemas/reaction.xsd 
Check your XML fixture validates against the schema using xmllint, e.g.:
	> xmllint --noout --schema reactions/schemas/reaction.xsd 
Add code to your program to validate XML files against the schema before loading them, using ***.


3: YAML and JSON 
-------

###3.1 YAML
Write a fixture, serialiser, and parser for YAML using Pyyaml, placing the work into the appropriate files.
Check the tests pass. 
###3.2 Extra credit: JSON
Write a fixture, serialiser and parser for JSON using Y.
Add tests and check they pass.

5: XDR
------

###5.1: XDR Serialiser and parser
Decide how to represent a reaction model as an XDR file format. Implement a serialiser and a parser for this format using the python XDR library.
###5.2: File size and timings comparisons
Run 
	> time python -m reactions --bigfile 10000 --out verybigsystem.yml
to produce a very large YAML model.
Run 
	> time python -m reactions --bigfile 10000 --out verybigsystem.xdr
to produce a very large XDR model.

Compare the timings.
Run
	> time python -m reactions --in verybigsystem.yml --out out.null
to read the very large YAML model.
Run 
	> time python -m reactions --in verybigsystem.xdr --out out.null
to read the very large YAML model.

Compare the timings.

Compare the file sizes.
Compress the files using zip, gzip, bzip, or your favourite compression tool.
Compare the file sizes.
Comment on what you find in a file notes.txt.

6: HDF5
###5.1: HDF5 Serialiser and parser
Decide how to represent a reaction model as an HDF5 file format. Implement a serialiser and a parser for this format using the python HDF5 library.
###5.2: File size and timings comparisons
Consider the relative performance of HDF5 for large files, as you did with XDR.

7: RDF
------

###7.0: Read about RDF
You should read through the W3Schools RDF tutorial at http://www.w3schools.com/rdf/rdf_intro.asp and the python RDF library docs at https://rdflib.readthedocs.org/en/latest/gettingstarted.html   

You should use easy_install or pip to install rdflib and rdfextras
 
###7.1: Create an RDF file for reactions
 
A starting ontology has been begun in reactions/schemas/ontology, you can use these terms in your file.
You should create your example file in system1.rdf: we've set up a scaffold for you.
 
###7.2: Write a parser and a serialiser
There's a lot of boiler plate to get right using Python's rdflib, so the work of importing the ontologies, creating the triple store, and reading and writing the files has been done for you.

###7.3: (Extra credit) Modify the ontology

The existing ontology is just a skeleton, mentioning that the classes exist.
You can use OWL http://www.w3.org/TR/2004/REC-owl-guide-20040210/ to specify the relationships of the entities.
This would make it easier for someone else's program to automatically understand your format

You could also use owl:sameAs to declare that your concepts are the same as those in another format. That's how you
make your formats understandable to the world. 
You could link your entities to terms from the systems biology ontology. An OWL file for SBO is at http://www.ebi.ac.uk/sbo/exports/Main/SBO_OWL.owl
The root namespace for this ontology is at http://biomodels.net/SBO/, so in XML/RDF, the SBO entity for a "rate constant" can be referred to unambiguously as http://biomodels.net/SBO/#SBO:0000009
You might want to consider using the following elements from the systems biology ontology:

* 0000009
* 0000010
* 0000011
* 0000012
* 0000176
* 0000205

But you may find better choices, or make reference to a different ontology.

