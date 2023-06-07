#include <stddef.h>
#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a node in a sorted list
 * @head: linked list
 * @number: list content
 *
 * Return: new node address
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t)), *temp, *temp1;

	new->n = number;
	if (head == NULL || new == NULL)
		return (NULL);
	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	temp = *head;
	temp1 = temp->next;
	if (number < temp->n)
	{
		*head = new;
		new->next = temp;
		return (new);
	}
	while (temp != NULL)
	{
		if (temp->n <= number && number <= temp1->n)
		{
			temp->next = new;
			new->next = temp1;
			return (new);
		}
		temp = temp->next;
		if (temp1->next != NULL)
			temp1 = temp1->next;
		else
		{
			temp->next = new;
			new->next = NULL;
			break;
		}	
	}
	return (new);
}
