# Create a program that prompts the user ten times for a test score between 60
# and 100. Each time a score is generated, your program should display what the
# grade is for a particular score. Here is the grade table:
# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A

# def compileGrade():


def grade():

	score = ""

	# Adding summary list to display all entered scores and result at the end
	summary = ["Scores and Grades"]

	# Dictionary of responces to score entries
	statements = {
	"a": "Your grade is A", "b": "Your grade is B", "c": "Your grade is C",
	"d": "Your grade is D", "error": "Score entered must be between 60 and 100. Please reenter. "
	}





	count = 1
	while count <= 10:
		print("Enter your score: ")

		# Get the usesr's score input
		score = input()

		if score >= 60 and score <= 69:
			score = str(score)
			appendD = "Score: " + score + "; " + statements["d"]
			summary.append(appendD)
		elif score >= 70 and score <= 79:
			score = str(score)
			appendC = "Score: " + score + "; " + statements["c"]
			summary.append(appendC)
		elif score >= 80 and score <= 89:
			score = str(score)
			appendB = "Score: " + score + "; " + statements["b"]
			summary.append(appendB)
		elif score >= 90 and score <= 100:
			score = str(score)
			appendA = "Score: " + score + "; " + statements["a"]
			summary.append(appendA)
		elif score < 60 or score > 100:
			score = str(score)
			print statements["error"]
			#C Counter reset to ensure 10 scores
			count -= 1

		count += 1

	for results in range(len(summary)):
		print summary[results]
	print "End of the program. Bye!"


# Call the function
grade()
