## (Array)Lists
**Definition**: random Accessible array of elements<br>
**Advantages:** simple to use <br>
**Disadvantages:** shifting in insertion and deletion or searching costly <br>

```python
	Access (indexing): O(1)
	Search: O(n)
		for i in range(len(myList)): or
		for item in myList:

	Insertion at the end: O(1) (amortized for resizing)
	Insertion at the beginning or middle: O(n)
	Deletion: O(n) (for arbitrary position - shifting)
```


---
## Tuples
**Definition**: immutable sequence of data <br>
**Advantages:** memory efficient, safe — can't be modified<br>
**Disadvantages:** can't be modified<br>

```python
	Access (indexing): O(1), no amortized time since cannot be resized
	Search: O(n)
	Insertion/Deletion: Not applicable since tuples are immutable.
```


---
## Dicts
**Definition**: hash table with key value mappings<br>
**Advantages:** fast access, delete, search <br>
**Disadvantages:** memory overhead, inefficient hash function can cause collisions <br>

```python
	Access/Search by key: O(1) amortized, O(n) in the worst case from hash collisions
		map['keyStringName']

	Insertion/Update: O(1) amortized, O(n) in the worst case from hash collisions
		map['keyStringName'] = newValue

	Deletion by key: O(1) amortized, O(n) in the worst case from hash collisions
		del map['keyStringName']
```

Note: Original key &rarr; Hash Function &rarr; (if same Hash Value, LinkedList of) Hash Values<br>

---
## Deques
**Definition**: double-ended queue allowing O(1) amortized insertions and deletions<br>
**Advantages:** queue with O(1) amortized time insertion and deletion on both ends. Can be used as stacks or queues <br>
**Disadvantages:** no random access time, memory overhead<br>

```python
	Access: Not applicable directly since sets are unordered
		queue.count(<element>)

	Search: O(1) amortized, O(n) in the worst case
		for i in range(len(myDeque)): or
		for item in myDeque:

	Insertion: O(1) amortized, O(n) in the worst case
		queue.append(<element>)
		queue.appendleft(<element>)
		queue.insert(i, <element>)

	Deletion: O(1) amortized, O(n) in the worst case
		queue.pop(<element>)
		queue.popleft(<element>)
		queue.remove(<element>) removes the first occurence
```


---
## Sets
**Definition**: unique sequence of elements implemented using hash table<br>
**Advantages:** uniqueness <br>
**Disadvantages:** no duplicates (uniqueness) <br>

```python
	Access: Not applicable directly since sets are unordered
	Search: O(1) amortized, O(n) in the worst case
		if element in mySet:
			print(True)

	Insertion: O(1) amortized, O(n) in the worst case
		set.add(<element>)

	Deletion: O(1) amortized, O(n) in the worst case
		set.discard(<element>)
```
---