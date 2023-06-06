#include "lists.h"
#include <stddef.h>

/**
 * check_cycle - checks if there is a cycle in the linked list
 * @list: linked list
 *
 * Return: 0 if it's not a cycle or 1 if it's a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp, *head;

	head = list;
	temp = list;
	while (temp != NULL)
	{
		if (temp->next == head)
			return (1);
		temp = temp->next;
	}
	return (0);
}
