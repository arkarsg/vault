# Predicate Calculus and $Z$ notation

The operators
- $\lnot$
- $\land$
- $\lor$
- $\implies$
- $\Leftrightarrow$ (equivalenece)

Quantifiers
- $\forall$
- $\exists$

---

## Sets
- A collection of elements
- Not ordered
- Not repeated

$\emptyset$ is a set with no elements

- $x \in X$ is a predicate

$$
\forall x \space \colon \space Z \space\cdot\space x > 5 \implies x \in N
$$
- $x \space\colon\space Z$ *declares* a new variable $x$ of **type** $Z$
- $x \in N$ is a predicate which is T or F depending on the value of previously declared $x$

A set of all natural numbers less than 99:
$$
\{ n : N \space|\space n < 99\}
$$

In general,
$$
\{ x : X \space|\space P(X) \}
$$
is the set of elements of $X$ for which the predicate $P$ is true

---



## Types
`Z` is strongly typed. Any set can be used as a type

>[!note]
>To define a type, we are not using subset $\subseteq$

## Relations
- A relation $R$ from $A$ to $B$, denoted by $R : A \leftrightarrow B$ is a *subset* of $A \times B$
- *domain* of $R$ is the set $\{ a : A | \exists b : B \cdot a R b\}$
- *range* of $R$ is the set $\{b : B | \exists a : A \cdot a R b\}$

![](Screenshot%202024-08-15%20at%204.56.34%20PM.png)

Above, $R : A \leftrightarrow B$
- Domain of $R$ : $\{c, d \}$
- Range of R : $\{x, y , z \}$

---
### Examples
$$
\text{divides} : N_1 \leftrightarrow N
$$
$$
\forall x : N_1 ; y : N \cdot x \space\text{divides}\space y \Leftrightarrow \exists k : N \cdot xk = y
$$
>[!note]
>Let $N_1$​ and $N$ be two sets. The relation `x divides y` holds true for any element $x$ in $N_1$​ and any element $y$ in $N$ if and only if (or equivalence) there exists some element $k$ in $N$ such that the product of $x$ and $k$ equals $y$.

---
## Domain and Range restriction
Suppose
- $R : A \leftrightarrow B$
- $S \subseteq A$
- $T \subseteq B$

#### Domain restriction
- $S \triangleleft R$ is the set $\{(a, b) : R | a \in S \}$

- **Domain restriction**: When we restrict a relation to only include inputs (from set $A$) that are part of a subset $S$.
- **Notation**: S◃ R
- **Meaning**: It means we're only considering the pairs $(a,b)$ in the relation $R$ where the input $a$ is in the subset $S$

#### Range restriction
- $R \triangleright T$ is the set $\{(a, b) : R | b \in T \}$

- **Range restriction**: When we restrict a relation to only include outputs (from set $B$) that are part of a subset $T$.
- **Notation**: R▹T
- **Meaning**: It means we're only considering the pairs $(a,b)$ in the relation $R$ where the output $b$ is in the subset $T$.

Then,
- $S \triangleleft R \in A \leftrightarrow B$
- $R \triangleright T \in A \leftrightarrow B$

### Example
Suppose we have the relation
$$
\text{has sibling} : \text{People} \leftrightarrow \text{People}
$$
And suppose $\text{female} \subseteq \text{People}$
- $\text{female} \triangleleft \text{has sibling}$ is the relation *is sister of*
	- We are looking for the relations where the *domain* (input) is female
- $\text{has sibling} \triangleright \text{female}$ is the relation *has sister*
	- We are looking for the relations where the *output* (output) is female

---
## Domain and range subtraction
Suppose,
- $R : A \leftrightarrow B$
- $S \subseteq A$
- $T \subseteq B$

#### Domain subtraction
 - S &#10852 R is the set $\{ (a, b) : R | a \notin S \}$
- **Meaning**: It creates a new relation by excluding the pairs $(a,b)$ from $R$ where $a$ is in the subset $S$.

#### Range subtraction
 - R &#10853 T is the set $\{ (a, b) : R | b \notin T \}$
 - **Meaning**: It creates a new relation by excluding the pairs $(a,b)$ from $R$ where $b$ is in the subset $T$.

Then,
- S ⩤ R = (A − S) ⊲ R
- R ⩥ T = R ⊳ (B − T)
- S ⩤ R ∈ A $\leftrightarrow$ B
- R ⩥ T ∈ A $\leftrightarrow$ B

### Example
Suppose we have the relation
$$
\text{has sibling} : \text{People} \leftrightarrow \text{People}
$$
- `female ⩤ has_sibling` is the relation `is_brother_of`
	- Exclude where the input is female. So, only include pairs where the input is not female.
