#include "lists.h"

/**
 * is_palindrome - check for palindrome linkedlist
 * @head: linkedlist
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *cp = *head;
	int buff[10240], init = 0, end = 0;

	if (!*head || !((*head)->next))
		return (1);

	while (cp)
	{
		buff[end] = cp->n;
		cp = cp->next;
		end++;
	}

	end--;

	while (init <= end / 2)
	{
		if (buff[init] != buff[end - init])
			return (0);
		init++;
	}

	return (1);
}
