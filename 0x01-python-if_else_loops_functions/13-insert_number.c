#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - insert node in a sorted linked list
 * @head: head of the list
 * @number: integer
 *
 * Return: header node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = NULL, *previous = NULL;
	listint_t *newNode = NULL;

	current = *head;
	previous = *head;
	newNode = malloc(sizeof(listint_t));
	if (!newNode)
		return (NULL);
	newNode->n = number;

	if (!current)
	{
		newNode->next = NULL;
		*head = newNode;
		return (*head);
	}
	else if ((*head)->n > number)
	{
		newNode->next = (*head);
		(*head) = newNode;
		return (*head);
	}
	while (current)
	{
		if (current->n > number)
		{
			newNode->next = current;
			previous->next = newNode;
			break;
		}
		previous = current;
		current = current->next;
	}
	if (!current)
	{
		newNode->next = NULL;
		previous->next = newNode;
	}
	return (*head);

}
