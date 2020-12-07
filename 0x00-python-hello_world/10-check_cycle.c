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

	if (!list)
		return (0);

	listint_t *rabbit = list->next;
	listint_t *turtle = list;



	while (1)
	{
		if (!rabbit || !rabbit->next)
			return (0);
		if (rabbit == turtle || rabbit->next == turtle)
			return (1);
		turtle = turtle->next;
		rabbit = rabbit->next->next;
	}
}
