# Trivialistrings

Contraction of _trivialities - strings = trivialistrings_.

## rev()

Reverse strings.

```python
rev('Hello World')
> 'dlroW olleH'
```

## kripkerize()

> **Barry Kripke:** _Is that a reference to my speech impediment? That's pretty hurtful. I can't control it._

Barry Kripke (The Big Bang Theory) suffers from rhotacism, the inability to pronounce or difficulty in pronouncing r sounds. Instead, it sounds like the letter w.

```python
kripkerize("Yes, yes, yes. He's a jolly good fellow. What time do the strippers arrive?")
> "Yes, yes, yes. He's a jolly good fellow. What time do the stwippews awwive?"
```

If Bawwy Kwipke wasn't unfowtunate enough, he also suffews fwom lambdacism, the inability to pwonounce ow difficulty in pwonouncing l sounds. Instead, it sounds like the lettew w.

```python
kripkerize("Yes, yes, yes. He's a jolly good fellow. What time do the strippers arrive?", lambdacism=True)
> "Yes, yes, yes. He's a jowwy good fewwow. What time do the stwippews awwive?"
```

## margonize()

> “Interesting capitalization,' I said. 'Yeah. I'm a big believer in random capitalization. The rules of capitalization are so unfair to words in the middle.” - Margo Spiegelman, Paper Towns

```python
margonize('As much as life can suck, it always beats the alternative.')
> 'As muCh aS liFE cAn suCK, IT AlwAys BEaTs tHE AltErnAtiVE.'
```