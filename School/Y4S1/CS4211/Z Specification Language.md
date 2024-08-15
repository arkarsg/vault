# Predicate Calculus

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
$R$ is an element of the *powerset* of $A \times B$