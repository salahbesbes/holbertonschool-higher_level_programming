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

	if (!*head)
		return (NULL);
	current = *head;
	newNode = malloc(sizeof(listint_t));
	if (!newNode)
		return (NULL);
	newNode->n = number;

	if ((*head)->n >= number)
	{
		printf("enter\n");
		newNode->next = current;
		*head = newNode;
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