- `has_sibling` ⩥ `female` is the relation `has_brother`
	- Exclude where the output is female. So, only include pairs where the output is not female.

---

## Relational image
If $R$ is an arbitrary binary relation on $X \times Y$, then the set
$$
\{ y \in Y : x R y \space \text{for some} \space x \in X \}
$$

is called the *image* or the range of $R$.

Formally, suppose $R : A \leftrightarrow B$ and $S \subseteq A$. Then,
- $R ⦇S⦈= \{ b : B | \exists a : S \cdot a R b \} \subseteq B$

### Example
- $\text{divides} (| \{8, 9 \} |)$ is the set of numbers divided by 8 or 9
- `has_sibling(| male |)` is the set of people who have a brother

---
## Inverse
For $R: A \leftrightarrow B$ then, the inverse relation
- $R^{-1} = \{ (b, a) : B \times A \space|\space a R b \}$
- $R^{-1} \in B \leftrightarrow A$

### Example
$$
succ : N \leftrightarrow N
$$
$$
\forall x, y : N \cdot x \space\textit{succ}\space y \Leftrightarrow x + 1 = y
$$

Then, 
$$
\textit{succ}^{-1} = \textit{pred}
$$

---

## Relational composition
![relational-composition|300](Screenshot%202024-08-15%20at%205.59.08%20PM.png)
 
- R ⨟ S = {(a, c) : A × C | ∃ b : B • a R b ∧ b S c }
- R ⨟ S ∈ A C
- `is_parent_of ⨟ is_parent_of = is_grandparent_of`

---

## Functions
### Partial functions

### Total functions

### Specifying functions

### Function overriding

---

## Sequences

### Functions for sequences


---

# State schema

- Specifies a relationship between **variable values**
- Specifies a **snapshot of a system**

Consists of 2 parts:
1. Variables *declared* and *typed* at the top
2. Predicate restraining possible values of the declared variables at the bottom

**Instance** of a schema
- Assignment of values to variables
```
|- Buffer ---------------------
| items : seq MSG                      declaration
|--------------------------------
| #items <= max                        predicate
|--------------------------------
```

# Operation schema

- Specifies how the system can *change*
- Express as a predicate the **relationship** between the instance of the state *before the operation* and *after the operation*

```
|- Join ------------------------------------
|items, items' : seq MSG
|msg? : MSG
|--------------------------------------------
|#items <= max                    valid instance both before & after
|#items' <= max
|#items < max                     buffer must not be completely full
|items' = items⁀<msg?>            relationship between instances
|-------------------------------------------
```

- `items` - Instance of the state before
- `items'` - instance of the state after
- `?` - An output

>[!warning] There is an implicit $\land$ between each line
### Schema inclusion
Including a schema in another schema declaration → creates a new schema with **predicates conjoined**
- type compatibility is needed to merge schemas

```
|- A --------
|x: T1
|y: T2
|-------------

|P(x,y)
|-------------
|- S --------
|A
|z: T3
|-------------
|Q(x,y,z)
|-------------

|- S -----------------
|x: T1
|y: T2
|z: T3
|---------------------
|P(x,y) ∧ Q(x,y,z)
|---------------------
```

In other words, we can simplify any **operation schema** into:

```
|- ∆ Buffer-------------------------------
|items, items' : seq MSG
|--------------------------------------------
|#items <= max
|#items' <= max
|--------------------------------------------
```

Then, write the `Join` operation as:
```
|- Join ------------------------------------
|∆ Buffer                       Schema inclusion
|msg? : MSG
|--------------------------------------------
|#items < max
|items' = items⁀<msg?>
|--------------------------------------------
```

## Leave op

```
|- Leave ------------------------------------
|∆ Buffer
|msg! : MSG
|--------------------------------------------
|items ≠ ∅
|items = <msg!>⁀items'
|--------------------------------------------
```

## Initial state
- To complete the specs, specify the initial state of the buffer

---

### Slow leave

```
|- SlowLeave ------------------
|∆ SlowBuffer
|Leave
|--------------------------------
|idle >= delay ∧ idle' = 0
|--------------------------------

|- SlowLeave ----------------------------------------
|items, items' : seq MSG
|idle, idle' : N
|msg! : MSG
|------------------------------------------------------
|items ≠ ∅
|items = <msg!>⁀items'
|idle >= delay ∧ idle' = 0
|------------------------------------------------------
```

---

# Reasoning about specification
- Introduce aux variables
	- **should not alter the functionality**
	- **should aid in the analysis**
- Add aux variables into original schema

## Example

$$
\forall \text{RecordedBuffer} \space\cdot\space \text{inhist} = \text{outhist} \do
$$