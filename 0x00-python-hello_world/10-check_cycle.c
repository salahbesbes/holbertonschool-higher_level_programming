#include "lists.h"
#include <stdio.h>
/**
* check_cycle - chech if the linked list has a cycle or not
* @list: linked list
*
* Return: 1
* Error: 0
*/
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *rabbit = current->next;
	listint_t *turtle = current;

	if (!list || !turtle)
		return (0);



	while (1)
	{
		if (!rabbit || !rabbit->next)
			break;
		if (rabbit == turtle || rabbit->next == turtle)
			return (1);
		turtle = turtle->next;
		rabbit = rabbit->next->next;
	}
	return (0);
}
