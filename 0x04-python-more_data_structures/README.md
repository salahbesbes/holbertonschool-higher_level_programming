#0x04. Python - More Data Structures: Set, Dictionary



In general,

	[f(x) if condition else g(x) for x in sequence]

And, for list comprehensions with if conditions only,

	[f(x) for x in sequence if condition]

Note that this actually uses a different language construct, a conditional expression, which itself is not part of the comprehension syntax, while the if after the for…in is part of list comprehensions and used to filter elements from the source iterable.

Conditional expressions can be used in all kinds of situations where you want to choose between two expression values based on some condition. This does the same as the ternary operator ?: that exists in other languages. For example:

	value = 123
	print(value, 'is', 'even' if value % 2 == 0 else 'odd')
