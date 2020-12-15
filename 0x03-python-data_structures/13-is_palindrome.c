#include "lists.h"
#include <stdio.h>
/**
 * check_both_nodes - check if both nodes are equale
 * @head: head
 * @idx1: index of first node
 * @idx2: index of second node
 *
 * Return: 1 /0
 */
int check_both_nodes(listint_t *head, int idx1, int idx2)
{
	int i = 0;
	listint_t *current = NULL;
	listint_t *corespond = NULL;

	printf("idx1 %d  , idx2 %d\n", idx1, idx2);
	if (idx1 == idx2)
		return (1);
	for (i = 0; i < idx2; i++)
	{
		if (i == idx1)
		{
			current = head;
		}
		if (i == idx2 - 1)
		{
			corespond = head;
		}
		head = head->next;
	}
	if (current->n == corespond->n)
		return (1);
	else
		return (0);
}


/**
 * is_palindrome - check if list is palindromique
 * @head: head
 * Return: 1
 * Error: 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = NULL;
	listint_t *corespond = NULL;
	int Index2 = 0, index1 = 0, length = 0, i = 0, res = 0;

	if (*head == NULL)
		return (1);
	current = *head;
	corespond = *head;
	while (corespond)
	{
		corespond = corespond->next;
		length++; /* we calculate the length */
	}
	Index2 = length;
	while (i < length / 2)
	{
		res = check_both_nodes(current, index1, Index2);
		if (res == 0)
			return (0);
		index1++;
		Index2--;
		i++;
	}
	/*
	*/

	return (1);


}
