# AI Engineering Journey — 180 Days

Java backend engineer → AI engineer.

*Current:* Day 2 · 400 XP · Streak 2 🔥 · Rank: Syntax Initiate

---

## Day 6 - 2026-07-25 - Tuples, unpacking, '//' vs '/'
*Learned*: 'tuple' = immutable sequence(list) '(....)'. Index/slices works like a list, but
can't mutate. slicing a tuple returns a tuple. There are three uses:
multiple return values. ('return a, b' packs a tuple, 'x,y' = unpacks the value from function)
Dict keys must be immutable and signalling "fixed group". Python '/' is ALWAYS float (17/5 = 3.4)
Use '//' for integer floor division
**Reflection** Unpacking multiple return values is cleaner than Java's wrapper classes.
The '/' vs '//' thing will burn if not careful.

## Day 5 - 2026-07-24 - Dict and Set
*Learned:* 'dict' = 'HashMap' with '{key, value} literals, bracket lookup.
Missing Key -> 'KeyError' (loud) throws error when key is not present, vs Java's silent 'null', 'get()' opts looks into Java-style default ('None' or or a fallback(custom default value) you supply)
'set' = 'HashSet' with {'a', 'b'} literals, duplicates don't exist. 
'{}' means an empty *dict*, empty set is denoted by 'setName()'. And as java returns null, Python returns None.
*Reflection:* dict/set really are HashMap/HashSet 

## Day 4 - 2026-07-23 - List and Slicing

## Day 3 - 2026-07-22 - Dynamic Typing

## Day 2 — 2026-07-16 · 250 XP · Streak 2
*Learned:* Python has no classpath — sys.path is per-interpreter, so venvs
isolate by giving each project its own interpreter. pip freeze is the lockfile;
requirements.txt in, .venv/ out — same rule as pom.xml in, target/ out.
*Reflection:* The isolation problem is identical to Maven's. The solution is
inverted, and the inversion is the whole lesson.

## Day 1 — 2026-07-15 · 150 XP · Streak 1
*Learned:* Python executes files top-to-bottom; def is a binding, not a
declaration. Indentation is the block structure.
*Reflection:* Two wrong predictions taught me more than a right one would have.